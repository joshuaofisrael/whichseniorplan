"""State pages with enough official, state-specific fact to leave the thin-page list.
Checked 20 Nov 2026. Facts are paraphrased from the cited state page. No plan names or prices.
"""

EXTRAS = {}

def add(slug, **kw):
    EXTRAS[slug] = kw

READS = [
    ("/guides/medigap-open-enrollment/", "When Medigap open enrollment starts", "/assets/images/calculator-tax-forms-thumb.png", "Calculator, pen and paperwork on a kitchen table"),
    ("/guides/medigap-plan-letters/", "What Medigap letters A through N cover", "/assets/images/retirement-tea-papers-thumb.png", "Older hands resting on a mug beside printed charts and papers on a wooden table"),
    ("/guides/medicare-costs-2027/", "2027 Medicare premiums from CMS", "/assets/images/retirement-tea-papers-thumb.png", "Older hands resting on a mug beside printed charts and papers on a wooden table"),
    ("/guides/ship-counseling/", "How free SHIP counseling works", "/assets/images/household-finances-paperwork-thumb.png", "Hands reviewing financial paperwork with a pen and coffee mug"),
]

add(
    "florida",
    title="Florida SHIP: Call SHINE at 1-800-963-5337",
    h1="Medicare help in Florida: SHINE and Medigap rules",
    desc="Florida SHINE is 1-800-963-5337. Issue age Medigap rates, a 30 day free look, and the state Medicaid office.",
    checked="20 Nov 2026",
    modified="2026-11-20",
    compare_html="""<aside class="compare" aria-label="Check another state"><p><strong>Check another state rule.</strong> [[/states/california/|California]] reopens Medigap around a birthday. [[/states/new-york/|New York]] takes applications all year. [[/states/texas/|Texas]] uses one 6 month window and still allows attained age rates. The federal clock is on [[/guides/medigap-open-enrollment/|Medigap open enrollment]].</p></aside>""",
    html="""
<h2>The Florida rule that changes the price later</h2>
<p>Florida prices Medicare Supplement policies on issue age. The Florida Department of Financial Services says every Florida Medicare Supplement policy must be sold that way. The premium does not go up because the buyer gets older. A person who buys at 65 keeps the 65 year old rate for that policy. The rate can still change for inflation, for the whole class of claims, or because Medicare's own benefits change. It cannot be raised for one person because that person filed claims or got sicker. The Office of Insurance Regulation has to approve a class rate change before it takes effect, and the company must mail at least 45 days' notice.</p>
<p>Switching companies resets the age. DFS uses this example: someone who bought at 65 and later moves to a new insurer is rated at the age on the new application, not at 65. That is the opposite of a state that lets a company use attained age and raise the premium on each birthday. [[/states/texas/|Texas]] still allows attained age policies. Florida does not.</p>
<h2>When Florida makes a company sell a policy</h2>
<p>Section 627.6741, as DFS summarizes it, requires an open enrollment period. The company has to accept the application and may not set the price from medical history, health status, or claims. For someone 65 or older, the window starts on the first day of the month the person turns 65 and is enrolled in Part B. If the birthday is the first day of a month, both Part B and this Medigap window start on the first day of the previous month.</p>
<p>Someone who delays Part B gets 6 months from the Part B effective date. DFS also describes a 2 month period after employer group health coverage ends, with the same right to be issued a policy. People under 65 have had their own window since 1 Oct 2009, including people with end stage renal disease. Once Part A and Part B are both in force, they have 6 months. Every company that sells Medicare Supplement policies in Florida must offer them to people under 65. Rates for disability and ESRD are higher than the age 65 rate. Those buyers get another open enrollment when they turn 65, and DFS says they have to apply for a new policy to receive the lower rate.</p>
<p>A company may not exclude a pre existing condition for more than 6 months. DFS defines that as a condition for which a physician gave or recommended treatment in the 6 months before the policy starts. If the new policy replaces another Medicare Supplement or other creditable coverage, the second policy must give credit for time already served. The federal letter chart is still the one on [[/guides/medigap-plan-letters/|the letters page]]. This site does not list the companies or the premiums. DFS keeps a rate search on its own site for that.</p>
<h2>Free look, grace period, and what SHINE will not do</h2>
<p>Section 627.674 gives a 30 day free look on Medicare Supplement policies. The clock starts the day the policy is delivered. The buyer can return it for a full refund of premiums. DFS says the free look does not apply to Medicare Advantage plans. A Medicare Select policy uses a network and usually costs less. Outside the network, except for emergency care, the Select policy can deny or pay less, while Medicare still pays its share of approved charges.</p>
<p>Grace periods are short and depend on how you pay. DFS cites section 627.608: at least 7 days if the premium is weekly, at least 10 days if it is monthly, and at least 31 days for quarterly, semiannual, or annual premiums. If a buyer cancels before the term ends, the company may refund on a short rate basis, which DFS describes as a 10 percent charge for cancelling early. Florida law, on that page, does not set a deadline for mailing the refund.</p>
<p>SHINE, Serving Health Insurance Needs of Elders, is the counseling program. The number on the shiphelp.org listing and on the DFS page is 1-800-963-5337. Counselors do not sell policies. For help paying premiums, DFS points people toward Medicaid and the Medicare Savings Programs rather than assuming everyone needs a supplement. Dollar limits for those programs are the federal 2026 table on our [[/guides/medicare-savings-programs/|savings program guide]], and the state can be more generous. Apply with the Agency for Health Care Administration, not through this site.</p>
""",
    faqs=[
        ("Do Florida Medigap premiums rise on every birthday?", "Not for the policy you already have. The Department of Financial Services says Florida Medicare Supplement policies are sold on an issue age basis, so the rate is tied to the age at purchase. A class rate change can still be approved, and a new company can rate you at the age when you apply there."),
        ("Can someone under 65 buy Medigap in Florida?", "Yes. DFS says that since 1 Oct 2009, people who get Part A and Part B because of disability, including end stage renal disease, have 6 months to buy, and every company that sells these policies in Florida must offer them. The premium is higher until a new open enrollment at age 65."),
    ],
    sources=[
        ("Medicare Supplement Insurance Overview, Florida Department of Financial Services", "https://www.myfloridacfo.com/division/consumers/understanding-insurance/medicare-supplement-insurance-overview"),
        ("Compare Medigap plan benefits", "https://www.medicare.gov/health-drug-plans/medigap/basics/compare-plan-benefits"),
    ],
    next_reads=READS,
)

