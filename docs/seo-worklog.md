# SEO-worklog — villatakservice.se

> Läs `docs/seo-agent-brief.md` för hela briefen. **Svara ägaren kort och rakt på sak.**
> Statuslegend: ☐ ej påbörjad · 🔄 pågår · ✅ klar. Vid omstart: fortsätt från första ☐/🔄.
> Sidor byggs via `tools/generate.py` (kör `python3 tools/generate.py`).

---
## ▶️ RESUME — börja här nästa gång (uppdaterad 2026-09-06)

**Läge:** Sajten är LIVE i prod. **61 sidor.** Autodeploy (push till main → FTP till hostingen, se `docs/DEPLOY.md`). Sitemap **Success** i GSC (Google indexerar själv).

**Klart hittills:**
- Teknik/SEO: NAP (Geal Entreprenad AB, Byggmästarvägen 18 Bromma, org 559303-7566, info@villatakservice.se), RoofingContractor/Service/FAQ/Article/Breadcrumb-schema, canonical, sitemap.xml, robots.txt.
- Money-kärna: 6 taktjänster + villa-pillar + områdes-hub + 10 ort-sidor.
- **Bygg & Renovering (7 sidor):** bygg (hub), byggfirma/total entreprenad, villarenovering, tillbyggnad, attefallshus, friggebod, nybyggnad-villa, fritidshus.
- Artiklar: 24 st (kluster + near-miss: mala-plattak, falsat-plattak, attefallshus-regler, vad-kostar-bygga-hus).
- UX/perf/a11y: self-hostat Inter, lokala webp, favicon, 404, tack, skip-link/focus, 0 externa resurser.
- **Kontaktformulär funkar** (egen `sendmail.php` → info@villatakservice.se, testat OK).
- Data: `docs/keywords/*.csv` + `analys.md`. Ads: `docs/ads-plan.md`.
- Cron "SEO-puls" (routine `trig_01EF7TMEUzn3jvNkZ2PjX6Fg`): 1 & 15 varje månad, rapport i routines-UI.

**NÄSTA STEG (prio):**
1. **Ägaren (viktigast):** GBP + Google-omdömen + backlinks (hitta.se/allabolag); starta Google Ads enligt `docs/ads-plan.md` + koppla konvertering (mål `/tack.html`) FÖRE skalning; Request indexing topp-3 (bygg/byggfirma/attefallshus) när kvoten nollställts.
2. **~15 sep (nästa byggomgång):** läs GSC-queries pos 8–20 (near-miss) → gör 3–5 riktade sidor/förstärkningar (Fas 3, datadrivet).
3. **Content-tempo:** 2–4 kvalitetsartiklar/vecka ur klusterplanen (inte massgenerering).
4. **Case före/efter:** när ägaren skickar foton → bygg referens-sektion (E-E-A-T).
5. **Ev. fler near-miss** (kolla volym i `docs/keywords`): uterum/inglasat, garage/carport, badrums-/köksrenovering, ta bort takmossa m.fl.

**Så fortsätter du:** läs `docs/seo-agent-brief.md` + denna fil → plocka första öppna punkten ovan. Sidor: redigera `tools/generate.py`, kör `python3 tools/generate.py`, validera, commit+push (auto-deploy). Skriv "продолжаем" för att dra igång.
---

## Audit — nuläge (2026-09-06)
- **Stack:** ren statisk HTML, ingen byggprocess. 6 sidor i repo-roten + `assets/`.
- **Kritiskt:** all schema/og pekar på fel domän `www.gealtak.se` (ska vara villatakservice.se). Namn växlar "Geal Tak AB" / "Geal entreprenad ab" → ska vara **Geal Entreprenad AB**.
- **Saknas:** canonical, og:url, geo-meta, sitemap.xml, robots.txt, RoofingContractor/Breadcrumb-schema, location-sidor, per-tjänst money pages, riktiga artikelsidor (bloggen = 1 statisk `artikel.html`).
- ** Warning:** obekräftade påståenden redan på sajten ("10+ års erfarenhet", "5 års garanti", "offert inom 24h", artikeldatum). → frågelista.

