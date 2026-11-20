"""National explainers. Internal links are [[/path/|label]]. Facts are from pages checked 16 Nov 2026."""

GUIDES = []

def add(**kw):
    GUIDES.append(kw)

add(
path="/guides/original-medicare-vs-medicare-advantage/",
title="Which Medicare Path Should I Pick?",
h1="Original Medicare or Medicare Advantage",
desc="How Original Medicare and Medicare Advantage differ on doctors, drugs, and out of pocket limits. Not a plan recommendation.",
body="""
<div class="answer"><p><strong>Short version:</strong> Original Medicare is Part A and Part B from the federal program. Medicare Advantage is a private plan that provides those benefits. You use one path at a time. This page describes the difference. It does not tell you which path to take.</p></div>
<p>Medicare.gov describes two main ways to get coverage. With Original Medicare you can use any doctor or hospital that takes Medicare. You can join a separate drug plan for Part D. You can also buy a Medigap policy to help pay your share of the costs. There is no yearly limit on what you pay out of pocket under Original Medicare unless you have other coverage, such as Medigap, or you join a Medicare Advantage plan.</p>
<p>Medicare Advantage, also called Part C, is the other path. You still have Medicare, and you must keep paying the Part B premium. The private plan provides the Part A and Part B benefits, and most plans include drug coverage. You may have to use doctors in the plan network and get approval before some services or drugs. The plan sets its own copays and has a yearly limit on out of pocket costs. After you reach that limit, the plan pays the full cost of covered health services for the rest of the year. Many plans offer extra benefits Original Medicare does not cover, such as some vision, hearing, or dental care. Those extras are not the same in every plan.</p>
<p>Medigap works with Original Medicare. Medicare.gov says you can buy a Medigap policy only if you have Original Medicare. This site does not list private plan names or prices. Use the plan comparison tool on Medicare.gov, or a SHIP counselor, for plans sold where you live.</p>
<h2>A simple way to sort the choice</h2>
<ul>
<li><strong>Doctors:</strong> Original Medicare works with any provider that takes Medicare. An Advantage plan may use a network.</li>
<li><strong>Drugs:</strong> Original Medicare needs a separate Part D plan if you want drug coverage. Most Advantage plans include drugs.</li>
<li><strong>Your share of the bill:</strong> Original Medicare charges the Part B deductible and usually 20 percent coinsurance, with no yearly cap unless you add coverage. Advantage plans set copays and have a yearly out of pocket limit.</li>
<li><strong>Extras:</strong> Routine dental, vision, and hearing are generally outside Original Medicare. Some Advantage plans add them. Read that plan.</li>
</ul>
<p>When you can join or leave a plan is covered under [[/guides/enrollment-periods/|enrollment periods]]. Nationwide 2026 dollar amounts are on the [[/guides/medicare-costs-2026/|2026 costs]] page.</p>
""",
faqs=[
("Can I have Original Medicare and Medicare Advantage at the same time?", "No. Medicare.gov describes them as the two main ways to get Medicare coverage. You use one or the other. You can switch only during enrollment periods Medicare publishes."),
("Does Medicare Advantage replace Part A and Part B?", "The plan provides your Part A and Part B benefits, but you stay in Medicare and you must keep paying the Part B premium."),
("Does this site recommend one path?", "No. We explain the rules Medicare publishes. A SHIP counselor can help you compare plans where you live. We do not sell plans."),
],
sources=[
("Parts of Medicare", "https://www.medicare.gov/basics/get-started-with-medicare/medicare-basics/parts-of-medicare"),
("What does Medicare cost?", "https://www.medicare.gov/basics/get-started-with-medicare/medicare-basics/what-does-medicare-cost"),
("Medigap basics", "https://www.medicare.gov/health-drug-plans/medigap/basics"),
],
related=[("/guides/original-medicare/", "Original Medicare"), ("/guides/medicare-advantage/", "Medicare Advantage"), ("/guides/medigap-plan-letters/", "Medigap letters"), ("/states/", "Your state")],
)

add(
path="/guides/original-medicare/",
title="What Original Medicare Covers | Which Senior Plan",
h1="What Original Medicare is",
desc="Original Medicare is Part A and Part B. What they help pay, what you still owe in 2026, and how drugs and Medigap fit.",
body="""
<div class="answer"><p><strong>Short version:</strong> Original Medicare is Part A (hospital insurance) and Part B (medical insurance). It is the federal coverage itself, not a private plan. Drug coverage is a separate Part D plan. Medigap is optional extra insurance that helps pay your share.</p></div>
<p>Part A helps cover inpatient hospital care, skilled nursing facility care, hospice, and some home health care. Part B helps cover services from doctors and other providers, outpatient care, home health care, durable medical equipment, and many preventive services such as screenings, vaccines, and yearly wellness visits.</p>
<p>For 2026, Medicare.gov lists these standard Original Medicare costs. Most people pay no Part A premium because they paid Medicare taxes long enough, generally at least 10 years. If you have to buy Part A, the 2026 premium is $311 or $565 a month, depending on how long you or your spouse worked. The Part A hospital deductible is $1,736 for each benefit period. Days 1 through 60 in the hospital are $0 after that deductible. Days 61 through 90 are $434 a day. Lifetime reserve days are $868 a day. The standard Part B premium is $202.90 a month, the Part B deductible is $283 a year, and you usually pay 20 percent of the Medicare approved amount after the deductible. People with higher incomes pay more. Details and the income table are on the [[/guides/medicare-costs-2026/|2026 costs]] page.</p>
<p>Original Medicare does not, by itself, pay for most outpatient prescriptions. You join a separate [[/guides/part-d/|Part D drug plan]] for that, or you get drug coverage through a Medicare Advantage plan instead of staying with Original Medicare. A [[/guides/medigap-plan-letters/|Medigap policy]] can help pay deductibles and coinsurance, but only if you have Original Medicare.</p>
<h2>Who gets it automatically</h2>
<p>Medicare.gov says some people get Part A and Part B without a separate signup because they already get benefits from Social Security or the Railroad Retirement Board. That includes people who start those benefits at least 4 months before they turn 65, people who have received disability benefits for 24 months, and people with ALS when disability benefits start. If you live in Puerto Rico or outside the United States, Medicare.gov says you get Part A automatically and must sign up if you want Part B. Everyone else contacts Social Security to sign up. See [[/guides/initial-enrollment-period/|the first enrollment period]].</p>
""",
faqs=[
("Is Original Medicare a private insurance plan?", "No. Part A and Part B are the federal coverage. Private companies sell Part D drug plans and Medigap policies that work with it, and private companies sell Medicare Advantage plans as the other way to get Medicare."),
("Does Original Medicare include prescriptions?", "Not for most drugs you pick up at a pharmacy. You join a separate Medicare drug plan, or you choose a Medicare Advantage plan that includes drugs."),
("Is there a yearly cap on what I pay?", "Medicare.gov says there is no yearly limit on what you pay out of pocket under Original Medicare unless you have other coverage, such as a Medigap policy, or you join a Medicare Advantage plan."),
],
sources=[
("Parts of Medicare", "https://www.medicare.gov/basics/get-started-with-medicare/medicare-basics/parts-of-medicare"),
("What does Medicare cost?", "https://www.medicare.gov/basics/get-started-with-medicare/medicare-basics/what-does-medicare-cost"),
("How do I sign up for Medicare?", "https://www.medicare.gov/basics/get-started-with-medicare/sign-up/how-do-i-sign-up-for-medicare"),
("2026 premiums and deductibles", "https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-deductibles"),
],
related=[("/guides/original-medicare-vs-medicare-advantage/", "Compare the two paths"), ("/guides/what-medicare-covers/", "What it covers"), ("/guides/medicare-costs-2026/", "2026 costs"), ("/guides/medicare-costs-2027/", "2027 costs")],
)

add(
path="/guides/medicare-advantage/",
title="What Medicare Advantage Is | Which Senior Plan",
h1="What Medicare Advantage is",
desc="Medicare Advantage is a private plan that delivers Part A and Part B, often with drugs. Networks, premiums, and the yearly cap.",
modified="2026-11-18",
checked="18 Nov 2026",
body="""
<div class="answer"><p><strong>Short version:</strong> Medicare Advantage is private health coverage that Medicare has approved. It provides your Part A and Part B benefits. Most plans include drug coverage. You must keep paying the Part B premium. Plan premiums, networks, and copays are not set on this site.</p></div>
<p>Medicare.gov calls these plans Part C. They are an alternative to Original Medicare for health and drug needs. The plan may require you to use doctors in its network and to get approval before some services or drugs. Out of pocket costs usually differ from Original Medicare. Plans have a yearly limit on what you pay for covered health services. After you hit that limit, the plan pays 100 percent of those covered services for the rest of the year. Some plans also lower the Part B premium a member pays, a feature Medicare.gov calls a Part B premium reduction and that ads sometimes call a [[/guides/medicare-give-back-benefit/|give back benefit]]; it is part of the plan, not a separate check.</p>
<p>Most plans offer extra benefits that Original Medicare does not cover, such as some vision, hearing, and dental care. Extras, premiums, and rules differ by plan and by county. We do not publish company names, star ratings, or premiums, because those change and we will not invent them. Compare plans on Medicare.gov or with a [[/guides/ship-counseling/|SHIP counselor]].</p>
<p>You generally need both Part A and Part B to join a Medicare Advantage plan. You can join during your [[/guides/initial-enrollment-period/|Initial Enrollment Period]], the [[/guides/open-enrollment/|fall open enrollment]] from October 15 through December 7, or a special enrollment period if you qualify. If you are already in a Medicare Advantage plan, you also have the [[/guides/medicare-advantage-open-enrollment/|Medicare Advantage open enrollment period]] from January 1 through March 31.</p>
<p>A Medigap policy is for Original Medicare. Medicare.gov says you can buy Medigap only if you have Original Medicare. Do not assume a Medigap letter works inside an Advantage plan.</p>
""",
faqs=[
("Do I still pay Part B if I join Medicare Advantage?", "Yes. Medicare.gov says you must keep paying your Part B premium to stay in the plan. The plan may also charge its own premium."),
("Will every Advantage plan cover dental?", "No. Medicare.gov says most plans offer extra benefits such as some vision, hearing, and dental care. You have to read the plan you are considering."),
("Where do I see plans in my state?", "On the Medicare Plan Finder at Medicare.gov, or through your state SHIP program. This site does not list plan names."),
],
sources=[
("Parts of Medicare", "https://www.medicare.gov/basics/get-started-with-medicare/medicare-basics/parts-of-medicare"),
("Joining a plan", "https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/joining-a-plan"),
("What does Medicare cost?", "https://www.medicare.gov/basics/get-started-with-medicare/medicare-basics/what-does-medicare-cost"),
],
related=[("/guides/original-medicare-vs-medicare-advantage/", "Compare the two paths"), ("/guides/how-to-compare-plans/", "How to compare"), ("/states/", "Your state")],
)

add(
path="/guides/medigap-plan-letters/",
title="Which Medigap Letter Should I Compare?",
h1="Medigap plan letters",
desc="What Medigap letters A through N cover in 2026, who can buy Plan C or F, and why Massachusetts, Minnesota, and Wisconsin differ.",
body="""
<div class="answer"><p><strong>Short version:</strong> In most states a Medigap letter means a fixed set of benefits. Plan G from one company has the same basic benefits as Plan G from another. The price is what changes. We do not list prices or company names.</p></div>
<p>Medicare.gov says you generally must have Part A and Part B to buy Medigap. Policies help pay your share of Original Medicare costs, such as copays, coinsurance, and deductibles. There are 10 standardized letters in most states: A, B, C, D, F, G, K, L, M, and N. Yes in the table means the plan covers that benefit. No means it does not.</p>
<div class="tablewrap"><table class="list"><thead><tr><th scope="col">Benefit</th><th>A</th><th>B</th><th>C</th><th>D</th><th>F</th><th>G</th><th>K</th><th>L</th><th>M</th><th>N</th></tr></thead><tbody>
<tr><th scope="row">Part A coinsurance and 365 extra hospital days</th><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
<tr><th scope="row">Part B coinsurance or copay</th><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>50%</td><td>75%</td><td>Yes</td><td>Yes, with copays</td></tr>
<tr><th scope="row">First 3 pints of blood</th><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>50%</td><td>75%</td><td>Yes</td><td>Yes</td></tr>
<tr><th scope="row">Part A hospice coinsurance or copay</th><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>50%</td><td>75%</td><td>Yes</td><td>Yes</td></tr>
<tr><th scope="row">Skilled nursing facility coinsurance</th><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>50%</td><td>75%</td><td>Yes</td><td>Yes</td></tr>
<tr><th scope="row">Part A deductible</th><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>50%</td><td>75%</td><td>50%</td><td>Yes</td></tr>
<tr><th scope="row">Part B deductible</th><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>No</td><td>No</td><td>No</td></tr>
<tr><th scope="row">Part B excess charges</th><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>No</td><td>No</td></tr>
<tr><th scope="row">Foreign travel emergency, up to plan limits</th><td>No</td><td>No</td><td>80%</td><td>80%</td><td>80%</td><td>80%</td><td>No</td><td>No</td><td>80%</td><td>80%</td></tr>
<tr><th scope="row">Out of pocket limit in 2026</th><td>None</td><td>None</td><td>None</td><td>None</td><td>None</td><td>None</td><td>$8,000</td><td>$4,000</td><td>None</td><td>None</td></tr>
</tbody></table></div>
<p>Plan N pays the Part B coinsurance, but you pay up to $20 for some office visits and up to $50 for an emergency room visit that does not lead to an inpatient admission. Plans F and G also offer a high deductible version in some states. In 2026 you pay Medicare covered costs up to $2,950 before that policy pays. For Plans K and L, after you meet the yearly out of pocket limit and the 2026 Part B deductible of $283, the plan pays covered services in full for the rest of the calendar year.</p>
<h2>Plans C and F</h2>
<p>If you were eligible for Medicare before January 1, 2020, you may still be able to buy Plan C or Plan F. If you became eligible on or after that date, you cannot buy Plan C or Plan F. Medicare.gov says Plans D and G give the same benefits as C and F except the Part B deductible, which only C and F cover.</p>
<h2>Three states use different designs</h2>
<p>Massachusetts uses a Core Plan, a Supplement 1 Plan, and a Supplement 1A Plan. Supplement 1 includes the Part B deductible and is no longer sold to people who became eligible on or after January 1, 2020. Minnesota uses a Basic Plan and an Extended Basic Plan, and it also has its own versions of some letters. Wisconsin has one base plan, optional riders, cost sharing plans similar to K and L, and a high deductible option. See the [[/states/massachusetts/|Massachusetts]], [[/states/minnesota/|Minnesota]], and [[/states/wisconsin/|Wisconsin]] pages.</p>
<p>When you can buy a letter without medical questions is the [[/guides/medigap-open-enrollment/|Medigap open enrollment]] window, which is not the same as the fall Medicare open enrollment.</p>
""",
faqs=[
("Are Medigap Plan G benefits the same at every company?", "Yes, in states that use the standard letters. Medicare.gov says the same letter has the same basic benefits no matter which company sells it. The premium is the difference."),
("Which letter should I buy?", "This site does not answer that. The right letter depends on your health, your budget, and whether you are still in a protected enrollment window. A SHIP counselor or your state insurance department can walk through policies sold where you live."),
("Does Medigap cover prescriptions?", "No. Medigap helps pay Original Medicare cost sharing. Outpatient drugs are Part D, which you buy separately if you stay with Original Medicare."),
],
sources=[
("Compare Medigap plan benefits", "https://www.medicare.gov/health-drug-plans/medigap/basics/compare-plan-benefits"),
("Medigap basics", "https://www.medicare.gov/health-drug-plans/medigap/basics"),
("Medigap in Massachusetts", "https://www.medicare.gov/health-drug-plans/medigap/basics/compare-plan-benefits/massachusetts"),
("Medigap in Minnesota", "https://www.medicare.gov/health-drug-plans/medigap/basics/compare-plan-benefits/minnesota"),
("Medigap in Wisconsin", "https://www.medicare.gov/health-drug-plans/medigap/basics/compare-plan-benefits/wisconsin"),
],
related=[("/guides/medigap-open-enrollment/", "When you can buy"), ("/guides/original-medicare/", "Original Medicare"), ("/states/", "Your state")],
)

