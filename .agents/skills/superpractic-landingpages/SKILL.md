---
name: superpractic-landingpages
description: Pornește la START LP, preia datele din screenshot, face research rapid pe Google despre problemele cumpărătorilor, copy educativ și imagine principală 500x500, cu aprobări separate și creare draft în Shopify.
---

# SuperPractic landing pages

Aplică regulile din `AGENTS.md` de la rădăcina repository-ului. Citește `docs/agent-rules.md`, `docs/copy-analysis.md` și `docs/copy-references.md` din aceeași rădăcină. Aceste fișiere sunt corpusul de lucru; nu este necesar un GPT personalizat, un serviciu Actions sau o aplicație web separată pentru lucrul în Codex.

Comanda simplă de pornire este `START LP`, fără diacritice. Dacă nu a fost atașat screenshot-ul produsului pentru această lucrare, cere în conversație o imagine de la furnizor în care se văd produsul, modelul/specificațiile și conținutul pachetului; acceptă mai multe screenshots. Așteaptă atașamentul înainte de research. Dacă imaginea este deja atașată comenzii, folosește-o și nu cere retrimiterea. Nu cere prețul.

1. Primește fotografia/screenshot-ul produsului în conversație, identifică-l și extrage informațiile vizibile. Pentru detalii esențiale lipsă cere o clarificare sau încă un screenshot; nu porni căutarea pe Alibaba.
2. Preia datele produsului din screenshot; nu face research direct pe Alibaba sau pe paginile furnizorului. Fă research rapid în stil GPT: citește textul din imagine, apoi folosește Google doar ca să înțelegi repede problemele oamenilor, experiențele, obiecțiile și soluțiile din piață. Pornește de la 1–3 căutări scurte și câteva surse utile, preferând România și semnale recente. Oprește când ai baza necesară pentru copy; extinde numai pentru o incertitudine care schimbă mesajul principal. Omite parametrii neclari neesențiali fără a întârzia procesul. Livrează concis cele trei liste ordonate: pain points, beneficii și utilizare, cu sursele consultate. Nu numi ipotezele tendințe demonstrate și nu inventa dovezi pentru viteză.
3. Propune numele și întregul text al paginii, cu normal 4 și maximum 5 headlines, inclusiv beneficiile scurte, „Angajamentul Nostru” și „De ce [nume]?”. Educă în limbaj simplu și explică detaliile tehnice confirmate. Finalizează reviziile în conversație și cere aprobarea explicită a versiunii complete. Până la etapa Shopify folosește referințele salvate; nu accesa Shopify și nu rula teste de conexiune, citiri de catalog/teme sau pregătiri de produs/șablon.
4. Generează numai imaginea principală după aprobarea textului. Exportă și verifică un fișier exact 500 × 500 px, folosind materialul real al produsului. Prezintă fișierul și cere aprobarea explicită a imaginii.
5. Numai după finalizarea și aprobarea întregului copy și aprobarea imaginii, intră în etapa Shopify și creează tu pagina: produs draft, copia unui șablon eligibil, tot copy-ul aprobat și imaginea principală aprobată. Atribuie șablonul noului produs fără o nouă confirmare generică de implementare. Nu seta prețuri și nu publica. Nu modifica codul sau șablonul original.
6. Verifică rezultatul, identificatorii, conținutul și fișierul final. Distinge permisiunile acordate de operațiile efectiv executate și verificarea API de verificarea vizuală.

Pentru conectivitate folosește `python3 tools/check_shopify_connection.py`, din rădăcina repository-ului, numai la etapa Shopify după ambele aprobări. Nu afișa credențiale. Pentru research extern, respectă politica de rețea; o cerere refuzată de proxy necesită domeniul permis prin configurația mediului, nu dezactivarea proxy-ului/TLS.

Fiecare sarcină cloud este izolată: lucrează în checkout-ul existent, fără worktree nou dacă proprietarul nu cere. Pentru continuarea unei revizii folosește conversația produsului și versiunile aprobate; o sarcină nouă nu presupune aprobări pe care nu le poate verifica.
