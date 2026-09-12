# SEO-brief — villatakservice.se (Geal Entreprenad AB)

## Driftläge: autonomt, utan stopp
- **Commit + push är förhandsgodkänt (av ägaren 2026-09-06).** Committa i logiska bitar och pusha direkt utan att fråga. Använd tydliga commit-meddelanden. Jobba på egen branch bara om du inte redan är på main enligt harness-regler; annars pusha main.
- Kör hela uppdraget i en följd. Fråga inte om lov, vänta inte på "go".
- Sakas ägarfakta (pris, garanti, cert, GBP/GSC-access) → sätt `[ПОДТВЕРДИТЬ У ВЛАДЕЛЬЦА]`, för upp frågan i listan, gå vidare. Blockera inte.
- Icke-principiella val (URL-namn, sektionsordning, formulering) → besluta själv efter best practice.
- Efter varje steg: en rad i `docs/seo-worklog.md` (✅/🔄/☐) + nästa. Inga pauser.
- Vid omstart: läs denna fil + worklog, fortsätt från första oavklarade punkt.
- **Fakta för verifiering (frågelistan)** ligger längst ned i `docs/seo-worklog.md`.

## Arbetsregler (för agenten)
- **Svara kort och rakt på sak.** Ingen fyllnad, ingen upprepning.
- Först audit → sedan plan → sedan ändringar. Skriv aldrig kod blint.
- Hitta inte på fakta om företaget (priser, garantier, år, case, omdömen, certifikat). Saknas fakta → lämna platshållare `[BEKRÄFTA MED ÄGARE]` + för upp i frågelista.
- Allt användarinnehåll på korrekt svenska. Rätt terminologi: takbyte, takomläggning, takrenovering, takläggare, takbesiktning, plåttak, tegeltak, betongpannor.
- Bryt inte bygget. Kör build/lint efter ändringar, visa att det är grönt.
- Commit i logiska bitar med tydliga meddelanden. Pusha inte utan bekräftelse.
- Separera vad agenten kan göra själv (on-page/teknik/innehåll) från vad ägaren måste göra (GBP, omdömen, backlinks).

## Roll & mål
Topp-SEO-ingenjör + innehållsstrateg. Kunden: takfirma **Geal Entreprenad AB**, domän villatakservice.se, bas Sundbyberg, arbetar i hela Stockholm. Mål: topp på Google.se för kommersiella sökord kring tak på villa i Stockholmsregionen. Marknad: endast Sverige. Språk: endast svenska.

## Nuläge (fakta — hitta inte på mer)
- Ny sajt: ~194 visningar / 3 mån, 0 klick, snittposition 44,4 — rankar i praktiken inte.
- GSC-sökord med visningar (plattform att bygga på): `takläggare sundbyberg`, `takrenovering sundbyberg`, `takbyte sundbyberg`, `besikta tak`, `besiktning av tak`, `villatak`, `villatak stockholm`.
- Tjänster: takbyte, takrenovering, plåttak, takmålning, takbesiktning, taktvätt.
- Områden: Sundbyberg, Solna, Bromma, Nacka, Täby, Danderyd, Lidingö, Sollentuna, Järfälla, Spånga.
- NAP (bekräftat 2026-09-06): **Geal Entreprenad AB**, Byggmästarvägen 18, 168 32 Bromma (Mariehäll). Tel: 08 12 410 276. E-post: info@villatakservice.se. Org.nr 559303-7566, moms SE559303756601. Bas i Bromma, Sundbyberg = topp-prioriterat närområde. (Tidigare "Lavettvägen 44, Sundbyberg" var fel.)
- Huvudkonkurrent: takrenoveringistockholm.se — service-only, ingen blogg, täcker bara Stockholm/Danderyd/Lidingö/Nacka.

## Strategi (prioritet uppifrån och ned)

### 1. Lokal SEO — största hävstången
- **Google Business Profile** = ägaruppgift #1 (map-pack ger takläggare flest leads).
- NAP-konsistens (namn, adress, tel) på hela sajten + i schema.
- Inför `schema.org RoofingContractor` (subtyp LocalBusiness) på start + kontakt: name, address, geo, telephone, areaServed, openingHours, priceRange, sameAs.