add(
path="/guides/part-d/",
title="Medicare Part D Drug Coverage | Which Senior Plan",
h1="Medicare Part D drug coverage",
desc="How 2026 Part D works: a $615 deductible, 25 percent coinsurance, and a $2,100 out of pocket cap. Plan premiums are not listed here.",
modified="2026-11-20",
checked="20 Nov 2026",
body="""
<div class="answer"><p><strong>Short version:</strong> Part D is outpatient drug coverage from a private plan that follows Medicare rules. In 2026 the standard deductible is $615 and the out of pocket cap is $2,100. After that cap you pay nothing for covered drugs. Your actual premium and drug prices depend on the plan.</p></div>
<p>You can get Part D as a standalone drug plan alongside Original Medicare, or as part of a Medicare Advantage plan. Medicare.gov says you need Part A or Part B to join a standalone drug plan, and both Part A and Part B to join a Medicare Advantage plan.</p>
<p>CMS describes the 2026 standard benefit in three phases. You pay the full cost of covered drugs until you meet the $615 deductible. Then you pay 25 percent coinsurance until your out of pocket spending reaches $2,100. In the catastrophic phase you pay no cost sharing for covered Part D drugs. Plans can charge a lower deductible than $615. The deductible on a specific plan is not something we guess.</p>
<!--NEXT_READS-->
<p>The monthly premium is set by the plan, not by a single national price. CMS also announced that the 2026 Part D base beneficiary premium is $38.99. That figure is used to calculate the [[/guides/general-enrollment-and-penalties/|late enrollment penalty]]. It is not the premium printed on every plan. People with higher incomes pay an extra Part D amount on top of the plan premium. The 2026 brackets are on the [[/guides/medicare-costs-2026/|2026 costs page]]. How Social Security sets the year, and the 2027 brackets CMS published on 17 Nov 2026, are on the [[/guides/irmaa-brackets-2027/|2027 IRMAA page]].</p>
<p>If you go 63 days or more without Part D or other creditable drug coverage after your first chance to join, you can owe a penalty for as long as you have drug coverage. [[/guides/extra-help/|Extra Help]] can remove that penalty and lower drug costs if you qualify. People with Medicaid or Extra Help may be able to change drug coverage once a month. Most other people can join or switch only during published enrollment periods.</p>
""",
faqs=[
("Is $38.99 the Part D premium I will pay?", "No. That is the 2026 national base beneficiary premium CMS uses in the penalty formula. The premium you pay is whatever the plan charges, plus any income related amount."),
("What is the most I pay for covered drugs in 2026?", "CMS set the annual out of pocket threshold at $2,100. After you reach it, you pay no cost sharing for covered Part D drugs."),
("Does every plan have a $615 deductible?", "No. $615 is the standard deductible for 2026. A plan can use a lower deductible. Check that plan."),
],
sources=[
("Final CY 2026 Part D redesign program instructions", "https://www.cms.gov/newsroom/fact-sheets/final-cy-2026-part-d-redesign-program-instructions"),
("How much does Medicare drug coverage cost?", "https://www.medicare.gov/health-drug-plans/part-d/basics/costs"),
("CY 2026 Part D base beneficiary premium", "https://www.cms.gov/files/document/july-28-2025-parts-c-d-announcement.pdf"),
("Joining a plan", "https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/joining-a-plan"),
],
related=[("/guides/extra-help/", "Extra Help"), ("/guides/medicare-costs-2027/", "2027 costs"), ("/guides/general-enrollment-and-penalties/", "Late penalties"), ("/guides/irmaa-brackets-2027/", "2027 IRMAA")],
next_reads=[
("/guides/extra-help/", "Extra Help limits and 2027 copays", "/assets/images/calculator-tax-forms-thumb.png", "Calculator, pen and paperwork on a kitchen table"),
("/guides/irmaa-brackets-2027/", "2027 IRMAA brackets for Part B and Part D", "/assets/images/retirement-tea-papers-thumb.png", "Older hands resting on a mug beside printed charts and papers on a wooden table"),
("/guides/general-enrollment-and-penalties/", "How the Part D late penalty is calculated", "/assets/images/piggy-bank-rain-thumb.png", "Pink ceramic piggy bank and coins on a rainy windowsill"),
("/guides/medicare-costs-2027/", "2027 Medicare costs from CMS", "/assets/images/retirement-tea-papers-thumb.png", "Older hands resting on a mug beside printed charts and papers on a wooden table"),
],
)

add(
path="/guides/enrollment-periods/",
title="Which Medicare Enrollment Window Applies?",
h1="Medicare enrollment periods and deadlines",
desc="The 7 month first window, Oct 15 to Dec 7 for plans, Jan 1 to Mar 31, and special cases. Start dates differ.",
modified="2026-11-20",
checked="20 Nov 2026",
image="/assets/images/household-finances-paperwork.png",
image_alt="Hands reviewing financial paperwork with a pen and coffee mug",
image_caption="Thumbnail for the enrollment deadlines guide.",
compare_html='<aside class="compare" aria-label="Check another deadline"><p><strong>Missed Part B?</strong> That is a different clock from plan switching. Read [[/guides/general-enrollment-and-penalties/|how the Part B late penalty is calculated]], or stay here if you are only changing an Advantage or drug plan during [[/guides/open-enrollment/|October 15 to December 7]].</p></aside>',
body="""
<div class="answer"><p><strong>Short version:</strong> Your first signup window is 7 months around your 65th birthday. Each fall, October 15 through December 7, you can change Advantage and drug plans for January 1. January 1 through March 31 is both the general enrollment period for Part A and Part B and a separate window if you are already in Medicare Advantage. Those two January windows do not do the same job.</p></div>
<div class="tablewrap"><table class="list"><thead><tr><th scope="col">Period</th><th scope="col">When</th><th scope="col">What it is for</th></tr></thead><tbody>
<tr><th scope="row">Initial Enrollment Period</th><td>7 months around the month you turn 65</td><td>First signup for Part A and Part B, and for a plan</td></tr>
<tr><th scope="row">Open enrollment</th><td>October 15 through December 7</td><td>Join, drop, or switch Advantage or drug plans. Coverage starts January 1</td></tr>
<tr><th scope="row">Medicare Advantage open enrollment</th><td>January 1 through March 31, or the first 3 months you have Medicare</td><td>Only if you are already in an Advantage plan. Switch plans, or return to Original Medicare and join a drug plan. Coverage starts the first of the next month</td></tr>
<tr><th scope="row">General Enrollment Period</th><td>January 1 through March 31</td><td>Sign up for Part B, and for Part A if you have to buy it, if you missed your first window. Coverage starts the next month</td></tr>
<tr><th scope="row">Special Enrollment Period</th><td>Depends on the event</td><td>Work coverage ending, losing Medicaid, moving, and other listed situations</td></tr>
<tr><th scope="row">Medigap open enrollment</th><td>6 months from the first month you have Part B and are 65 or older</td><td>Buy any Medigap letter without health questions. It does not repeat every year</td></tr>
</tbody></table></div>
<p>These windows are not interchangeable. Missing the fall deadline does not open the Medigap window, and the January Advantage window does not let someone with only Original Medicare join an Advantage plan. Each page below stays inside one set of rules.</p>
<ul>
<li>[[/guides/initial-enrollment-period/|Initial Enrollment Period]]</li>
<li>[[/guides/open-enrollment/|October 15 to December 7]]</li>
<li>[[/guides/medicare-advantage-open-enrollment/|January Advantage window]]</li>
<li>[[/guides/special-enrollment-periods/|Special enrollment periods]]</li>
<li>[[/guides/general-enrollment-and-penalties/|How the Part B late penalty is calculated]]</li>
<li>[[/guides/medigap-open-enrollment/|Medigap open enrollment]]</li>
</ul>
<!--NEXT_READS-->
<h2>Signing up for Part B is not the same as joining a plan</h2>
<p>Medicare.gov's joining a plan page, read 20 Nov 2026, keeps the two steps apart. You need both Part A and Part B to join a Medicare Advantage plan. You need either Part A or Part B to join a standalone drug plan. You also have to live in the plan's service area. If you live in another state for part of the year, Medicare.gov says to check whether that plan will cover you there before you join.</p>
<p>When the plan starts depends on which window you used. During fall open enrollment, coverage starts January 1, and the plan has to have the request by December 7. During Medicare Advantage open enrollment, coverage starts the first day of the month after the plan gets the request. That January window is not only January 1 through March 31. Medicare.gov also lists the first 3 months you have Medicare, and only if you are already in an Advantage plan. Someone who joined an Advantage plan during the Initial Enrollment Period can change to another Advantage plan, or go back to Original Medicare with or without a drug plan, within the first 3 months they have both Part A and Part B.</p>
<p>There is a second Initial Enrollment Period for people who already have Part A and add Part B later. Medicare.gov says it starts 3 months before the month you are first eligible for both, and you have 2 months after you have both for the first time. Plan coverage in that window generally starts the first of the month after the plan gets the request. If you sign up for Part A or Part B during a special enrollment period because of an exceptional situation, the same page gives you 2 months to join a plan. The situations themselves are on the [[/guides/special-enrollment-periods/|special enrollment]] page, not a single calendar date.</p>
<p>The General Enrollment Period is the Part A and Part B door if you missed the first window and you do not have a special period. It runs January 1 through March 31, and coverage starts the month after you sign up. A penalty can follow. The arithmetic is on [[/guides/general-enrollment-and-penalties/|the penalty page]], including the 2027 example Medicare.gov now prints. Medigap is still its own 6 month clock, and several states rewrite it. [[/states/new-york/|New York]] keeps applications open all year. [[/states/california/|California]] adds a birthday window. [[/states/texas/|Texas]] keeps the one time six months and splits the under 65 rules.</p>
""",
faqs=[
("Is October 15 the only time I can change plans?", "No. It is the main yearly window for Advantage and drug plans. Other windows apply when you first join Medicare, when you already have an Advantage plan in the first quarter or in your first 3 months with Medicare, and when you have a special situation."),
("Does the fall window reset my Medigap protections?", "No. Medigap open enrollment is a one time 6 month period in most states. Medicare.gov says it does not repeat every year the way Medicare open enrollment does. New York is one state that keeps Medigap applications open all year."),
("What if I miss a deadline?", "You may have to wait for the next general or open enrollment period, and you may owe a late enrollment penalty. The penalty page shows Medicare.gov's 10 percent rule and the 2026 and 2027 examples."),
],
sources=[
("Joining a plan", "https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/joining-a-plan"),
("When does Medicare coverage start?", "https://www.medicare.gov/basics/get-started-with-medicare/sign-up/when-does-medicare-coverage-start"),
("Get ready to buy Medigap", "https://www.medicare.gov/health-drug-plans/medigap/ready-to-buy"),
],
related=[("/guides/initial-enrollment-period/", "First signup"), ("/guides/open-enrollment/", "Fall window"), ("/guides/general-enrollment-and-penalties/", "Part B penalty math"), ("/states/", "Get local help")],
next_reads=[
("/guides/general-enrollment-and-penalties/", "How the Part B late penalty is calculated", "/assets/images/piggy-bank-rain-thumb.png", "Pink ceramic piggy bank and coins on a rainy windowsill"),
("/guides/open-enrollment/", "Fall open enrollment, October 15 to December 7", "/assets/images/household-finances-paperwork-thumb.png", "Hands reviewing financial paperwork with a pen and coffee mug"),
("/guides/special-enrollment-periods/", "Special enrollment after job coverage ends", "/assets/images/household-finances-paperwork-thumb.png", "Hands reviewing financial paperwork with a pen and coffee mug"),
("/guides/medigap-open-enrollment/", "The separate Medigap six month window", "/assets/images/calculator-tax-forms-thumb.png", "Calculator, pen and paperwork on a kitchen table"),
],
)