## 1. Teknisk grund + NAP/schema  ✅
- ✅ Generator `tools/generate.py` (delad header/footer/head/schema) — kör `python3 tools/generate.py`
- ✅ NAP-fix: namn Geal Entreprenad AB, domän villatakservice.se, canonical, og:url, geo-meta, twitter (alla 45 sidor)
- ✅ RoofingContractor + BreadcrumbList-schema (index+kontakt+alla nya); FAQPage/Service/Article per typ
- ✅ robots.txt + sitemap.xml (46 URL:er)
- ✅ Nav: "Områden" tillagd på alla sidor; footer fick Områden-kolumn; tjänstekort länkar till money pages

## 2. Money-kärna  ✅
- ✅ Tjänstesidor (6): takbyte, takrenovering, takbesiktning, plattak, takmalning, taktvatt (H1, intent-intro, "vad ingår", process, ROT-box, FAQ+schema, CTA)
- ✅ Villa-pillar: villatak.html (villatak, villatak stockholm, takbyte villa)
- ✅ Områdes-hub: omraden.html
- ✅ Location-matris (10): Sundbyberg, Solna, Bromma, Spånga, Sollentuna, Järfälla, Täby, Danderyd, Lidingö, Nacka — unik lokaltext/ort
- ✅ Intern länkning tjänst↔ort↔artikel↔pillar med sökords-ankare (0 orphans)

## 3. Cluster-artiklar (topical authority)  ✅
Bottom-funnel: ✅ vad-kostar-takbyte ✅ vad-kostar-takrenovering ✅ takbyte-eller-takrenovering ✅ rot-avdrag-takarbete ✅ sa-valjer-du-taklaggare ✅ bygglov-takbyte ✅ nar-ska-taket-bytas
Problem: ✅ taklackage ✅ fuktskada-mogel-vind ✅ mossa-pa-taket ✅ istappar-isbildning
Komponenter: ✅ hangrannor-stupror ✅ takfonster ✅ taksakerhet-snorasskydd ✅ skorstensrenovering
Material/energi: ✅ tegel-betong-plattak ✅ takmaterial-livslangd ✅ vindsisolering ✅ solceller-tak `[scope?]` ✅ energieffektivt-tak
Säsong: ✅ takarbete-vintern ✅ var-checklista-tak
- ✅ Byggt om artiklar.html-hubben (riktiga länkar) + tog bort dubblett-sidan artikel.html

## 4. Verifiering  ✅
- ✅ 45 HTML-sidor: 0 trasiga länkar, 0 dubbletttitlar, exakt en H1/sida, 0 orphans
- ✅ 102 JSON-LD-block valida; sitemap.xml valid XML; alla sidor i sitemap
- ✅ Alla använda CSS-klasser finns i style.css

## 5. Nästa (kommande sessioner)  ☐
- ☐ Fler komponent-/materialsidor vid behov (undertak/underlagspapp, vindskivor/fotplåt, bandtäckning, papptak, sedumtak, snöskottning)
- ☐ E-E-A-T: bygg ut Om oss (erfarenhet/cert), case före/efter med ort+foto `[ПОДТВЕРДИТЬ]`
- ☐ Data-driven: dra GSC Queries var 2–4 v, ta near-miss (pos 8–20) → nya sidor
- ☐ När fakta bekräftats: fyll i priser, ROT-siffror 2026, garanti, sameAs/GBP

## ROADMAP (SEO-strategi — kvalitet före kvantitet)
> Princip: **inte** massproducera sidor. Google "scaled content abuse" (mars 2024) straffar det, särskilt på ung domän. Ett intent = en stark sida. Mål: ~5–15 nya kvalitetssidor/vecka, inbyggda i länkning. Expandera på DATA (GSC near-miss), inte blint.

**✅ Fas 0 (klart):** money-kärna (tjänst×ort), villa-pillar, 22 artiklar, teknik/schema/sitemap, live-deploy, kontaktformulär.

