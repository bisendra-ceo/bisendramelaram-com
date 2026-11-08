"""Seller guides for bisendramelaram.com, one question per page.

Every fact here comes from a primary source listed in SOURCES, with the date the
source shows. Anything only Bisendra can supply is a visible [To fill] box.
Writing rules: no em dashes, question-style H2s, sentence-case headings.
"""
from html import escape

HOME = "https://bisendramelaram.com"
GUIDE = "https://longislandhomes.co"
CHECKED = "November 2026"


def todo(text):
    return f'<span class="todo">[To fill: {escape(text)}]</span>'


# key: (label, url)
SOURCES = {
    "dtf_transfer": ("New York State Department of Taxation and Finance, Real estate transfer tax (page updated June 1, 2026)",
                     "https://www.tax.ny.gov/bus/transfer/rptidx.htm"),
    "rpl462": ("New York Real Property Law section 462, property condition disclosure statement (NY State Senate, revised July 4, 2025)",
               "https://www.nysenate.gov/legislation/laws/RPP/462"),
    "nysba": ("New York State Bar Association, new disclosure and flood rules take effect, March 20, 2024",
              "https://nysba.org/breaking-news-new-rules-on-property-condition-disclosure-and-flood-risk-go-into-effect-today/"),
    "arc": ("Nassau County Assessment Review Commission, filing an appeal", "https://www.nassaucountyny.gov/arc"),
    "lrv": ("Nassau County LandRecord Lookup, property assessment records", "https://lrv.nassaucountyny.gov/"),
    "hempstead_tax": ("Town of Hempstead Receiver of Taxes, tax payment schedule",
                      "https://hempsteadny.gov/381/Tax-Payment-Schedule"),
    "dtf_newbuyers": ("NYS Department of Taxation and Finance, Assessments and property taxes for new homebuyers (updated May 14, 2026)",
                      "https://www.tax.ny.gov/pit/property/new-homebuyers/"),
    "irs701": ("IRS Topic no. 701, Sale of your home (reviewed October 12, 2026)", "https://www.irs.gov/taxtopics/tc701"),
    "irs_inherit": ("IRS, Gifts and inheritances FAQ (reviewed September 29, 2026)",
                    "https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances"),
    "courts_dies": ("New York State Unified Court System, When someone dies", "https://nycourts.gov/courthelp/WhenSomeoneDies"),
    "nassau_surr": ("Surrogate's Court, Nassau County (New York State Unified Court System)",
                    "https://courts.state.ny.us/COURTS/10JD/nassau/surrogates.shtml"),
    "it2663": ("NYS Form IT-2663, Nonresident Real Property Estimated Income Tax Payment Form (2024 form)",
               "https://www.tax.ny.gov/pdf/2024/inc/it2663_2024_fill_in.pdf"),
    "rpapl1304": ("New York RPAPL section 1304, 90-day pre-foreclosure notice (NY State Senate)",
                  "https://www.nysenate.gov/legislation/laws/RPA/1304"),
    "hopp": ("NYS Homes and Community Renewal, foreclosure prevention counseling (Attorney General's Homeowner Protection Program)",
             "https://hcr.ny.gov/prevention-counseling"),
    "cfpb_scra": ("Consumer Financial Protection Bureau, foreclosure protection for servicemembers (reviewed May 31, 2023)",
                  "https://www.consumerfinance.gov/ask-cfpb/i-am-on-active-duty-in-the-military-or-have-been-on-active-duty-within-the-past-year-am-i-protected-from-foreclosure-en-306"),
    "nar_settlement": ("National Association of REALTORS, What the NAR settlement means for home buyers and sellers (updated May 24, 2024)",
                       "https://www.nar.realtor/the-facts/what-the-nar-settlement-means-for-home-buyers-and-sellers"),
    "dos_guide": ("New York Department of State, consumer guide to working with real estate licensees (August 2021)",
                  "https://dos.ny.gov/system/files/documents/2021/08/realestate_guide_08-20-21.pdf"),
    "dos_1736": ("New York Department of State, Disclosure Form for Buyer and Seller (DOS-1736)",
                 "https://dos.ny.gov/system/files/documents/2023/09/dos-1736-f-disclosure-form-for-buyer-and-seller_09.2021.pdf"),
    "nar_acronyms": ("National Association of REALTORS, designations and certifications acronym guide",
                     "https://www.nar.realtor/sites/default/files/documents/NAR-Acronyms-for-AEs-V3-01-2021-10-25.pdf"),
    "fema_msc": ("FEMA Flood Map Service Center, search by address", "https://msc.fema.gov/portal/search"),
    "fema_risk": ("FEMA, flood risk for homeowners and renters (updated November 4, 2020)",
                  "https://www.fema.gov/flood-maps/products-tools/know-your-risk/homeowners-renters"),
    "onekey_page": ("OneKey MLS, market statistics (monthly county reports)", "https://corporate.onekeymls.com/market-statistics"),
    "onekey_sep": ("OneKey MLS Local Market Update, Nassau County, September 2026 (current as of October 7, 2026)",
                   "https://corporate.onekeymls.com/s/NassauCounty-t8fn.pdf"),
}

# OneKey MLS Local Market Update, Nassau County, single-family homes.
# (month, new listings, closed sales, days on market, median price, % of original list received)
# Each monthly report shows that month in 2025 and 2026. Reports checked Nov 8, 2026.
ONEKEY_2026 = [
    ("January", 672, 619, 55, 835000, 97.2),
    ("February", 576, 489, 54, 850000, 98.7),
    ("March", 1014, 527, 58, 849000, 99.0),
    ("April", 1352, 478, 51, 852000, 99.2),
    ("May", 1164, 579, 51, 890000, 100.3),
    ("June", 1241, 743, 42, 875000, 101.3),
    ("July", 1063, 891, 38, 880000, 101.0),
    ("August", 951, 881, 38, 911000, 100.5),
    ("September", 929, 757, 40, 860000, 99.8),
]
ONEKEY_2025 = [
    ("January", 783, 650, 66, 810000, 98.5),
    ("February", 755, 507, 68, 800000, 98.8),
    ("March", 1063, 577, 63, 816000, 98.1),
    ("April", 1198, 552, 45, 790000, 100.1),
    ("May", 1291, 600, 45, 810000, 100.1),
    ("June", 1182, 732, 42, 850000, 100.6),
    ("July", 1079, 828, 34, 855000, 100.6),
    ("August", 897, 908, 37, 870000, 100.1),
    ("September", 1037, 789, 43, 842500, 98.9),
]
ONEKEY_REPORTS = [
    ("January", "https://corporate.onekeymls.com/s/2026-01_Nassau_County.pdf"),
    ("February", "https://corporate.onekeymls.com/s/2026-02_Nassau_County.pdf"),
    ("March", "https://corporate.onekeymls.com/s/NassauCounty.pdf"),
    ("April", "https://corporate.onekeymls.com/s/NassauCounty-46tn.pdf"),
    ("May", "https://corporate.onekeymls.com/s/NassauCounty-prnw.pdf"),
    ("June", "https://corporate.onekeymls.com/s/NassauCounty-xp82.pdf"),
    ("July", "https://corporate.onekeymls.com/s/NassauCounty-69bl.pdf"),
    ("August", "https://corporate.onekeymls.com/s/NassauCounty-yb65.pdf"),
    ("September", "https://corporate.onekeymls.com/s/NassauCounty-t8fn.pdf"),
]