add(
path="/guides/initial-enrollment-period/",
title="Initial Enrollment Period Around Age 65 | Which Senior Plan",
h1="Your Initial Enrollment Period",
desc="The 7 month Initial Enrollment Period around age 65, when coverage starts, and who gets Medicare without a separate signup.",
body="""
<div class="answer"><p><strong>Short version:</strong> The Initial Enrollment Period lasts 7 months. It starts 3 months before the month you turn 65 and ends 3 months after that month. If your birthday is on the first of the month, Part A can start a month earlier, and the Medicare &amp; You handbook describes a shifted 7 month window.</p></div>
<p>Medicare.gov says this is generally your first chance to sign up. Coverage always starts on the first of a month. If you qualify for premium free Part A, that Part A starts the month you turn 65. If your birthday is the first day of the month, Part A starts the month before you turn 65.</p>
<p>For Part B, and for Part A if you pay a premium, the start date depends on the month you sign up. Sign up before the month you turn 65 and coverage starts the month you turn 65. Sign up during the birthday month or the 3 months after and coverage starts the next month. The Medicare &amp; You handbook on Medicare.gov adds the first of the month case for the window itself: if your birthday is on the first day of a month, the 7 month period starts 4 months before that birthday month and ends 2 months after it.</p>
<p>You can also join a Medicare Advantage plan or a drug plan during this same 7 months. You need both Part A and Part B for an Advantage plan. You need either Part A or Part B for a standalone drug plan. If you ask to join a plan before Part A or Part B starts, plan coverage starts when that Part starts. If you ask after Part A or Part B has started, plan coverage starts the first of the month after the plan gets your request.</p>
<h2>Some people are enrolled without filing</h2>
<p>Medicare.gov says you get Part A and Part B automatically if you already receive Social Security or Railroad Retirement benefits, including if those benefits start at least 4 months before you turn 65. People with ALS get Medicare the month disability benefits start. Other people under 65 get Medicare after 24 months of disability benefits. In Puerto Rico and outside the United States, Part A can start automatically while Part B still requires a signup.</p>
<p>If none of that applies, you contact Social Security to sign up. Medicare.gov lists the phone as 1-800-772-1213, and TTY 1-800-325-0778. If you or your spouse worked for a railroad, the Railroad Retirement Board number listed on Medicare.gov is 1-877-772-5772. Missing this window can mean waiting until the [[/guides/general-enrollment-and-penalties/|General Enrollment Period]] and paying a penalty, unless you have a [[/guides/special-enrollment-periods/|special enrollment period]].</p>
""",
faqs=[
("How long is the first signup window?", "Seven months: 3 months before the month you turn 65, the birthday month, and 3 months after. A birthday on the first of the month changes the start of Part A and, in the Medicare & You handbook, the count of the 7 months."),
("Do I have to call Medicare to enroll in Part A and Part B?", "You contact Social Security, or the Railroad Retirement Board if your work record is there. Medicare.gov says an online Social Security account is the fastest path for people who need to sign up."),
("When should I look at a drug plan?", "During the same Initial Enrollment Period if you want drug coverage as soon as you are eligible. Waiting 63 days or more without creditable drug coverage can cause a Part D penalty."),
],
sources=[
("When does Medicare coverage start?", "https://www.medicare.gov/basics/get-started-with-medicare/sign-up/when-does-medicare-coverage-start"),
("How do I sign up for Medicare?", "https://www.medicare.gov/basics/get-started-with-medicare/sign-up/how-do-i-sign-up-for-medicare"),
("Joining a plan", "https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/joining-a-plan"),
("Medicare & You handbook", "https://www.medicare.gov/publications/10050-medicare-and-you.pdf"),
],
related=[("/guides/enrollment-periods/", "All the windows"), ("/guides/special-enrollment-periods/", "If you have job coverage"), ("/guides/medigap-open-enrollment/", "Medigap timing")],
)

add(
path="/guides/open-enrollment/",
title="Which Fall Medicare Deadline Should I Use?",
h1="Open enrollment: October 15 to December 7",
desc="From October 15 through December 7 you can change Advantage and drug plans. Coverage starts January 1.",
body="""
<div class="answer"><p><strong>Short version:</strong> October 15 through December 7 is the yearly open enrollment for Medicare Advantage and Medicare drug plans. If the plan gets your request by December 7, the new coverage starts January 1.</p></div>
<p>Medicare.gov says that during this period you can join, drop, or switch to another Medicare Advantage plan with or without drug coverage. You can move from Original Medicare to Medicare Advantage, or from Medicare Advantage back to Original Medicare. If you are in Original Medicare, you can join, drop, or switch a standalone drug plan.</p>
<p>This is not a new Initial Enrollment Period for Part B. If you never signed up for Part B, this fall window does not replace the [[/guides/general-enrollment-and-penalties/|General Enrollment Period]] or a special enrollment period. It is also not the one time [[/guides/medigap-open-enrollment/|Medigap open enrollment]]. Dropping an Advantage plan in the fall does not by itself give you a fresh right to buy any Medigap letter without health questions.</p>
<p>SHIP counselors are busiest in this season. The national SHIP line published by shiphelp.org is 1-877-839-2675, and 1-800-MEDICARE is 1-800-633-4227 (TTY 1-877-486-2048). Your state page lists the local program. We do not run a plan picker and we do not ask for your Medicare number.</p>
""",
faqs=[
("When does a plan I join in the fall start?", "January 1, if the plan gets your request by December 7."),
("Can I use this window to sign up for Part B for the first time?", "No. This window changes Advantage and drug coverage. Part B signup uses the Initial Enrollment Period, a special enrollment period, or the General Enrollment Period from January 1 through March 31."),
("Is this the same as Medigap open enrollment?", "No. Medigap open enrollment is a one time 6 month period that starts when you are 65 or older and you have Part B."),
],
sources=[
("Joining a plan", "https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/joining-a-plan"),
("SHIP Help, find your SHIP", "https://www.shiphelp.org/what-we-do/"),
("Help with drug costs, Medicare phone", "https://www.medicare.gov/basics/costs/help/drug-costs"),
],
related=[("/guides/medicare-advantage-open-enrollment/", "January Advantage window"), ("/guides/how-to-compare-plans/", "How to compare"), ("/states/", "State SHIP contacts")],
)

add(
path="/guides/medicare-advantage-open-enrollment/",
title="Medicare Advantage Open Enrollment | Which Senior Plan",
h1="Medicare Advantage open enrollment",
desc="From January 1 through March 31, people already in Medicare Advantage can switch plans or return to Original Medicare and join a drug plan.",
body="""
<div class="answer"><p><strong>Short version:</strong> January 1 through March 31 is the Medicare Advantage open enrollment period. It is only for people already in a Medicare Advantage plan. You can switch to another Advantage plan, or drop it, return to Original Medicare, and join a drug plan. Coverage starts the first of the month after the plan gets your request.</p></div>
<p>Medicare.gov also says this kind of change is available within the first 3 months you have Medicare, if you are in an Advantage plan. It is not a window for someone who has only Original Medicare to join an Advantage plan. That change waits for the next fall open enrollment, unless a special enrollment period applies.</p>
<p>The same calendar dates, January 1 through March 31, are also the General Enrollment Period for Part A and Part B. That is a different rule for a different problem: people who missed their first Part B signup. Do not mix the two. One changes an Advantage plan you already have. The other signs you up for Part B, possibly with a penalty. Both are explained side by side on the [[/guides/enrollment-periods/|enrollment overview]].</p>
<p>If you drop an Advantage plan and return to Original Medicare, ask whether you have a right to buy a Medigap policy. That right is not automatic every winter. See [[/guides/medigap-open-enrollment/|Medigap open enrollment and guaranteed issue rights]].</p>
""",
faqs=[
("Can I join my first Advantage plan in February?", "Not under this window, unless you already have an Advantage plan or you are in your first 3 months of Medicare and already in a plan, or you have a separate special enrollment period."),
("How fast does a January switch start?", "Medicare.gov says coverage starts the first of the month after the plan gets your request."),
("Is January 1 to March 31 also for Part B?", "The dates match the General Enrollment Period, but that period is for signing up for Part B or premium Part A. It is a different use of the same months."),
],
sources=[
("Joining a plan", "https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/joining-a-plan"),
("When does Medicare coverage start?", "https://www.medicare.gov/basics/get-started-with-medicare/sign-up/when-does-medicare-coverage-start"),
],
related=[("/guides/open-enrollment/", "Fall open enrollment"), ("/guides/general-enrollment-and-penalties/", "General enrollment"), ("/guides/medicare-advantage/", "What Advantage is")],
)

add(
path="/guides/special-enrollment-periods/",
title="Medicare Special Enrollment Periods | Which Senior Plan",
h1="Special enrollment periods",
desc="Special enrollment periods after job coverage, after Medicaid ends, and after release from incarceration, from Medicare.gov.",
body="""
<div class="answer"><p><strong>Short version:</strong> A special enrollment period lets you sign up for Part B, and premium Part A, without a late penalty after your first window closes. Each situation has its own start, end, and form. The full list is on Medicare.gov, not on a single calendar date.</p></div>
<h2>Coverage from a current job</h2>
<p>The Medicare &amp; You handbook says that if you delayed Part B, or premium Part A, because you had group health plan coverage from current employment (yours, a spouse's, or a family member's if you have a disability), you can sign up any time you still have that coverage, and during the 8 month period that begins the month after employment ends or coverage ends, whichever happens first. Coverage generally starts the first day of the month after you sign up.</p>
<p>The live Medicare.gov signup page adds three limits. This special period ends 8 months after the group health plan coverage or the employment ends, whichever happens first. COBRA is not treated as that group health plan coverage, and taking COBRA does not move the end date. If you sign up while you or your spouse are still working, or in the first full month after employer coverage ends, you can ask to delay the Part B start date by up to 3 months. Missing that 8 month window is listed as a situation that does not qualify.</p>
<h2>Other situations Medicare.gov lists</h2>
<p>If Medicaid coverage ended on or after January 1, 2023, Medicare.gov lists a special enrollment period that ends 6 months after the Medicaid coverage ends. You use form CMS-10797. If you were released from incarceration on or after January 1, 2023 and missed a chance to sign up while you were incarcerated, the period starts the day you are released and ends on the last day of the 12th month after the month you are released.</p>
<p>The same page lists more situations, including bad information from an employer or health plan on or after January 1, 2023, volunteering abroad, and TRICARE. Several of them use form CMS-10797, which you send to Social Security. Plan changes have their own special periods too, for a move, for losing other coverage, for Medicaid, or for Extra Help. Those plan windows are summarized on the Medicare.gov joining a plan page.</p>
<p>If you have a disability and the job coverage is from a family member who is not your spouse, Medicare.gov says the employer must be in a large group health plan. Read the page for your own facts before you rely on a row in a table.</p>
""",
faqs=[
("Does COBRA give me more time to sign up for Part B?", "Medicare.gov says COBRA is not group health plan coverage for this purpose, and getting COBRA does not change when the special enrollment period ends."),
("How long do I have after I stop working?", "The handbook describes an 8 month period that begins the month after employment ends or the job coverage ends, whichever happens first. The live signup page says the period ends 8 months after coverage or employment ends, whichever happens first."),
("What form do I use?", "Medicare.gov tells people in several of these situations to fill out form CMS-10797 and send it to Social Security."),
],
sources=[
("When does Medicare coverage start?", "https://www.medicare.gov/basics/get-started-with-medicare/sign-up/when-does-medicare-coverage-start"),
("Medicare & You handbook", "https://www.medicare.gov/publications/10050-medicare-and-you.pdf"),
("Joining a plan", "https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/joining-a-plan"),
],
related=[("/guides/initial-enrollment-period/", "First window"), ("/guides/general-enrollment-and-penalties/", "If you missed it"), ("/guides/ship-counseling/", "Free counseling")],
)

