---
name: superpractic-landingpages
description: Pornește la START LP, cere screenshot-ul furnizorului, apoi face research, copy educativ și imagine principală 500x500, cu aprobări separate și creare draft în Shopify.
---

# SuperPractic landing pages

Aplică regulile din `AGENTS.md` de la rădăcina repository-ului. Citește `docs/agent-rules.md`, `docs/copy-analysis.md` și `docs/copy-references.md` din aceeași rădăcină. Aceste fișiere sunt corpusul de lucru; nu este necesar un GPT personalizat, un serviciu Actions sau o aplicație web separată pentru lucrul în Codex.

Comanda simplă de pornire este `START LP`, fără diacritice. Dacă nu a fost atașat screenshot-ul produsului pentru această lucrare, cere în conversație o imagine de la furnizor în care se văd produsul, modelul/specificațiile și conținutul pachetului; acceptă mai multe screenshots. Așteaptă atașamentul înainte de research. Dacă imaginea este deja atașată comenzii, folosește-o și nu cere retrimiterea. Nu cere prețul.

1. Primește fotografia/screenshot-ul produsului în conversație și identifică-l. Linkul furnizorului este opțional, dar poate fi necesar pentru model și specificații.
2. Fă research detaliat, cu surse datate și probleme actuale ale cumpărătorilor. Livrează cele trei liste ordonate: pain points, beneficii și utilizare. Nu numi ipotezele tendințe demonstrate.
3. Propune numele și întregul text al paginii, cu normal 4 și maximum 5 headlines. Educă în limbaj simplu și explică detaliile tehnice confirmate. Cere feedback și aprobarea explicită a textului.
4. Generează numai imaginea principală după aprobarea textului. Exportă și verifică un fișier exact 500 × 500 px, folosind materialul real al produsului. Prezintă fișierul și cere aprobarea explicită a imaginii.
5. După ambele aprobări, folosește accesul Shopify din mediul configurat pentru produs draft și copia unui șablon eligibil. Nu seta prețuri și nu publica. Nu modifica codul sau șablonul original.
6. Verifică rezultatul, identificatorii, conținutul și fișierul final. Distinge permisiunile acordate de operațiile efectiv executate și verificarea API de verificarea vizuală.

Pentru conectivitate folosește `python3 tools/check_shopify_connection.py`, din rădăcina repository-ului. Nu afișa credențiale. Pentru research extern, respectă politica de rețea; o cerere refuzată de proxy necesită domeniul permis prin configurația mediului, nu dezactivarea proxy-ului/TLS.

Fiecare sarcină cloud este izolată: lucrează în checkout-ul existent, fără worktree nou dacă proprietarul nu cere. Pentru continuarea unei revizii folosește conversația produsului și versiunile aprobate; o sarcină nouă nu presupune aprobări pe care nu le poate verifica.
