#!/usr/bin/env python3
"""Builds bisendramelaram.com into ../site as plain static HTML.

Edit the content below, then run:  python3 tools/build.py
Cloudflare Pages serves the /site folder as is (no build command).
"""
import json
import os
import shutil
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
STATIC = os.path.join(ROOT, "tools", "static")

DOMAIN = "https://bisendramelaram.com"
GUIDE = "https://longislandhomes.co"
# Keep False until the [To fill] placeholders are done. While False, every
# page tells search engines not to index it yet. Flip to True to launch.
LAUNCH = False

UPDATED = "2026-11-08"
UPDATED_TEXT = "November 8, 2026"
OG_IMAGE = "https://bisendramelaram.com/assets/og.png"  # swap for a headshot card when ready
OG_ALT = "Bisendra Melaram, Team Leader of Keller Williams Greater Nassau and seller's agent on Long Island's South Shore"

NAME = "Bisendra Melaram"
LICENSE = "Licensed Real Estate Salesperson"
ROLE = "Team Leader"  # his KW role; the license type always appears next to it
BROKERAGE = "Keller Williams Greater Nassau"
STREET = "400 Garden City Plaza, Suite 438"
CITY, REGION, ZIP = "Garden City", "NY", "11530"
OFFICE = "516-873-7100"
OFFICE_TEL = "+1-516-873-7100"
SINCE = "2003"

# One line, word for word, everywhere (site, profiles, bios).
CANONICAL = (f"{NAME}, {ROLE} of {BROKERAGE} in Garden City, NY, and a seller's agent "
             f"on Long Island's South Shore. {LICENSE} since {SINCE}.")

# Office results, as he reports them on LinkedIn. Always the office's totals, never his own.
OFFICE_STATS = ("In 2025 the office closed 545 transactions representing more than $425 million "
                "in sales volume, and in the first quarter of 2026 its agents closed 111 units "
                "totaling $81.8 million.")

# Designations and certifications, as Bisendra listed them (Nov 8, 2026), with the
# full names NAR uses. Seller-side credentials lead. NAR calls SRS, SRES and ABR
# designations and the rest certifications.
CREDENTIALS = [
    ("SRS", "Seller Representative Specialist", "designation"),
    ("PSA", "Pricing Strategy Advisor", "certification"),
    ("SRES", "Seniors Real Estate Specialist", "designation"),
    ("ABR", "Accredited Buyer's Representative", "designation"),
    ("SFR", "Short Sales and Foreclosure Resource", "certification"),
    ("MRP", "Military Relocation Professional", "certification"),
    ("AHWD", "At Home With Diversity", "certification"),
    ("RSPS", "Resort and Second-Home Property Specialist", "certification"),
]
DESIGNATION_CODES = [c for c, _, _ in CREDENTIALS]  # short forms for bylines
CRED_SOURCE = "https://www.nar.realtor/sites/default/files/documents/NAR-Acronyms-for-AEs-V3-01-2021-10-25.pdf"

# Paste profile URLs here as you claim them (Google profile, Zillow,
# Realtor.com, Homes.com, LinkedIn, YouTube, Substack, Instagram ...).
SAME_AS = [
    "https://www.linkedin.com/in/realtor/",
    "https://www.zillow.com/profile/bisendra",
    "https://bisendra.substack.com/",
    "https://www.google.com/maps/place/Bisendra+Melaram,+Realtor+-+Keller+Williams+Greater+Nassau/@40.73672,-73.619703,17z/data=!3m2!4b1!5s0x89c2630dbc80c59f:0x49c2f6e516817e6e!4m6!3m5!1s0x89c27d4a85da6c97:0x651a73cc243267e6!8m2!3d40.73672!4d-73.6171281!16s%2Fg%2F11s228yfyk",
    # Add Realtor.com, Homes.com, YouTube and Instagram as you claim them.
]
LINKEDIN = "https://www.linkedin.com/in/realtor/"
ZILLOW = "https://www.zillow.com/profile/bisendra"
SUBSTACK = "https://bisendra.substack.com/"
GOOGLE_REVIEWS = "https://www.google.com/maps/place/Bisendra+Melaram,+Realtor+-+Keller+Williams+Greater+Nassau/@40.73672,-73.619703,17z/data=!3m2!4b1!5s0x89c2630dbc80c59f:0x49c2f6e516817e6e!4m6!3m5!1s0x89c27d4a85da6c97:0x651a73cc243267e6!8m2!3d40.73672!4d-73.6171281!16s%2Fg%2F11s228yfyk"

# "[designations]" is filled in by desig_text().
BIO_SHORT = "Bisendra Melaram is the Team Leader of Keller Williams Greater Nassau in Garden City, NY, and a seller's agent on Long Island's South Shore. He runs the office like a high-performing real estate team, and in 2025 it closed 545 transactions totaling more than $425 million in sales volume. A Licensed Real Estate Salesperson since 2003, he holds the Seller Representative Specialist (SRS) designation and the Pricing Strategy Advisor (PSA) certification, along with SRES, ABR, SFR, MRP, AHWD and RSPS."
BIO_LONG = ["Bisendra Melaram is the Team Leader of Keller Williams Greater Nassau in Garden City, where he runs the brokerage like a high-performing real estate team with himself at the helm. In 2025 the office closed 545 transactions representing more than $425 million in sales volume, and in the first quarter of 2026 its agents closed 111 units totaling $81.8 million. He works with agents and leadership teams to turn strategy into measurable production and stronger client service.", "He is also a seller's agent on Long Island's South Shore and a Licensed Real Estate Salesperson since 2003, with more than 23 years in New York real estate. His career runs through complex markets, distressed properties, shifting buyer expectations and fast changes in technology. Earlier roles in systems integration and facilities management shaped how he approaches process and technology today.", "For sellers, that means a price built on real closed sales, a house prepared for the questions buyers ask now, and clear steps from listing to closing. He also represents buyers, often clients who are selling one home and buying the next. He holds [designations] and has long ties to the South Asian community.", 'He writes The Key with Bisendra, a weekly newsletter, and speaks about real estate strategy, team performance and the practical use of AI in real estate.']