add(
path="/guides/general-enrollment-and-penalties/",
title="How Is the Part B Late Penalty Calculated?",
h1="How the Part B late enrollment penalty is calculated",
desc="Part B adds 10 percent per full 12 months without it. Medicare.gov 2026 and 2027 examples, plus Part D math.",
modified="2026-11-20",
checked="20 Nov 2026",
image="/assets/images/piggy-bank-rain.png",
image_alt="Pink ceramic piggy bank and coins on a rainy windowsill",
image_caption="Thumbnail for the late enrollment penalty guide.",
compare_html='<aside class="compare" aria-label="Check another charge"><p><strong>A penalty is not IRMAA.</strong> The 10 percent clock below is for signing up late. Income can add a separate amount. The [[/guides/irmaa-brackets-2027/|2027 IRMAA brackets]] start above $112,000 for a single filer. The premium those percentages sit on is the [[/guides/medicare-costs-2027/|2027 Part B premium of $209.40]].</p></aside>',
body="""
<div class="answer"><p><strong>Short version:</strong> Medicare.gov adds 10 percent of the standard Part B premium for each full 12 months you could have had Part B and did not. The extra is part of the monthly premium for as long as you have Part B. It is not a one time fee. A partial year does not count. If you missed the first window and you do not have a [[/guides/special-enrollment-periods/|special enrollment period]], you can sign up from January 1 through March 31. Coverage starts the month after you sign up.</p></div>
<h2>The 10 percent rule</h2>
<p>Count full 12 month periods only. One full year without Part B is 10 percent. Two full years is 20 percent. Three is 30 percent. Medicare.gov then adds that percentage of the standard premium to the standard premium, and rounds the sum to the nearest 10 cents. The standard premium changes every year, so the dollar penalty changes even when the percentage stays put. Higher income can raise the bill again, on top of this math. That income surcharge is [[/guides/irmaa-brackets-2027/|IRMAA]], and it uses a tax return, not the number of months you waited.</p>
<p>You generally do not owe the Part B penalty if you qualify for a special enrollment period, or if you are in a [[/guides/medicare-savings-programs/|Medicare Savings Program]]. Job coverage has to be from current work. COBRA does not keep the Part B special period open. The limits are on the special enrollment page.</p>
<!--NEXT_READS-->
<h2>Medicare.gov's own examples</h2>
<p>These two blocks are Medicare.gov's examples, copied as arithmetic from the avoid penalties page read 20 Nov 2026. They are not a bill for a named person.</p>
<p>For 2026, a wait of 2 full years (24 months) is a 20 percent penalty. Twenty percent of the $202.90 standard premium is $40.58. Added to $202.90 that is $243.48, which Medicare.gov rounds to $243.50 for 2026.</p>
<p>For 2027, the same 2 year wait is still 20 percent, now of the $209.40 standard premium. Twenty percent is $41.88. Added to $209.40 that is $251.28, which Medicare.gov rounds to $251.30 for 2027.</p>
<h2>A hypothetical with a different delay</h2>
<p>Hypothetical, not a Medicare.gov example: someone waits 3 full 12 month periods and does not have a special enrollment period. The percentage is 30. Thirty percent of the 2027 standard premium is 0.30 times $209.40, which is $62.82. Added to $209.40 that is $272.22. Using the same nearest 10 cents rounding Medicare.gov shows in its examples, $272.22 becomes $272.20 a month in 2027. A wait of 30 months would still be only 2 full 12 month periods. The extra 6 months would not add another 10 percent. Do not treat this paragraph as your premium. Social Security calculates the real one.</p>
<h2>Part A uses a different clock</h2>
<p>Only people who pay a premium for Part A can owe a Part A penalty. Medicare.gov says the monthly premium may go up 10 percent, and you pay the higher premium for twice the number of years you could have signed up but did not. The example on that page: eligible for 2 years and not signed up, the higher premium lasts 4 years. It then stops. That is the part that does not match Part B.</p>
<p>CMS, on 17 Nov 2026, set the 2027 Part A premiums at $328 a month with at least 30 quarters of work, and $597 with fewer than 30. The 2026 bases were $311 and $565. Hypothetical, using only those published premiums and Medicare.gov's 10 percent rule: 10 percent of $328 is $32.80, so the higher 2027 premium would be $360.80. Ten percent of $597 is $59.70, so $656.70. If the uncovered stretch was 2 years, those higher amounts would last 4 years. CMS did not publish those penalty totals. They are the arithmetic, labeled so they are not mistaken for a fact sheet line.</p>
<h2>Part D is 1 percent a month</h2>
<p>The Part D penalty is 1 percent of the national base beneficiary premium for each full month you went without Part D or other creditable drug coverage after you were first eligible. Medicare.gov uses a gap of 63 days in a row, after the Initial Enrollment Period, as the point where the penalty can start. The monthly penalty is rounded to the nearest 10 cents, added to the plan premium, and it lasts as long as you have drug coverage, even if you change plans. The base changes, so the dollar amount can change each year. The base is not the premium printed on your plan.</p>
<p>Medicare.gov's example is a 14 month gap. The national base is $38.99 in 2026 and $41.33 in 2027. Fourteen percent of $38.99 is $5.46, rounded to $5.50 in 2026. Fourteen percent of $41.33 is $5.79, rounded to $5.80 in 2027. Both figures are added to the plan premium for that year.</p>
<p>Hypothetical, for a 20 month gap in 2027: 20 percent of $41.33 is $8.266, which rounds to $8.30 a month under the same nearest 10 cents step. That illustration is not on the Medicare.gov example. You generally avoid the Part D penalty if you had creditable drug coverage, or if you get [[/guides/extra-help/|Extra Help]]. Extra Help also stops the penalty while you have it. Drug plan rules for 2026, including the $2,100 cap, are on the [[/guides/part-d/|Part D]] page. The 2027 cap of $2,400 is on the [[/guides/medicare-costs-2027/|2027 costs]] page.</p>
""",
faqs=[
("How is the Part B late enrollment penalty calculated?", "Medicare.gov adds 10 percent for each full 12 months you could have had Part B but did not. A 2 year wait is 20 percent of that year's standard premium, added to the premium and rounded to the nearest 10 cents. In the 2027 example that is $251.30 a month."),
("Does the Part B penalty ever stop?", "Medicare.gov says you pay it for as long as you have Part B. It is not a one time late fee. The Part A penalty is the one that runs for twice the number of years you delayed and then ends."),
("Is the Part D penalty the same dollar amount every year?", "No. It is recalculated from that year's national base beneficiary premium. Medicare.gov lists $38.99 for 2026 and $41.33 for 2027. Its 14 month example is $5.50 in 2026 and $5.80 in 2027."),
],
sources=[
("Avoid late enrollment penalties", "https://www.medicare.gov/basics/costs/medicare-costs/avoid-penalties"),
("When does Medicare coverage start?", "https://www.medicare.gov/basics/get-started-with-medicare/sign-up/when-does-medicare-coverage-start"),
("How much does Medicare drug coverage cost?", "https://www.medicare.gov/health-drug-plans/part-d/basics/costs"),
("2027 Medicare Parts A and B premiums and deductibles", "https://www.cms.gov/newsroom/fact-sheets/2027-medicare-parts-b-premiums-deductibles"),
("2026 Medicare Parts A and B premiums and deductibles", "https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-deductibles"),
],
related=[("/guides/special-enrollment-periods/", "Ways to avoid a penalty"), ("/guides/extra-help/", "Extra Help"), ("/guides/irmaa-brackets-2027/", "2027 IRMAA brackets"), ("/guides/enrollment-periods/", "All windows")],
next_reads=[
("/guides/irmaa-brackets-2027/", "2027 IRMAA income brackets", "/assets/images/retirement-tea-papers-thumb.png", "Older hands resting on a mug beside printed charts and papers on a wooden table"),
("/guides/special-enrollment-periods/", "Special enrollment that can avoid the penalty", "/assets/images/household-finances-paperwork-thumb.png", "Hands reviewing financial paperwork with a pen and coffee mug"),
("/guides/extra-help/", "Extra Help, which waives the Part D penalty", "/assets/images/calculator-tax-forms-thumb.png", "Calculator, pen and paperwork on a kitchen table"),
("/guides/enrollment-periods/", "Which enrollment window applies", "/assets/images/household-finances-paperwork-thumb.png", "Hands reviewing financial paperwork with a pen and coffee mug"),
],
)

COST_THUMB = "/assets/images/retirement-tea-papers.png"
COST_THUMB_SM = "/assets/images/retirement-tea-papers-thumb.png"
COST_THUMB_ALT = "Older hands resting on a mug beside printed charts and papers on a wooden table"

add(
path="/guides/medicare-costs-2026/",
title="2026 Medicare Costs and Premiums | Which Senior Plan",
h1="Medicare costs in 2026",
desc="Official 2026 Part A and Part B premiums, deductibles, and income brackets from CMS and Medicare.gov. Private plan premiums are not listed.",
modified="2026-11-20",
checked="20 Nov 2026",
image=COST_THUMB,
image_alt=COST_THUMB_ALT,
image_caption="Thumbnail for this costs guide.",
compare_html='<aside class="compare" aria-label="Check another year"><p><strong>2027 figures are out.</strong> CMS published the [[/guides/medicare-costs-2027/|2027 Part A and Part B amounts]] on 17 Nov 2026. The income brackets that raise them are on the [[/guides/irmaa-brackets-2027/|2027 IRMAA page]]. This page stays the 2026 table.</p></aside>',
body="""
<div class="answer"><p><strong>Short version:</strong> These are the 2026 amounts CMS and Medicare.gov published for Part A and Part B. They are not quotes for a Medicare Advantage, Part D, or Medigap policy. Those prices are set by the plan.</p></div>
<h2>Part A</h2>
<div class="tablewrap"><table class="list"><thead><tr><th scope="col">2026 Part A cost</th><th scope="col">Amount</th></tr></thead><tbody>
<tr><th scope="row">Premium for most people (about 40 quarters of work)</th><td>$0</td></tr>
<tr><th scope="row">Premium with at least 30 quarters</th><td>$311 a month</td></tr>
<tr><th scope="row">Full premium with fewer than 30 quarters</th><td>$565 a month</td></tr>
<tr><th scope="row">Hospital deductible, each benefit period</th><td>$1,736</td></tr>
<tr><th scope="row">Hospital coinsurance, days 61 through 90</th><td>$434 a day</td></tr>
<tr><th scope="row">Lifetime reserve days</th><td>$868 a day</td></tr>
<tr><th scope="row">Skilled nursing facility coinsurance, days 21 through 100</th><td>$217 a day</td></tr>
</tbody></table></div>
<p>CMS says about 99 percent of people with Medicare pay no Part A premium. Days 1 through 60 in the hospital are $0 after the deductible. There is no limit on how many benefit periods you can have.</p>
<!--NEXT_READS-->
<h2>Part B</h2>
<p>The standard premium is $202.90 a month. The deductible is $283 for the year. After the deductible you usually pay 20 percent of the Medicare approved amount for Part B services. The standard premium for immunosuppressive drug coverage only, for certain people whose full Medicare ended 36 months after a kidney transplant, is $121.60 a month.</p>
<h2>Higher premiums based on income</h2>
<p>CMS says about 8 percent of people with Part B pay an income related monthly adjustment. The 2026 full Part B amounts, using modified adjusted gross income, are below. The income is from the tax return Social Security uses, not a guess about this year's pay.</p>
<div class="tablewrap"><table class="list"><thead><tr><th scope="col">Single income</th><th scope="col">Joint income</th><th scope="col">Part B total premium</th><th scope="col">Part D add on</th></tr></thead><tbody>
<tr><td>$109,000 or less</td><td>$218,000 or less</td><td>$202.90</td><td>$0</td></tr>
<tr><td>Above $109,000 to $137,000</td><td>Above $218,000 to $274,000</td><td>$284.10</td><td>$14.50</td></tr>
<tr><td>Above $137,000 to $171,000</td><td>Above $274,000 to $342,000</td><td>$405.80</td><td>$37.50</td></tr>
<tr><td>Above $171,000 to $205,000</td><td>Above $342,000 to $410,000</td><td>$527.50</td><td>$60.40</td></tr>
<tr><td>Above $205,000 and under $500,000</td><td>Above $410,000 and under $750,000</td><td>$649.20</td><td>$83.30</td></tr>
<tr><td>$500,000 or more</td><td>$750,000 or more</td><td>$689.90</td><td>$91.00</td></tr>
</tbody></table></div>
<p>Married people who lived with a spouse and file a separate return pay a Part B total of $202.90 if income is $109,000 or less, $649.20 if income is above $109,000 and under $391,000, and $689.90 at $391,000 or more. The matching Part D add on amounts are $0, $83.30, and $91.00. The Part D amount is added to the plan premium. It is not the plan premium. How the brackets are chosen, and the 2027 table, are on the [[/guides/irmaa-brackets-2027/|IRMAA guide]].</p>
<p>Help with these costs, if your income is limited, is a [[/guides/medicare-savings-programs/|Medicare Savings Program]] run by your state. For outpatient drug rules in 2026, including the $2,100 out of pocket cap, see [[/guides/part-d/|Part D]]. For free local counseling, use [[/guides/ship-counseling/|SHIP]].</p>
""",
faqs=[
("Are these the prices of Medicare Advantage plans?", "No. Advantage, Part D, and Medigap premiums are set by each company. The figures on this page are the federal Part A and Part B amounts for 2026."),
("Does everyone pay $202.90 for Part B?", "That is the standard 2026 premium. People with higher incomes pay more, and a late enrollment penalty can add more. Some people pay less because a state Medicare Savings Program pays the premium."),
("Why does the Part A deductible say each benefit period?", "CMS and Medicare.gov charge the hospital deductible once per benefit period, not once per calendar year. A new benefit period can mean another deductible."),
],
sources=[
("2026 Medicare Parts A and B premiums and deductibles", "https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-deductibles"),
("What does Medicare cost?", "https://www.medicare.gov/basics/get-started-with-medicare/medicare-basics/what-does-medicare-cost"),
("2027 Medicare Parts A and B premiums and deductibles", "https://www.cms.gov/newsroom/fact-sheets/2027-medicare-parts-b-premiums-deductibles"),
],
related=[("/guides/medicare-costs-2027/", "2027 costs"), ("/guides/part-d/", "Part D costs"), ("/guides/medicare-savings-programs/", "Help paying"), ("/guides/general-enrollment-and-penalties/", "Penalties")],
next_reads=[
("/guides/medicare-costs-2027/", "2027 Medicare costs from CMS", COST_THUMB_SM, COST_THUMB_ALT),
("/guides/part-d/", "Part D drug costs and the yearly cap", COST_THUMB_SM, COST_THUMB_ALT),
("/guides/medicare-savings-programs/", "Medicare Savings Programs", COST_THUMB_SM, COST_THUMB_ALT),
("/guides/irmaa-brackets-2027/", "Which incomes raise the 2027 IRMAA surcharge", COST_THUMB_SM, COST_THUMB_ALT),
],
)

