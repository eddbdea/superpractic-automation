# SuperPractic Agent

Agentul este folosit direct în Codex, cu regulile proiectului din `AGENTS.md` și skill-ul local `superpractic-landingpages`.

## Cum trimiți un produs

Deschide o sarcină Codex cu repository-ul `eddbdea/superpractic-automation` și mediul cloud în care este configurat Shopify. Scrie numai:

> START LP

Agentul îți cere un screenshot de la furnizor în care se văd produsul și informațiile despre el: numele/modelul, specificațiile și ce conține pachetul. Atașează fotografia sau mai multe screenshots; apoi începe research-ul. Poți atașa screenshot-ul chiar împreună cu START LP, caz în care agentul îl folosește fără să-l ceară din nou.

Poți adăuga linkul furnizorului și instrucțiuni. Pentru alt produs, începe o sarcină nouă pe același proiect; pentru revizii, continuă sarcina produsului respectiv.

## Ce face agentul

Datele produsului din screenshot → research rapid pe Google despre problemele și obiecțiile cumpărătorilor → text educativ pentru conversie, cu maximum 4–5 headlines → aprobarea textului → generarea unei singure imagini principale de exact 500 × 500 → aprobarea imaginii → produs draft și șablon nou în Shopify.

Întregul copy se stabilește și se revizuiește în conversație. Agentul începe lucrul în Shopify numai după aprobarea versiunii complete a textului și a imaginii principale; până atunci folosește exemplele salvate în proiect, fără teste de conexiune sau citiri din Shopify. După aprobări creează singur produsul draft, completează pagina și atribuie șablonul duplicat, fără încă o confirmare generică de implementare.

Beneficiile imediat sub numele produsului au fiecare emoji în față și nu se termină cu punct. Șablonul nou se duplică din **`kit-lant`** și se denumește după produs. Agentul completează numai câmpurile native existente, inclusiv tabelul cu emoji; nu adaugă secțiuni/blocuri Custom Liquid sau cod Liquid/CSS/JavaScript. O altă bază se folosește numai la cererea explicită a proprietarului.

Secțiunea de angajament se numește **Efect Garantat 💯**, cu expresiile relevante din text evidențiate cu bold. **De ce [NumeProdus]? 👀** are dedesubt exact două propoziții scurte despre esența produsului, cu bold pe elementele importante. Beneficiile din tabel sunt scurte, integral cu bold, fiecare cu emoji în față, fără explicații suplimentare sau punct la final. Aceste reguli se aplică și viitoarelor workflow-uri.

Research-ul este rapid, în stil GPT: agentul citește textul din screenshot, face câteva căutări Google scurte despre problemele și obiecțiile pieței și se oprește imediat ce are baza necesară pentru copy. Nu se face direct pe Alibaba. Agentul verifică suplimentar numai incertitudinile care schimbă mesajul principal și nu inventează dovezi pentru a termina mai repede.

Poza principală este simplă: produsul cu cantitatea verificată vizibilă pe el, fundal relevant și un mesaj mare de 2–3 cuvinte, cu majuscule în albastrul SuperPractic (#2563EB). Pentru un produs fără etichetă, agentul creează o etichetă informativă simplă. Un fundal ÎNAINTE/DUPĂ folosește numai fotografii reale ale rezultatului; în lipsa lor se alege o scenă relevantă. Fișierul final are exact 500 × 500 px și se aprobă înainte de Shopify.

Prețul și publicarea rămân la proprietar. Agentul nu modifică codul temei sau șablonul-model și nu generează imagini suplimentare.

## Starea execuției

Regulile și referințele sunt salvate local în acest checkout. Shopify este configurat în mediul cloud; autentificarea, crearea unui produs draft, încărcarea imaginii 500 × 500 și duplicarea/atribuirea șablonului au fost verificate prin API. Verificarea API nu confirmă automat aspectul vizual al paginii. Nu există o aplicație web sau un GPT personalizat implementat; acestea nu sunt necesare pentru execuția în Codex.

Instrucțiunile proiectului sunt versionate pe ramura `main`. Pentru o sarcină nouă, selectează repository-ul `eddbdea/superpractic-automation`, ramura `main` și mediul cloud cu Shopify configurat. Salvarea configurației draft nu publică snapshot-ul: folosește Save and publish în onboarding pentru activarea modificărilor mediului. Pornirea unei sarcini noi trebuie verificată separat; nu este confirmată doar prin salvarea configurației sau prin existența fișierelor pe GitHub.

La etapa Shopify, după ambele aprobări, pentru diagnosticarea conexiunii rulează `python3 tools/check_shopify_connection.py`. Nu sunt necesare pachete Python externe; scriptul folosește biblioteca standard și credențialele din mediul cloud.