**▶️ Fas 1 (KLAR 2026-09-06) — Bygg & Renovering (utökad scope från Keyword Planner):**
- ✅ bygg.html (hub) + byggfirma/total entreprenad, villarenovering, tillbyggnad, attefallshus, nybyggnad-villa (5 money-sidor, Service+FAQ-schema, korrekt ROT-info)
- ✅ Förstärkt tak: artiklar `mala-plattak.html`, `falsat-plattak.html`
- ✅ "Bygg" i nav + footer; intern länkning från tjanster/index/villatak; landing-sidor klara för Google Ads
- Totalt 57 sidor, validering grön (0 trasiga, 0 orphans, 131 JSON-LD ok).
- Data (Planner, Sverige/mån): attefallshus 50k · byggfirma 5k (Low konk!) · nyckelfärdigt hus/hustillverkare/bygga fritidshus 5k · hantverkare 5k · måla/falsat plåttak 5k.

**▶️ Fas 2 (v 3–8) — trust + tempo:** GBP + omdömen + case (viktigast lokalt); 2–4 kvalitetsartiklar/vecka ur klusterplanen; 2–3 naturliga backlinks/mån (hitta.se, allabolag).

**▶️ Fas 3 (mån 2+) — datadriven expansion:** varannan vecka (cron-agent "SEO-puls") dra GSC-queries pos 8–20 → punktvis nya/förstärkta sidor. Ingen massgenerering.

**Mätning:** GSC-position på plattform-sökord + near-miss; visningar/klick; map-pack.

## Register: tema → sökord → URL → status → inkommande
| Kluster | Målsökord | URL | Status |
|---|---|---|---|
| Pillar villa | villatak, tak på villa | villatak.html | ✅ |
| Money | takbyte, takbyte pris | takbyte.html | ✅ |
| Money | takrenovering, takomläggning | takrenovering.html | ✅ |
| Money | takbesiktning, besikta tak | takbesiktning.html | ✅ |
| Money | plåttak | plattak.html | ✅ |
| Money | takmålning | takmalning.html | ✅ |
| Money | taktvätt, ta bort mossa | taktvatt.html | ✅ |
| Ort×tjänst | takläggare [ort] | taklaggare-*.html (10) | ✅ |
| Beslut | vad kostar takbyte | vad-kostar-takbyte.html | ✅ |
| Beslut | rot-avdrag tak | rot-avdrag-takarbete.html | ✅ |
| Beslut | välja takläggare | sa-valjer-du-taklaggare.html | ✅ |
| Beslut | bygglov takbyte | bygglov-takbyte.html | ✅ |
| Problem | takläckage | taklackage.html | ✅ |
| Problem | fukt/mögel vind | fuktskada-mogel-vind.html | ✅ |
| Problem | mossa på taket | mossa-pa-taket.html | ✅ |
| Problem | istappar/isbildning | istappar-isbildning.html | ✅ |
| Komponent | hängrännor/stuprör | hangrannor-stupror.html | ✅ |
| Komponent | takfönster | takfonster.html | ✅ |
| Komponent | taksäkerhet/snörasskydd | taksakerhet-snorasskydd.html | ✅ |
| Komponent | skorstensrenovering | skorstensrenovering.html | ✅ |
| Material | tegel vs betong vs plåt | tegel-betong-plattak.html | ✅ |
| Material | takmaterial livslängd | takmaterial-livslangd.html | ✅ |
| Energi | vindsisolering | vindsisolering.html | ✅ |
| Energi | energieffektivt tak | energieffektivt-tak.html | ✅ |
| Energi | solceller tak `[scope]` | solceller-tak.html | ✅ |
| Säsong | takarbete vintern | takarbete-vintern.html | ✅ |
| Säsong | vår-checklista tak | var-checklista-tak.html | ✅ |