add(
path="/guides/what-medicare-covers/",
title="What Medicare Covers | Which Senior Plan",
h1="What Medicare covers",
desc="What Part A and Part B help pay, and why a specific test can still be denied. Use Medicare.gov to check one item.",
body="""
<div class="answer"><p><strong>Short version:</strong> Part A helps with inpatient hospital care, skilled nursing facility care, hospice, and some home health care. Part B helps with doctor services, outpatient care, durable medical equipment, and many preventive services. A specific item can still be uncovered.</p></div>
<p>Medicare.gov says coverage of a test, item, or service depends on three things: federal and state laws, national coverage decisions, and local coverage decisions by the companies that process claims in each state. Those companies decide whether something is medically necessary in their area. The practical step Medicare.gov gives is to ask the doctor whether Medicare will cover the service, and to check that item on Medicare.gov.</p>
<p>Original Medicare is not a list we can safely shorten into "everything medically necessary." The federal site keeps an item by item list for that reason. We link it rather than retype it. Things Original Medicare generally does not cover are on the [[/guides/what-medicare-does-not-cover/|not covered]] page, including non medical long term care, routine hearing aids, and most dental care.</p>
<p>A Medicare Advantage plan has to cover what Original Medicare covers, and it may add extras. It can also use networks and prior approval. Confirm the item with that plan, not with a general article.</p>
""",
faqs=[
("Does Medicare cover every service my doctor orders?", "Not automatically. Medicare.gov says coverage also depends on national and local decisions about medical necessity."),
("Where do I check one test or piece of equipment?", "On Medicare.gov, in the coverage search, and with the doctor who would order it."),
("Does Advantage cover the same services?", "Medicare.gov says to ask whether your Medicare Advantage plan covers the same items and services. Plans can also offer extra benefits."),
],
sources=[
("What Original Medicare covers", "https://www.medicare.gov/what-medicare-covers"),
("Parts of Medicare", "https://www.medicare.gov/basics/get-started-with-medicare/medicare-basics/parts-of-medicare"),
],
related=[("/guides/what-medicare-does-not-cover/", "What it does not cover"), ("/guides/original-medicare/", "Original Medicare"), ("/guides/medicare-advantage/", "Medicare Advantage")],
)

add(
path="/guides/what-medicare-does-not-cover/",
title="What Original Medicare Does Not Cover | Which Senior Plan",
h1="What Original Medicare does not cover",
desc="Original Medicare does not cover long term care, most dental care, routine hearing aids, or routine eyeglasses exams. Some plans add extras.",
body="""
<div class="answer"><p><strong>Short version:</strong> Original Medicare does not pay for everything. If Part A and Part B do not cover an item, you pay unless other coverage pays, or you are in a Medicare Advantage, Medicare Cost, or PACE plan that covers it.</p></div>
<p>Medicare.gov lists these examples of what Original Medicare does not cover:</p>
<ul>
<li>Eye exams for prescription eyeglasses</li>
<li>Non medical long term care</li>
<li>Cosmetic surgery</li>
<li>Massage therapy</li>
<li>Routine physical exams</li>
<li>Hearing aids and exams for fitting them</li>
<li>Concierge care, also called retainer based or boutique medicine</li>
<li>Services from a doctor who has opted out of Medicare, except in an emergency or urgent need</li>
<li>Most dental care, including routine cleanings, tooth extractions, and dentures</li>
</ul>
<p>The same page says Original Medicare may still pay for some dental services that are closely related to other covered care. It also says some Advantage, Cost, and PACE plans cover extra vision, hearing, or dental services. That is a feature of those plans, not a promise that every plan includes them.</p>
<p>A Medigap policy helps pay Original Medicare cost sharing. It does not turn an uncovered service into a covered one. Part D covers outpatient drugs that are on the plan formulary, not the gaps in this list.</p>
""",
faqs=[
("Does Medicare pay for a nursing home stay that is only custodial?", "Medicare.gov lists non medical long term care among the services Original Medicare does not cover. A skilled nursing facility stay under Part A rules is different from custodial long term care."),
("Will Medigap pay for dental cleanings?", "No. Medigap helps with costs Original Medicare already covers. It does not add routine dental coverage."),
("Can a private plan cover any of this?", "Medicare.gov says some Medicare Advantage, Medicare Cost, and PACE plans cover extra vision, hearing, or dental services. You have to read that plan."),
],
sources=[
("What's not covered by Original Medicare", "https://www.medicare.gov/providers-services/original-medicare/not-covered"),
("What Original Medicare covers", "https://www.medicare.gov/what-medicare-covers"),
],
related=[("/guides/what-medicare-covers/", "What it covers"), ("/guides/medicare-advantage/", "Advantage extras"), ("/guides/medigap-plan-letters/", "What Medigap adds")],
)

add(
path="/guides/medicare-savings-programs/",
title="Medicare Savings Programs in 2026 | Which Senior Plan",
h1="Medicare Savings Programs",
desc="2026 income and resource limits for QMB, SLMB, QI, and QDWI. Your state Medicaid agency takes the application and may use higher limits.",
body="""
<div class="answer"><p><strong>Short version:</strong> Medicare Savings Programs help pay Medicare premiums and, for one program, deductibles and coinsurance. Your state runs them. The 2026 federal limits are below. Alaska and Hawaii use slightly higher income limits, and many states let people qualify with more income or resources than this table.</p></div>
<div class="tablewrap"><table class="list"><thead><tr><th scope="col">Program</th><th scope="col">What it helps pay</th><th scope="col">Monthly income, single / couple</th><th scope="col">Resources, single / couple</th></tr></thead><tbody>
<tr><th scope="row">QMB</th><td>Part A and Part B premiums, and deductibles, coinsurance, and copays for Medicare covered services</td><td>$1,350 / $1,824</td><td>$9,950 / $14,910</td></tr>
<tr><th scope="row">SLMB</th><td>Part B premium. You need Part A and Part B</td><td>$1,616 / $2,184</td><td>$9,950 / $14,910</td></tr>
<tr><th scope="row">QI</th><td>Part B premium. You need Part A and Part B. You apply every year</td><td>$1,816 / $2,455</td><td>$9,950 / $14,910</td></tr>
<tr><th scope="row">QDWI</th><td>Part A premium only, for some working people with a disability who lost premium free Part A</td><td>$5,405 / $7,299</td><td>$4,000 / $6,000</td></tr>
</tbody></table></div>
<p>If you qualify for QMB, SLMB, or QI, you also get [[/guides/extra-help/|Extra Help]] with drug costs. Medicare.gov says you will pay no more than $12.65 in 2026 for each drug your plan covers. QMB also means Medicare providers are not allowed to bill you for Medicare covered services, including deductibles and coinsurance. A small Medicaid copay can still apply.</p>
<p>QI has extra rules. You must apply every year. States approve applications first come, first served, with priority for people who had QI the year before. QI is only for people who do not qualify for other Medicaid coverage.</p>
<p>Apply through the state Medicaid agency, even if you think you are over the federal limits. Each [[/states/|state page]] names the agency Medicaid.gov lists and the phone numbers on that directory. Limits can change, and this table is the 2026 federal set.</p>
""",
faqs=[
("Do these programs replace Medicare?", "No. They help pay Medicare costs. You still have Medicare. The state decides which program you qualify for."),
("What if my income is a little over the table?", "Apply anyway. Medicare.gov says you may qualify in your state even if income or resources are higher than the federal limits, and that Alaska and Hawaii use slightly higher income limits."),
("Does QMB stop doctor bills?", "For services and items Medicare covers, Medicare.gov says providers are not allowed to bill a QMB enrollee for the deductible, coinsurance, or copay. Show both cards."),
],
sources=[
("Medicare Savings Programs", "https://www.medicare.gov/basics/costs/help/medicare-savings-programs"),
("Where can people get help with Medicaid and CHIP?", "https://www.medicaid.gov/about-us/where-can-people-get-help-medicaid-chip"),
],
related=[("/guides/extra-help/", "Extra Help"), ("/guides/medicare-and-medicaid/", "Medicare and Medicaid"), ("/states/", "State Medicaid contacts")],
)

add(
path="/guides/extra-help/",
title="Extra Help: 2026 Limits and 2027 Drug Copays",
h1="Extra Help with drug costs",
desc="2026 Extra Help limits are $23,940 income and $18,090 resources. 2027 copays are up to $5.80 and $14.40.",
modified="2026-11-20",
checked="20 Nov 2026",
image="/assets/images/calculator-tax-forms.png",
image_alt="Calculator, pen and paperwork on a kitchen table",
image_caption="Thumbnail for the Extra Help guide.",
compare_html='<aside class="compare" aria-label="Check another help program"><p><strong>Extra Help is one program.</strong> A [[/guides/medicare-savings-programs/|Medicare Savings Program]] can pay the Part B premium and may bring Extra Help with it. People with higher income have the opposite problem: the [[/guides/irmaa-brackets-2027/|2027 IRMAA brackets]] add a Part D amount on top of the plan premium.</p></aside>',
body="""
<div class="answer"><p><strong>Short version:</strong> Extra Help pays toward Part D premiums, deductibles, and other drug costs for people with limited income and resources. Medicare.gov, read 20 Nov 2026, still labels the income and resource table as 2026: $23,940 and $18,090 for one person, $32,460 and $36,100 for a married couple. The same page puts the copays under a 2027 heading: up to $5.80 for a generic and up to $14.40 for a brand name drug. You also pay no Part D late penalty while you have Extra Help.</p></div>
<h2>Who gets it without an application</h2>
<p>Medicare.gov lists three automatic paths: full benefit Medicaid, a [[/guides/medicare-savings-programs/|Medicare Savings Program]] that pays the Part B premium, or Supplemental Security Income from Social Security. Medicare mails a notice. The notice can also name a drug plan if you do not have one, and you can pick a different plan. If you still meet the limits, you keep Extra Help next year. A notice arrives if you lose it or if you are moved to a different plan. If no notice comes, Medicare.gov says you keep Extra Help and you keep the same plan.</p>
<p>Everyone else applies through Social Security. You can apply for Extra Help and a Medicare Savings Program at the same time. Social Security sends the state what it needs to start the savings program application unless you say not to on the Extra Help form. A [[/guides/ship-counseling/|SHIP counselor]] can help with the paperwork at no charge. If income or resources change later, you can apply again at any time.</p>
<p>Two timing rules are easy to miss. Extra Help lasts through December 31 of the year even if income changes in the middle of the year. And people with Medicaid or Extra Help may change drug coverage once a month. Most other people cannot.</p>
<!--NEXT_READS-->
<h2>What the 2026 limits are, and what they are not</h2>
<div class="tablewrap"><table class="list"><thead><tr><th scope="col">2026 situation</th><th scope="col">Income limit</th><th scope="col">Resource limit</th></tr></thead><tbody>
<tr><th scope="row">Individual</th><td>$23,940</td><td>$18,090</td></tr>
<tr><th scope="row">Married couple</th><td>$32,460</td><td>$36,100</td></tr>
</tbody></table></div>
<p>Medicare.gov says these limits may go up each year. On 20 Nov 2026 the page still headed that table "2026." It also has a link asking about Alaska and Hawaii, but the dollar limits for those states were not in the main table. This page does not invent them. The [[/guides/medicare-savings-programs/|savings program guide]] has a related note: Alaska and Hawaii use slightly higher income limits for those programs, and the higher dollars were not on the federal table we read.</p>
<p>A different 2026 figure lives on the Medicare Savings Programs page, not in the Extra Help copay list: people who get Extra Help through that route pay no more than $12.65 in 2026 for each drug the plan covers. That sentence is about 2026. It is not the 2027 schedule below.</p>
<h2>What Medicare.gov says you pay in 2027</h2>
<p>Under the heading "What you'll pay under Extra Help in 2027," Medicare.gov lists a plan premium of $0 and a plan deductible of $0. At a pharmacy in the plan's network, the copay is up to $5.80 for each generic and up to $14.40 for each brand name drug. Once total drug costs reach $2,400, including certain payments made for you, you pay $0 for each covered drug for the rest of the year. The $2,400 threshold is the same 2027 Part D cap on the [[/guides/medicare-costs-2027/|2027 costs]] page. It is not a new number invented here.</p>
<p>One tighter cap sits on top of that. If you also have full Medicaid and you are in the Qualified Medicare Beneficiary program, Medicare.gov says you pay no more than $4.90 for each covered drug in 2027. QMB is the program that also stops providers from billing you Medicare deductibles and coinsurance. It is described on the savings program page.</p>
<p>These $0 premium and $0 deductible lines are what Extra Help charges. They are not the premium every Part D plan charges people who do not have Extra Help. Plan premiums without Extra Help are on Medicare.gov's plan finder, not on this site. The [[/guides/part-d/|Part D]] page explains the 2026 standard benefit, including the $615 deductible ceiling and the $2,100 cap, for people who are not in Extra Help.</p>
<p>If the pharmacy price looks wrong, Medicare.gov says to contact the plan, tell them how many days of medicine you have left, and that you can call 1-800-MEDICARE at 1-800-633-4227 (TTY 1-877-486-2048). The plan may ask for proof of Extra Help before it corrects the cost.</p>
<p>Extra Help is not available in Puerto Rico, the U.S. Virgin Islands, Guam, the Northern Mariana Islands, or American Samoa. Medicare.gov says other help exists there and tells people to call the local Medicaid office. Discount cards are a separate trap: Medicare.gov says they are not creditable coverage. Paying with one instead of the Medicare plan does not count toward the deductible or the out of pocket maximum, and a long stretch on a discount card instead of Part D can feed the [[/guides/general-enrollment-and-penalties/|Part D late penalty]].</p>
""",
faqs=[
("Do I apply for Extra Help at the state Medicaid office?", "Automatic Extra Help comes with full Medicaid, a Medicare Savings Program, or SSI. If you do not get it automatically, Medicare.gov says Social Security takes the application. You can apply for Extra Help and a Medicare Savings Program together."),
("Will Extra Help remove a Part D penalty?", "Medicare.gov says you will not have to pay a Part D late enrollment penalty while you get Extra Help."),
("What will Extra Help charge for a prescription in 2027?", "Medicare.gov lists up to $5.80 for a generic and up to $14.40 for a brand name drug at a network pharmacy, with a $0 premium and a $0 deductible. After total drug costs reach $2,400, the copay is $0. Full Medicaid plus QMB is capped at $4.90."),
],
sources=[
("Help with drug costs", "https://www.medicare.gov/basics/costs/help/drug-costs"),
("Medicare Savings Programs", "https://www.medicare.gov/basics/costs/help/medicare-savings-programs"),
("2027 Medicare Parts A and B premiums and deductibles", "https://www.cms.gov/newsroom/fact-sheets/2027-medicare-parts-b-premiums-deductibles"),
],
related=[("/guides/part-d/", "Part D"), ("/guides/medicare-savings-programs/", "Medicare Savings Programs"), ("/guides/irmaa-brackets-2027/", "2027 IRMAA"), ("/guides/ship-counseling/", "Free help applying")],
next_reads=[
("/guides/medicare-savings-programs/", "Medicare Savings Programs that can include Extra Help", "/assets/images/calculator-tax-forms-thumb.png", "Calculator, pen and paperwork on a kitchen table"),
("/guides/part-d/", "How Part D works without Extra Help", "/assets/images/retirement-tea-papers-thumb.png", "Older hands resting on a mug beside printed charts and papers on a wooden table"),
("/guides/general-enrollment-and-penalties/", "How the Part D late penalty is calculated", "/assets/images/piggy-bank-rain-thumb.png", "Pink ceramic piggy bank and coins on a rainy windowsill"),
("/guides/ship-counseling/", "Free help applying for Extra Help", "/assets/images/household-finances-paperwork-thumb.png", "Hands reviewing financial paperwork with a pen and coffee mug"),
],
)

