# Топ-10 — план villatakservice.se (deep research 2026-10-05)

Исходно (GSC 3 мес): 0 кликов, 4 280 показов, ср. позиция 49. Близко к топу: «takläggare bromma» 9.8, «totalentreprenad bromma» 9.5.
Источники: Whitespark LSRF 2026, Google Spam policies (doorway / scaled content), Google docs по ИИ-изображениям и IPTC. Данные GSC/SERP: `~/sites-hub/audits/2026-10-05/gsc-3m.md`.

## Что решает (по весу)
- **Карты (local pack):** GBP 32% (основная категория, близость, часы) → отзывы 20% (свежесть и ровный поток важнее количества) → on-page 15%.
- **Органика:** on-page 33% (отдельная сильная страница на каждую услугу, привязка к городу) → ссылки 24%.
- **Риск:** 20 шаблонных страниц `taklaggare-<ort>` могут попасть под doorway / scaled content. Каждой нужна уникальная польза, а слабые лучше объединить или закрыть noindex.
- **ИИ-картинки** допустимы как иллюстрации и схемы. Нельзя выдавать их за фото наших объектов. Метаданные IPTC (`trainedAlgorithmicMedia`) не удалять.
- **Предел:** без открытого адреса топ карт реален в Бромме и рядом (Sundbyberg, Solna, Spånga). В дальних городах карты, скорее всего, не взять, только органику.

## Шаги
### Владелец (вне сайта)
1. GBP: основная категория «Takläggare», дополнительные «Plåtslagare» и «Byggföretag». Плюс услуги, зоны обслуживания, часы, 20+ реальных фото, пост раз в неделю.
2. Отзывы: ссылка/QR каждому клиенту после работы, цель 2–4 в месяц ровно. Не покупать и не фильтровать. Отвечать на все отзывы.
3. Одинаковые название/адрес/телефон (NAP) на hitta, eniro, Reco, Servicefinder, Byggahus, allabolag. Ссылки от поставщиков и партнёров, местные клубы и BRF.
4. Реальные фото до/после с объектов и подтверждение гарантии и страховщика.

### Сайт (Claude Code, промт ниже)
5. Страницы услуг (takmålning, takbesiktning, takbyte, takrenovering, taktvätt) довести до 1200–1500 слов.
6. Город-страницы: уникальный контент для топ-8 по показам, остальным noindex и объединение в хаб.
7. Изображения: 2–4 на страницу (Recraft-иллюстрации плюс реальные фото, когда появятся), шведский alt, понятные имена файлов.
8. Блок доверия под H1, раздел /projekt с кейсами, AggregateRating, когда появятся отзывы.
9. Через 4 и 8 недель сравнить GSC с базой от 05.10.

---

## ПРОМТ для Claude Code (копировать целиком)