def money(n):
    return f"${n:,.0f}"


def season_table():
    rows = "".join(
        f"<tr><td>{m}</td><td>{nl:,}</td><td>{cs:,}</td><td>{dom}</td><td>{money(p)}</td><td>{pct}%</td>"
        f"<td>{b[3]}</td><td>{b[5]}%</td></tr>"
        for (m, nl, cs, dom, p, pct), b in zip(ONEKEY_2026, ONEKEY_2025))
    return ('<div class="tablewrap"><table><thead><tr><th>Month</th><th>New listings 2026</th><th>Closed sales 2026</th>'
            '<th>Median days on market 2026</th><th>Median price 2026</th><th>Percent of original list price 2026</th>'
            '<th>Median days on market 2025</th><th>Percent of original list price 2025</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div>'
            '<p class="note">Nassau County single-family homes, from the OneKey MLS Local Market Update for each month, '
            'checked November 8, 2026. These are countywide figures, not figures for any one town. October through December '
            'are added as OneKey publishes them.</p>')


def price_table():
    rows = "".join(f"<tr><td>{m} 2026</td><td>{money(p)}</td><td>{pct}%</td><td>{dom}</td></tr>"
                   for m, _, _, dom, p, pct in ONEKEY_2026)
    return ('<div class="tablewrap"><table><thead><tr><th>Month</th><th>Median sale price</th>'
            '<th>Percent of original list price received</th><th>Median days on market</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div>'
            '<p class="note">Nassau County single-family homes, OneKey MLS monthly Local Market Updates, checked November 8, 2026. '
            'Countywide figures, not any one town.</p>')


def transfer_rows():
    out = []
    for price in (600000, 860000, 1200000):
        state = price / 500 * 2
        mansion = price * 0.01 if price >= 1000000 else 0
        out.append(f"<tr><td>{money(price)}</td><td>{money(state)}</td>"
                   f"<td>{money(mansion) if mansion else 'None'}</td></tr>")
    return ('<div class="tablewrap"><table><thead><tr><th>Sale price</th><th>State transfer tax, usually paid by the seller</th>'
            '<th>Mansion tax, paid by the buyer</th></tr></thead><tbody>' + "".join(out) + '</tbody></table></div>'
            '<p class="note">Worked from the rates the New York State Department of Taxation and Finance publishes: $2 for each $500 of '
            'consideration, plus a 1 percent mansion tax on residences sold for $1 million or more. The supplemental rates on that page '
            'apply only in New York City.</p>')


def T(slug, name):
    return f'<a href="{GUIDE}/towns/{slug}/">{name}</a>'


TOWN_LINKS = ", ".join([T("valley-stream", "Valley Stream"), T("lynbrook", "Lynbrook"),
                        T("rockville-centre", "Rockville Centre"), T("oceanside", "Oceanside"),
                        T("baldwin", "Baldwin"), T("freeport", "Freeport")])

GUIDES = []


def guide(**kw):
    GUIDES.append(kw)


# 1. Pricing -------------------------------------------------------------
guide(
    path="/sellers/pricing/", short="Pricing a home in Nassau County",
    title="How to price a home to sell in Nassau County | Bisendra Melaram",
    desc="How to set a list price for a Nassau County home from closed sales, with 2026 OneKey MLS county data, by seller's agent Bisendra Melaram, PSA.",
    h1="How to price a home to sell in Nassau County",
    answer="Price a Nassau County home from recent closed sales of similar homes nearby, then adjust for condition, size, lot, flood zone and school district. In September 2026 Nassau single-family homes sold for a median $860,000 and 99.8 percent of their original list price, so homes priced near the market tend to sell close to it.",
    about="Pricing a home for sale in Nassau County, NY",
    sections=[
        ("Why do closed sales matter more than asking prices?",
         "<p>An asking price is what a seller hopes for. A closed sale is what a buyer paid, what a lender financed and what an appraiser supported. "
         "When a buyer finances the purchase, the lender's appraisal is built on comparable closed sales, so a contract price far above them can leave a gap "
         "the buyer has to cover in cash or the seller has to give back.</p>"),
        ("What does the Nassau County market say in 2026?",
         "<p>OneKey MLS publishes monthly figures for single-family homes across Nassau County. In 2026 the county median ranged from $835,000 in January to "
         "$911,000 in August, and sellers received between 97.2 and 101.3 percent of their original list price.</p>" + price_table()),
        ("What changes the price of a South Shore home?",
         "<ul>"
         "<li>The flood zone. New York's property condition disclosure asks whether any part of the property is in a FEMA floodplain, whether flood insurance is required, and whether flood claims were filed. Buyers price that in.</li>"
         "<li>The school district. District lines on the South Shore do not follow town names, and the disclosure form asks the seller to name the district.</li>"
         "<li>Village or hamlet. Homes in incorporated villages carry village taxes on top of town, county and school taxes.</li>"
         "<li>Condition, permits and certificates of occupancy. The disclosure form asks about them, and open permits slow a closing.</li>"
         "<li>Size, lot, parking, and how recently the kitchen, baths, roof and systems were updated.</li>"
         "</ul>"
         f"<p>Each <a href=\"{GUIDE}/towns/\">South Shore town guide</a> covers the flood, school district and village questions for that town.</p>"),
        ("What happens when a home is priced above the market?",
         "<p>It usually sits. In OneKey's 2026 county figures, the months with the shortest median days on market, June through August at 38 to 42 days, "
         "were also the months when sellers received the most of their original list price, 100.5 to 101.3 percent. In January, homes took a median 55 days "
         "and sellers received 97.2 percent.</p>"),
        ("How does Bisendra build a price?",
         "<p>He holds the Pricing Strategy Advisor (PSA) certification from the National Association of REALTORS, and he prices from closed sales on your street "
         f"and in your section of town, not from what neighbors are asking. {todo('how you walk a seller through pricing: which sales you pull, how far back, how you adjust, and how you present it')}</p>"),
    ],
    steps=("How to set a list price for a Nassau County home", [
        ("Pull recent closed sales", "Find similar homes that closed nearby in the last three to six months, in the same school district and flood zone if you can."),
        ("Adjust for differences", "Adjust each sale for size, bedrooms and baths, lot, condition, updates and parking."),
        ("Check the competition", "Look at active and pending listings to see what buyers can choose from right now."),
        ("Check the trend", "Compare the latest county figures from OneKey MLS to see whether prices and days on market are moving."),
        ("Set the price and review it", "List within the range the sales support, then review it against new sales and showing activity."),
    ]),
    faqs=[
        ("Should I price high and leave room to negotiate?",
         "Usually not. Buyers and their agents compare your home with recent closed sales, and a price well above them tends to draw fewer showings. In 2026 Nassau County sellers received a median 97.2 to 101.3 percent of original list price, per OneKey MLS."),
        ("Does my Nassau County assessment tell me what my home is worth?",
         "Not for a sale. Nassau County assesses homes at 0.1 percent of the county's estimate of market value, for tax purposes. Buyers pay based on recent closed sales, condition and location, which can differ a lot from the county's estimate."),
        ("What is a Pricing Strategy Advisor?",
         "PSA is a certification from the National Association of REALTORS for agents trained in pricing homes and working with appraisals and market data. Bisendra Melaram holds the PSA certification."),
        ("How often should my list price be reviewed?",
         "Whenever new comparable sales close or showing activity changes. If similar homes nearby are going to contract and yours is not, price is the first thing to look at."),
    ],
    sources=["onekey_sep", "onekey_page", "rpl462", "lrv", "nar_acronyms"],
    related=["/sellers/best-time-to-sell/", "/sellers/cost-to-sell/", "/sellers/property-taxes/", "/how-i-sell-a-home/"],
)