add(
path="/guides/ship-counseling/",
title="Free SHIP Medicare Counseling | Which Senior Plan",
h1="Free SHIP counseling",
desc="SHIP is free local Medicare counseling in every state. The national line is 1-877-839-2675. Local names include SHINE, HICAP, and SHIIP.",
body="""
<div class="answer"><p><strong>Short version:</strong> SHIP is the State Health Insurance Assistance Program. Counselors help you compare Medicare choices at no charge. They do not sell plans. The national number published by shiphelp.org is 1-877-839-2675. Your state uses its own program name and phone.</p></div>
<p>shiphelp.org says the national technical assistance center does not itself give individual counseling. You call the local program or use the SHIP locator. The local name is not always "SHIP." The same site gives HICAP, SHIIP, SHINE, and VICAP as examples. California uses HICAP. Florida uses SHINE. New York uses HIICAP. The [[/states/|state pages]] use the name and phone printed on that state's shiphelp.org page on 16 Nov 2026.</p>
<p>A counselor can explain enrollment deadlines, Medigap letters, Advantage and drug plans, and help with Medicare Savings Programs and Extra Help. Bring your questions. You do not give our site your Medicare number, and we have no form that sends your information to an insurance agent.</p>
<p>For federal questions, Medicare.gov lists 1-800-MEDICARE as 1-800-633-4227, 24 hours a day, 7 days a week, and TTY 1-877-486-2048. That line is not a substitute for the local SHIP if you want someone who works in your state.</p>
<p>Programs are funded through the U.S. Administration for Community Living. Which Senior Plan is not a SHIP and is not part of that program.</p>
""",
faqs=[
("Does SHIP charge a fee?", "No. shiphelp.org describes SHIP as free Medicare counseling from the local program."),
("Will a SHIP counselor sell me a plan?", "The program's role is counseling, not sales. Which Senior Plan also does not sell plans or share your contact details with agents."),
("What if the phone on a state page has changed?", "Use the SHIP locator at shiphelp.org or call 1-877-839-2675. Each state page links the shiphelp.org page we checked and shows the date."),
],
sources=[
("Get help with Medicare enrollment", "https://www.shiphelp.org/what-we-do/"),
("SHIP contact us", "https://www.shiphelp.org/what-we-do/contact-us/"),
("SHIP programs by state", "https://www.shiphelp.org/ships/"),
("Help with drug costs, Medicare phone", "https://www.medicare.gov/basics/costs/help/drug-costs"),
],
related=[("/states/", "Find your state"), ("/guides/how-to-compare-plans/", "How to compare plans"), ("/guides/enrollment-periods/", "Deadlines")],
)

add(
path="/guides/medicare-and-medicaid/",
title="Medicare and Medicaid Together | Which Senior Plan",
h1="Medicare and Medicaid together",
desc="Medicare is federal. Medicaid is run by your state. You can have both. Medicare Savings Programs are one kind of help, not the whole of Medicaid.",
modified="2026-11-18",
checked="18 Nov 2026",
body="""
<div class="answer"><p><strong>Short version:</strong> Medicare is federal health insurance for people 65 and older and for some younger people with disabilities. Medicaid is a joint federal and state program. If you qualify, you can have both. The state decides Medicaid eligibility.</p></div>
<p>Having both is often called being dual eligible. Full Medicaid can cover services Medicare does not, and it can lead to [[/guides/extra-help/|Extra Help]] with drugs. A [[/guides/medicare-savings-programs/|Medicare Savings Program]] is narrower. QMB, SLMB, QI, and QDWI help with Medicare premiums and, in the case of QMB, Medicare cost sharing. They are not the same thing as full Medicaid, even though the state Medicaid agency usually takes the application. Someone who has both programs and needs a nursing home level of care may also be able to join [[/guides/pace-program/|PACE]], a program that combines Medicare and Medicaid services into one coordinated team in some areas.</p>
<p>Medicaid.gov publishes a directory of state agencies, phones, and websites. Each [[/states/|state page]] repeats the agency name, the member phone numbers, and the link from that directory, checked 16 Nov 2026. We do not invent a state's income limit for full Medicaid. Those rules are broader than the federal Medicare Savings Program table and they differ by state.</p>
<p>If you lose Medicaid, you may get a special chance to sign up for Medicare or change a plan. The timing Medicare.gov describes is on the [[/guides/special-enrollment-periods/|special enrollment]] page. People who have Medicaid or Extra Help may also change drug coverage once a month.</p>
""",
faqs=[
("Can I have Medicare and Medicaid at the same time?", "Yes. Medicare.gov says that if you qualify, you can have both."),
("Is a Medicare Savings Program the same as Medicaid?", "It is run through the state and it can come with Extra Help, but QMB, SLMB, QI, and QDWI are specific programs that help with Medicare costs. Full Medicaid is broader and uses state rules."),
("Where do I apply?", "At the state Medicaid agency. Start with your state page for the phone and website Medicaid.gov lists, then confirm on that site."),
],
sources=[
("Parts of Medicare", "https://www.medicare.gov/basics/get-started-with-medicare/medicare-basics/parts-of-medicare"),
("Medicare Savings Programs", "https://www.medicare.gov/basics/costs/help/medicare-savings-programs"),
("Where can people get help with Medicaid and CHIP?", "https://www.medicaid.gov/about-us/where-can-people-get-help-medicaid-chip"),
],
related=[("/states/", "State Medicaid agencies"), ("/guides/medicare-savings-programs/", "Savings programs"), ("/guides/extra-help/", "Extra Help")],
)

add(
path="/guides/how-to-compare-plans/",
title="Which Medicare Plan Should I Compare?",
h1="How to compare plans without a sales pitch",
desc="Use Medicare.gov Plan Finder or a free SHIP counselor. We do not list plan names, star ratings, or premiums, and we do not collect leads.",
body="""
<div class="answer"><p><strong>Short version:</strong> Compare plans on Medicare.gov or with your state SHIP program. Have your drug list, your doctors, and the enrollment window you are in. This website will not rank plans or ask for your phone number.</p></div>
<h2>Use the federal tool</h2>
<p>Medicare.gov runs the plan comparison tool at medicare.gov/plan-compare. It asks where you live because Advantage and drug plans are local. It can show premiums, deductibles, drug costs, and star ratings that we are not copying onto these pages. Those figures change. A copied list would go stale, and a made up list would be worse.</p>
<h2>Or sit with a counselor</h2>
<p>[[/guides/ship-counseling/|SHIP counseling]] is free and local. The counselor does not work for an insurance company. The national line is 1-877-839-2675, and every state page has the local number from shiphelp.org. That is the right place for "which plan should I pick," which this site will not answer.</p>
<h2>What to have ready</h2>
<ul>
<li>Your ZIP code and whether you have Medicaid or Extra Help</li>
<li>The prescriptions you take, and the dose</li>
<li>The doctors and hospitals you want to keep</li>
<li>Which enrollment period you are actually in</li>
</ul>
<p>Then separate the decision into the path (Original Medicare plus Part D, with or without Medigap, or Medicare Advantage) and the specific contract. The [[/guides/original-medicare-vs-medicare-advantage/|comparison page]] is only the first split. A star rating is not a promise about your drugs or your doctors.</p>
<p>Do not send your Medicare number, Social Security number, or bank details through this site. We have no quote form. Anyone who calls you because you "requested Medicare quotes" did not get your name from us.</p>
""",
faqs=[
("Why are there no plan names on this site?", "Plan names, premiums, and formularies change, and listing them would look like a recommendation. Medicare.gov and SHIP are the places that can show current plans."),
("Can I compare Medigap here?", "You can compare what each letter covers on our Medigap page. Prices are not listed. Your state insurance department and SHIP can show policies sold to you."),
("Is the Plan Finder a government site?", "Yes. medicare.gov/plan-compare is on the federal Medicare site. Which Senior Plan is not that site and is not endorsed by it."),
],
sources=[
("Medicare Plan Finder", "https://www.medicare.gov/plan-compare/"),
("Joining a plan", "https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/joining-a-plan"),
("SHIP Help", "https://www.shiphelp.org/what-we-do/"),
],
related=[("/guides/ship-counseling/", "SHIP counseling"), ("/guides/original-medicare-vs-medicare-advantage/", "The two paths"), ("/states/", "Your state")],
)

add(
path="/guides/medigap-open-enrollment/",
title="Which Medigap Enrollment Window Is Mine?",
h1="Medigap open enrollment",
desc="You get one 6 month Medigap open enrollment when you are 65 or older and you have Part B. It does not repeat every fall.",
body="""
<div class="answer"><p><strong>Short version:</strong> Federal law gives you a 6 month Medigap open enrollment period. It starts the first month you have Part B and you are 65 or older. During that window you can buy any Medigap policy the company sells, and the company cannot use medical underwriting to deny you for a pre existing condition.</p></div>
<p>Medicare.gov says this window is one time. It does not come back every fall the way Medicare open enrollment does. After it ends, a company may refuse to sell you a policy, or charge more, if you do not pass medical underwriting. There are exceptions, called guaranteed issue rights or Medigap protections, for certain situations. The federal page describes those rights and tells you to check your state insurance department, because state law can add more.</p>
<p>People under 65 who have Medicare because of a disability or ESRD may not be able to buy Medigap until they turn 65. Federal law generally does not require companies to sell Medigap to people under 65. Some states require it anyway. We do not keep a private scoreboard of those state laws. Ask the state insurance department or SHIP, and read the state page for the office we could verify.</p>
<p>If you buy a Medicare SELECT policy, Medicare.gov says you have 12 months to change your mind and switch to a standard Medigap policy. SELECT plans may require you to use certain hospitals and, in some cases, certain doctors.</p>
<p>The letter you are allowed to buy also depends on when you were first eligible. Plan C and Plan F are closed to people who became eligible on or after January 1, 2020. That rule is on the [[/guides/medigap-plan-letters/|letters page]], along with the 2026 benefit chart.</p>
""",
faqs=[
("Is Medigap open enrollment the same as October 15 to December 7?", "No. The fall window changes Advantage and drug plans. Medigap open enrollment is a one time 6 month period tied to Part B and age 65."),
("Can a company turn me down later?", "Yes. After the 6 months, Medicare.gov says the company may deny a policy or charge more based on medical underwriting, unless you have a guaranteed issue right or a state protection."),
("Do I have to buy Medigap?", "No. It is optional insurance that helps pay Original Medicare costs. This site does not tell you to buy it."),
],
sources=[
("Medigap basics", "https://www.medicare.gov/health-drug-plans/medigap/basics"),
("Get ready to buy a Medigap policy", "https://www.medicare.gov/health-drug-plans/medigap/ready-to-buy"),
("Compare Medigap plan benefits", "https://www.medicare.gov/health-drug-plans/medigap/basics/compare-plan-benefits"),
],
related=[("/guides/medigap-plan-letters/", "Plan letters"), ("/guides/open-enrollment/", "Fall Medicare window"), ("/states/", "State insurance help")],
)