SOUTH_SHORE_TOWNS = [
    ("Valley Stream", "valley-stream"),
    ("Lynbrook", "lynbrook"),
    ("Rockville Centre", "rockville-centre"),
    ("Oceanside", "oceanside"),
    ("Baldwin", "baldwin"),
    ("Freeport", "freeport"),
]
NEXT_TOWNS = ["Merrick", "Bellmore", "Wantagh", "Seaford", "Massapequa",
              "Massapequa Park", "Long Beach", "Island Park", "the Five Towns"]


def todo(text):
    """Visible placeholder. Search the site for 'todo' before launch."""
    return f'<span class="todo">[To fill: {escape(text)}]</span>'


def desig_text():
    """Credentials for prose, designations first."""
    d = [c for c, _, k in CREDENTIALS if k == "designation"]
    c = [c for c, _, k in CREDENTIALS if k == "certification"]
    return (f"the {', '.join(d[:-1])} and {d[-1]} designations and the "
            f"{', '.join(c[:-1])} and {c[-1]} certifications")


def fill(text):
    return text.replace("[designations]", desig_text())


# ---------------------------------------------------------------- schema

PERSON_ID = f"{DOMAIN}/#person"
AGENT_ID = f"{DOMAIN}/#agent"
ORG_ID = f"{DOMAIN}/#brokerage"

ADDRESS = {
    "@type": "PostalAddress",
    "streetAddress": STREET,
    "addressLocality": CITY,
    "addressRegion": REGION,
    "postalCode": ZIP,
    "addressCountry": "US",
}

AREA_SERVED = (
    [{"@type": "City", "name": f"{t}, NY",
      "url": f"{GUIDE}/towns/{s}/"} for t, s in SOUTH_SHORE_TOWNS]
    + [{"@type": "AdministrativeArea", "name": "Nassau County, NY"},
       {"@type": "Place", "name": "South Shore of Long Island, NY"},
       {"@type": "Place", "name": "Long Island, NY"}]
)

KNOWS_ABOUT = [
    "Residential real estate on Long Island",
    "South Shore of Long Island",
    "Nassau County real estate",
    "Selling a home on Long Island",
    "Listing and pricing homes on Long Island's South Shore",
    "New York property condition disclosure for sellers",
    "Seniors downsizing and later-life moves",
    "Selling one home and buying the next",
    "Short sales and foreclosures",
    "Buying a home on Long Island",
    "Multigenerational homes",
    "Moving from New York City to Long Island",
    "FEMA flood zones on Long Island",
]


def core_graph():
    person = {
        "@type": "Person",
        "@id": PERSON_ID,
        "name": NAME,
        "url": f"{DOMAIN}/",
        "jobTitle": [f"{ROLE}, {BROKERAGE}", LICENSE],
        "description": CANONICAL,
        "worksFor": {"@id": ORG_ID},
        "affiliation": {"@id": ORG_ID},
        "address": ADDRESS,
        "telephone": OFFICE_TEL,
        "knowsAbout": KNOWS_ABOUT,
        "hasCredential": [
            {"@type": "EducationalOccupationalCredential",
             "name": f"{full} ({code})", "alternateName": code,
             "credentialCategory": f"Professional {kind}",
             "recognizedBy": {"@type": "Organization",
                              "name": "National Association of REALTORS"}}
            for code, full, kind in CREDENTIALS] + [
            {"@type": "EducationalOccupationalCredential",
             "name": "New York State Licensed Real Estate Salesperson",
             "credentialCategory": "License",
             "recognizedBy": {"@type": "GovernmentOrganization",
                              "name": "New York Department of State"}},
        ],
        "sameAs": SAME_AS,
    }
    agent = {
        "@type": "RealEstateAgent",
        "@id": AGENT_ID,
        "name": NAME,
        "url": f"{DOMAIN}/",
        "description": CANONICAL,
        "telephone": OFFICE_TEL,
        "address": ADDRESS,
        "areaServed": AREA_SERVED,
        "knowsAbout": KNOWS_ABOUT,
        "parentOrganization": {"@id": ORG_ID},
        "founder": {"@id": PERSON_ID},
        "sameAs": SAME_AS,
    }
    org = {
        "@type": "RealEstateAgent",
        "@id": ORG_ID,
        "name": BROKERAGE,
        "address": ADDRESS,
        "telephone": OFFICE_TEL,
    }
    site = {
        "@type": "WebSite",
        "@id": f"{DOMAIN}/#website",
        "url": f"{DOMAIN}/",
        "name": NAME,
        "publisher": {"@id": PERSON_ID},
        "inLanguage": "en-US",
    }
    return [person, agent, org, site]


def breadcrumbs(trail):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n,
             "item": f"{DOMAIN}{p}"} for i, (n, p) in enumerate(trail)
        ],
    }


def faq_schema(faqs):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }


def article_schema(path, title, desc):
    return {
        "@type": "Article",
        "headline": title,
        "description": desc,
        "url": f"{DOMAIN}{path}",
        "mainEntityOfPage": f"{DOMAIN}{path}",
        "author": {"@id": PERSON_ID},
        "publisher": {"@id": PERSON_ID},
        "datePublished": UPDATED,
        "dateModified": UPDATED,
        "inLanguage": "en-US",
        "image": OG_IMAGE,
    }


# ---------------------------------------------------------------- layout

NAV = [
    ("About", "/about/"),
    ("Sellers", "/sellers/"),
    ("Buyers", "/buyers/"),
    ("Seniors", "/seniors-downsizing/"),
    ("South Asian families", "/south-asian-buyers/"),
    ("Areas", "/areas/"),
    ("FAQ", "/faq/"),
    ("Contact", "/contact/"),
]