# 2. Cost to sell --------------------------------------------------------
guide(
    path="/sellers/cost-to-sell/", short="What it costs to sell",
    title="What it costs to sell a home on Long Island | Bisendra Melaram",
    desc="Seller costs on Long Island: negotiable commission, New York transfer tax at $2 per $500, attorney fees, payoffs, concessions and taxes on the gain.",
    h1="What it costs to sell a home on Long Island",
    answer="Selling a Long Island home usually costs the commission you negotiate, New York's transfer tax of $2 for every $500 of the price, your attorney's fee, your mortgage payoff and any credits you give the buyer. On an $860,000 sale the state transfer tax is $3,440. Buyers pay the 1 percent mansion tax at $1 million and up.",
    about="Seller closing costs on Long Island, NY",
    sections=[
        ("How is the real estate commission set?",
         "<p>By agreement between you and your listing agent. The National Association of REALTORS states that agent compensation is fully negotiable and not set by law. "
         "Since August 17, 2024, offers of compensation to buyer's agents can no longer appear on MLS platforms, though sellers can still offer them off the MLS, "
         "and sellers can offer buyers concessions such as help with closing costs.</p>"),
        ("How much is the New York transfer tax?",
         "<p>New York charges $2 for each $500 of the price, or 0.4 percent, and the seller pays it by default. Residences sold for $1 million or more also carry "
         "a 1 percent mansion tax, which the buyer pays. Outside New York City the transfer is reported on Form TP-584, filed with the county clerk.</p>"
         + transfer_rows()),
        ("What does a seller's attorney cost?",
         f"<p>Fees vary by firm and by how much work the sale needs, so ask for a written quote before you list. {todo('optional: whether you can refer sellers to attorneys you work with, with no fee figures unless the attorney confirms them')}</p>"),
        ("What comes out of the proceeds at closing?",
         "<ul><li>The payoff on your mortgage and any home equity line.</li>"
         "<li>The transfer tax and the commission you agreed to.</li>"
         "<li>Any credit you agreed to give the buyer, for repairs or closing costs.</li>"
         "<li>Property tax adjustments. Town of Hempstead general taxes are billed in halves due January 1 and July 1, and school taxes in halves due October 1 and April 1, "
         "so taxes you prepaid or still owe are adjusted between you and the buyer at closing.</li>"
         "<li>Final water and other utility charges.</li></ul>"),
        ("Do you owe income tax on the sale?",
         "<p>Often not on your main home. The IRS lets you exclude up to $250,000 of gain, or $500,000 on a joint return, if you owned and lived in the home for at least two "
         "of the last five years. If you live outside New York when you sell, the state collects estimated tax at closing on Form IT-2663, figured at the top state rate, "
         "10.90 percent on the 2024 form. Ask a tax adviser about your own numbers.</p>"),
    ],
    steps=("How to estimate your net proceeds from a Long Island sale", [
        ("Start with a realistic price", "Use recent closed sales nearby, not asking prices."),
        ("Subtract the payoffs", "Ask your lender for a payoff figure on the mortgage and any home equity line."),
        ("Subtract the transfer tax", "Multiply the price by 0.4 percent, which is $2 for each $500."),
        ("Subtract commission and attorney fees", "Use the commission in your listing agreement and your attorney's written quote."),
        ("Allow for credits and adjustments", "Leave room for buyer credits, tax adjustments and final utility bills."),
    ]),
    faqs=[
        ("Who pays the New York State transfer tax on Long Island?",
         "The seller, by default. The New York State Department of Taxation and Finance says the base transfer tax of $2 for each $500 of the price is paid by the grantor, which is the seller."),
        ("Who pays the mansion tax?",
         "The buyer. New York's 1 percent mansion tax applies to residences sold for $1 million or more, and the state says the buyer pays it."),
        ("Is the real estate commission negotiable in New York?",
         "Yes. The National Association of REALTORS states that broker compensation is fully negotiable and not set by law. Agree on it in writing in your listing agreement."),
        ("I moved out of New York. Is anything due at closing?",
         "Yes, if you are a nonresident selling New York real property. Form IT-2663 and an estimated tax payment are submitted with the deed when it is recorded. If the sale is a loss, no estimated tax is due, but the form is still completed."),
    ],
    sources=["dtf_transfer", "nar_settlement", "hempstead_tax", "irs701", "it2663"],
    related=["/sellers/pricing/", "/sellers/property-taxes/", "/sellers/choosing-a-listing-agent/", "/how-i-sell-a-home/"],
)