### 2. Matris tjänst × område (konkurrentens största lucka)
Egna location-sidor per område. Prioritet: Sundbyberg → Solna → Bromma → Spånga → Sollentuna → Järfälla → Täby → Danderyd → Lidingö → Nacka.
- Unik text per område (inte mall-copypaste). Lokala landmärken, bebyggelse/taktyper, lokal CTA.
- URL: `/takläggare-[ort]` eller `/[ort]/takbyte`.
- Sökord: `takläggare [ort]`, `takbyte [ort]`, `takrenovering [ort]`, `takbesiktning [ort]`.

### 3. Starka tjänstesidor (money pages)
En optimerad sida per tjänst med intent:
- Takbyte → takbyte, takbyte kostnad, takbyte pris, byta tak villa
- Takrenovering → takrenovering stockholm, takrenovering pris, takomläggning
- Takbesiktning → takbesiktning, besikta tak, besiktning av tak (har redan visningar!)
- Plåttak, Takmålning, Taktvätt — separat
Varje: tydlig H1 med sökord, intro med intent, "vad ingår", process i steg, ROT-avdrag, FAQ + FAQPage-schema, CTA + formulär/telefon.

### 4. "Villa"-vinkeln = din domän
Ta det ingen tar: `villatak`, `tak på villa`, `takbyte villa`, `takrenovering villa`, `takläggare villa`. Tegel/betong/plåt-specifikt för villor. Differentiator för varumärke/domän.

### 5. Innehållskluster (bloggen "Artiklar" — konkurrenten saknar den)
Informationsartiklar som länkar internt till money pages. Prioritet efter köpintent:
- Vad kostar ett takbyte? (prisguide, spann — "beror på")
- Takbyte eller takrenovering — vad ska jag välja?
- ROT-avdrag för takarbete (verifiera aktuell % och tak för 2026 — skriv inte ur minnet)
- Tegeltak vs betongpannor vs plåttak — för- och nackdelar
- Hur ofta ska man besikta taket? / Tecken på att taket behöver bytas
- Så lång tid tar ett takbyte
Varje: Article-schema, interna länkar till tjänst + område, ärlig fakta.

## On-page-krav (per sida)
- `title` ≤ ~60 tecken, sökord först + lokal krok. Ex: `Takbyte i Sundbyberg – fast pris & ROT | Geal Entreprenad AB`.
- `meta description` ≤ ~155 tecken, sökord + CTA.
- Exakt en H1 med huvudsökord; logisk H2/H3-hierarki.
- Unika title/description/H1 per sida (kolla dubbletter på hela sajten).
- Canonical, läsbara URL:er, alt-text på bilder (sökord + geo där det passar), intern länkning tjänst↔område↔artikel.
- Schema: RoofingContractor (globalt), FAQPage (tjänster), Article (blogg), BreadcrumbList.

## Teknisk SEO-checklista
- sitemap.xml + robots.txt korrekta, sitemap skickad till GSC.
- Alla nyckelsidor indexerbara (inget oavsiktligt noindex), kolla Coverage/Pages i GSC.
- Core Web Vitals: komprimera/lazy-load takbilder (webp, dimensioner), kolla LCP/CLS mobilt.
- Mobilanpassning, HTTPS, inga brutna länkar/404, redirects utan kedjor.
- Snabb TTFB.

## Utanför repot — ägaruppgifter (imitera inte, lista)
- Google Business Profile: skapa/fyll, kategori RoofingContractor, objektfoton, områden.
- Omdömen: samla Google-omdömen (starkaste lokala signalen + trust).
- Backlinks: lokala kataloger (hitta.se, eniro, allabolag), branschkataloger, partnerskap.
- Bekräfta fakta: priser/spann, garantier, erfarenhet, ROT-detaljer, case med före/efter-foto.

