# Next-level worklog — villatakservice.se

> Genomförande av `docs/next-level-brief.md`. Autonomt läge, blockerande ägarfakta = **[OWNER]**.
> Bygg: `python3 tools/generate.py` · Lint: `python3 tools/validate.py` (bägge gröna).
> Status: **5/5 uppgifter klara + follow-up klar.** 63 sidor, 148 JSON-LD-block, 0 lint-fel.

---
## ▶️ RESUME — börja här nästa gång (uppdaterad 2026-09-08)

**Läge:** Hela `next-level-brief.md` (1–5) + follow-up (inline consent, sök i nav/footer) är
GENOMFÖRT, committat och pushat till `main` (autodeploy). Allt kod-arbete är klart och grönt.

**Arbetsflöde (memorera):** redigera `tools/generate.py` → `python3 tools/generate.py` →
`python3 tools/validate.py` (ska vara grön) → commit + push. Statiska sidor
(index/tjanster/om-oss/kontakt/artiklar) genereras EJ – patcha dem för hand/skript.

**NÄSTA STEG (prio-ordning):**
1. **[OWNER] – kod väntar bara på ID:n.** Fyll i `GA4_ID` + `META_PIXEL_ID` i `assets/js/main.js`.
   Utan dem laddas ingen spårning. Verifiera sedan `RATES` (kr/m²) i kalkylatorn.
2. **[OWNER] Rich Results Test** på index.html (WebSite/SearchAction) + takbyte.html (HowTo).
3. **[OWNER] GBP + Google-omdömen + foto före/efter + backlinks** (hitta/eniro/allabolag).
   Kräver ägarens inloggning – kan ej göras av agent.
4. **Case-sida** (referens/omdömen) när ägaren skickar foton → E-E-A-T-sektion.
5. **Konverteringsspårning** för tel/mailto-klick (event `contact`) när GA4 är aktivt.
6. **HowTo på fler processidor** (byggfirma, villarenovering) när de får riktiga steg.
7. **Fas 3 (datadrivet):** dra GSC-queries pos 8–20 → punktvisa nya/förstärkta sidor. Ingen massgenerering.

**Så fortsätter du:** läs denna fil + `docs/next-level-brief.md` → plocka första öppna punkten
ovan. Skriv "продолжаем" för att dra igång.
---

## Genomfört (2026-09-08)

### 1. Analytics: GA4 + Consent Mode v2 + cookie-banner + tack-konvertering ✅
- Samtyckesstyrd spårning i `assets/js/main.js` – laddas på **alla** sidor (statiska + genererade) via befintlig `main.js`.
- Consent Mode v2 med **default DENIED** för alla lagringstyper; `wait_for_update` satt.
- GA4 (`gtag.js`) laddas **först efter aktivt samtycke**; `analytics_storage` uppdateras till granted.
- Cookie-banner (Acceptera alla / Endast nödvändiga), val sparas i `localStorage` (`vts_consent`).
- Konvertering `generate_lead` (GA4) + `Lead` (Meta) fyras på `/tack.html` efter samtycke.
- Integritetspolicyn uppdaterad (cookies/analytics/consent; borttaget felaktigt "Google Fonts").
- **[OWNER]** `GA4_ID` måste fyllas i `main.js` (t.ex. `G-XXXXXXXXXX`).

### 2. Kalkylator takbyte (lead-magnet) + prefill ✅
- Ny sida `kalkylator-takbyte.html`: area + material + lutning → prisspann **före och efter ROT**.
- Kalkylator-JS i `main.js` (branschtypiska kr/m²-spann; ROT 30 %/50 000-tak/1 ägare).
- "Få exakt offert"-CTA prefyller kontaktformuläret via `?tjanst=&meddelande=` (läses av `main.js` på kontakt).
- Länkad från `takbyte.html` och `vad-kostar-takbyte.html`.
- Tydlig disclaimer: grov uppskattning, **ej offert** — respekterar policyn "inga fasta priser".
- **[OWNER]** verifiera/justera `RATES` (kr/m²) i `main.js` mot era egna kalkyler.

### 3. Fördjupade ort-sidor ✅
- Alla 10 orter: **≥3 unika lokala stycken** (stadsdelar, byggnadstyper, epoker, klimat/kust, logistik).
- **Unik lokal FAQ** per ort (ersätter tidigare mallade frågor).
- `LOC` omstrukturerad till dict (`intro`/`paras`/`items`/`faq`).
- **[OWNER]** riktiga lokala priser/kundcase (foton före/efter + ort) höjer E-E-A-T ytterligare.

### 4. Schema WebSite+SearchAction + HowTo + sök ✅
- `WebSite` + `SearchAction` i `index.html` → `/sok.html?q={search_term_string}`.
- Ny `sok.html`: klientbaserad sök över alla indexerbara sidor (60 poster), noindex+nolist.
- `HowTo`-schema på processidor: `takbyte.html` + `nybyggnad-villa.html`.

