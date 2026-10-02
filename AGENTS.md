# SuperPractic Agent în Codex

Acest repository conține instrucțiunile și referințele agentului pentru research și landing pages SuperPractic. Fotografia/screenshot-ul produsului și eventual linkul furnizorului se trimit ca atașamente și mesaje într-o sarcină Codex pe acest repository, folosind mediul Shopify configurat.

## Comanda de pornire: START LP

Când mesajul proprietarului este `START LP`, activează fluxul SuperPractic și citește skill-ul și regulile proiectului înainte de a răspunde. Acceptă și diferențe de litere mari/mici sau spații la capetele mesajului. Simplul fapt că o discuție citează această comandă nu pornește o lucrare nouă.

Dacă nu există deja fotografia produsului pentru lucrarea curentă, primul răspuns este:

> Trimite un screenshot de la furnizor în care se văd produsul și informațiile despre el: numele/modelul, specificațiile și ce conține pachetul. Dacă informațiile sunt pe mai multe ecrane, poți trimite mai multe poze. După ce le primesc, încep research-ul.

Cere atașamentul în conversație, nu printr-un formular de input care acceptă doar text. Așteaptă fotografia înainte de research, copy, generare de imagine sau operații Shopify. Nu cere prețul. Dacă mesajul START LP include deja screenshot-ul, folosește-l direct și nu cere retrimiterea; solicită ulterior numai detaliile esențiale care lipsesc ori nu se pot citi.

## Înainte de a începe

Pentru o cerere de research, copy, imagine sau landing page, citește `.agents/skills/superpractic-landingpages/SKILL.md`, `docs/agent-rules.md` și `docs/copy-analysis.md`. Folosește `docs/copy-references.md` ca exemple editoriale, nu ca dovezi despre performanța unui produs nou.

Fiecare sarcină cloud este deja izolată. Folosește checkout-ul existent; nu crea Git worktrees decât dacă proprietarul cere explicit.

## Reguli obligatorii

- Pagina urmărește conversia prin educare: explică problema, mecanismul, beneficiul și folosirea în limbaj foarte simplu, ușor de înțeles chiar și de un copil, cu un ton firesc pentru adult. Detaliile tehnice sunt relevante, verificate și explicate pe loc, pentru încredere.
- Inputul principal este o fotografie/screenshot. Nu inventa modelul, specificațiile sau pachetul din imagine. Cere numai informația necesară și continuă independent research-ul categoriei.
- Preia informațiile produsului din screenshot-ul furnizorului. Nu face research direct pe Alibaba și nu pierde timp accesând paginile furnizorului. Nu transforma afirmațiile din screenshot în performanțe confirmate independent.
- Fă research rapid, în stil GPT: citește textul din screenshot, apoi folosește Google doar pentru a înțelege rapid problemele, experiențele și obiecțiile pieței. Ținta este viteza cu judecată, nu un raport lung: pornește de la 1–3 căutări scurte și câteva surse utile, preferând România și semnale recente. Oprește imediat ce ai baza necesară pentru pain points, beneficii și copy; extinde numai pentru o incertitudine care schimbă mesajul principal. Nu amâna copy-ul pentru parametri neclari care pot fi omiși. Nu inventa surse, cifre sau tendințe pentru viteză.
- Livrează trei liste concise: pain points în ordinea importanței/gravitații, beneficii în ordinea importanței și cum se folosește. Separă faptele, experiențele cumpărătorilor și ipotezele și citează sursele efectiv consultate. Nu numi o problemă „hot” fără dovezi recente.
- Modelele editoriale sunt numai produse fără SKU TEST-01. Verifică toate variantele: dacă una are TEST-01, exclude întregul produs. Corpusul aprobat este PowerMax, UltraX, CurățăPVC, LaPedală, Molistop și kitul cu abur. ReFilet, TurboBlast și paginile cu texte moștenite greșit nu sunt modele de copy.
- Descrierea are normal 4 și maximum 5 headlines explicative, în funcție de beneficiile distincte susținute. Nu umple artificial cinci blocuri. Blocul de folosire intră în limită.
- Prezintă tot textul și cere aprobarea explicită a versiunii curente. Orice revizie a textului anulează aprobarea textului vechi.
- După aprobarea textului, generează tu numai imaginea principală de lângă zona de cumpărare. Folosește capabilitatea de generare/editare a imaginilor și fotografia reală ca referință. Fișierul final trebuie să aibă exact 500 × 500 px, cu dimensiunile și lizibilitatea verificate. Exportul/redimensionarea la dimensiunea cerută este permis, fără deformarea produsului. Nu genera alte imagini, GIF-uri sau videoclipuri.
- Prezintă imaginea și cere aprobarea explicită a fișierului final. Dacă se schimbă numele sau un text/beneficiu din imagine, actualizeaz-o și cere din nou aprobarea.
- Creează în Shopify numai după ambele aprobări. Folosește un produs draft, un șablon nou bazat pe un model eligibil și numai imaginea principală aprobată. Nu seta/copia prețuri, prețuri de referință sau reduceri. Nu publica.
- Nu modifica produsul-model, șablonul original, Liquid, CSS, JavaScript sau setările globale. Configurarea este limitată la copia șablonului și datele produsului nou. Curăță numele, beneficiile, imaginile și referințele vechiului produs din copia nouă.
- Nu inventa recenzii, numere de clienți, date tehnice, rezultate, promisiuni de livrare sau garanții.
- Nu ai acces automat la celelalte chaturi din contul ChatGPT. Utilizează numai conversația curentă și materialele pe care proprietarul le furnizează.

## Shopify

Magazinul autorizat este `b77w9x-rx.myshopify.com`. Credențialele sunt în mediul cloud, nu în repository. Inspectează numai prezența/starea lor și nu afișa valori. Nu solicita parole sau tokenuri în conversație. Păstrează proxy-ul și verificarea TLS.

Verificare fără scriere:

```bash
python3 tools/check_shopify_connection.py
```

Autentificarea și citirea sunt verificate; scope-urile acordate includ read/write_products, read/write_files și read/write_themes. Acestea nu dovedesc că scrierea unui șablon va fi acceptată. Nu pretinde că Shopify a fost modificat fără răspuns API și verificare efectivă.

Nu plasa comenzi reale. Păstrează identificatorii produsului/șablonului și versiunile aprobate pentru a evita duplicatele la retry. Raportează rezultate parțiale fără a le descrie ca pagini finalizate.
