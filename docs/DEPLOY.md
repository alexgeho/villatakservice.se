# Deploy — villatakservice.se

Live-sajten ligger på en LiteSpeed-hosting (FTP), **inte** kopplad till GitHub automatiskt.
Repot är sanningskällan; hostingen uppdateras via FTP-deploy (GitHub Actions).

## Engångsuppsättning (autodeploy)
1. Skaffa FTP-uppgifter från din hostingleverantör (host, användarnamn, lösenord).
2. I GitHub: **Settings → Secrets and variables → Actions → New repository secret**, lägg till:
   - `FTP_SERVER` (t.ex. `ftp.villatakservice.se`)
   - `FTP_USERNAME`
   - `FTP_PASSWORD`
3. Kontrollera `.github/workflows/deploy.yml`:
   - `server-dir`: `./` om FTP-kontot redan pekar på webbroten, annars `/public_html/`.
   - `protocol`: `ftps` (byt till `ftp` om hosten inte stödjer FTPS).
4. Kör deploy: fliken **Actions → Deploy to hosting (FTP) → Run workflow** (eller pusha en commit).

Efter första lyckade körningen deployar varje push till `main` automatiskt.

## Verifiera efter deploy
- `https://villatakservice.se/` visar nya versionen (namn "Geal Entreprenad AB", nav "Områden").
- `https://villatakservice.se/sitemap.xml` ger **HTTP 200** (inte 404).
- `https://villatakservice.se/robots.txt` ger 200.

## Google Search Console
1. Sitemaps → ta bort den gamla raden med status "Couldn't fetch" (⋮ → Remove).
2. Lägg till `sitemap.xml` på nytt och Submit. När sitemap ger 200 blir status "Success".
3. (Valfritt) URL inspection på några nya sidor → "Request indexing".

## Felsökning
- **"Couldn't fetch" / 404 på sitemap** = filerna finns inte på servern → kör deploy.
- **Filerna hamnar i fel mapp** = justera `server-dir` (./ vs /public_html/).
- **Anslutning nekas** = testa `protocol: ftp` istället för `ftps`, kontrollera host/port hos leverantören.