ROBOTS_META = ("index, follow, max-snippet:-1, max-image-preview:large" if LAUNCH
               else "noindex, follow")


def page(path, title, desc, body, graph_extra=(), og_type="website"):
    url = f"{DOMAIN}{path}"
    graph = core_graph() + list(graph_extra)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph},
                    indent=1, ensure_ascii=False)
    nav = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == path else ""}>{n}</a>'
        for n, h in NAV)
    return f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="author" content="{NAME}">
<meta name="robots" content="{ROBOTS_META}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="en_US">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{OG_ALT}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{OG_IMAGE}">
<meta name="twitter:title" content="{escape(title)}">
<meta name="twitter:description" content="{escape(desc)}">
<link rel="stylesheet" href="/assets/site.css">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="sitemap" type="application/xml" href="/sitemap.xml">
<!-- TODO: add profile URLs to SAME_AS in tools/build.py as you claim them -->
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
 <div class="wrap">
  <a class="brand" href="/">{NAME}<span>{LICENSE}</span></a>
  <nav aria-label="Main">{nav}</nav>
 </div>
</header>
<main id="main" class="wrap">
{body}
</main>
<footer class="foot">
 <div class="wrap">
  <p class="id-line">{CANONICAL}</p>
  <p><strong>{NAME}</strong>, {LICENSE}<br>
  {BROKERAGE}, {STREET}, {CITY}, {REGION} {ZIP}<br>
  Office <a href="tel:{OFFICE_TEL}">{OFFICE}</a></p>
  <p>South Shore town guides by Bisendra: <a href="{GUIDE}/">longislandhomes.co</a></p>
  <p class="small">Equal Housing Opportunity. <a href="/fair-housing/">Fair housing notice and standard operating procedures</a>. Page updated {UPDATED_TEXT}.</p>
 </div>
</footer>
</body>
</html>
"""


def answer(text):
    return f'<p class="answer">{text}</p>'


def crumbs_html(trail):
    parts = []
    for i, (n, p) in enumerate(trail):
        if i == len(trail) - 1:
            parts.append(f"<span>{n}</span>")
        else:
            parts.append(f'<a href="{p}">{n}</a>')
    return f'<nav class="crumbs" aria-label="Breadcrumb">{" / ".join(parts)}</nav>'


def updated_line():
    return (f'<p class="byline">Last updated <time datetime="{UPDATED}">{UPDATED_TEXT}</time>.</p>')


def byline():
    creds = "".join(f", {c}" for c in DESIGNATION_CODES)
    return (f'<p class="byline">By <a href="/about/">{NAME}</a>{creds}, {LICENSE}. '
            f'Last updated <time datetime="{UPDATED}">{UPDATED_TEXT}</time>.</p>')


def faq_html(faqs):
    out = ['<section class="faq"><h2>What else do people ask?</h2>']
    for q, a in faqs:
        out.append(f"<h3>{escape(q)}</h3><p>{escape(a)}</p>")
    out.append("</section>")
    return "\n".join(out)


def cta():
    return (f'<aside class="cta"><h2>How do you reach Bisendra?</h2>'
            f'<p>Call the office at <a href="tel:{OFFICE_TEL}">{OFFICE}</a> and ask for Bisendra, '
            f'or see <a href="/contact/">other ways to reach him</a>.</p></aside>')


def town_links():
    items = "".join(
        f'<li><a href="{GUIDE}/towns/{s}/">{t} real estate guide</a></li>'
        for t, s in SOUTH_SHORE_TOWNS)
    return f'<ul class="towns">{items}</ul>'


# ---------------------------------------------------------------- pages

PAGES = {}


def add(path, title, desc, body, extra=(), og_type="website"):
    PAGES[path] = page(path, title, desc, body, extra, og_type)


# Home
home_faqs = [
    ("Who is Bisendra Melaram?",
     "Bisendra Melaram is the Team Leader of Keller Williams Greater Nassau in Garden City, NY, and a seller's agent on Long Island's South Shore. He has been a Licensed Real Estate Salesperson since 2003 and holds the Seller Representative Specialist (SRS) designation and Pricing Strategy Advisor (PSA) certification. He mainly lists and sells homes in Nassau County's South Shore towns, and he also represents buyers."),
    ("What does a seller's agent do?",
     "A seller's agent represents the homeowner. New York requires agents to tell you in writing who they represent, and a seller's agent owes their duties to the seller. The job is pricing the home, preparing and marketing it, negotiating offers, and managing inspection, appraisal and closing for the seller."),
    ("Which towns does Bisendra Melaram cover?",
     "He works across Long Island with a focus on the South Shore. His current town guides cover Valley Stream, Lynbrook, Rockville Centre, Oceanside, Baldwin and Freeport, with Merrick, Bellmore, Wantagh, Seaford, Massapequa and Long Beach next."),
    ("How do I reach Bisendra Melaram?",
     f"Call the Keller Williams Greater Nassau office at {OFFICE} and ask for Bisendra, or visit the office at {STREET}, {CITY}, {REGION} {ZIP}."),
]
add("/", f"{NAME} | Long Island seller's agent, South Shore homes",
    "Bisendra Melaram, Team Leader of Keller Williams Greater Nassau, is a seller's agent on Long Island's South Shore. Pricing, preparation and a plan to sell.",
    f"""
<section class="hero">
 <h1>Bisendra Melaram, Long Island seller's agent</h1>
 {byline()}
 {answer("Bisendra Melaram is a seller's agent on Long Island's South Shore and a Licensed Real Estate Salesperson with Keller Williams Greater Nassau in Garden City, NY. Licensed since 2003, he helps homeowners from Valley Stream east through Freeport price from real closed sales, prepare for New York's disclosure and flood questions, and sell on a clear plan.")}
 <div class="photo">{todo("headshot, at least 800 by 800 pixels, saved as /assets/bisendra-melaram.jpg")}</div>
