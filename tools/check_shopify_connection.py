"""Read-only Shopify connection check. Credentials come from environment settings."""

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


# Confirmed from the public storefront and explicitly selected by the owner.
# Use this destination instead of the incorrectly populated runtime domain binding.
SHOP_DOMAIN = "b77w9x-rx.myshopify.com"
API_VERSION = "2026-10"


def request_json(url, body, headers):
    request = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        # Never log response bodies: authentication responses can contain secrets.
        raise RuntimeError(f"Shopify returned HTTP {error.code}.") from None
    except urllib.error.URLError:
        raise RuntimeError("Shopify connection failed; check network and TLS configuration.") from None
    except (ValueError, TimeoutError):
        raise RuntimeError("Shopify returned an invalid response or timed out.") from None


def main():
    names = ("SHOPIFY_CLIENT_ID", "SHOPIFY_CLIENT_SECRET")
    missing = [name for name in names if not os.environ.get(name)]
    if missing:
        print("Missing environment settings: " + ", ".join(missing))
        return 2
    print("Authorized Shopify store: " + SHOP_DOMAIN)

    token_response = request_json(
        f"https://{SHOP_DOMAIN}/admin/oauth/access_token",
        json.dumps({
            "grant_type": "client_credentials",
            "client_id": os.environ["SHOPIFY_CLIENT_ID"],
            "client_secret": os.environ["SHOPIFY_CLIENT_SECRET"],
        }).encode(),
        {"Content-Type": "application/json", "Accept": "application/json"},
    )
    token = token_response.get("access_token")
    if not isinstance(token, str) or not token:
        raise RuntimeError("Shopify did not issue an access token.")

    # GraphQL POST contains queries only; no product, price or theme mutations.
    result = request_json(
        f"https://{SHOP_DOMAIN}/admin/api/{API_VERSION}/graphql.json",
        json.dumps({"query": """
            query ConnectionCheck {
              shop { name myshopifyDomain }
              currentAppInstallation { accessScopes { handle } }
              products(first: 5) { nodes { id title handle templateSuffix } }
              themes(first: 5) { nodes { id name role } }
            }
        """}).encode(),
        {"Content-Type": "application/json", "X-Shopify-Access-Token": token},
    )
    if result.get("errors"):
        raise RuntimeError("Shopify query failed; check installation, granted scopes and API fields.")
    data = result.get("data")
    if not isinstance(data, dict) or not all(data.get(key) is not None for key in (
        "shop", "currentAppInstallation", "products", "themes"
    )):
        raise RuntimeError("Shopify returned incomplete connection-check data.")
    print(json.dumps(data, ensure_ascii=False, indent=2))
    print("Read-only Shopify connection verified. No products or themes changed.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except RuntimeError as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