## Ägarsvar (2026-09-06) — inarbetade ✅
1. ✅ Namn = Geal Entreprenad AB.
2. ✅ Domän villatakservice.se, icke-www (canonical).
3. ✅ E-post → info@villatakservice.se (bytt överallt).
4. ✅ Pris: "gratis platsbesök och kostnadsförslag" — inga fasta priser publiceras.
5. ✅ ROT 2026 verifierat (Skatteverket via BraByggare): 30 % av arbetskostnaden, max 50 000 kr/person/år, ROT+RUT gemensamt tak 75 000 kr/person/år. Inarbetat i rot-box + rot-artikel.
6. ✅ "10+ års erfarenhet / 5 års garanti / offert inom 24h" bekräftade — kvar.
7. ✅ Cert: F-skatt + ansvarsförsäkring + ID06 — tillagt i Om oss + villatak-pillar.
8. 🔄 Case före/efter: ägaren skickar foton → bygg referens-sektion/-sida när de kommer.
9. ✅ NYTT: registrerad adress **Byggmästarvägen 18, 168 32 Bromma** (ej Lavettvägen/Sundbyberg). Bytt i NAP/schema/footer/kontakt/karta. Bas i copy flyttad till Bromma (Mariehäll); Sundbyberg kvar som topp-prioriterat närområde.
10. ✅ Org.nr 559303-7566, moms SE559303756601 — i schema (identifier/vatID) + footer + Om oss.
11. ✅ Solceller: vi monterar — scope-reservation borttagen.
12. ✅ Skorsten: vi gör allt (inkl. murning) — reservation borttagen.
13. ✅ Vindsisolering: vi utför — reservation borttagen.
14. ✅ Total entreprenad (hela villan) — nämnt i Om oss + villatak.

### Kvar hos ägaren
- 🔄 Skicka case-foton (före/efter + ort).
- ☐ sameAs: sociala konton finns ej ännu. **OBS: jag kan inte skapa konton åt er** (kräver er identitet/inloggning). Skapa GBP + ev. Facebook/Instagram → skicka URL:er så wire:ar jag `sameAs`.
- ☐ GBP skapas, omdömen samlas, sitemap skickas till GSC, kataloger (hitta.se/eniro/allabolag).

## Ägaruppgifter (utanför repot — imitera ej)
- Google Business Profile: skapa/fyll, kategori RoofingContractor, foton, områden.
- Samla Google-omdömen.
- Backlinks: hitta.se, eniro, allabolag, branschkataloger.
- Skicka sitemap.xml till GSC efter deploy.

## 6. E-E-A-T (från extern audit-checklista)  🔄
Tillämpat på villatakservice.se:
- ✅ Integritetspolicy (GDPR) `integritetspolicy.html` + länk i footer på alla sidor + länk från formulärets samtyckesruta.
- ✅ Separat FAQ-sida `faq.html` med FAQPage-schema (footer-länk).
- ✅ Kontakt förstärkt: org.nr, "Så hittar du hit" + parkering; karta/adress = Bromma.
- ✅ Om oss förstärkt: F-skatt, ansvarsförsäkring, ID06, org.nr, total entreprenad.
- ✅ Redan uppfyllt: multi-sidor (ej landningssida), unika title/desc/H1, interna "Läs mer" (ej externa), giltig HTML-struktur, aktuellt år i footer (auto), sitemap/robots/canonical/schema.
- ☐ Ägare: samla omdömen (Google/Trustpilot), case före/efter, backlinks, säkerställ stabilt SSL på hosting.
- ☐ Ev. senare: sidan "Villkor" + "Referenser/Omdömen" (bygg när case/omdömen finns).

## 7. UX/UI + prestanda/integritet (självständigt)  ✅
- ✅ A11y: `:focus-visible`, skip-to-content, `prefers-reduced-motion`, `scroll-margin-top` (sticky header).
- ✅ Bugg: 17 trasiga in-page-ankare (Snabblänkar) → sektioner fick riktiga id:n.
- ✅ Favicon (`assets/favicon.svg`, tak-ikon) + `theme-color` på alla sidor.
- ✅ 404-sida (`404.html`, noindex, ej i sitemap) med populära länkar.
- ✅ **Självhostat typsnitt**: Inter (variabel, latin-subset) i `assets/fonts/` + `@font-face`. Google Fonts borttaget överallt → inga externa font-requests (GDPR/prestanda).
- ✅ **Lokala bilder**: pexels-hotlinks på startsidan nedladdade, komprimerade till webp i `assets/images/` → 0 externa bild-requests.
- ✅ Resultat: 48 sidor, 0 externa resurser (font/bild), 0 trasiga länkar/ankare, 106 JSON-LD ok.
- ☐ Kvar (ägare/funktion): kontaktformulärets `action="#"` behöver riktig hanterare (Formspree/Getform/hosting); ev. äkta dark-tema via `prefers-color-scheme`.