# 3. Best time ----------------------------------------------------------
guide(
    path="/sellers/best-time-to-sell/", short="Best time to list",
    title="Best time to list a South Shore home | Bisendra Melaram",
    desc="When to list a Nassau County home, from 2025 and 2026 OneKey MLS monthly data: days on market, percent of list price received and new listings.",
    h1="When is the best time to list a home on the South Shore?",
    answer="In 2026, Nassau County single-family homes sold fastest and closest to their asking price from June through August, when median days on market fell to 38 to 42 and sellers received 100.5 to 101.3 percent of original list price, per OneKey MLS. New listings peaked in April, and 2025 followed the same pattern.",
    about="Seasonality of home sales in Nassau County, NY",
    sections=[
        ("What do the 2025 and 2026 numbers show?",
         "<p>Across both years, homes that closed in late spring and summer sold faster and for a larger share of their original price than homes that closed in winter. "
         "Closed sales peaked in July and August. New listings were highest in April and May, which means more competition for sellers listing then.</p>" + season_table()),
        ("Is there an advantage to listing in winter?",
         "<p>Less competition. At the end of January 2026 there were 1,497 single-family homes for sale in Nassau County, compared with 2,327 at the end of June. "
         "The tradeoff in 2026 was a longer median time to sell, 55 days in January, and a lower share of the original price, 97.2 percent.</p>"),
        ("Does the month matter more than the price?",
         "<p>No. A well-priced, well-prepared home sells in any month, and an overpriced one sits in May. Use the season to plan your timing, then price from closed sales "
         f"and prepare the house. See <a href=\"/sellers/pricing/\">how to price a Nassau County home</a>.</p>"),
        ("How should South Shore sellers plan around the calendar?",
         "<ul><li>Give yourself time to prepare. Repairs, permits and the disclosure form, including its flood answers, take weeks, not days.</li>"
         "<li>Know your tax dates. Town of Hempstead school taxes are due in halves on October 1 and April 1, and general taxes on January 1 and July 1, and they are adjusted at closing.</li>"
         "<li>Line up your next move before you list, especially if you are buying in the same season everyone else is.</li></ul>"),
        ("When does Bisendra recommend listing?",
         f"<p>{todo('your own view on timing a South Shore listing, in your words')}</p>"),
    ],
    faqs=[
        ("What is the best month to sell a house in Nassau County?",
         "In 2025 and 2026 OneKey MLS data, homes that closed in June, July and August sold fastest and for the highest share of their original list price. Because closings follow contracts by weeks, that points to listing in spring."),
        ("Are there fewer buyers in winter on Long Island?",
         "OneKey's county figures show fewer closed sales and fewer homes for sale in January and February. Fewer listings means less competition for the sellers who do list."),
        ("Do these numbers apply to my town?",
         "They are countywide figures for Nassau single-family homes. Town patterns can differ, so ask for the closed sales in your own town and section."),
    ],
    sources=["onekey_page", "onekey_sep", "hempstead_tax"],
    related=["/sellers/pricing/", "/sellers/property-condition-disclosure/", "/sellers/cost-to-sell/"],
    onekey_reports=True,
)

# 4. Disclosure ----------------------------------------------------------
guide(
    path="/sellers/property-condition-disclosure/", short="New York property condition disclosure",
    title="NY property condition disclosure for sellers | Bisendra Melaram",
    desc="What New York home sellers must disclose under Real Property Law 462: who files, when, the flood questions since 2024, and how to prepare.",
    h1="New York property condition disclosure: what sellers must disclose now",
    answer="New York sellers of one to four family homes must give the buyer a signed property condition disclosure statement before the buyer signs the contract. Since March 20, 2024, sellers can no longer give a $500 credit instead, and the form asks eight flood questions, from FEMA flood zones and required insurance to past claims and federal flood aid.",
    about="New York property condition disclosure statement, Real Property Law section 462",
    sections=[
        ("Who has to complete the disclosure?",
         "<p>Sellers of one to four family homes used as a residence. Real Property Law section 462 excludes unimproved land, condominium units, cooperative apartments, "
         "and property in a homeowners association that the seller does not own in fee. Section 463 lists further exemptions, so ask your attorney whether one applies to you.</p>"),
        ("When is it due?",
         "<p>Before the buyer signs a binding contract of sale. The seller signs it and delivers it to the buyer or the buyer's agent, and a copy signed by both is attached to the contract.</p>"),
        ("What are the flood questions?",
         "<ol>"
         "<li>Is any part of the property in a FEMA-designated floodplain?</li>"
         "<li>Is any part in a special flood hazard area, the 100-year floodplain, on current FEMA maps?</li>"
         "<li>Is any part in a moderate risk flood zone, the 500-year floodplain?</li>"
         "<li>Is the property subject to a federal requirement to carry flood insurance?</li>"
         "<li>Has the seller, or to the seller's knowledge a prior owner, received FEMA, SBA or other federal flood disaster aid?</li>"
         "<li>Is there flood insurance on the property? If so, a copy of the policy is attached.</li>"
         "<li>Is there a FEMA elevation certificate? If so, a copy is attached.</li>"
         "<li>Has a flood damage claim ever been filed with any insurer, including the National Flood Insurance Program?</li>"
         "</ol>"
         "<p>Separate questions ask about flooding, drainage or grading problems that caused standing water, and whether the structure has had water seep in or flood damage. "
         "The form also notes that standard homeowner's policies usually do not cover flood damage.</p>"),
        ("What else does the form ask?",
         "<ul><li>How long you have owned and lived in the home, and any rights others have to use the property.</li>"
         "<li>Shared walls, fences or driveways, special assessments, and certificates of occupancy.</li>"
         "<li>The age of the structure, with a lead paint note for homes built before 1978.</li>"
         "<li>Fuel storage tanks, spills, landfill use, asbestos, lead plumbing, radon and mold testing.</li>"
         "<li>Wetlands, rot, fire damage, pests, the roof and structural defects.</li>"
         "<li>Water source, sewer or septic, electric service, and known defects in plumbing, heating, cooling, the foundation and other systems.</li>"
         "<li>The school district the home is in.</li></ul>"),
        ("Do you have to inspect your own home or research public records?",
         "<p>No. The statute says the disclosure is not a warranty and the seller has no duty to inspect or check public records. You answer from what you actually know, "
         "and you must give the buyer a revised statement if you learn something that makes an answer materially wrong, until title transfers or the buyer moves in.</p>"),
        ("How does Bisendra prepare sellers for the disclosure?",
         f"<p>He has it ready before the first showing, flood answers included, so the questions buyers ask do not come up for the first time in attorney review. "
         f"{todo('your checklist or how you walk sellers through the form, in your words')}</p>"),
    ],
    steps=("How to prepare your New York property condition disclosure", [
        ("Look up your flood zone", "Search your address on FEMA's Flood Map Service Center and note the zone."),
        ("Gather flood records", "Find your flood insurance policy, any elevation certificate, and any claim or aid records."),
        ("Gather permits and certificates", "Collect certificates of occupancy and permits for past work, and ask the building department about any open permits."),
        ("Collect system records", "Pull records on the roof, heating, fuel tanks, radon or mold tests and septic or sewer work."),
        ("Answer from what you know", "Complete each answer honestly, mark unknown where you do not know, and review it with your attorney before listing."),
    ]),
    faqs=[
        ("Can I still give the buyer a $500 credit instead of the disclosure?",
         "No. Since March 20, 2024, New York sellers of most one to four family homes must complete the property condition disclosure statement. The $500 credit option is gone."),
        ("Does a condo or co-op seller fill out the disclosure?",
         "Not this one. New York Real Property Law section 462 excludes condominium units and cooperative apartments from the property condition disclosure statement."),
        ("Do I have to hire an inspector before I answer?",
         "No. The statute says the seller has no duty to inspect the property or search public records. You answer from your actual knowledge."),
        ("What if my answers change after the buyer signs?",
         "If you learn something that makes an answer materially inaccurate, you must deliver a revised statement as soon as practicable, up until title transfers or the buyer moves in."),
    ],
    sources=["rpl462", "nysba", "fema_msc"],
    related=["/sellers/second-home/", "/sellers/pricing/", "/sellers/inherited-home/"],
    guide_link=("South Shore flood zone guide", f"{GUIDE}/guides/flood-zones/"),
)

