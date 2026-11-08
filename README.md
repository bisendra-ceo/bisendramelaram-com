# bisendramelaram.com

Plain static site for bisendramelaram.com, by Bisendra Melaram.

- `site/` is what gets published. Cloudflare Pages serves it with no build command.
- `tools/build.py` holds the content and builds `site/`. Edit it, then run `python3 tools/build.py`.
- `SETUP.md` has the Cloudflare Pages steps, crawler settings and launch checklist.
- `NEEDED.md` lists what's still needed from Bisendra.

Every page has a direct answer up top, question-style headings, schema.org markup (Person, RealEstateAgent, Article, FAQPage, BreadcrumbList), a byline and last-updated date, plus robots.txt, sitemap.xml and llms.txt.