### 5. Meta retarget-pixel (consent-gated) ✅
- Meta Pixel i samma consent-modul; laddas **endast** efter samtycke; `Lead` på tack-sidan.
- **[OWNER]** `META_PIXEL_ID` måste fyllas i `main.js`.

### Verktyg
- Nytt: `tools/validate.py` — lint (JSON-LD, exakt 1 H1, interna länkar/ankare, sitemap-konsistens).

---

## Gap-tabell (mot briefen)

| # | Uppgift | AC | Status | Kvar / villkor |
|---|---------|----|--------|----------------|
| 1 | GA4 + Consent v2 + banner | GA4 laddas endast efter samtycke; /tack.html → konvertering | ✅ Kod klar | **[OWNER]** GA4_ID → aktiv datainsamling |
| 2 | Kalkylator + prefill | Kalkylatorsida finns + leder till form | ✅ Klar | **[OWNER]** verifiera kr/m²-spann |
| 3 | Djupare ort-sidor | ≥3 unika lokala stycken + lokal FAQ/ort | ✅ Klar (10/10) | **[OWNER]** ev. lokala priser/case |
| 4 | WebSite+SearchAction + HowTo | Valida i Rich Results Test | ✅ Kod klar | **[OWNER]** kör Rich Results Test för att bekräfta |
| 5 | Meta retarget-pixel | Consent-gated, ID → [OWNER] | ✅ Kod klar | **[OWNER]** META_PIXEL_ID |

## Acceptance-kriterier — självkontroll

- **AC1a** GA4 laddas ej före samtycke → ✅ `gtag.js` injiceras först i `grantConsent()`.
- **AC1b** /tack.html fixerar konvertering → ✅ `generate_lead` fyras när GA4 laddats på tack-sidan *(kräver GA4_ID)*.
- **AC2** Kalkylatorsida finns och leder till form → ✅ `kalkylator-takbyte.html`, CTA → `kontakt.html#form` med prefill.
- **AC3** ≥3 unika lokala stycken + lokal FAQ/ort → ✅ verifierat i genererad HTML (t.ex. 3 unika i Sundbyberg).
- **AC4** WebSite+SearchAction + HowTo valida → ✅ giltig JSON-LD (lint grön); **kör Rich Results Test för slutbekräftelse [OWNER]**.
- **AC5** Meta-pixel consent-gated → ✅ laddas i `grantConsent()`, aldrig i default-läge.

## Backlog (prioriterat)

