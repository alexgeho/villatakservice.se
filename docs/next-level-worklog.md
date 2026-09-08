# Next-level worklog — villatakservice.se

> Genomförande av `docs/next-level-brief.md`. Autonomt läge, blockerande ägarfakta = **[OWNER]**.
> Bygg: `python3 tools/generate.py` · Lint: `python3 tools/validate.py` (bägge gröna).
> Status: **5/5 uppgifter klara.** 63 sidor, 148 JSON-LD-block, 0 lint-fel.

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