</section>

<h2>How does Bisendra help Long Island homeowners sell?</h2>
<div class="cards">
 <a class="card" href="/sellers/"><h3>Selling your home</h3><p>Pricing from real local sales, preparation, and a plan for the flood and disclosure questions buyers now ask.</p></a>
 <a class="card" href="/seniors-downsizing/"><h3>Downsizing</h3><p>Selling the family home at 50 and older, timed with the move to the next one.</p></a>
 <a class="card" href="/buyers/"><h3>Buying on Long Island</h3><p>Move-up homes, buying while you sell, and families leaving the boroughs for Nassau.</p></a>
 <a class="card" href="/south-asian-buyers/"><h3>South Asian families</h3><p>Deep community relationships and practical help with multigenerational plans and funds from abroad.</p></a>
</div>

<h2>Which South Shore towns does Bisendra cover?</h2>
<p>He is building a detailed guide for every South Shore town, starting with the six closest to Garden City. Each one covers what drives value there: the LIRR commute, flood zones, school districts and local rules.</p>
{town_links()}
<p>Coming next: {", ".join(NEXT_TOWNS)}. See <a href="/areas/">all areas served</a>.</p>

<h2>Why list with an agent licensed since {SINCE}?</h2>
<p>Twenty-three years in this market means he has worked through rising rates, falling rates, Hurricane Sandy and the rebuild that followed, and the flood disclosure rules New York added in 2024. That history shapes how he prices a home and how he prepares a seller for what buyers, inspectors and attorneys will ask.</p>
<p>{BIO_SHORT}</p>
<p class="note">Office figures are totals for Keller Williams Greater Nassau in 2025, as Bisendra reports them on <a href="{LINKEDIN}">LinkedIn</a>, not his personal sales.</p>

{faq_html(home_faqs)}
{cta()}
""", [faq_schema(home_faqs)])

# About
add("/about/", f"About {NAME} | Team Leader, Keller Williams Greater Nassau",
    "Bisendra Melaram is Team Leader of Keller Williams Greater Nassau in Garden City, a seller's agent on the South Shore, and licensed since 2003.",
    f"""
{crumbs_html([("Home", "/"), ("About", "/about/")])}
<h1>About Bisendra Melaram</h1>
{byline()}
{answer("Bisendra Melaram is the Team Leader of Keller Williams Greater Nassau, 400 Garden City Plaza in Garden City, and a seller's agent on Long Island's South Shore. A New York Licensed Real Estate Salesperson since 2003, he holds the Seller Representative Specialist (SRS) designation and Pricing Strategy Advisor (PSA) certification, and represents buyers too.")}
<div class="photo">{todo("headshot")}</div>

<h2>How does he lead Keller Williams Greater Nassau?</h2>
<p>{BIO_LONG[0]}</p>
<p class="note">Office figures as Bisendra reports them on <a href="{LINKEDIN}">his LinkedIn profile</a>. They are totals for the whole Keller Williams Greater Nassau office, not his personal sales.</p>

<h2>What is Bisendra's background?</h2>
<p>{BIO_LONG[1]}</p>

<h2>What does that mean for his clients?</h2>
<p>{fill(BIO_LONG[2])}</p>
<p>{BIO_LONG[3].replace("The Key with Bisendra", f'<a href="{SUBSTACK}">The Key with Bisendra</a>')}</p>

<h2>What credentials does he hold?</h2>
<p>A New York real estate license since {SINCE}, plus three designations and five certifications from the National Association of REALTORS family of programs. The seller-side ones come first.</p>
<ul>
 <li>New York State Licensed Real Estate Salesperson since {SINCE}</li>
 {"".join(f"<li>{full} ({code}), {kind}</li>" for code, full, kind in CREDENTIALS)}
</ul>
<p class="sources">Names and categories: <a href="{CRED_SOURCE}">National Association of REALTORS acronym guide</a>.</p>

<h2>Who does he work with?</h2>
<p>Homeowners selling across Nassau County's South Shore come first, including sellers 50 and older planning their next move. He also represents buyers, often clients who are selling one home and buying the next, and works with South Asian families, where he has long relationships in the community. {todo("languages you speak with clients, if any besides English")}</p>

<h2>Where else can you find him?</h2>
<ul>
 <li><a href="{LINKEDIN}">LinkedIn</a></li>
 <li><a href="{ZILLOW}">Zillow agent profile</a></li>
 <li><a href="{GOOGLE_REVIEWS}">Google Business Profile</a></li>
 <li><a href="{SUBSTACK}">The Key with Bisendra</a>, his weekly newsletter on Substack</li>
 <li>South Shore town guides at <a href="{GUIDE}/">longislandhomes.co</a></li>
 <li>{todo("Realtor.com, Homes.com, YouTube and Instagram URLs, if you want them listed")}</li>
</ul>