# 5. Inherited home ------------------------------------------------------
guide(
    path="/sellers/inherited-home/", short="Selling an inherited home",
    title="Selling an inherited home in Nassau County | Bisendra Melaram",
    desc="How to sell an inherited home in Nassau County: Surrogate's Court, probate and administration, who signs, taxes on inherited property, and the house itself.",
    h1="How do you sell an inherited home in Nassau County?",
    answer="An inherited Nassau County home is usually sold by the estate's executor or administrator, appointed by the Nassau County Surrogate's Court in Mineola. Probate applies when there is a will and administration when there is not. The IRS generally sets the heirs' tax basis at the home's fair market value on the date of death.",
    about="Selling an estate or inherited home in Nassau County, NY",
    sections=[
        ("Which court handles a Nassau County estate?",
         "<p>The Surrogate's Court, Nassau County, at 262 Old Country Road, Mineola, NY 11501, phone 516-493-3800. The New York courts explain that the Surrogate's Court "
         "decides what happens to a person's property after death.</p>"),
        ("What is the difference between probate and administration?",
         "<p>Probate is the process when the person left a will, and property is divided as the will directs. Administration is the process when there is no will, and property "
         "is divided as the law directs. The courts also offer a simpler small estate process for estates with less than $50,000 of personal property, and they note that "
         "houses and land are real property, not personal property. Ask the estate's attorney which process fits.</p>"),
        ("Who can sign the contract and deed?",
         "<p>The executor or administrator serves as the estate's fiduciary. Who can sign, and when, depends on the will, the court's appointment and how title was held, so the "
         "estate's attorney confirms it before the home is listed.</p>"),
        ("How are taxes handled on an inherited home?",
         "<ul><li>The IRS says the basis of inherited property is generally its fair market value on the date of death, or the alternate valuation date if the executor elects it on Form 706.</li>"
         "<li>Gross proceeds from selling inherited property are generally included in income, so keep the date-of-death valuation and the closing statement.</li>"
         "<li>If the seller is an estate, trust or individual who is not a New York resident, Form IT-2663 and an estimated tax payment go in with the deed at closing.</li>"
         "<li>Property taxes keep coming due. In the Town of Hempstead, general taxes are due in halves on January 1 and July 1 and school taxes on October 1 and April 1.</li></ul>"),
        ("Does the estate have to fill out the property condition disclosure?",
         "<p>Section 462 covers sellers of one to four family homes, and section 463 lists exemptions. Whether an estate sale qualifies is a question for the estate's attorney. "
         "If the form is completed, it is answered from actual knowledge, and the statute does not require the seller to inspect.</p>"),
        ("What should happen to the house while the estate is open?",
         "<p>Keep it insured, heated in winter and checked on. Tell the insurance company the home is vacant, because coverage can change. Keep the utilities on for showings and the "
         f"inspection, and save the mail for tax bills. {todo('how you help executors with an estate sale: cleanout, repairs, family coordination, in your words')}</p>"),
    ],
    steps=("How to sell an inherited home in Nassau County", [
        ("Hire an estate attorney", "Ask whether probate, administration or another process applies, and who can sign."),
        ("Get the fiduciary appointed", "The Surrogate's Court, Nassau County appoints the executor or administrator."),
        ("Value the home as of the date of death", "A date-of-death valuation supports the tax basis the IRS describes."),
        ("Protect the house", "Keep insurance, heat, utilities and tax payments current while the estate is open."),
        ("Price and list it", "Price from recent closed sales nearby and prepare the house for buyers and inspectors."),
    ]),
    faqs=[
        ("Can heirs sell a house before probate is finished in New York?",
         "It depends on the will, the court's appointment and how title was held. The estate's executor or administrator is the fiduciary, and the estate's attorney confirms when a contract can be signed."),
        ("Is the small estate process enough to sell a house?",
         "The New York courts describe the small estate process for estates with less than $50,000 of personal property, and they note that houses and land are real property, not personal property. Ask the estate's attorney which process fits."),
        ("What is the tax basis of an inherited house?",
         "Generally its fair market value on the date of death, according to the IRS, or the alternate valuation date if the executor elects it on the estate tax return."),
        ("Where is the Nassau County Surrogate's Court?",
         "262 Old Country Road, Mineola, NY 11501. The court's phone number is 516-493-3800."),
    ],
    sources=["nassau_surr", "courts_dies", "irs_inherit", "it2663", "rpl462", "hempstead_tax"],
    related=["/sellers/property-condition-disclosure/", "/sellers/pricing/", "/sellers/cost-to-sell/"],
)

# 6. Downsizing (SRES) ---------------------------------------------------
guide(
    path="/downsizing/", short="Downsizing and later-life moves", crumb="Downsizing",
    title="Downsizing on Long Island | Bisendra Melaram, SRES",
    desc="How to sell a long-time Long Island home and plan the next move, from Bisendra Melaram, who holds the Seniors Real Estate Specialist (SRES) designation.",
    h1="Downsizing and selling a long-time home on Long Island",
    answer="Downsizing works best when the sale and the next move are planned together: price from recent closed sales, prepare the house, and line up the dates so you move once. Bisendra Melaram holds the Seniors Real Estate Specialist (SRES) designation, training focused on later-life moves, and works alongside your attorney and tax adviser.",
    about="Downsizing and selling a long-time home on Long Island, NY",
    sections=[
        ("What does an SRES agent do differently?",
         "<p>The Seniors Real Estate Specialist designation from the National Association of REALTORS trains agents in the questions that come with a later-life move: timing a "
         "sale with a purchase, sorting a house full of belongings, working with family members you choose to involve, and knowing when to bring in an attorney or tax adviser. "
         f"{todo('one or two examples, without client names, of how you handled a downsizing sale')}</p>"),
        ("How do you sell a home you have lived in for decades?",
         "<p>One room at a time. Decide what moves with you, what goes to family, and what gets sold or donated. Then fix the few things a buyer's inspector will flag, gather "
         "permits and certificates of occupancy for past work, and price from what similar homes nearby have sold for.</p>"),
        ("Will you owe tax on the sale?",
         "<p>Often not much. The IRS lets you exclude up to $250,000 of gain, or $500,000 on a joint return, on the sale of your main home if you owned and lived in it for at "
         "least two of the last five years. Long-time owners can have gains above that, so ask a tax adviser before you list.</p>"),
        ("What happens to your STAR benefit when you move?",
         "<p>It stays with the property you leave. The New York State Department of Taxation and Finance tells new homeowners to register for the STAR credit once the new home "
         "becomes their primary residence.</p>"),
        ("Can you buy the next home before you sell this one?",
         "<p>Sometimes. It depends on your savings, your equity and what a lender approves. Options include a purchase contract contingent on your sale, or a sale that gives "
         "you time to move. Talk to a lender and your attorney early.</p>"),
        ("Who should be part of the plan?",
         "<p>You decide. Many sellers bring in adult children, an attorney and a financial or tax adviser. Bisendra keeps everyone you choose informed and takes direction from you.</p>"),
    ],
    faqs=[
        ("What is an SRES?",
         "SRES stands for Seniors Real Estate Specialist, a National Association of REALTORS designation for agents trained in later-life moves, such as downsizing and selling a long-time home. Bisendra Melaram holds it."),
        ("When is the right time to downsize?",
         "When the house costs more in money, time or upkeep than it gives back. Common signs are rooms nobody uses, stairs that have become hard, and taxes or repairs that strain the budget. The timing is your call."),
        ("Do I pay tax when I sell the home I raised my kids in?",
         "Possibly on part of the gain. The IRS excludes up to $250,000, or $500,000 for a married couple filing jointly, on a main home owned and lived in for two of the last five years. Ask a tax adviser about the rest."),
        ("Does my STAR exemption move to my new home?",
         "No. The New York State tax department tells new homeowners to register for the STAR credit once the new home is their primary residence."),
    ],
    sources=["nar_acronyms", "irs701", "dtf_newbuyers"],
    related=["/sellers/pricing/", "/sellers/cost-to-sell/", "/sellers/best-time-to-sell/", "/how-i-sell-a-home/"],
)

