# Content calendar for bisendramelaram.com

Fresh, dated facts are what get a page quoted by Google and AI assistants. Every refresh ends the same way: change `UPDATED` and `UPDATED_TEXT` in `tools/build.py`, add a dated line to `UPDATES`, rebuild, and redeploy.

## Every month
- When OneKey MLS posts the new Nassau County Local Market Update, add the month to `ONEKEY_2026` (and the prior-year row to `ONEKEY_2025`) and its link to `ONEKEY_REPORTS` in `tools/seller_guides.py`. This updates the pricing and best-time pages. Then update the September figures quoted in the pricing and cost answers if a newer month changes them.
- Publish one new seller question as its own page when Bisendra hears a new one from clients. Add it to `GUIDES` and it lands in the sitemap, llms.txt and the sellers hub automatically.
- Fill one more yellow box with Bisendra's own words (see NEEDED.md).

## Fixed dates
- Early December: confirm the next Assessment Review Commission window and update the property taxes guide.
- January: recheck the New York transfer tax page, the nonresident estimated tax form (IT-2663) for the new year's rate, and the Town of Hempstead tax schedule.
- After any change in New York disclosure law: update the property condition disclosure guide and its sources.
- After any change to NAR or MLS commission rules: update the cost-to-sell and choosing-a-listing-agent guides.

## Every quarter
- Reread every seller guide's sources and update the "checked" month (`CHECKED` in `tools/seller_guides.py`).
- Check that every outside link still opens.