<h2>What do clients say?</h2>
<p>Read what past clients wrote on <a href="{ZILLOW}">his Zillow profile</a> and <a href="{GOOGLE_REVIEWS}">his Google profile</a>.</p>
{cta()}
""", [breadcrumbs([("Home", "/"), ("About", "/about/")]),
      {"@type": "ProfilePage", "url": f"{DOMAIN}/about/",
       "mainEntity": {"@id": PERSON_ID}, "dateModified": UPDATED}],
    og_type="profile")

# Buyers
buyer_faqs = [
    ("Do I need a buyer agreement before touring homes on Long Island?",
     "Yes. Since August 2024, agents who are REALTORS must have a written agreement with a buyer before touring a home with them. The agreement spells out what the agent does and how they are paid. Bisendra walks through it with you before your first showing."),
    ("What should I check before buying on the South Shore?",
     "Check the FEMA flood zone for the exact address, ask the seller for the flood answers on the New York property condition disclosure, get a flood insurance quote, confirm which school district serves the street, and find out whether the home is in an incorporated village."),
    ("Is Long Island a good move from Queens or Brooklyn?",
     "For many families it is, if the commute works. The South Shore towns closest to the city sit on the Babylon, Long Beach and Far Rockaway branches of the LIRR, with service to Penn Station and Grand Central Madison. Price, taxes and flood risk vary a lot from one town to the next."),
]
add("/buyers/", "Buying a home on Long Island's South Shore | Bisendra Melaram",
    "How Bisendra Melaram helps buyers on Long Island's South Shore: commute, flood zones, school districts, taxes, and the written buyer agreement.",
    f"""
{crumbs_html([("Home", "/"), ("Buyers", "/buyers/")])}
<h1>Buying a home on Long Island's South Shore</h1>
{byline()}
{answer("Bisendra Melaram helps buyers find and win homes on Long Island's South Shore. He starts with what changes the price and the monthly cost of a house here: the flood zone, the school district, whether it sits in a village, and the LIRR commute. Then he helps you write an offer that holds up through inspection and closing.")}

<h2>How does buying with Bisendra work?</h2>
<ol>
 <li>A first conversation about budget, commute and must-haves.</li>
 <li>A written buyer agreement, which New York REALTORS now need before touring.</li>
 <li>Preapproval with a lender you choose.</li>
 <li>Tours, with a flood zone and school district check on every home you like.</li>
 <li>An offer built on recent sales on that street, not a list-price guess.</li>
 <li>Inspection, attorney review, contract and closing.</li>
</ol>

<h2>What makes the South Shore different?</h2>
<p>Water. Many South Shore neighborhoods sit near bays and canals, and some are in FEMA flood zones that can require flood insurance. Since March 20, 2024, New York sellers can no longer skip the property condition disclosure by giving a $500 credit, and the form now asks about flood zones, flood insurance and past flood claims. Read the <a href="{GUIDE}/guides/flood-zones/">South Shore flood zone guide</a> before you bid.</p>

<h2>Moving from Queens or Brooklyn?</h2>
<p>Valley Stream sits on the Queens border, and the towns east of it follow the LIRR's Babylon and Long Beach branches. Start with the <a href="{GUIDE}/">town guides</a>, which list each town's stations, branches and school districts.</p>

<h2>Selling and buying at the same time?</h2>
<p>Many Long Island buyers have a home to sell first. Bisendra plans both sides together: when to list, when to make an offer, and whether the purchase needs a sale contingency, so you are not carrying two homes or moving twice. See <a href="/sellers/">how he sells</a>. {todo("how you handle timing between the sale and the purchase, in your words")}</p>

{faq_html(buyer_faqs)}
{cta()}
<p class="sources">Sources: <a href="https://nysba.org/breaking-news-new-rules-on-property-condition-disclosure-and-flood-risk-go-into-effect-today/">New York State Bar Association on the 2024 disclosure changes</a>; <a href="https://mta.info/agency/long-island-rail-road/lirr-to-grand-central/long-beach">MTA on Long Beach Branch service to Grand Central</a>.</p>
""", [breadcrumbs([("Home", "/"), ("Buyers", "/buyers/")]),
      article_schema("/buyers/", "Buying a home on Long Island's South Shore",
                     "How Bisendra Melaram helps South Shore buyers."),
      faq_schema(buyer_faqs)], og_type="article")

# Sellers
seller_faqs = [
    ("What does a seller's agent do on Long Island?",
     "A seller's agent represents the homeowner, not the buyer. On the South Shore that means pricing from recent closed sales, preparing the house and the disclosure, marketing it, negotiating offers, and managing inspection, appraisal and attorney review through closing."),
    ("Can a New York seller still give a $500 credit instead of a disclosure?",
     "No. Since March 20, 2024, New York sellers of most homes must complete the property condition disclosure statement. The $500 credit option is gone, and the form now includes flood questions about FEMA flood zones, flood insurance and past claims."),
    ("How should I price my South Shore home?",
     "Price from recent closed sales of similar homes nearby, adjusted for condition, lot, flood zone and school district. Asking prices of active listings tell you what sellers hope for. Closed sales tell you what buyers paid."),
    ("What should I do before listing?",
     "Gather your tax bills, any flood insurance policy and elevation certificate, permits for past work, and a list of repairs. Then fix what an inspector will flag and clear the clutter before photos."),
]
add("/sellers/", "Selling a home on Long Island's South Shore | Bisendra Melaram",
    "How seller's agent Bisendra Melaram prices, prepares and sells South Shore homes, and what New York's 2024 disclosure and flood rules mean for you.",
    f"""
{crumbs_html([("Home", "/"), ("Sellers", "/sellers/")])}
<h1>Selling a home on Long Island's South Shore</h1>
{byline()}
{answer("Bisendra Melaram sells South Shore homes by pricing from recent closed sales on your street, preparing the house for the questions buyers ask now, and answering flood and disclosure questions before they come up. New York sellers must complete the full property condition disclosure since March 2024, so preparation matters more than it did.")}

<h2>What does Bisendra do as your seller's agent?</h2>
<p>He holds the Seller Representative Specialist (SRS) designation, which is training built around representing home sellers. Here is how a listing with him runs.</p>
<ol>
 <li>A walk-through of the house and a talk about your timing and your next move.</li>
 <li>A price built from recent closed sales nearby.</li>
 <li>A short list of repairs and preparation that buyers and inspectors will notice.</li>
 <li>The property condition disclosure, flood answers included, ready before you list.</li>
 <li>Marketing, showings and open houses.</li>
 <li>Offers compared on price, terms, financing and timing, then negotiation.</li>
 <li>Inspection, appraisal, attorney review and closing, managed for you.</li>