add(
path="/guides/medicare-give-back-benefit/",
title="Is the Medicare Give Back Benefit Real?",
h1="Is the Medicare give back benefit real?",
desc="Yes, but it is a Medicare Part B premium reduction some Advantage plans offer, not a check. What CMS rules and Medicare.gov say.",
published="2026-11-18",
checked="18 Nov 2026",
image="/assets/images/calculator-tax-forms.png",
image_alt="Calculator, pen and paperwork on a kitchen table",
image_caption="AI-generated thumbnail for this give back guide.",
body="""
<div class="answer"><p><strong>Short version:</strong> Yes, the benefit is real, but Medicare.gov calls it a Part B premium reduction, not a give back. Only some Medicare Advantage plans offer it. It lowers what is withheld from your Social Security check or billed to you. It is never paid to you as cash.</p></div>
<p>Medicare.gov says some Medicare Advantage plans will help pay all or part of a member's Part B premium, and that this is sometimes called a Medicare Part B premium reduction. The feature is not available in every area, and a specific plan has to choose to offer it. The standard 2026 Part B premium is $202.90 a month, and the reduction cannot be larger than that amount.</p>
<p>CMS rules describe how the reduction works. A Medicare Advantage plan that offers it agrees to accept a lower monthly payment from Medicare, and in exchange the member's Part B premium bill or Social Security withholding goes down by a set amount, in multiples of 10 cents. The rule says the reduction will never result in a payment to the beneficiary. If the reduction is larger than what someone actually owes under a hold harmless rule, the person simply owes nothing more that month, not a refund.</p>
<p>The size of the reduction is set by the plan and can be different from one county to the next, including $0 in many plans. Plans publish the figure in that year's Summary of Benefits, not on this site. A plan with a large premium reduction can still have a network, prior approval rules, and its own deductible or copays. Read the whole plan, not just the premium line, before you compare it with [[/guides/original-medicare-vs-medicare-advantage/|Original Medicare]] or another Medicare Advantage plan.</p>
<p>This site does not say which plan to pick. Compare the real numbers for plans sold where you live on the Medicare Plan Finder at Medicare.gov, or ask a free [[/guides/ship-counseling/|SHIP counselor]] to go through a specific plan's Summary of Benefits with you.</p>
""",
faqs=[
("Will I get a check for the give back benefit?", "No. The CMS rule for this benefit says the reduction never results in a payment to the beneficiary. It only lowers what is withheld from your Social Security check or billed to you for Part B."),
("Can I get this with Original Medicare or a Medigap policy?", "No. Medicare.gov describes the Part B premium reduction as a feature of some Medicare Advantage plans. Original Medicare and Medigap do not reduce the Part B premium."),
("Does every Medicare Advantage plan offer it?", "No. Medicare.gov says it is not available in every area, and each plan decides whether to offer it. Check a specific plan's Summary of Benefits or the Medicare Plan Finder for the current amount."),
],
sources=[
("Understanding health plan costs", "https://www.medicare.gov/health-drug-plans/health-plans/costs"),
("Understanding Medicare Advantage Plans", "https://www.medicare.gov/publications/12026-understanding-medicare-advantage-plans.pdf"),
("Medicare Part B premium reduction rule, 42 CFR 408.21", "https://www.cms.gov/regulations-and-guidance/regulations-and-policies/quarterlyproviderupdates/downloads/cms6016f.pdf"),
],
related=[("/guides/medicare-advantage/", "What Medicare Advantage is"), ("/guides/medicare-costs-2026/", "2026 Medicare costs"), ("/guides/medicare-costs-2027/", "2027 Medicare costs"), ("/guides/how-to-compare-plans/", "How to compare plans")],
next_reads=[
("/guides/medicare-advantage/", "What Medicare Advantage is", "/assets/images/calculator-tax-forms-thumb.png", "Calculator, pen and paperwork on a kitchen table"),
("/guides/medicare-costs-2027/", "2027 Medicare costs from CMS", "/assets/images/calculator-tax-forms-thumb.png", "Calculator, pen and paperwork on a kitchen table"),
("/guides/how-to-compare-plans/", "How to compare plans", "/assets/images/calculator-tax-forms-thumb.png", "Calculator, pen and paperwork on a kitchen table"),
("/guides/ship-counseling/", "Free SHIP counseling", "/assets/images/calculator-tax-forms-thumb.png", "Calculator, pen and paperwork on a kitchen table"),
],
)

add(
path="/guides/pace-program/",
title="What Is the PACE Program for Seniors?",
h1="What is the PACE program for seniors?",
desc="PACE brings nursing home level care to people 55 and older in their community. Who can join, what it costs, and how to find a program.",
published="2026-11-18",
checked="18 Nov 2026",
image="/assets/images/household-finances-paperwork.png",
image_alt="Hands reviewing financial paperwork with a pen and coffee mug",
image_caption="AI-generated thumbnail for this PACE guide.",
body="""
<div class="answer"><p><strong>Short version:</strong> PACE, the Program of All Inclusive Care for the Elderly, is a Medicare and Medicaid program that brings nursing home level care to people in their own community instead of a facility. It is only available in some states and only inside the service area of a PACE organization.</p></div>
<p>Medicare.gov describes PACE as a comprehensive medical and social services program for older adults who need nursing home level care. A team of doctors, nurses, and other professionals coordinates everything the team decides a member needs, including hospital care, home care, dentistry, physical and occupational therapy, nutrition counseling, transportation to the PACE center, and prescription drugs.</p>
<p>Medicare.gov lists four conditions to join. You must be at least 55. You must live in the service area of a PACE organization. Your state must find that you need a nursing home level of care. You must be able to live safely in the community with help from the PACE team. You do not have to already have Medicare or Medicaid. Medicare.gov says eligibility is not limited to people who have either program, although most participants have Medicare, Medicaid, or both.</p>
<p>Cost depends on what coverage you already have. If you have Medicaid, Medicare.gov says you pay no monthly premium for PACE. If you have Medicare but not Medicaid, you pay a monthly premium for the long term care part of the benefit, plus a Part D drug premium. If you have neither program, you can pay the premium yourself. In every case, Medicare.gov says there is no deductible, copayment, or coinsurance for any drug, service, or care the PACE team approves.</p>
<p>PACE is one of two plan types Medicare.gov groups under health plans that lower costs. The other is a Special Needs Plan, a type of [[/guides/medicare-advantage/|Medicare Advantage]] plan for people with Medicare and Medicaid, a long term care need, or a chronic condition. A Special Needs Plan keeps you in a network plan. PACE replaces separate doctor visits with one coordinated team and a day center. Medicare.gov says you will be disenrolled from PACE if you join a different Medicare drug plan while you are in it.</p>
<p>To find out whether a PACE organization serves your area, search for PACE plans in your area on Medicare.gov or call your state Medicaid office. A [[/guides/ship-counseling/|SHIP counselor]] or your state Medicaid agency, listed on your [[/states/|state page]], can also explain whether PACE or a Special Needs Plan fits your situation. This site does not tell you which one to choose.</p>
""",
faqs=[
("Do I need Medicare or Medicaid to join PACE?", "No. Medicare.gov says eligibility for PACE is not limited to people who have Medicare or Medicaid, though most participants have one or both. You can pay the premium yourself if you have neither."),
("Is PACE available in every state?", "No. Medicare.gov says PACE is only available in some states that offer it under Medicaid, and only inside the service area of a specific PACE organization."),
("Will PACE pay for a nursing home stay?", "PACE is built to help you avoid one. Medicare.gov says PACE helps eligible older adults get nursing home level care in the community, though it can cover nursing home care when the PACE team decides it is medically necessary."),
],
sources=[
("PACE", "https://www.medicare.gov/health-drug-plans/health-plans/your-coverage-options/other-medicare-health-plans/PACE"),
("Medicare health plans that lower costs", "https://www.medicare.gov/basics/costs/help/medicare-lower-costs"),
],
related=[("/guides/medicare-and-medicaid/", "Medicare and Medicaid together"), ("/guides/medicare-savings-programs/", "Help paying Medicare costs"), ("/guides/medicare-advantage/", "Medicare Advantage")],
next_reads=[
("/guides/medicare-and-medicaid/", "Medicare and Medicaid together", "/assets/images/household-finances-paperwork-thumb.png", "Hands reviewing financial paperwork with a pen and coffee mug"),
("/guides/medicare-savings-programs/", "Help paying Medicare costs", "/assets/images/household-finances-paperwork-thumb.png", "Hands reviewing financial paperwork with a pen and coffee mug"),
("/guides/medicare-advantage/", "Medicare Advantage", "/assets/images/household-finances-paperwork-thumb.png", "Hands reviewing financial paperwork with a pen and coffee mug"),
("/guides/ship-counseling/", "Free SHIP counseling", "/assets/images/household-finances-paperwork-thumb.png", "Hands reviewing financial paperwork with a pen and coffee mug"),
],
)

add(
path="/guides/medicare-costs-2027/",
title="2027 Medicare Part B Premium Is $209.40",
h1="Medicare costs in 2027",
desc="CMS 2027 Part B premium is $209.40, Part A hospital deductible is $1,776, and the Part D out of pocket cap is $2,400.",
published="2026-11-19",
modified="2026-11-20",
checked="20 Nov 2026",
image=COST_THUMB,
image_alt=COST_THUMB_ALT,
image_caption="Thumbnail for this costs guide.",
compare_html='<aside class="compare" aria-label="Check another year"><p><strong>Need 2026 instead?</strong> The [[/guides/medicare-costs-2026/|2026 Part A and Part B table]] stays posted for this coverage year. Bracket rules are on the [[/guides/irmaa-brackets-2027/|2027 IRMAA page]].</p></aside>',
body="""
<div class="answer"><p><strong>Short version:</strong> On 17 Nov 2026, CMS published the 2027 Part A and Part B amounts. The standard Part B premium is $209.40 a month. The Part A hospital deductible is $1,776 per benefit period. Medicare.gov lists the 2027 Part D out of pocket threshold at $2,400. These are federal figures, not a quote for a private Advantage, Part D, or Medigap plan.</p></div>
<h2>What changed from 2026</h2>
<p>Compared with the [[/guides/medicare-costs-2026/|2026 costs]] page, the CMS fact sheet raises the standard Part B premium by $6.50, from $202.90 to $209.40. The Part B yearly deductible moves from $283 to $292. The Part A hospital deductible moves from $1,736 to $1,776. Day rates for longer hospital stays and skilled nursing coinsurance rise in step with that deductible. About 99 percent of people with Medicare still pay no Part A premium when they have enough work quarters.</p>
<h2>Part A</h2>
<div class="tablewrap"><table class="list"><thead><tr><th scope="col">2027 Part A cost</th><th scope="col">Amount</th></tr></thead><tbody>
<tr><th scope="row">Premium for most people (about 40 quarters of work)</th><td>$0</td></tr>
<tr><th scope="row">Premium with at least 30 quarters</th><td>$328 a month</td></tr>
<tr><th scope="row">Full premium with fewer than 30 quarters</th><td>$597 a month</td></tr>
<tr><th scope="row">Hospital deductible, each benefit period</th><td>$1,776</td></tr>
<tr><th scope="row">Hospital coinsurance, days 61 through 90</th><td>$444 a day</td></tr>
<tr><th scope="row">Lifetime reserve days</th><td>$888 a day</td></tr>
<tr><th scope="row">Skilled nursing facility coinsurance, days 21 through 100</th><td>$222 a day</td></tr>
</tbody></table></div>
<p>Days 1 through 60 in the hospital are $0 after the deductible. CMS and Medicare.gov still charge the hospital deductible once per benefit period, not once per calendar year. There is no limit on how many benefit periods you can have.</p>
<!--NEXT_READS-->
<h2>Part B</h2>
<p>The standard Part B premium is $209.40 a month. The deductible is $292 for the year. After the deductible you usually pay 20 percent of the Medicare approved amount for Part B services. For certain people whose full Medicare ended 36 months after a kidney transplant, the standard premium for immunosuppressive drug coverage only is $125.70 a month in 2027.</p>
<h2>Higher premiums based on income</h2>
<p>CMS says the income related monthly adjustment amounts affect roughly 9 percent of people with Part B. The 2027 full Part B totals use modified adjusted gross income from the tax return Social Security uses. The brackets below are from the CMS 2027 fact sheet.</p>
<div class="tablewrap"><table class="list"><thead><tr><th scope="col">Single income</th><th scope="col">Joint income</th><th scope="col">Part B total premium</th><th scope="col">Part D add on</th></tr></thead><tbody>
<tr><td>$112,000 or less</td><td>$224,000 or less</td><td>$209.40</td><td>$0</td></tr>
<tr><td>Above $112,000 to $141,000</td><td>Above $224,000 to $282,000</td><td>$293.10</td><td>$15.40</td></tr>
<tr><td>Above $141,000 to $177,000</td><td>Above $282,000 to $354,000</td><td>$418.80</td><td>$39.70</td></tr>
<tr><td>Above $177,000 to $212,000</td><td>Above $354,000 to $424,000</td><td>$544.40</td><td>$64.00</td></tr>
<tr><td>Above $212,000 and under $500,000</td><td>Above $424,000 and under $750,000</td><td>$670.00</td><td>$88.30</td></tr>
<tr><td>$500,000 or more</td><td>$750,000 or more</td><td>$711.80</td><td>$96.40</td></tr>
</tbody></table></div>
<p>Married people who lived with a spouse and file a separate return pay a Part B total of $209.40 if income is $112,000 or less, $670.00 if income is above $112,000 and under $388,000, and $711.80 at $388,000 or more. The matching Part D add on amounts are $0, $88.30, and $96.40. The Part D amount is added to the plan premium. It is not the plan premium. The reason the brackets exist, and the separate filer cliff, are explained on the [[/guides/irmaa-brackets-2027/|IRMAA guide]].</p>
<h2>Part D cap and deductible ceiling</h2>
<p>Medicare.gov and the CMS CY 2027 Part D parameters set the annual out of pocket threshold at $2,400 for covered Part D drugs in 2027, up from $2,100 in 2026. After that threshold, you pay $0 for covered Part D drugs for the rest of the calendar year. No Part D plan may use a deductible above $700 in 2027 ($615 was the 2026 ceiling). The national base beneficiary premium Medicare.gov lists for the late enrollment penalty formula is $41.33 in 2027 ($38.99 in 2026). That base is not the premium printed on every plan.</p>
<p>Plan premiums, formularies, and pharmacy prices still come from the plan you compare on Medicare.gov. This page does not name plans. If income is limited, a [[/guides/medicare-savings-programs/|Medicare Savings Program]] or [[/guides/extra-help/|Extra Help]] may lower what you pay. A [[/guides/ship-counseling/|SHIP counselor]] can walk through numbers for your ZIP code without a sales pitch.</p>
""",
faqs=[
("Are these Medicare Advantage plan prices?", "No. Advantage, Part D, and Medigap premiums are set by each company. The figures here are the federal Part A and Part B amounts for 2027, plus the Part D out of pocket threshold and deductible ceiling Medicare.gov and CMS publish."),
("Does everyone pay $209.40 for Part B?", "That is the standard 2027 premium. People with higher incomes pay more, and a late enrollment penalty can add more. Some people pay less because a state Medicare Savings Program pays the premium."),
("What is the 2027 Part D out of pocket cap?", "Medicare.gov lists $2,400 as the 2027 out of pocket threshold for covered Part D drugs. After you reach it, you pay nothing more for those covered drugs for the rest of the year."),
],
sources=[
("2027 Medicare Parts A and B premiums and deductibles", "https://www.cms.gov/newsroom/fact-sheets/2027-medicare-parts-b-premiums-deductibles"),
("What does Medicare cost?", "https://www.medicare.gov/basics/get-started-with-medicare/medicare-basics/what-does-medicare-cost"),
("How much does Medicare drug coverage cost?", "https://www.medicare.gov/health-drug-plans/part-d/basics/costs"),
("Announcement of CY 2027 MA Capitation Rates and Part C and Part D Payment Policies", "https://www.cms.gov/files/document/2027-announcement.pdf"),
],
related=[("/guides/medicare-costs-2026/", "2026 costs"), ("/guides/part-d/", "Part D"), ("/guides/medicare-savings-programs/", "Help paying"), ("/guides/original-medicare/", "Original Medicare")],
next_reads=[
("/guides/medicare-costs-2026/", "2026 Medicare costs table", COST_THUMB_SM, COST_THUMB_ALT),
("/guides/part-d/", "How Part D drug coverage works", COST_THUMB_SM, COST_THUMB_ALT),
("/guides/medicare-savings-programs/", "Medicare Savings Programs", COST_THUMB_SM, COST_THUMB_ALT),
("/guides/irmaa-brackets-2027/", "2027 IRMAA brackets for Part B and Part D", COST_THUMB_SM, COST_THUMB_ALT),
],
)

