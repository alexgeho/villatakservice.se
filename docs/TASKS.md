# TASKS — villatakservice.se (главный сайт; takbytepris.nu — сателлит)

## 2026-10-31 — стратегия Ting (seo-arkitektura.md)
- [x] калькулятор takbyte в первом экране главной (вместо фото справа); расчёт → заявка с предзаполненным сообщением
- [x] тексты для каталогов hitta / eniro / reco.se (+ allabolag, Google) с одинаковым NAP Geal Entreprenad AB → docs/kataloger.md
- [ ] владелец (BankID/логин): hitta, eniro, allabolag — добавить тел+сайт+категорию; reco.se — создать профиль
- [x] часы 08–17 везде (решение владельца 31.10): GBP изменён (на модерации), сайт уже 08–17

## 2026-11-07 — SEO-уровень
- [x] SEO-уровень 07.11: golvslipning Lidingö/Danderyd/Huddinge (поз. 10–21) — title/description под запрос + ответ вверху (услуга, бесплатный визит, ROT 30 %)

## 2026-11-07 — страницы услуг как лендинги (владелец: «как taklia»)
- [x] форма заявки в hero всех страниц услуга×район (605 стр.), E-post обяз., Telefon не обяз., источник = страница
- [x] картинки страницы — галерея сразу под hero
- [x] блок доверия (только реальные факты) + кнопки «Få offert» ведут к форме на странице
- [x] sendmail.php: ошибка возвращает на ту же страницу
- [x] новые картинки Replicate (240 шт., 80 страниц) для страниц с показами
- [ ] отзывы/референции — только реальные (нужны от владельца / Google)
- [x] hero: фоновая картинка во весь экран + форма поверх (владелец 07.11)
- [x] преимущества сразу под hero, потом галерея
- [ ] партнёры/сертификаты — только реальные у Geal (у taklia это фирма Daniel — брать нельзя), ждём список от владельца
- [x] (09.11 ersatt av rollout_ds) эталон taklia (владелец 07.11) — ПИЛОТ только taklaggare-sollentuna, ждёт «ок», потом tools/landing_v3.py на все: форма 2 колонки + Ort + «Bifoga bild», фото рядом с текстом, «Begär offert» с формой внизу
- [ ] фото реального консультанта в форму (как «Johan» на taklia) — нужно фото владельца/сотрудника
- [x] (владелец 07.11) «текстовых полотен не должно быть» — пилот takbyte.html: 8 блоков фото+текст зигзагом, интро + 3–4 факта, фоны чередуются; 5 новых картинок
- [x] (09.11 rollout_ds.py, 683 sidor) после «ок» по пилоту takbyte: то же на всех страницах (включая главную, блок «Takbyte» со скриншота) + landing_v3
- [x] (владелец 07.11) дизайн-система taklia на пилоте takbyte: Fraunces/Inter, акцентное слово в H2, радиус 0, шапка (лого | меню | телефон + Kontakt), форма 417/36, блоки 90, фоны чередуются — assets/css/ds-taklia.css
- [x] логотип Recraft: 12 вариантов на рабочем столе (villatak-logo) — владелец выбрал 5A, стоит в шапке пилота (assets/images/logo-villatak-5a.svg); favicon — при раскатке
- [x] критик: пилот takbyte vs taklia + DS → 25 пунктов исправлены (кроме выпадающих меню и 2-рядной шапки 1024 — проверить после «ок»)
- [x] 09.11 Ägaren (pilot takbyte): inte foto+bockar i varje block — blanda: foto+bockar / foto+2 stycken / bara text 2 stycken (epoker, tid = text; material = foto+stycken)
- [x] 09.11 Ägaren «Da» → utrullning av pilot takbyte till 683 landningssidor (tools/rollout_ds.py, körs i generate.py; takbyte.html skyddad i HAND_MADE)
- [ ] Startsidan + statiska sidor (index, tjanster, om-oss, kontakt, artiklar) i DS taklia — inte gjort än
- [ ] Artiklar (article-shell) — oförändrade prosa-sidor, besluta om de ska få DS
- [x] 09.11 Ägaren: ikoner i Recraft för steg och «Därför väljer kunder oss» (tools/ikoner_ds.py klart, väntar på ikonfiler)
- [x] 09.11 Ägaren «такие сделай иконки» (taklia): illustrationer i taklia-stil (Recraft-stil från taklias steg/why, accent #A8431F) på steg och fördelar, alla sidor
- [x] 09.11 Ägaren: illustrationer «мрачно, дом серый» → allt positivt, ljust (ljusa hus, tegeltak, mycket vitt, lätt skuggning) — ny Recraft-omgång v2 — klar: Recraft-stil «Villatakservice bright ink v2» (716d3e40…), 23 PNG + webp i assets/icons
- [x] 09.11 Ägaren «сделай большие картинки»: illustrationer 240 (fördelar) / 200 (steg); fix CSS-selector efter ?v=
- [x] 09.11 «посещает работяга а не фраер»: fordel-besok — рабочий в спецодежде (каска/комбинезон), не человек в рубашке; правило для всех иллюстраций с людьми