add(
    "california",
    title="California HICAP Line Is 1-800-434-0222",
    h1="Medicare help in California: HICAP and the birthday rule",
    desc="California HICAP is 1-800-434-0222. Medigap birthday window is 60 days under Insurance Code section 10192.11.",
    checked="20 Nov 2026",
    modified="2026-11-20",
    compare_html="""<aside class="compare" aria-label="Check another state"><p><strong>The birthday rule is not national.</strong> [[/states/florida/|Florida]] uses issue age pricing and a one time window. [[/states/new-york/|New York]] accepts Medigap applications all year. [[/states/texas/|Texas]] gives six months from the Part B start date. Federal timing is on [[/guides/medigap-open-enrollment/|Medigap open enrollment]].</p></aside>""",
    html="""
<h2>What HICAP will sit down and do</h2>
<p>California's counseling program is HICAP, the Health Insurance Counseling and Advocacy Program, inside the California Department of Aging. The department's page says the counseling is free and confidential, and that it is one to one. It covers Medicare questions, long term care insurance, and planning for long term care. It also says HICAP can help with an appeal or a denial, and can provide legal assistance or a legal referral on Medicare or long term care insurance problems. That is the state program talking about its own service. Which Senior Plan does not tell you which contract to buy.</p>
<p>The same page limits who the counseling is for: people 65 or older who are eligible for Medicare, people under 65 with a disability who are eligible for Medicare, and people who will be eligible soon. The phone printed on shiphelp.org, and repeated by the Department of Aging, is 1-800-434-0222. You can also pick a county office from the department's site. HICAP is not an insurance company, and a counselor is not a plan salesperson.</p>
<h2>Two different Medigap clocks</h2>
<p>Insurance Code section 10192.11 sets both. The first is the familiar 6 month window. It begins on the first day of the first month in which the person is both 65 or older and enrolled in Part B. During that window an issuer may not deny a policy, condition it, or charge more because of health status, claims experience, medical care, or a medical condition. Every Medicare supplement policy the company currently sells has to be available to those applicants.</p>
<p>The second clock is the birthday rule, in subdivision (h). A person who already has Medicare supplement coverage gets an annual open enrollment of 60 days or more, starting on the birthday. In that window the person may buy a policy with benefits equal to or less than the policy they already have. The issuer may not deny the policy or price it from health, claims, or medical condition, as long as the person is covered by another Medicare supplement policy when the window opens. The company has to send notice at least 30 days, and no more than 60 days, before the window, and it has to put the notice on any letter about a benefit change or a premium change.</p>
<p>Read that limit twice. The birthday window is not a pass to move from a lean letter to a richer one without health questions. Equal or lesser benefits is the statute's line. It is also not the fall [[/guides/open-enrollment/|October 15 to December 7]] period, which changes Advantage and drug plans and does not reopen Medigap underwriting. The letter benefits themselves are the federal chart on [[/guides/medigap-plan-letters/|the letters page]]. Premiums are not printed here. Ask HICAP or the plan, and compare the current contracts on Medicare.gov.</p>
""",
    faqs=[
        ("What does the California birthday rule allow?", "Insurance Code section 10192.11 gives someone who already has a Medicare supplement policy 60 days or more, starting on the birthday, to buy another policy with equal or lesser benefits. The issuer cannot use health to deny that policy or set the price."),
        ("Is the birthday rule the same as October open enrollment?", "No. Fall open enrollment changes Medicare Advantage and Part D plans. The birthday rule is a state Medigap window, and only for a policy that is not richer than the one you already have."),
    ],
    sources=[
        ("California Insurance Code section 10192.11", "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=INS&sectionNum=10192.11"),
        ("Medicare Counseling (HICAP), California Department of Aging", "https://www.aging.ca.gov/Programs_and_Services/Medicare_Counseling/"),
    ],
    next_reads=READS,
)