add(
path="/guides/irmaa-brackets-2027/",
title="2027 IRMAA Starts Above $112,000 Single",
h1="2027 IRMAA brackets for Part B and Part D",
desc="The 2027 IRMAA surcharge starts above $112,000 single or $224,000 joint. CMS Part B and Part D amounts.",
published="2026-11-20",
modified="2026-11-20",
checked="20 Nov 2026",
image=COST_THUMB,
image_alt=COST_THUMB_ALT,
image_caption="Thumbnail for the 2027 IRMAA brackets.",
compare_html='<aside class="compare" aria-label="Check another year"><p><strong>Check the other year before you quote a number.</strong> SSA\'s premiums page, read 20 Nov 2026, still prints the [[/guides/medicare-costs-2026/|2026 chart]] (above $109,000 single). CMS published the [[/guides/medicare-costs-2027/|2027 premium]] and these brackets on 17 Nov 2026. A late signup charge is a different bill: [[/guides/general-enrollment-and-penalties/|the Part B penalty]].</p></aside>',
body="""
<div class="answer"><p><strong>Short version:</strong> In 2027, the income related monthly adjustment (IRMAA) starts when modified adjusted gross income is above $112,000 on an individual return or above $224,000 on a joint return. CMS says it affects roughly 9 percent of people with Part B, and about the same share of people with Part D. The Part B add on is part of the Part B premium. The Part D add on is extra, on top of whatever the drug plan charges. Below $112,000 and $224,000, the Part B total is the standard $209.40 and the Part D add on is $0.</p></div>
<h2>Two official pages, two years</h2>
<p>Do not average them. On 17 Nov 2026, CMS published the 2027 Part B totals and the 2027 Part D add on amounts in its premiums fact sheet. The Social Security page that explains the program, <a href="https://www.ssa.gov/benefits/medicare/medicare-premiums.html" rel="noopener" target="_blank">ssa.gov/benefits/medicare/medicare-premiums.html</a>, still titled its dollar chart "Monthly Medicare Premiums for 2026" when this page was checked on 20 Nov 2026. That chart starts the surcharge above $109,000 single and $218,000 joint, and it uses the 2026 standard premium of $202.90. Until SSA replaces that chart, the 2027 dollars live on the CMS fact sheet, and the method lives on the SSA page.</p>
<p>SSA decides whether you pay it. CMS publishes the brackets. If you have only Part B, SSA says the adjustment applies only to Part B. If you have only drug coverage, it applies only there. If you enroll in the other one later in the same year, and you are already paying an adjustment, SSA says it applies the adjustment to the new coverage without a second letter.</p>
<!--NEXT_READS-->
<h2>2027 full Part B and the Part D add on</h2>
<p>The income is modified adjusted gross income. SSA defines that as adjusted gross income plus tax exempt interest. The rows are the ones CMS printed for people with full Part B. "Total monthly premium" already includes the standard $209.40. The Part D column is only the add on.</p>
<div class="tablewrap"><table class="list"><thead><tr><th scope="col">Single income</th><th scope="col">Joint income</th><th scope="col">Part B IRMAA</th><th scope="col">Part B total</th><th scope="col">Part D add on</th></tr></thead><tbody>
<tr><td>$112,000 or less</td><td>$224,000 or less</td><td>$0.00</td><td>$209.40</td><td>$0.00</td></tr>
<tr><td>Above $112,000 up to $141,000</td><td>Above $224,000 up to $282,000</td><td>$83.70</td><td>$293.10</td><td>$15.40</td></tr>
<tr><td>Above $141,000 up to $177,000</td><td>Above $282,000 up to $354,000</td><td>$209.40</td><td>$418.80</td><td>$39.70</td></tr>
<tr><td>Above $177,000 up to $212,000</td><td>Above $354,000 up to $424,000</td><td>$335.00</td><td>$544.40</td><td>$64.00</td></tr>
<tr><td>Above $212,000 and under $500,000</td><td>Above $424,000 and under $750,000</td><td>$460.60</td><td>$670.00</td><td>$88.30</td></tr>
<tr><td>$500,000 or above</td><td>$750,000 or above</td><td>$502.40</td><td>$711.80</td><td>$96.40</td></tr>
</tbody></table></div>
<p>CMS writes the cut points as "less than or equal to" and "greater than," not as a rounded slogan. One dollar over $112,000 is enough to leave the standard premium. The first step is $83.70 a month for Part B, which is $1,004.40 over a year (12 times $83.70), plus $15.40 a month for Part D, which is $184.80 over a year. Together that first step is $99.10 a month, or $1,189.20 a year, before the drug plan's own premium. Those yearly figures are arithmetic on the CMS monthly amounts. CMS did not print the yearly totals.</p>
<p>Set beside the 2026 chart, the first cliff moved. SSA's 2026 page starts the surcharge above $109,000 single and $218,000 joint, at $81.20 on Part B and $14.50 on Part D. CMS's 2027 page starts it above $112,000 and $224,000, at $83.70 and $15.40. The rest of the 2026 dollar table is on the [[/guides/medicare-costs-2026/|2026 costs]] page, taken from the CMS 2026 fact sheet. The full 2027 Part A and Part B deductible table, without this commentary, is on the [[/guides/medicare-costs-2027/|2027 costs]] page.</p>
<h2>Married, filing separately</h2>
<p>This row is the one people miss. It applies when you lived with your spouse at any time during the tax year and you file a separate return. CMS does not give this group the middle brackets.</p>
<div class="tablewrap"><table class="list"><thead><tr><th scope="col">Separate return income</th><th scope="col">Part B IRMAA</th><th scope="col">Part B total</th><th scope="col">Part D add on</th></tr></thead><tbody>
<tr><td>$112,000 or less</td><td>$0.00</td><td>$209.40</td><td>$0.00</td></tr>
<tr><td>Above $112,000 and under $388,000</td><td>$460.60</td><td>$670.00</td><td>$88.30</td></tr>
<tr><td>$388,000 or above</td><td>$502.40</td><td>$711.80</td><td>$96.40</td></tr>
</tbody></table></div>
<p>Crossing $112,000 on a separate return jumps Part B from $209.40 to $670.00 and adds $88.30 to Part D. That is the same Part B total a joint filer does not reach until income is above $424,000. The filing status is doing more work than the income is.</p>
<h2>What share of the premium that is</h2>
<p>SSA says that for most people the government pays about 75 percent of the Part B premium and the beneficiary pays the remaining 25 percent. At higher income, SSA says you pay 35, 50, 65, 80, or 85 percent of the total Part B cost, depending on the bracket. Those five shares line up with the five surcharge rows. The dollar totals above are CMS's, not a fresh multiplication. Rounding means a percentage of an unpublished total will not always land on the penny CMS printed, so this page does not recompute them.</p>
<p>Part D works differently. Plan premiums vary, so the law uses a base premium to set the add on. SSA says the extra Part D amount is tied to that base, not to the premium on your plan, and that it is withheld from Social Security even if you pay the plan directly. If the add on is larger than the Social Security check, or there is no check, SSA says another federal agency bills you. That agency may be CMS or the Railroad Retirement Board. The 2027 base used in the [[/guides/general-enrollment-and-penalties/|late penalty]] formula is $41.33. The IRMAA add on is not that base, and it is not the plan premium.</p>
<h2>Which tax return, and how to ask for a new one</h2>
<p>SSA uses the most recent federal tax return the IRS provides. On the page checked 20 Nov 2026, the worked description is still about the 2026 premium: generally a return filed in 2025 for tax year 2024, and sometimes a return filed in 2024 for tax year 2023. If SSA used the older year and you filed the newer return, or you did not have to file, SSA says to call or visit a local office so the record can be updated. This page does not invent a sentence SSA has not posted about which return sets the 2027 amount. The pattern on that page is the newest return the IRS has sent.</p>
<p>A life changing event can support a new decision if income went down because of it. SSA's list is: you married, divorced, or your spouse died; you or your spouse stopped working or cut your hours; you or your spouse lost income producing property in a disaster or another event you could not control; an employer's pension was scheduled to stop, end, or reorganize; or you or your spouse got a settlement because an employer closed, went bankrupt, or reorganized. The form SSA names is Form SSA-44. SSA wants documents that match the event, and a signed copy of the return if you filed one for that year. An amended return that changes the income SSA counts also has to be shown, with the IRS receipt.</p>
<p>Disagreeing with the decision is an appeal, not the same form. SSA says the appeal can be filed online, or on Form SSA-561-U2, or through a local office. The phone on that page is 1-800-772-1213 (TTY 1-800-325-0778). If the argument is that the IRS income figure is wrong, SSA says the correction has to happen at the IRS. If SSA added a Part D amount and you do not have drug coverage, SSA says to call 1-800-MEDICARE at 1-800-633-4227 (TTY 1-877-486-2048), because the drug coverage flag comes from CMS.</p>
<p>None of this picks a plan. A [[/guides/ship-counseling/|SHIP counselor]] can read a letter with you. People whose income is low enough for a [[/guides/medicare-savings-programs/|Medicare Savings Program]] are in a different system, one that can pay the Part B premium rather than raise it. Immunosuppressive drug only Part B, for some people whose full Medicare ended 36 months after a kidney transplant, has its own 2027 totals on the same CMS fact sheet. The standard premium for that coverage is $125.70, and the IRMAA dollars match the full Part B add on ($83.70, $209.40, $335.00, $460.60, $502.40), so the totals run from $125.70 to $628.10. The separate return totals for that limited coverage are $125.70, $586.30, and $628.10.</p>
""",
faqs=[
("What income triggers IRMAA in 2027?", "CMS set the first surcharge above $112,000 on an individual return and above $224,000 on a joint return. At or under those amounts, the Part B premium stays $209.40 and the Part D add on is $0."),
("Why does Social Security still show $109,000?", "The SSA premiums page checked 20 Nov 2026 still labels its dollar chart as 2026. CMS published the 2027 brackets on 17 Nov 2026. Use the year printed on the table you are reading."),
("Can I appeal an IRMAA letter?", "SSA says yes. File online, use Form SSA-561-U2, or contact a local office at 1-800-772-1213. A life changing event that cut your income uses Form SSA-44 instead of an appeal. If the IRS income number is wrong, SSA says to fix it with the IRS."),
],
sources=[
("2027 Medicare Parts A and B premiums and deductibles", "https://www.cms.gov/newsroom/fact-sheets/2027-medicare-parts-b-premiums-deductibles"),
("Medicare premiums for higher income beneficiaries", "https://www.ssa.gov/benefits/medicare/medicare-premiums.html"),
("2026 Medicare Parts A and B premiums and deductibles", "https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-deductibles"),
("Avoid late enrollment penalties", "https://www.medicare.gov/basics/costs/medicare-costs/avoid-penalties"),
],
related=[("/guides/medicare-costs-2027/", "2027 costs"), ("/guides/medicare-costs-2026/", "2026 costs"), ("/guides/part-d/", "Part D"), ("/guides/general-enrollment-and-penalties/", "Late penalty"), ("/guides/ship-counseling/", "Free counseling")],
next_reads=[
("/guides/medicare-costs-2027/", "Full 2027 Part A and Part B amounts", COST_THUMB_SM, COST_THUMB_ALT),
("/guides/medicare-costs-2026/", "The 2026 brackets SSA still prints", COST_THUMB_SM, COST_THUMB_ALT),
("/guides/general-enrollment-and-penalties/", "How the Part B late penalty is calculated", "/assets/images/piggy-bank-rain-thumb.png", "Pink ceramic piggy bank and coins on a rainy windowsill"),
("/guides/part-d/", "Part D costs without the income surcharge", COST_THUMB_SM, COST_THUMB_ALT),
],
)