## Arbetsmetod
1. Skanna projektet → audit: stack, var innehållet ligger, URL/meta, vad som finns/är trasigt.
2. Föreslå plan (URL-karta: tjänster + områden + artiklar; prioritet) → vänta på "go".
3. Bygg efter prioritet: teknik + schema + start/tjänster → location-matris → blogg.
4. Efter varje etapp: build/lint grönt, kort rapport gjort + nästa.
5. Håll `docs/seo-worklog.md` uppdaterad (gjort/nästa).

## Mätning
Följ i GSC positionsrörelse på plattform-sökorden (`takläggare/takbyte/takrenovering sundbyberg`, `besikta tak`, `villatak`) + visningar/klick. Närmaste mål: 44 → topp-10 på lokala "sundbyberg"-sökord + in i map-pack.

---

## Addendum — topical authority (pillar → cluster)
Bygg inte bara 6 tjänster. Bygg semantisk arkitektur som täcker HELA temat "tak på villa" + närliggande. Google värderar domänens tematiska auktoritet, inte enskilda sidor. Full täckning + tät intern länkning → även money-sidor rankar bättre.

**Modell hub-and-spoke:**
- **Pillars (breda hubbar):** `Takbyte villa`, `Takrenovering`, `Tak på villa – komplett guide` (villatak).
- **Cluster:** smala artiklar/sidor runt varje pillar; länkar UPP till pillar + i SIDLED till varandra.
- **Money-sidor (tjänst × ort):** får länkar från relevanta artiklar med **sökords-ankare** (inte "läs mer" utan t.ex. "takbyte i Sundbyberg").
- **Inga orphan pages.** Varje sida länkar till 2–3 relevanta + får inkommande. Contextual-länkar, inte bara meny.

**Kluster (kärna → utåt):**
- Kärna: takbyte/renovering/besiktning/plåttak/målning/tvätt × orter.
- Komponenter: hängrännor & stuprör, takfönster, skorsten(srenovering), taksäkerhet (snörasskydd/takstege/glidskydd), vindskivor/fotplåt/ståndskivor, undertak/underlagspapp/läkt.
- Isolering/energi: vindsisolering/tilläggsisolering, energieffektivt tak, solceller på tak (minst info-nivå, `[ПОДТВЕРДИТЬ scope]`).
- Problem/symptom (top-funnel): takläckage, fuktskada/mögel vind, istappar/isbildning + snöskottning, mossa på taket.
- Material: tegel vs betong vs plåt, bandtäckning/falsat plåt/papptak/sedumtak, livslängd per material.
- Beslut/pengar (prio): vad kostar takbyte/renovering, ROT-avdrag (verifiera % + tak 2026), bygglov för takbyte, försäkring & garanti, så väljer du takläggare.
- Säsong: takarbete på vintern, vår-checklista.

**Prioordning:** 1) money-kärna → 2) bottom-funnel beslut (kostnad, ROT, välja, bygglov) → 3) problem/symptom → 4) komponenter → 5) material + energi → 6) säsong.

**Regler mot utspädning:**
- Ett intent = en sida. Kolla kannibalisering (title/H1/intent) före ny sida.
- Info ≠ kommersiellt. Artikel svarar + länkar till money-sida; blanda inte.
- Varje sida: schema efter typ (Article/FAQPage/Service/BreadcrumbList).
- Ankare efter sökord, varierade, ingen spam.

**Data-driven expansion (löpande):** var 2–4 v — dra GSC Queries, ta near-miss (pos 8–20) + oväntade träffar som nya teman. Kolla autocomplete / "People also ask" / "Related searches". För register i worklog: tema → sökord → URL → status → inkommande.

**E-E-A-T:** Om oss (erfarenhet, ID06/behörighet/försäkring `[ПОДТВЕРДИТЬ]`), case före/efter med ort+foto, konsekvent NAP, sameAs till GBP/soc.

## Underhåll / hur sidorna byggs
Sidorna genereras av `tools/generate.py` (Python, ingen runtime-dep). Redigera innehåll där och kör `python3 tools/generate.py` → skriver statiska `.html` i repo-roten. Gemensam header/footer/head + schema ligger i generatorn, sidinnehåll i `PAGES`. Detta håller ~40 sidor konsekventa och orphan-fria.