add(
    "new-york",
    title="New York Medigap Stays Open All Year",
    h1="Medicare help in New York: year round Medigap",
    desc="New York insurers must take Medigap applications all year. HIICAP is 1-800-701-0501. No Medicare Select plans.",
    checked="20 Nov 2026",
    modified="2026-11-20",
    compare_html="""<aside class="compare" aria-label="Check another state"><p><strong>Most states close the window.</strong> [[/states/texas/|Texas]] gives six months from the Part B start. [[/states/california/|California]] adds a birthday window for an equal or lesser policy. [[/states/florida/|Florida]] locks the rate to the age at purchase. The federal one time window is on [[/guides/medigap-open-enrollment/|Medigap open enrollment]].</p></aside>""",
    html="""
<h2>Applications do not stop after six months</h2>
<p>The New York Department of Financial Services says state law and regulation require any insurer that writes Medigap to accept a Medicare enrollee's application at any time of year. The insurer may not deny the policy, and may not set the premium apart, because of health status, claims experience, medical condition, or because the person is in treatment. A policy sold to a group is different: only members of that group can buy it.</p>
<p>DFS says this open enrollment and the portability rules cover people who have Medicare because of age or because of disability, and people with end stage renal disease. That is wider than the federal 6 month window, which is tied to age 65 and the start of Part B. New York did not copy that calendar. HIICAP, the counseling program, is still the right place to walk through a specific policy. The number on the shiphelp.org listing is 1-800-701-0501. This page does not rank letters or companies.</p>
<h2>One rate for the policy form</h2>
<p>Insurance Law section 4317 community rates Medicare supplemental coverage. For that coverage, the premium for everyone on a given policy form is the same, based on the experience of the pool covered by that form, without regard to age, sex, health status, tobacco use, or occupation. The superintendent can allow separate community rates for geographic regions, down to a single county, if the region is approved in the rate filing. DFS publishes a carrier list and premium comparison tables, including a premium table it marked updated 1 Oct 2026. We are not copying those dollars. They change, and a copied price would be a plan quote.</p>
<p>Companies do not have to sell every letter. DFS says that for policies sold on or after 1 Jan 2020, an insurer offers plans A and B and either D or G. Not every company offers the rest. Plans C and F remain closed to people who became eligible on or after 1 Jan 2020, which is the federal rule on our [[/guides/medigap-plan-letters/|letters page]]. People who already had C or F can keep renewing them.</p>
<h2>Waiting periods, and a product that is not for sale</h2>
<p>A Medigap policy may wait up to 6 months before it covers a pre existing condition. DFS defines that as a condition for which a physician gave or recommended treatment in the 6 months before the effective date. The insurer has to shorten the wait by days the person already had creditable coverage, if any break was not more than 63 days. Creditable coverage on the DFS list includes a group health plan, Medicaid, TRICARE, the Federal Employees Health Benefits Program, and a prior Medicare supplement, Medicare Select, or Medicare Advantage plan. Credit for time on Medicare itself is required only if the application arrives before or during the 6 month period that starts when the person is both 65 or older and enrolled in Part B.</p>
<p>Medicare Select, the network version of Medigap, is a blank row in New York right now. DFS says no insurer is currently offering Medicare Select in the state. If that changes, the DFS page is the place to check, not a recycled sentence on this site. Advantage plans are federal. DFS tells New Yorkers to use Medicare.gov for those contracts, which is the same instruction on our [[/guides/how-to-compare-plans/|comparison guide]].</p>
""",
    faqs=[
        ("Can I apply for Medigap in New York after the six month federal window?", "Yes. The Department of Financial Services says an insurer that sells Medigap must accept a Medicare enrollee's application throughout the year, and may not deny it or price it from health status. Group policies are limited to members of the group."),
        ("Is Medicare Select sold in New York?", "Not at the moment. The Department of Financial Services page, read 20 Nov 2026, says no insurer is currently offering Medicare Select in New York State."),
    ],
    sources=[
        ("Protections for Medicare Beneficiaries Residing in New York, Department of Financial Services", "https://www.dfs.ny.gov/consumers/health_insurance/information_for_medicare_beneficiaries"),
        ("New York Insurance Law section 4317", "https://www.nysenate.gov/legislation/laws/ISC/4317"),
    ],
    next_reads=READS,
)