1. **[OWNER] Fyll i ID:n** i `assets/js/main.js`: `GA4_ID` + `META_PIXEL_ID`. Utan dessa laddas ingen spårning.
2. **[OWNER] Google Business Profile** (map-pack #1-hävstång) + Google-omdömen + foto före/efter.
3. **[OWNER] Google Ads** enligt `docs/ads-plan.md` — starta efter GA4-ID + konvertering verifierad.
4. **[OWNER] Backlinks**: hitta.se, eniro, allabolag (2–3/mån) + `sameAs` när sociala konton finns.
5. Länka `sok.html` från footer/nav när de statiska sidornas footer nästa gång rörs (nu nåbar via URL + SearchAction).
6. Överväg HowTo på fler processidor (byggfirma, villarenovering) när de får riktiga steg.
7. Case-sida (referens/omdömen) när ägaren skickar foton — bygg E-E-A-T-sektion.
8. Konverteringsspårning för telefon/mail-klick (event `contact`) när GA4 är aktivt.

## Follow-up (2026-09-08) — inline consent + sök i nav/footer ✅

- **Consent Mode v2 default (denied) flyttat INLINE till `<head>`** i generatorns mall
  (`CONSENT_INLINE`), placerat FÖRE `main.js`. Future-proof för GTM. `main.js` gör nu bara
  consent-**update** efter samtycke (idempotent fallback om inline saknas via `__vtsConsentDefault`).
- **Samma inline-block tillagt i de 5 handunderhållna sidorna** (index/tjanster/om-oss/kontakt/artiklar).
- **`sok.html` inte längre föräldralös:** länk i huvudnavigationen (`Sök`) OCH i footern på alla sidor.
- Verifierat: 63/63 sidor har inline-consent före main.js (0 fel ordning) och Sök i nav + footer.
- AC1 ✅ (inline consent-default före main.js på alla genererade sidor) · AC2 ✅ (sok.html i nav på alla sidor).

## [OWNER] — blockerande fakta / åtgärder

- **GA4_ID** (Google Analytics 4 Measurement-ID) → `main.js`.
- **META_PIXEL_ID** (Meta/Facebook Pixel-ID) → `main.js`.
- **Verifiera kr/m²-spann** (`RATES` i `main.js`) för kalkylatorn — eller be om att stänga av verktyget om det krockar med "inga fasta priser"-policyn (nuvarande lösning använder branschtypiska spann med tydlig disclaimer).
- **Kör Rich Results Test** på index.html (WebSite/SearchAction) + takbyte.html (HowTo) för extern bekräftelse.
- **GBP, omdömen, foto före/efter, backlinks** — kräver ägarens identitet/inloggning (kan ej skapas av agent).

## Follow-up (2026-09-10) — GSC: 404-redirects, canonical-validering, indexering ✅

**Utgångsläge (GSC Page indexing, "villatakservice.se" domän-property):** 4 indexerade, 6 ej indexerade i 2 grupper.

### Gjort
- **Not found (404) × 3** — gamla borttagna URL:er som Google mindes. Löst med 301 i `.htaccess` (regel 4):
  - `/takrenovering-stockholm.html` → `/takrenovering.html`
  - `/takreparation-stockholm.html` → `/takrenovering.html` (ingen egen takreparation-sida finns)
  - `/bygg-renovering.html` → `/villarenovering.html`
  - Committad + pushad + auto-deployad. Verifierat live: alla tre svarar `301` mot rätt mål.
  - **"Validate fix" startad i GSC** (Started 9/10/26).
- **Duplicate without user-selected canonical × 3** — `http://…/`, `http://…/index.html`, `https://…/index.html`.
  - Redan täckt av befintliga `.htaccess`-regler (http→https, www→icke-www, index.html→/). Verifierat live: alla 301 → kanonisk `https://villatakservice.se/`.
  - **"Validate fix" startad i GSC** (Started 9/10/26).
- **Sitemap** — `sitemap.xml`: 60 URL, alla svarar 200, inga gamla 404-URL, lokal == live. `robots.txt` OK (Allow: /, pekar på sitemap). Var läst 6/9 (Google kände bara till 47 sidor) → **åter-submittad** för färsk läsning av alla 60.
- **Request Indexing (prioriterad crawl-kö):**
  - ✅ `https://villatakservice.se/` (startsidan) — skickad.
  - ⚠️ `https://villatakservice.se/takbyte.html` — **Quota Exceeded** (dagskvoten ~10-12 URL slut). Ej skickad.

### RESUME — nästa gång (börja här)
1. **[imorgon / när kvot återställts] Request Indexing** för:
   - `https://villatakservice.se/takbyte.html`
   - `https://villatakservice.se/takrenovering.html`
   - (URL Inspection-fältet uppe i GSC → klistra URL → Enter → "REQUEST INDEXING". Kräver full https-URL.)
2. **[om ~3-7 dagar] Kolla valideringsstatus** i GSC → Indexing → Pages → klicka "Not found (404)" resp. "Duplicate without user-selected canonical" → status ska gå Passed. Om "Failed": inspektera vilken URL och varför.
3. **[om ~1 vecka] Kolla sitemap** GSC → Sitemaps: "Discovered pages" bör stiga mot 60 (var 47).
4. Kvarstående [OWNER]-blockerare oförändrade: **GA4_ID + META_PIXEL_ID** i `main.js`, GBP/omdömen/backlinks (se backlog ovan).

**Not:** Request Indexing snabbar bara på crawl — ingen garanti. Valideringarna löper på egen hand (dagar–~2 v).

## Follow-up (2026-09-11) — Request Indexing (batch) + GBP skapad

### A. Request Indexing — 10 URL (dagskvot ~10-12)
Skickade "Request Indexing" i GSC (URL Inspection) för sidor som INTE var indexerade
(unknown / discovered / crawled-not-indexed):
1. tjanster.html · 2. takbesiktning.html · 3. takmalning.html · 4. taktvatt.html ·
5. villatak.html · 6. vad-kostar-takbyte.html · 7. rot-avdrag-takarbete.html ·
8. taklackage.html · 9. vad-kostar-takrenovering.html · 10. sa-valjer-du-taklaggare.html

Redan indexerade (hoppade över, sparade kvot): takbyte, takrenovering, plattak,
taklaggare-solna, hangrannor-stupror. **Not:** GSC "known pages" var stale (10 st) —
i verkligheten är fler indexerade. ~35 sidor kvar att köa nästa dagar (kvot/dag).

### B. GBP (Google Business Profile) skapad för **Geal Entreprenad AB** ✅
- Adress: Byggmästarvägen 18, 168 32 Bromma · Tel i profilen: 08-124 102 76 ·
  Website: villatakservice.se · WhatsApp-chat: https://wa.me/46707577575
- Service-area: Bromma, Sundbyberg, Solna, Spånga, Sollentuna, Järfälla, Täby, Danderyd, Lidingö, Nacka.
- Beskrivning (SE) med nyckelord (tak + villarenovering/tillbyggnad/totalentreprenad) tillagd.
- **Kategorier satta ✅ (pending review ~10 min):**
  Primär = **Roofing Service** (tak) · Sekundära = **Construction Company** (Byggföretag) + **General Contractor**.
  Not: GBP-UI på engelska → kategorier måste väljas ur listan PÅ ENGELSKA (svenska ord ger fel);
  visas ändå på svenska för svenska besökare. ("villa" finns ej som kategori → General Contractor istället.)
  Ev. senare byte: `Roofing Service` → `Roofing contractor` (= exakt Takläggare) om man vill, ej kritiskt.
- **Konton:** GBP hanteras via `870717ag@gmail.com` (samma konto som RealMar AB).
  `aleksandrgerhard@gmail.com` = 0 profiler. GBP hanteras "nya vägen" via Google Sök, ej Manager-listan.
- **Så hittar du profilen igen:** logga in på `870717ag@gmail.com` → googla "Geal Entreprenad AB"
  → panelen "Your business on Google" (Edit profile / Photos / Edit services / Ask for reviews).

### RESUME — GBP-nästa steg (börja här nästa gång, prio-ordning)
1. **Verifiera profilen** — annars syns den EJ i Maps/map-pack. Kort/video/telefon. Kräver ägaren.
2. **Foton**: logo, team, bil, före/efter-bilder (viktigt för förtroende + ranking).
3. **Edit services**: takbyte, takrenovering, takmålning, taktvätt, takbesiktning, villarenovering, tillbyggnad.
4. **Google-omdömen**: dela review-länk till nöjda kunder (starkaste map-pack-faktorn).
5. **Öppettider**: kontrollera (står nu Mon 7am).
6. **NAP-konsistens**: samma telefon/adress på sajt = GBP = allabolag (Geal Entreprenad AB, org 559303-7566).
   Kolla att GBP-tel 08-124 102 76 matchar sajten (annars byt till mobil 070-757 75 75 på båda).
7. **GSC:** fortsätt Request Indexing för resterande ~35 sidor (kvot ~10/dag).
   Kolla även valideringsstatus (404/canonical) + sitemap "Discovered pages" (mål 60).

## Follow-up (2026-09-12) — Dalarna-kluster (Borlänge + regionen) ✅

**Affärsmodell:** Geal Entreprenad AB fångar leads via egen sajt; utförande via lokal
samarbetspartner (bekant med byggföretag) på plats i Dalarna. → Samma varumärke,
en sajt. Ingen egen NAP/adress i Dalarna anges (ärlighet); ingen GBP i regionen.

### Gjort (committat + pushat, autodeploy)
- **11 nya sidor:** `dalarna.html` (hub) + `taklaggare-{borlange,falun,ludvika,
  avesta,hedemora,sater,mora,leksand,rattvik,smedjebacken}.html`.
- Unikt lokalt innehåll/ort (industri-/trähus-/bruks-historia, Siljan/fritidshus,
  snölast, frys–tö, istappar) + unik lokal FAQ. Matchar Stockholm-sidornas nivå.
- Generator: `DALARNA_AREAS` + `DAL`-dict + `slug()` + egen ort-loop
  (partner-ramverk, snörasskydd-vinkel) + hub. `render()` fick geo-override →
  `geo.region=SE-W`, `geo.placename="<ort>, Dalarna"` (Stockholm kvar SE-AB).
- Länkat: hub från `omraden.html` + footer (generator **och** 5 statiska sidor).
  Auto in i `sitemap.xml` + `sok.html`-index. `validate.py` grönt: **74 sidor, 170 JSON-LD, 0 fel**.
- Tjänster återanvänds (länkar till takbyte/takrenovering/besiktning/snörasskydd/
  taktvätt/hängrännor) — inga dubblettservice-sidor per ort (undviker doorway).

### RESUME — Dalarna nästa steg (prio)
1. **[OWNER] Partner-fakta** om товарищ vill synas: firmanamn/org.nr/ev. lokal
   adress+tel. Då kan vi lägga separat LocalBusiness/GBP i Borlänge (starkaste
   map-pack-signalen för Dalarna) — annars rankar Dalarna-sidorna organiskt.
2. `service_schema`/`local_business_schema` `areaServed` listar bara Stockholm —
   överväg per-sida-override som lägger Dalarna-orter på Dalarna-sidorna.
3. **GSC:** Request Indexing för de 11 nya URL:erna (efter deploy verifierad live).
4. Fler orter vid behov: Gagnef, Vansbro, Malung, Orsa, Älvdalen.
5. [OWNER] ev. lokala kundcase/foton från Dalarna-partnern → E-E-A-T.