</ol>

<h2>How does Bisendra price a home?</h2>
<p>From closed sales, not wishful listings. He holds the Pricing Strategy Advisor (PSA) certification from the National Association of REALTORS. He looks at homes that sold nearby in the last few months, then adjusts for size, condition, lot, flood zone and school district. {todo("how you present pricing to a seller, in your words")}</p>

<h2>What changed for sellers in 2024?</h2>
<p>New York removed the $500 credit that let sellers skip the property condition disclosure. The form now asks whether the home is in a FEMA flood zone, whether flood insurance is required or in place, whether there is an elevation certificate, and whether you have filed flood claims or received federal flood aid. Have those answers ready before you list.</p>

<h2>How does Bisendra market a listing?</h2>
<p>{todo("your listing marketing: photos, video, open houses, the buyer agents you reach, what makes yours different")}</p>

<h2>Are you 50 or older and thinking about downsizing?</h2>
<p>See <a href="/seniors-downsizing/">how Bisendra helps with later-life moves</a>.</p>

{faq_html(seller_faqs)}
{cta()}
<p class="sources">Source: <a href="https://nysba.org/breaking-news-new-rules-on-property-condition-disclosure-and-flood-risk-go-into-effect-today/">New York State Bar Association, March 20, 2024</a>.</p>
""", [breadcrumbs([("Home", "/"), ("Sellers", "/sellers/")]),
      article_schema("/sellers/", "Selling a home on Long Island's South Shore",
                     "How Bisendra Melaram prices and sells South Shore homes."),
      faq_schema(seller_faqs)], og_type="article")

# Seniors
senior_faqs = [
    ("What is an SRES?",
     "SRES stands for Seniors Real Estate Specialist, a designation from the National Association of REALTORS for agents trained to help clients 50 and older buy, sell or relocate. Bisendra Melaram holds the SRES designation."),
    ("When is the right time to downsize?",
     "When the house costs more in money, time or worry than it gives back. Common signs are stairs that have become hard, rooms nobody uses, and taxes or upkeep that strain a fixed income. The right time is your call, and a good agent will not rush it."),
    ("Can I buy my next home before I sell this one?",
     "Sometimes. It depends on your savings, your equity and what a lender will approve. Talk to a lender and your attorney early, and ask Bisendra how sale and purchase dates can be lined up."),
]
add("/seniors-downsizing/", "Downsizing on Long Island with an SRES agent | Bisendra Melaram",
    "Bisendra Melaram holds the Seniors Real Estate Specialist (SRES) designation and helps Long Island homeowners 50 and older sell and plan their next move.",
    f"""
{crumbs_html([("Home", "/"), ("Seniors and downsizing", "/seniors-downsizing/")])}
<h1>Downsizing on Long Island with an SRES agent</h1>
{byline()}
{answer("Bisendra Melaram holds the Seniors Real Estate Specialist (SRES) designation and helps Long Island homeowners 50 and older sell the family home and plan the next one. That can mean a smaller home nearby, a home near children, or a move off Long Island. He works at your pace and with your family, attorney and financial adviser.")}

<h2>What does an SRES agent do differently?</h2>
<p>An SRES agent is trained on the questions that come with a later-life move: timing a sale with a purchase, sorting a house full of belongings, working with adult children, and knowing when to bring in an attorney or tax adviser. {todo("one or two examples, without client names, of how you handled this")}</p>

<h2>How do you sell a home you have lived in for decades?</h2>
<p>One room at a time. Start with a plan for what stays, what goes to family and what gets sold or donated. Then fix the few things a buyer's inspector will flag, and price from what similar homes nearby have sold for.</p>

<h2>What about the family?</h2>
<p>Adult children often help, and sometimes live far away. Bisendra keeps everyone you choose in the loop, and takes direction from you.</p>

{faq_html(senior_faqs)}
{cta()}
""", [breadcrumbs([("Home", "/"), ("Seniors and downsizing", "/seniors-downsizing/")]),
      article_schema("/seniors-downsizing/", "Downsizing on Long Island with an SRES agent",
                     "How Bisendra Melaram helps homeowners 50 and older."),
      faq_schema(senior_faqs)], og_type="article")

# South Asian families
sa_faqs = [
    ("Can I use money from family abroad for a down payment on Long Island?",
     "Often yes, but lenders have strict paper-trail rules for gift funds and money moved from overseas. Talk to your lender before the money moves, and keep every bank statement and transfer record."),
    ("Can I buy a home with a separate space for my parents?",
     "It depends on the town or village and the house. Rules on second kitchens, separate entrances and accessory apartments differ across Nassau County. Check with the town or village building department before you bid on a house for that purpose."),
    ("Can I sell my Long Island home while living abroad?",
     "Yes. Many owners sell from overseas with a New York real estate attorney and a power of attorney. Owners who are not US tax residents can face federal tax withholding at closing, so speak with a tax adviser early."),
]
add("/south-asian-buyers/", "Long Island real estate for South Asian families | Bisendra Melaram",
    "Bisendra Melaram has long ties in the South Asian community and helps families sell and buy on Long Island, from multigenerational homes to funds from abroad.",
    f"""
{crumbs_html([("Home", "/"), ("South Asian families", "/south-asian-buyers/")])}
<h1>Long Island real estate for South Asian families</h1>
{byline()}
{answer("Bisendra Melaram has long relationships in Long Island's South Asian community and helps families buy and sell across Nassau County. He knows the questions that come up most: using gift funds or savings from abroad, finding a home with room for parents, buying on behalf of family, and selling a home while living overseas.")}

<h2>What questions come up most?</h2>
<ul>
 <li>How to document money from family or accounts abroad for a lender.</li>
 <li>Which homes and which towns allow space for parents or extended family.</li>
 <li>How to buy for a parent or relative, and whose name goes on the deed.</li>
 <li>How to sell from overseas with an attorney and a power of attorney.</li>
