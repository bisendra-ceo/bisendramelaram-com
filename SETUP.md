# Going live on Cloudflare Pages

This repo is a plain static site. The files Cloudflare serves are in `site/`. There is no build step.

## Before launch

1. Fill the placeholders. Every unfinished spot shows on the page as a yellow `[To fill: ...]` box. Run `python3 tools/build.py` and it prints how many are left. The list of what's needed is in `NEEDED.md`.
2. Flip `LAUNCH = False` to `LAUNCH = True` at the top of `tools/build.py`, then run `python3 tools/build.py` again. Until then every page carries a `noindex` tag, so Google and AI tools won't index unfinished pages even if the site is live.
3. Commit and push.

## Compliance check (do this before launch)

- New York advertising rules: every page shows your name as Licensed Real Estate Salesperson with Keller Williams Greater Nassau, the office address and office phone. Keep it that way.
- Titles: a March 2025 HGAR legal column says DOS allows licensees only the titles real estate broker, associate real estate broker or real estate salesperson, and bars corporate titles like president or vice president unless you are an officer of the licensed corporation. It doesn't mention CEO either way. The site leaves "CEO" off until your broker or attorney clears it.
- Fair housing: the `/fair-housing/` page on bisendramelaram.com needs the DOS Housing and Anti-Discrimination Notice and the Keller Williams Greater Nassau standard operating procedures (or links to them). Get both from your broker.

## Cloudflare setup, in order

1. Create a free Cloudflare account at dash.cloudflare.com.
2. Add your domain (Websites, Add a site, Free plan). Cloudflare gives you two nameservers. Log in where you bought the domain and replace its nameservers with those two. This can take a few hours to switch over.
3. Go to Workers & Pages, Create, Pages, Connect to Git. Pick GitHub and allow access to this repo only.
4. Build settings:
   - Production branch: the branch holding this code (see the note at the bottom)
   - Framework preset: None
   - Build command: leave empty
   - Build output directory: `site`
5. Save and Deploy. You get a free `*.pages.dev` preview address. Check it before attaching the domain.
6. In the Pages project, open Custom domains, add the bare domain (`bisendramelaram.com`) and then `www`. Cloudflare creates the DNS records.
7. Redirect `www` to the bare domain: Rules, Redirect Rules, from `www.yourdomain/*` to `https://yourdomain/${1}` with a 301.

## Make sure AI crawlers can get in

Cloudflare can block AI crawlers on your behalf, which would undo the whole point of these sites.

1. In the domain's dashboard, open Security, Bots (on some accounts it's under AI Crawl Control or AI Audit). Turn off "Block AI bots" / "Block AI Scrapers and Crawlers".
2. In AI Crawl Control, set search and assistant crawlers (GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot, Google-Extended, Applebot) to Allow. Do not block any category that includes Googlebot or Bingbot.
3. Turn off "Managed robots.txt" (or "Instruct AI bot traffic with robots.txt") so Cloudflare doesn't replace the `robots.txt` in this repo.
4. Leave Bot Fight Mode off. It can challenge real crawlers.
5. Check it worked: open `https://yourdomain/robots.txt` and confirm it is the file from this repo, starting with "Search engines and AI assistants are welcome here."

## After launch

1. Google Search Console: add the domain property, verify with the DNS record Cloudflare can add for you, and submit `https://yourdomain/sitemap.xml`.
2. Bing Webmaster Tools: import from Search Console, or add the site and submit the same sitemap. ChatGPT search leans on Bing, so don't skip this.
3. Test a page in Google's Rich Results Test and the Schema Markup Validator (validator.schema.org).
4. Refresh market numbers monthly, change `UPDATED` in `tools/build.py`, rebuild and push. The sitemap dates update with it.

## Branch note

These files were pushed to the branch `claude/project-thread-3ual3x`. Because the repo was empty, GitHub likely made it the default branch. Either point Cloudflare's production branch at it, or rename it to `main` in GitHub (Settings, Branches) and use `main`.