# 7. Short sale ----------------------------------------------------------
guide(
    path="/sellers/short-sale-pre-foreclosure/", short="Short sales and pre-foreclosure",
    title="Short sales and pre-foreclosure on Long Island | Bisendra Melaram",
    desc="Behind on a Long Island mortgage? New York's 90-day notice, free counseling, short sales and other options, from SFR-certified agent Bisendra Melaram.",
    h1="Short sales and pre-foreclosure options on Long Island",
    answer="If you are behind on a Long Island mortgage, New York law requires your lender to send a notice at least 90 days before starting foreclosure on an owner-occupied home, with a list of housing counseling agencies. Free counseling is available through the state Attorney General's Homeowner Protection Program. A short sale needs your lender's written approval.",
    about="Short sales and pre-foreclosure options in New York",
    sections=[
        ("What is the 90-day notice?",
         "<p>Under New York's RPAPL section 1304, a lender, assignee or loan servicer must give the borrower notice at least 90 days before starting legal action, including "
         "foreclosure, on a home loan. The notice must list at least five housing counseling agencies that serve the county, with their addresses and phone numbers. "
         "It covers loans on one to four family homes and condominiums the borrower lives in as a principal residence.</p>"),
        ("Where can you get free help?",
         "<p>Through the Homeowner Protection Program run by the New York State Office of the Attorney General, which funds free counseling and legal services. Start with an "
         "agency on the list in your 90-day notice. Be wary of anyone who charges upfront to save your home.</p>"),
        ("What options do you have before a foreclosure?",
         "<ul><li>Catch up on the missed payments, or agree to a repayment plan.</li>"
         "<li>Ask the servicer about a loan modification.</li>"
         "<li>Sell the home at market value and pay off the loan, if there is enough equity.</li>"
         "<li>A short sale, if the home is worth less than what you owe.</li>"
         "<li>Other options your servicer and counselor can explain, such as handing over the deed.</li></ul>"),
        ("How does a short sale work?",
         "<p>The lender agrees to accept less than the full payoff so the home can be sold. Expect to submit financial documents, a hardship letter and a signed contract, and expect "
         "the lender to review the price against its own valuation. Every lien holder, including a second mortgage or home equity line, has to agree. Ask your attorney and a tax "
         "adviser how any unpaid balance is treated before you sign.</p>"),
        ("What is an SFR?",
         "<p>Short Sales and Foreclosure Resource is a National Association of REALTORS certification for agents trained in short sales and distressed sales. Bisendra Melaram "
         f"holds it and has worked through distressed markets since 2003. {todo('how you handle a short sale listing, without client names')}</p>"),
    ],
    steps=("What to do when you fall behind on a Long Island mortgage", [
        ("Open every letter", "Read the 90-day notice and keep the list of counseling agencies it includes."),
        ("Call a counselor", "Contact a free housing counselor funded through the Attorney General's Homeowner Protection Program."),
        ("Talk to your servicer", "Ask about repayment plans and modifications, and get answers in writing."),
        ("Get a market value", "Find out what the home would sell for, from recent closed sales nearby."),
        ("Decide with your attorney", "Choose between keeping the home, a market sale and a short sale before the foreclosure moves forward."),
    ]),
    faqs=[
        ("How much notice does a New York lender give before foreclosure?",
         "At least 90 days for a home loan on an owner-occupied one to four family home or condominium, under RPAPL section 1304. The notice lists at least five housing counseling agencies."),
        ("Is foreclosure counseling free in New York?",
         "Yes. The Attorney General's Homeowner Protection Program funds free counseling and legal services for homeowners facing foreclosure."),
        ("Does a short sale need my lender's approval?",
         "Yes. In a short sale the lender accepts less than the full payoff, so it has to approve the sale in writing, and every other lien holder has to agree too."),
        ("Can I sell my house if I am behind on payments?",
         "Often yes, as long as the sale closes before the foreclosure is complete and the payoff is covered or the lender approves a short sale. Ask your attorney about your timeline."),
    ],
    sources=["rpapl1304", "hopp", "nar_acronyms"],
    related=["/sellers/pricing/", "/sellers/cost-to-sell/", "/sellers/military-relocation/"],
)