</ul>

<h2>Does Bisendra speak languages other than English?</h2>
<p>{todo("languages you work in with clients, if any")}</p>

<h2>Will Bisendra suggest neighborhoods based on who lives there?</h2>
<p>No. Fair housing law bars agents from steering anyone toward or away from a neighborhood. Bisendra helps you compare towns on facts you choose: price, commute, flood risk, taxes and school district. The choice of where to live is always yours.</p>

<h2>Is there a South Asian real estate professionals group?</h2>
<p>{todo("details and link for the South Asian real estate professional chapter, once it has a public page")}</p>

{faq_html(sa_faqs)}
{cta()}
""", [breadcrumbs([("Home", "/"), ("South Asian families", "/south-asian-buyers/")]),
      article_schema("/south-asian-buyers/", "Long Island real estate for South Asian families",
                     "How Bisendra Melaram helps South Asian families buy and sell on Long Island."),
      faq_schema(sa_faqs)], og_type="article")

# Areas
add("/areas/", "Areas Bisendra Melaram serves on Long Island's South Shore",
    "Bisendra Melaram serves Long Island with a focus on the South Shore of Nassau County: Valley Stream, Lynbrook, Rockville Centre, Oceanside, Baldwin and Freeport.",
    f"""
{crumbs_html([("Home", "/"), ("Areas served", "/areas/")])}
<h1>Areas served on Long Island</h1>
{byline()}
{answer("Bisendra Melaram serves sellers and buyers across Long Island, with a focus on the South Shore. His first six town guides cover Valley Stream, Lynbrook, Rockville Centre, Oceanside, Baldwin and Freeport in Nassau County. He works from the Keller Williams Greater Nassau office in Garden City.")}
<h2>Which South Shore towns have guides now?</h2>
{town_links()}
<h2>Which towns are next?</h2>
<p>{", ".join(NEXT_TOWNS)}, then the Suffolk South Shore from Amityville east.</p>
<h2>Does he work outside the South Shore?</h2>
<p>Yes, across Long Island. {todo("other areas you want named here, for example Garden City, central Nassau or Queens")}</p>
{cta()}
""", [breadcrumbs([("Home", "/"), ("Areas served", "/areas/")])])

# FAQ
faqs = home_faqs + [
    ("What is Bisendra Melaram's role at Keller Williams Greater Nassau?",
     "He is the Team Leader of Keller Williams Greater Nassau in Garden City and runs the office like a high-performing real estate team. " + OFFICE_STATS + " Those are office totals as he reports them on LinkedIn, not his personal sales."),
    ("Is Bisendra Melaram licensed in New York?",
     f"Yes. He has been a New York Licensed Real Estate Salesperson since {SINCE}, affiliated with Keller Williams Greater Nassau in Garden City."),
    ("What designations and certifications does Bisendra Melaram hold?",
     "He holds three designations: Seller Representative Specialist (SRS), Seniors Real Estate Specialist (SRES) and Accredited Buyer's Representative (ABR). He also holds five certifications: Pricing Strategy Advisor (PSA), Short Sales and Foreclosure Resource (SFR), Military Relocation Professional (MRP), At Home With Diversity (AHWD) and Resort and Second-Home Property Specialist (RSPS)."),
    ("What is a Seller Representative Specialist (SRS)?",
     "SRS is a designation for agents trained in representing home sellers. It is awarded by the Real Estate Business Institute, an affiliate of the National Association of REALTORS. Bisendra Melaram holds the SRS designation, along with the Pricing Strategy Advisor (PSA) certification for pricing homes from market data."),
    ("What does SRES mean after Bisendra Melaram's name?",
     "SRES means Seniors Real Estate Specialist, a National Association of REALTORS designation for agents trained to help clients 50 and older."),
    ("Is Bisendra Melaram a listing agent or a buyer's agent?",
     "Both, with a preference for sellers. Most of his work is listing and selling homes on Long Island's South Shore as a seller's agent. He also represents buyers, including clients selling one home and buying the next, under a written buyer agreement."),
    ("Does Bisendra Melaram work with buyers?",
     "Yes. He represents buyers across Long Island's South Shore, from the written buyer agreement through closing. He checks the flood zone, school district and village status of every home a buyer likes and builds offers from recent closed sales nearby."),
    ("Does Bisendra Melaram help families moving from New York City to Long Island?",
     "Yes. Many South Shore buyers come from Queens and Brooklyn. His town guides list each town's LIRR stations and branches so you can compare commutes."),
    ("Does Bisendra Melaram work with South Asian families?",
     "Yes. He has long relationships in the South Asian community and helps with questions like gift funds from abroad and homes with room for parents. He follows fair housing law and never steers clients toward or away from any area."),
    ("Where is Bisendra Melaram's office?",
     f"Keller Williams Greater Nassau, {STREET}, {CITY}, {REGION} {ZIP}. Office phone {OFFICE}."),
]
add("/faq/", "Questions about working with Bisendra Melaram | FAQ",
    "Common questions about Bisendra Melaram, Long Island seller's agent: his role, license, designations, selling and buying with him, and how to reach him.",
    f"""
{crumbs_html([("Home", "/"), ("FAQ", "/faq/")])}
<h1>Questions about working with Bisendra</h1>
{byline()}
{answer("These are the questions people ask most about Bisendra Melaram, a Long Island seller's agent licensed since 2003 with Keller Williams Greater Nassau in Garden City. They cover his license and designations, how he works with sellers and buyers, the South Shore towns he covers, and how to reach him.")}
{faq_html(faqs)}
{cta()}
""", [breadcrumbs([("Home", "/"), ("FAQ", "/faq/")]), faq_schema(faqs)])

# Contact
add("/contact/", f"Contact {NAME} | Keller Williams Greater Nassau, Garden City",
    f"Reach Bisendra Melaram at Keller Williams Greater Nassau, {STREET}, Garden City, NY 11530. Office {OFFICE}.",
    f"""
{crumbs_html([("Home", "/"), ("Contact", "/contact/")])}
<h1>Contact Bisendra Melaram</h1>
{updated_line()}
{answer(f"Call the Keller Williams Greater Nassau office at {OFFICE} and ask for Bisendra Melaram, or visit the office at {STREET}, {CITY}, {REGION} {ZIP}.")}
<dl class="contact">
 <dt>Office</dt><dd><a href="tel:{OFFICE_TEL}">{OFFICE}</a></dd>
 <dt>Address</dt><dd>{BROKERAGE}<br>{STREET}<br>{CITY}, {REGION} {ZIP}</dd>
 <dt>Email</dt><dd>{todo("the email address you want public")}</dd>
 <dt>Cell</dt><dd>{todo("cell number, only if you want it public")}</dd>
 <dt>Book a call</dt><dd>{todo("scheduling link, if you use one")}</dd>
