# villatakservice.se — персональный next-level бриф (SEO/growth)

> Заточен по аудиту 2026-09-08. Агент: прочти это + docs/seo-worklog.md + docs/seo-agent-brief.md
> + docs/ads-plan.md, веди docs/next-level-worklog.md. Автономно, owner-факт → [OWNER] + дальше.

**Стек:** ЧИСТЫЙ статический HTML — 61 файл `.html` генерируются Python-скриптом
`tools/generate.py` (общий head/header/footer/schema + блок PAGES) → правь ГЕНЕРАТОР, не
руками .html. Деплой = GitHub Actions FTP. Компания: **Geal Entreprenad AB** (org 559303-7566).

**Что уже зрело (НЕ переделывай):** уникальные title/desc/canonical/OG на всех 61, полная
schema (RoofingContractor/Organization/Service/FAQ/Article/Breadcrumb/Image), чистые
sitemap/robots/.htaccess, ~26 статей блога, 10 city-страниц, консистентный NAP, отличный CWV.

**Задачи (приоритет сверху):**
1. **Аналитики НЕТ ВООБЩЕ — начни с этого (блокирует весь ads-plan).** Встрой в общий head
   генератора GA4 + Consent Mode v2 (default denied) + cookie-баннер. На `sendmail.php`-успех
   (страница `/tack.html`) — событие конверсии generate_lead. AC: GA4 грузится только после
   согласия; заход на /tack.html фиксирует конверсию в GA4.
2. **Калькулятор стоимости takbyte как лид-магнит.** Сейчас `main.js` = только меню+аккордеон.
   Добавь интерактивный оценщик (площадь/материал/уклон → диапазон + ROT) на отдельной
   странице, префилл контактной формы. AC: страница-калькулятор существует и ведёт в форму.
3. **Углуби city-страницы (не добавляй новые).** Сейчас ~15% уникального на страницу (риск
   «scaled content»). Больше локальной специфики: районы, тип застройки, локальные цены/кейс,
   уникальный FAQ на город. AC: ≥3 уникальных локальных абзаца + локальный FAQ на каждый город.
4. **Schema-добивки:** WebSite+SearchAction (sitelinks searchbox) + HowTo на процессных
   страницах («så gör vi»). AC: валидны в Rich Results Test.
5. **Ретаргет-пиксель Meta** consent-gated — под запланированные Google/Meta Ads. ID → [OWNER].

**[OWNER] (главный рост):** Google Business Profile (#1 для кровельщика — map-pack), реальные
отзывы, фото «до/после» (E-E-A-T), бэклинки (hitta/eniro/allabolag), запуск Ads после п.1.

**Верификация:** независимый агент-ревьюер проверит по AC + git diff (CONFIRMED/провал).