# 8. Military ------------------------------------------------------------
guide(
    path="/sellers/military-relocation/", short="Selling for military orders",
    title="Selling a Long Island home on military orders | Bisendra Melaram, MRP",
    desc="Selling or renting your Long Island home when military orders move you: the IRS five-year suspension, SCRA protections and selling from a distance.",
    h1="Selling a Long Island home when military orders move you",
    answer="If military orders move you off Long Island, the usual IRS home sale rules apply with one added benefit: servicemembers on qualified official extended duty can suspend the five-year test for up to 10 years. If your mortgage predates active duty, federal law also limits foreclosure during service and for 12 months after.",
    about="Selling a home on Long Island for a military relocation",
    sections=[
        ("Should you sell now or rent the home out?",
         "<p>The tax rules are a big part of the answer. The IRS lets you exclude up to $250,000 of gain, or $500,000 on a joint return, if you owned and lived in the home for two "
         "of the five years before the sale. If you or your spouse are on qualified official extended duty, you can elect to suspend that five-year period for up to 10 years, "
         "which gives you more time to rent first and still sell with the exclusion. Confirm your dates with a tax adviser.</p>"),
        ("What protections does the SCRA give homeowners?",
         "<p>The Consumer Financial Protection Bureau explains that if you took out the mortgage before active duty, you generally cannot be foreclosed on without a court order "
         "while on active duty and for 12 months after. You can also ask for the interest rate to be cut to 6 percent, fees included, for active duty plus one year.</p>"),
        ("Can you sell a Long Island home from another state or overseas?",
         "<p>Yes. Your attorney can handle much of the closing, and a power of attorney can let someone sign for you. Plan for showings, the inspection and the final walk-through "
         "with the house empty or tenanted. If you are no longer a New York resident when you sell, Form IT-2663 and an estimated tax payment go in with the deed.</p>"),
        ("What is an MRP?",
         "<p>Military Relocation Professional is a National Association of REALTORS certification for agents trained in military moves and benefits. Bisendra Melaram holds it. "
         f"{todo('how you work with military sellers on short timelines, in your words')}</p>"),
    ],
    faqs=[
        ("Do military homeowners get extra time for the home sale tax exclusion?",
         "Yes. If you or your spouse are on qualified official extended duty, the IRS lets you suspend the five-year test period for up to 10 years."),
        ("Can I be foreclosed on while deployed?",
         "If you took out the mortgage before active duty, the CFPB says you generally cannot be foreclosed on without a court order while on active duty and for 12 months after."),
        ("Can I close on my Long Island sale without being there?",
         "Often yes, with your attorney and a power of attorney. Ask your attorney early what the buyer's side and the title company will accept."),
    ],
    sources=["irs701", "cfpb_scra", "it2663", "nar_acronyms"],
    related=["/sellers/cost-to-sell/", "/sellers/short-sale-pre-foreclosure/", "/sellers/best-time-to-sell/"],
)

# 9. Second home ---------------------------------------------------------
guide(
    path="/sellers/second-home/", short="Selling a second home or beach property",
    title="Selling a Long Island second home | Bisendra Melaram, RSPS",
    desc="Selling a Long Island second home or waterfront property: taxes when it is not your main home, nonresident estimated tax, and flood disclosure.",
    h1="Selling a second home or beach property on Long Island",
    answer="Selling a Long Island second home or beach property follows the same disclosure and transfer tax rules as any sale, with two differences: the IRS home sale exclusion covers only your main home, and owners who live outside New York pay estimated state tax at closing on Form IT-2663. Near the water, the flood answers carry extra weight.",
    about="Selling a second home or waterfront property on Long Island, NY",
    sections=[
        ("How is the gain taxed if it is not your main home?",
         "<p>The IRS exclusion of up to $250,000, or $500,000 on a joint return, applies to the sale of your main home. A second home generally does not qualify, so the gain is "
         "usually taxable. Keep records of what you paid and what you spent on improvements, and talk to a tax adviser before you set a price you need to net.</p>"),
        ("What if you live outside New York?",
         "<p>Nonresident individuals, estates and trusts selling New York real property submit Form IT-2663 with an estimated tax payment when the deed is recorded. The estimate "
         "uses the top state rate, 10.90 percent on the 2024 form. If the sale is a loss, no estimated tax is due, but the form is still completed.</p>"),
        ("Why do the flood answers matter more near the water?",
         "<p>Buyers of waterfront and near-water homes read the flood section of the property condition disclosure first. It asks about FEMA flood zones, required flood insurance, "
         "elevation certificates, federal flood aid and past claims. Have the policy, the elevation certificate and any claim history ready before you list. FEMA notes that nearly "
         "25 percent of flood insurance claims come from outside high-risk zones.</p>"
         f"<p>See the <a href=\"{GUIDE}/guides/flood-zones/\">South Shore flood zone guide</a>.</p>"),
        ("What if the home is rented?",
         "<p>Tell your attorney early. An existing lease affects showings, the buyer's move-in date and the contract, and rental records help buyers who plan to rent it out too.</p>"),
        ("What is an RSPS?",
         "<p>Resort and Second-Home Property Specialist is a National Association of REALTORS certification for agents trained in vacation, resort and second-home sales. "
         f"Bisendra Melaram holds it. {todo('how you market second homes and beach properties, in your words')}</p>"),
    ],
    faqs=[
        ("Can I use the $250,000 exclusion on a second home?",
         "Generally no. The IRS exclusion applies to the sale of your main home, the one you owned and lived in for at least two of the last five years."),
        ("I live in another state. What do I owe New York when I sell?",
         "Nonresidents file Form IT-2663 with an estimated tax payment when the deed is recorded, figured at the top state rate on the gain. You settle the actual tax on your New York return."),
        ("Do beach houses need a flood disclosure?",
         "Yes, if the home is a one to four family residence. New York's property condition disclosure includes eight flood questions, and sellers can no longer give a $500 credit instead."),
    ],
    sources=["irs701", "it2663", "rpl462", "fema_risk", "nar_acronyms"],
    related=["/sellers/property-condition-disclosure/", "/sellers/cost-to-sell/", "/sellers/best-time-to-sell/"],
)