## ⏰ Öppna ägaruppgifter — PÅMINN OM DESSA (läses av cron-agenten "SEO-puls")
- [ ] **Google Business Profile** – skapa/fyll (kategori Roofing contractor, adress Bromma, foton, områden). Största lokala hävstången.
- [ ] **Google-omdömen** – be nöjda kunder om 3–5 recensioner.
- [ ] **Backlinks** – hitta.se, eniro, allabolag, branschkataloger (2–3/mån).
- [ ] **Google Ads** – starta enligt `docs/ads-plan.md` (prio Tak + Byggfirma). Koppla konvertering (mål = /tack.html) FÖRE skalning.
- [ ] **Request indexing** (imorgon, kvot nollställd) – bygg.html, byggfirma.html, attefallshus.html. Ev. re-submit sitemap för snabbare omläsning.
- [ ] **Case före/efter** – skicka foton + ort → bygg referens-sektion.
- [ ] Nästa contentomgång: efter GSC-data (near-miss pos 8–20) ~15 sep.

## Logg
- 2026-09-07: **GSC-fix "Duplicate without user-selected canonical"** → `.htaccess` med 301 (http→https, www→icke-www, /index.html→/) + säkerhetsheaders (HSTS, nosniff, X-Frame, Referrer/Permissions-Policy) + cache-headers. Verifierat LIVE: alla redirects 301 rätt, headers aktiva. Full teknisk audit körd: 0 dubbletttitlar/desc, alla canonicals rätt host, 59/59 sitemap-URL:er = 200, 404 ger 404, 143 JSON-LD valida, sitemap lastmod färsk. **Ägaren:** klicka "VALIDATE FIX" i GSC på duplicate-felet. Kvar (valfritt): titlar >60 tecken (kosmetiskt), OSM-kart-iframe på kontakt = enda externa requesten.
- 2026-09-06: Fas 1b — +friggebod, +fritidshus (bygg), +attefallshus-regler, +vad-kostar-bygga-hus (near-miss). Ads-kampanjplan i docs/ads-plan.md. 61 sidor, validering grön (0 trasiga/orphans, 143 JSON-LD).
- 2026-09-06: LIVE i prod via FTP-autodeploy (GitHub Actions). Sitemap submittad + "Success" i GSC (47 URL). Kontaktformulär byggt utan tredjepart (`sendmail.php` → info@villatakservice.se, honeypot + validering + tack.html). Testat: valid→tack, ogiltig→fel, honeypot→tyst.
- 2026-09-06: UX/UI + a11y + prestanda: focus/skip-link/reduced-motion/scroll-margin, favicon, 404, självhostat Inter, lokala webp-bilder. 0 externa resurser kvar.
- 2026-09-06: E-E-A-T-audit (bygghub.nu) genomläst; tillämpliga punkter inarbetade — integritetspolicy, FAQ-sida, förstärkt kontakt/om-oss. 47 sidor totalt, validering grön (0 trasiga, 0 orphans, 105 JSON-LD ok).
- 2026-09-06: Audit klar. Brief + worklog uppdaterade med autonomt läge + topical-authority-addendum.
- 2026-09-06: Byggt generator + 40 nya sidor (6 tjänster, villa-pillar, områdes-hub, 10 orter, 22 artiklar), patchat 6 ursprungssidor (NAP/domän/nav/footer/schema), skapat sitemap.xml + robots.txt, byggt om artiklar-hubben, tagit bort dubblett artikel.html. Verifiering grön (0 trasiga länkar, 0 orphans, 102 valida JSON-LD). Totalt 45 sidor.