add(
    "texas",
    title="Texas Medigap Window Is 6 Months Once",
    h1="Medicare help in Texas: one Medigap window, two under 65 rules",
    desc="Texas gives one 6 month Medigap window when Part B starts. Under 65 disability rights differ from ESRD and ALS.",
    checked="20 Nov 2026",
    modified="2026-11-20",
    compare_html="""<aside class="compare" aria-label="Check another state"><p><strong>Texas is not Florida or New York.</strong> [[/states/florida/|Florida]] bans attained age rate hikes. [[/states/new-york/|New York]] takes Medigap applications all year. [[/states/california/|California]] adds a birthday window for an equal or lesser policy. Federal rules are on [[/guides/medigap-open-enrollment/|Medigap open enrollment]].</p></aside>""",
    html="""
<h2>One window, and it starts with Part B</h2>
<p>The Texas Department of Insurance tells buyers they get one Medicare supplement open enrollment, and it lasts six months. It begins when the person enrolls in Part B. It is not the fall market, which TDI separately describes as October 15 to December 7 for drug plans and Advantage plans. During the six months, a company must sell a policy even if the person has health problems. The buyer needs both Part A and Part B. TDI also says the buyer can use that right more than once before the six months end: cancel a policy bought in the window and buy a different Medicare supplement policy.</p>
<p>Outside that window, health can matter. TDI says that if you wait until the window is over, or the policy lapses, a company might refuse to sell another policy when there is a pre existing condition. A pre existing condition, on that page, is one for which a doctor gave treatment or recommended treatment in the previous six months. During the open enrollment itself, a company may still wait up to six months before it covers those conditions, unless the person has Medicare because of end stage renal disease or ALS.</p>
<h2>Under 65, Texas splits the market</h2>
<p>People under 65 who have Medicare because of a disability also get six months from the day they enroll in Part B, but TDI says that right applies only to Plan A. They get a full open enrollment again during the first six months after they turn 65.</p>
<p>End stage renal disease and ALS are treated more like age 65. TDI says someone under 65 with ESRD or ALS can buy any available plan during open enrollment, pays the age 65 rate for plans A, B, and D, and can be charged up to twice the age 65 rate for the other plans. This site is not going to guess which of those prices is current. The TDI guide is the source, and HICAP, the Texas counseling program at 1-800-252-9240, can read a live quote with you.</p>
<h2>63 days, a free look, and a Medicaid pause</h2>
<p>Losing certain other coverage can create a guaranteed issue right outside the six months. TDI's lists depend on when Medicare eligibility started. Before 1 Jan 2020, the letters include C and F. On or after that date, they include D and G instead, along with A, B, K, and L, including high deductible F or G in the matching era. Someone under 65 with a disability other than ESRD or ALS can buy Plan A on that right. People who lose Medicaid because their finances changed have a guaranteed issue right as well. The clock is 63 days from the day coverage ends or from the date of the notice that it will end, whichever is later. On these policies the company may not add a pre existing waiting period. The person has to show proof that coverage ended.</p>
<p>TDI's free look is 30 days from the day the policy is received, for a full refund. It does not apply to Medicare Advantage. Dropping a supplement to join an Advantage plan can mean the supplement is gone. Policies are renewable: the company cannot cancel or refuse to renew except for an intentional false statement on the application or for unpaid premium. The company may raise the premium once a year. If the policy is attained age, TDI says the premium can also rise on the birthday. An issue age policy is priced from the age at purchase. Texas still allows both. [[/states/florida/|Florida]] does not.</p>
<p>If the buyer later gets Medicaid, TDI says the supplement's benefits and premiums can be suspended for up to two years. The company has to be told within 90 days of Medicaid eligibility. Lose Medicaid inside those two years and the policy is reinstated, if the person contacts the company within 90 days of losing Medicaid. After two years, reinstating means applying again. None of this is a recommendation to suspend, drop, or buy. It is the state page's description of the right.</p>
""",
    faqs=[
        ("When does Medigap open enrollment start in Texas?", "The Texas Department of Insurance says the one time six month window begins when you enroll in Part B. It is not the October 15 to December 7 period used for Advantage and drug plans."),
        ("What can someone under 65 buy in Texas?", "TDI says a disability that is not ESRD or ALS opens six months to buy Plan A. ESRD and ALS can buy any available plan, at the age 65 rate for A, B, and D, and at up to twice that rate for other plans. A full window opens again for the first six months after age 65."),
    ],
    sources=[
        ("Medicare supplement insurance guide, Texas Department of Insurance", "https://www.tdi.texas.gov/pubs/consumer/medsup.html"),
        ("Compare Medigap plan benefits", "https://www.medicare.gov/health-drug-plans/medigap/basics/compare-plan-benefits"),
    ],
    next_reads=READS,
)