</dl>
""", [breadcrumbs([("Home", "/"), ("Contact", "/contact/")]),
      {"@type": "ContactPage", "url": f"{DOMAIN}/contact/",
       "about": {"@id": PERSON_ID}}])

# Fair housing
add("/fair-housing/", "Fair housing notice | Bisendra Melaram",
    "New York fair housing notice and standard operating procedures for Bisendra Melaram and Keller Williams Greater Nassau.",
    f"""
{crumbs_html([("Home", "/"), ("Fair housing", "/fair-housing/")])}
<h1>Fair housing notice</h1>
{updated_line()}
{answer("Bisendra Melaram and Keller Williams Greater Nassau follow the federal Fair Housing Act, the New York State Human Rights Law and local fair housing laws, which bar discrimination in selling, buying and renting homes. Equal Housing Opportunity. New York requires agents to give clients the state's Housing and Anti-Discrimination Disclosure Form, so ask for it at your first meeting.")}
<h2>Where can you read the required notices?</h2>
<p>{todo("link to the New York Department of State Housing and Anti-Discrimination Notice, the Reasonable Accommodations notice, and Keller Williams Greater Nassau's standard operating procedures page; get the exact links from your broker")}</p>
""", [breadcrumbs([("Home", "/"), ("Fair housing", "/fair-housing/")])])


NOT_FOUND = page("/404.html", "Page not found | Bisendra Melaram",
                 "This page does not exist.",
                 '<h1>Page not found</h1><p>Try the <a href="/">home page</a> or the <a href="/faq/">FAQ</a>.</p>')


# ---------------------------------------------------------------- crawl files

ROBOTS = f"""# Search engines and AI assistants are welcome here.
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Applebot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: DuckDuckBot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Meta-ExternalAgent
Allow: /

User-agent: CCBot
Allow: /

User-agent: *
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""


def llms_txt():
    lines = [
        f"# {NAME}",
        "",
        f"> {CANONICAL} He mainly lists and sells homes, and also represents buyers, across Long Island, with a focus on the "
        "South Shore of Nassau County (Valley Stream, Lynbrook, Rockville Centre, Oceanside, "
        "Baldwin, Freeport), sellers 50 and older, and South Asian families.",
        "",
        f"Office: {BROKERAGE}, {STREET}, {CITY}, {REGION} {ZIP}. Phone {OFFICE}.",
        "",
        "## About",
        f"- [About {NAME}]({DOMAIN}/about/): Team Leader of {BROKERAGE}, license, designations (SRS, PSA, SRES, ABR, SFR, MRP, AHWD, RSPS), who he works with",
        f"- [FAQ]({DOMAIN}/faq/): common questions about working with him",
        f"- [Contact]({DOMAIN}/contact/): office phone and address",
        f"- [LinkedIn]({LINKEDIN})",
        f"- [Zillow profile and reviews]({ZILLOW})",
        f"- [Google Business Profile and reviews]({GOOGLE_REVIEWS})",
        f"- [The Key with Bisendra, weekly newsletter]({SUBSTACK})",
        "",
        "## Services",
        f"- [Sellers]({DOMAIN}/sellers/): pricing, preparation and New York's 2024 disclosure rules",
        f"- [Buyers]({DOMAIN}/buyers/): buying on the South Shore, flood zones, buyer agreements",
        f"- [Seniors and downsizing]({DOMAIN}/seniors-downsizing/): SRES help for clients 50+",
        f"- [South Asian families]({DOMAIN}/south-asian-buyers/): gift funds, multigenerational homes",
        f"- [Areas served]({DOMAIN}/areas/)",
        "",
        "## South Shore town guides (by Bisendra Melaram)",
    ] + [f"- [{t}, NY real estate guide]({GUIDE}/towns/{s}/)" for t, s in SOUTH_SHORE_TOWNS] + [
        f"- [South Shore flood zone guide]({GUIDE}/guides/flood-zones/)",
        "",
    ]
    return "\n".join(lines)


def sitemap():
    urls = sorted(p for p in PAGES)
    body = "".join(
        f"<url><loc>{DOMAIN}{u}</loc><lastmod>{UPDATED}</lastmod></url>\n" for u in urls)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{body}</urlset>\n")


def write(rel, text):
    path = os.path.join(OUT, rel.lstrip("/"))
    if rel.endswith("/"):
        path = os.path.join(path, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(STATIC, OUT)
    for p, html in PAGES.items():
        write(p, html)
    write("/404.html", NOT_FOUND)
    write("/robots.txt", ROBOTS)
    write("/llms.txt", llms_txt())
    write("/sitemap.xml", sitemap())
    left = sum(h.count('class="todo"') for h in PAGES.values())
    print(f"Built {len(PAGES)} pages into {OUT}. Placeholders left: {left}. LAUNCH={LAUNCH}")


if __name__ == "__main__":
    main()