```
Проект ~/villatakservice.se (статический HTML, генерация через tools/generate.py → python3 tools/generate.py → python3 tools/validate.py должен быть зелёным → commit + push = автодеплой). Статичные страницы index/tjanster/om-oss/kontakt/artiklar правятся руками; bygg.html генерируется.
Цель — топ-10 Google.se. Прочитай docs/top10-plan.md и ~/sites-hub/audits/2026-10-05/gsc-3m.md. Работай автономно, шаг за шагом, после каждого шага — validate + commit.
Правила: текст на шведском, без фиктивных фактов (никаких выдуманных лет опыта, гарантий, отзывов, цен — цены не публикуем, только «Gratis besök och kostnadsförslag» и ROT-правила). Где нужен факт владельца — оставь пометку [OWNER] в docs/seo-worklog.md, не на сайте.

Шаг 1 — Страницы услуг (по порядку: takmalning, takbesiktning, takbyte, takrenovering, taktvatt):
- 1200–1500 слов полезного текста: когда нужно, признаки, процесс по шагам, материалы (plåt/betongpannor/tegel/papp) с плюсами и минусами, сроки и сезон в Стокгольме, ROT 2026, частые ошибки, чек-лист, FAQ 6–8 вопросов (FAQPage schema).
- H1/title/description под главный запрос из GSC (takmålning, målning plåttak, takbesiktning stockholm, takbyte pris/kostnad без цифр).
- Внутренние ссылки: на 3–5 город-страниц и 2 смежные услуги, описательный анкор.

Шаг 2 — Город-страницы taklaggare-*.html (20 шт.):
- Возьми показы из gsc-3m.md. Топ-8 (sundbyberg, bromma, danderyd, sollentuna, solna, täby, spånga, nacka) → по 900–1200 слов, у каждой уникальное: типичная застройка и эпохи района (конкретные кварталы), типичные кровли и их проблемы, климат (берег/ветер/деревья), местные правила (bygglov/детальный план, при наличии), FAQ под район, ссылки на соседние районы (NEIGHBORS) и на услуги.
- Не менять только название города в шаблоне: каждый абзац должен быть специфичен. Проверь попарную похожесть текстов (shingles/Jaccard) — цель < 30 %.
- Остальные 12 со слабым показом: оставить, но добавить уникальные 400+ слов; если невозможно сделать полезно — noindex,follow и ссылка на хаб omraden.
- Явно: офис в Бромме, остальные — зона обслуживания (без фиктивных адресов). Service-schema с areaServed.

Шаг 3 — Блок доверия под H1 на услугах и городах: телефон (tel:), «Gratis besök och kostnadsförslag», «ROT-avdrag direkt på fakturan», «F-skatt», «Ansvarsförsäkring» (последние два — только если подтверждено, иначе [OWNER]). Минимум текста, одна кнопка.

Шаг 4 — Изображения:
- Сгенерируй иллюстрации через Replicate (модель recraft-ai/recraft-v3 или актуальная Recraft; токен REPLICATE_API_TOKEN из env/~/.zshrc; если нет — найди на диске, не спрашивай) по шаблонам из раздела «Картинки» docs/top10-plan.md.
- Конвертируй в WebP 1600px (cwebp -metadata all — сохранить XMP/IPTC; если метаданных нет, проставь exiftool -XMP-iptcExt:DigitalSourceType=http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia).
- Имена: <usluga>-<что-изображено>.webp (напр. takmalning-plattak-process.webp). alt на шведском, описательный, без кейворд-спама. width/height, loading="lazy" (кроме первого), подпись «Illustration» под ИИ-картинками.
- НЕ использовать ИИ-картинки как «наш объект/до-после/кейс». Под реальные фото — папка assets/images/projekt/ (пусто, ждёт владельца).
- 2–4 картинки на услугу, 1–2 на город-страницу (разные, не одна на все).

Шаг 5 — /projekt.html (хаб кейсов) с шаблоном кейса: район, материал, проблема, что сделали, сроки, фото до/после. Пока кейсов нет — страница noindex, в worklog [OWNER]: нужны 3–5 объектов с фото.

Шаг 6 — Schema: RoofingContractor на главной (sameAs → GBP-ссылка [OWNER]), Service+areaServed, FAQPage, BreadcrumbList; AggregateRating — только когда есть реальные отзывы.

Шаг 7 — Проверка: validate.py зелёный, Lighthouse mobile ≥ 90 (картинки не ломают LCP), скриншоты 2 страниц в чат, обнови docs/seo-worklog.md (KLART/NÄSTA, дата повторной проверки GSC: +4 недели).
```

---

## Картинки (Recraft через Replicate)

Модель: `recraft-ai/recraft-v3` (style `realistic_image` для сцен, `digital_illustration` для схем), 1536×1024 (3:2).
Хвост стиля (добавлять к каждому):
`clean editorial illustration, Scandinavian suburban villa context, soft overcast Nordic daylight, muted palette with deep navy #1f2f46 accents, light gray and white, high detail, no text, no letters, no logos, no watermark, no people's faces`

Негатив: `text, letters, logo, watermark, brand names, distorted roof geometry, extra chimneys, cartoon, oversaturated colors, faces`

| Файл | Промт (+ хвост) |
|---|---|
| takmalning-plattak-process.webp | cutaway of a standing-seam metal roof being repainted: left half old faded rusty sheet, right half freshly painted dark gray, roller and spray equipment resting on the roof, Swedish 1960s villa |
| takmalning-betongpannor.webp | close-up of concrete roof tiles half cleaned and half coated with fresh black roof paint, moss removed, gentle slope |
| takbesiktning-checklista.webp | isometric diagram of a gabled villa roof with highlighted inspection points: ridge, chimney flashing, valleys, gutters, roof windows, underlayment, small numbered markers |
| takbyte-lager.webp | exploded isometric layers of a new roof: rafters, plywood decking, underlayment membrane, battens, counter battens, concrete tiles, gutter |
| takrenovering-fore-efter-illustration.webp | split illustration of the same Swedish 1970s villa roof, left mossy worn tiles, right renovated clean new tiles, clearly illustrative not a photo |
| taktvatt-mossa.webp | low-pressure roof washing of moss-covered concrete tiles, water spray, gutter protected, overcast day |
| takmaterial-jamforelse.webp | four roof material samples side by side on a light background: standing-seam steel, concrete tile, clay tile, bitumen roofing felt |
| ort-<stad>-villa.webp | typical <EPOCH> <HOUSE TYPE> villa in <STAD> Stockholm suburb with <ROOF MATERIAL> roof, birch and pine trees, autumn — по 1 уникальной на топ-8 городов |

Значения для ort: Bromma — 1930s funkis villa, red clay tile; Sundbyberg — 1950s villa, concrete tile; Danderyd — large 1920s villa, black standing-seam steel; Sollentuna — 1970s split-level, concrete tile; Solna — 1940s small villa, red clay tile; Täby — 1970s radhus row, bitumen felt; Spånga — 1960s villa, brown concrete tile; Nacka — seaside villa on rock, standing-seam steel.