# 10. Choosing a listing agent -------------------------------------------
guide(
    path="/sellers/choosing-a-listing-agent/", short="Choosing a listing agent",
    title="How to choose a listing agent on Long Island | Bisendra Melaram",
    desc="How to choose a Long Island listing agent: verify the New York license, ask how they price from closed sales, read the listing agreement, negotiate the fee.",
    h1="How to choose a listing agent on Long Island",
    answer="Choose a Long Island listing agent by checking their New York license on the Department of State's eAccessNY system, asking how they would price your home from recent closed sales, reading the written listing agreement, and agreeing on the commission, which is fully negotiable and not set by law. Get their marketing plan in writing.",
    about="Choosing a listing agent to sell a home on Long Island, NY",
    sections=[
        ("How do you check an agent's license?",
         "<p>Search their name on eAccessNY from the New York Department of State website, dos.ny.gov, or call the Department at (518) 474-4429. The Department warns consumers "
         "not to rely only on business cards or ads.</p>"),
        ("Who will the agent represent?",
         "<p>New York agents must tell you whom they represent at your first substantive contact, using the state's Disclosure Form for Buyer and Seller. A listing agent "
         "represents the seller. Ask how the firm handles a buyer who is also its client.</p>"),
        ("What should you ask in the interview?",
         "<ul><li>Which closed sales support your price, and how they adjusted for your home.</li>"
         "<li>What they will fix, change or stage before photos, and what they would leave alone.</li>"
         "<li>Where the listing will be marketed, who shoots photos and video, and how showings are handled.</li>"
         "<li>How they will prepare the property condition disclosure, flood answers included.</li>"
         "<li>How often you will hear from them, and from whom.</li>"
         "<li>Which recent sales they handled, and where you can check them.</li></ul>"),
        ("What should be in the listing agreement?",
         "<p>The term and how to end it early, the commission, what the seller offers buyer's agents if anything, and what the agent commits to do. Since August 17, 2024, "
         "offers of compensation to buyer's agents no longer appear on the MLS, though sellers can still make them off the MLS. Read it with your attorney.</p>"),
        ("What do designations tell you?",
         "<p>They show training in a specialty. The Seller Representative Specialist (SRS) designation covers representing sellers, and the Pricing Strategy Advisor (PSA) "
         "certification covers pricing and appraisals. Ask any agent what their designations mean for your sale.</p>"),
        ("What should make you cautious?",
         "<ul><li>A suggested price far above recent closed sales with no data behind it.</li>"
         "<li>Pressure to sign a long agreement on the spot.</li>"
         "<li>Vague answers about marketing, disclosure or who will actually show the home.</li></ul>"),
    ],
    steps=("How to interview and hire a Long Island listing agent", [
        ("Verify the license", "Look the agent up on eAccessNY from dos.ny.gov."),
        ("Ask for a price with proof", "Ask for the closed sales behind the suggested price."),
        ("Get the plan in writing", "Ask for the marketing, preparation and communication plan in writing."),
        ("Read the listing agreement", "Review the term, commission and early termination terms with your attorney."),
        ("Negotiate and sign", "Agree on the commission, which is negotiable, then sign."),
    ]),
    faqs=[
        ("How do I check if a real estate agent is licensed in New York?",
         "Use eAccessNY on the New York Department of State website, dos.ny.gov, and search by the agent's or firm's name. You can also call the Department at (518) 474-4429."),
        ("Are real estate commissions negotiable on Long Island?",
         "Yes. The National Association of REALTORS states that broker compensation is fully negotiable and not set by law. Settle it in the written listing agreement."),
        ("What is a Seller Representative Specialist?",
         "SRS is a designation for agents trained in representing home sellers, awarded by the Real Estate Business Institute, a National Association of REALTORS affiliate. Bisendra Melaram holds it."),
        ("Does a listing agent have to say who they represent?",
         "Yes. New York requires agents to disclose whom they represent at the first substantive contact, using the Department of State's Disclosure Form for Buyer and Seller."),
    ],
    sources=["dos_guide", "dos_1736", "nar_settlement", "nar_acronyms"],
    related=["/how-i-sell-a-home/", "/sellers/pricing/", "/sellers/cost-to-sell/", "/about/"],
)

# 11. Property taxes -----------------------------------------------------
guide(
    path="/sellers/property-taxes/", short="Property taxes, grievances and your sale",
    title="Nassau property taxes and grievances | Bisendra Melaram",
    desc="How Nassau County property taxes affect a sale: assessments at 0.1 percent, Town of Hempstead due dates, grieving with ARC, and STAR for the buyer.",
    h1="How Nassau County property taxes and grievances affect your sale",
    answer="Nassau County property taxes shape what buyers will pay, because they add to the monthly cost of every home. Owners can grieve their assessment with the county's Assessment Review Commission, and the next filing window runs January 4 to March 1, 2027, online through AROW. Tax bills are adjusted between seller and buyer at closing.",
    about="Nassau County property tax assessments and grievances",
    sections=[
        ("How does Nassau County assess a home?",
         "<p>Nassau County records show a level of assessment of 0.1 percent of market value, so an assessed value is the county's estimate of market value divided by 1,000. "
         "For Class 1 residential property, the county's records note that assessed value cannot rise more than 6 percent a year or 20 percent over five years, apart from new "
         "construction and renovations. The county's market value is a tax estimate, not a sale price.</p>"),
        ("When are property taxes due in the Town of Hempstead?",
         "<p>All six South Shore towns in these guides are in the Town of Hempstead, whose Receiver of Taxes collects school and general taxes.</p>"
         '<div class="tablewrap"><table><thead><tr><th>Tax</th><th>Due</th><th>Last day without penalty</th></tr></thead><tbody>'
         "<tr><td>General tax, first half</td><td>January 1</td><td>February 10</td></tr>"
         "<tr><td>School tax, second half</td><td>April 1</td><td>May 10</td></tr>"
         "<tr><td>General tax, second half</td><td>July 1</td><td>August 10</td></tr>"
         "<tr><td>School tax, first half</td><td>October 1</td><td>November 10</td></tr>"
         "</tbody></table></div>"
         "<p>Incorporated villages bill their own village taxes separately.</p>"),
        ("How do you grieve a Nassau County assessment?",
         "<p>File with the Assessment Review Commission after the Department of Assessment sets its tentative roll. For the next roll, the window runs from January 4, 2027, to "
         "March 1, 2027, and you can file online through AROW, Assessment Review On the Web. Someone filing for a relative or friend uses form AR10A, and a registered "
         "representative uses form AR10B. Questions go to ARC at (516) 571-3214.</p>"),
        ("Why do taxes matter to your sale price?",
         "<p>Buyers budget by monthly cost, and taxes are part of it, along with the mortgage and insurance. Two similar homes in different school districts or in and out of a "
         "village can carry different tax bills, and buyers notice. Have your current bills ready when you list, and know whether a grievance is pending.</p>"
         f"<p>Compare village and hamlet taxes in the <a href=\"{GUIDE}/compare/\">South Shore town comparison</a>.</p>"),
        ("What happens to exemptions when the home sells?",
         "<p>Your STAR benefit does not move with you. The New York State tax department tells new owners to register for the STAR credit once the home becomes their primary "
         "residence, and that in the first year they may receive the prior owner's exemption instead. Most other exemptions are offered by the local taxing jurisdiction.</p>"),
    ],
    steps=("How to grieve a Nassau County property assessment", [
        ("Look up your assessment", "Find your property's market value and assessed value in Nassau County's LandRecord Lookup."),
        ("Compare it with sales", "Compare the county's market value with recent closed sales of similar homes nearby."),
        ("Watch for the tentative roll", "The Department of Assessment sets the next tentative roll on January 4, 2027."),
        ("File with ARC by March 1", "File online through AROW between January 4 and March 1, 2027, or use a representative."),
        ("Keep the decision", "Keep the result with your tax bills to show buyers when you sell."),
    ]),
    faqs=[
        ("When can I grieve my Nassau County property taxes?",
         "The Assessment Review Commission accepts appeals after the tentative roll is set. For the next roll, the window runs January 4, 2027, to March 1, 2027, online through AROW."),
        ("When are school taxes due in the Town of Hempstead?",
         "In two halves: the first half is due October 1 and can be paid without penalty through November 10, and the second half is due April 1, payable without penalty through May 10."),
        ("Do property taxes get split at closing on Long Island?",
         "Yes. Taxes the seller has prepaid or still owes are adjusted between seller and buyer at closing, based on the period each one owns the home."),
    ],
    sources=["arc", "lrv", "hempstead_tax", "dtf_newbuyers"],
    related=["/sellers/cost-to-sell/", "/sellers/pricing/", "/sellers/best-time-to-sell/"],
)
