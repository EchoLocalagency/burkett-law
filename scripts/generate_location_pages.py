#!/usr/bin/env python3
"""One-shot generator for Phase 4 location pages.

Writes 20 pages under /san-diego/[practice]-attorney/[city]/index.html with:
  - Unique per-city + per-practice hero, opening paragraph, courthouse block,
    neighborhood/city context, distance/logistics, and city-specific FAQ.
  - Service + areaServed:City + BreadcrumbList schema (NO LocalBusiness).
  - Author @id -> bio Person, provider @id -> homepage #legalservice.
  - Body-copy link back to the practice pillar.
  - >=600 words visible content, >=4 of 6 differentiation blocks.

Run: python3 scripts/generate_location_pages.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# --- City data ---------------------------------------------------------------
# Each city carries: display name, slug, region, courthouse (name, addr, note),
# neighborhood paragraph, distance/logistics paragraph.

CITIES = {
    "la-jolla": {
        "name": "La Jolla",
        "region": "coastal San Diego",
        "courthouse_name": "San Diego Central Family Courthouse (Downtown)",
        "courthouse_addr": "1100 Union Street, San Diego, CA 92101",
        "courthouse_note": (
            "La Jolla sits inside the City of San Diego, so family-law matters "
            "for La Jolla residents are heard at the Central Courthouse "
            "downtown rather than at Vista, El Cajon, or Chula Vista. Central "
            "handles the bulk of the county's family-law calendar, and "
            "hearings usually get set on tighter tracks than the outer "
            "courthouses because of the volume."
        ),
        "neighborhood": (
            "La Jolla households tend to be high-earning, dual-professional, "
            "and property-heavy — a beach-adjacent primary residence, a "
            "second property, brokerage and retirement accounts, and often "
            "restricted stock or partnership interests from careers in "
            "biotech, medicine, or finance. That asset mix shapes what family "
            "law here actually looks like day to day. The paperwork stays the "
            "same, but the number of pages and the level of documentation "
            "runs long."
        ),
        "distance": (
            "La Jolla is a short drive from my Mission Valley office — "
            "roughly 15 minutes up Interstate 5 without traffic. Most La "
            "Jolla clients meet at Mission Valley rather than at the "
            "Downtown courthouse, and I only bring them to Central for "
            "actual hearings."
        ),
    },
    "chula-vista": {
        "name": "Chula Vista",
        "region": "South County",
        "courthouse_name": "South County Regional Center (Chula Vista Courthouse)",
        "courthouse_addr": "500 Third Avenue, Chula Vista, CA 91910",
        "courthouse_note": (
            "Chula Vista family-law matters are heard at the South County "
            "Regional Center, not at the Central Courthouse downtown. Filing "
            "in the correct courthouse matters — a case for Chula Vista "
            "residents filed downtown can end up transferred, adding weeks "
            "to the calendar. South County has its own bench, its own "
            "calendaring practice, and its own family-court-services queue."
        ),
        "neighborhood": (
            "Chula Vista is the second-largest city in San Diego County and "
            "a hub for cross-border families — households with one "
            "spouse who lives, works, or holds assets in Mexico, or "
            "school-aged children who cross the border for school or family "
            "visits. That reality shapes questions about jurisdiction, "
            "service of process, custody schedules that account for border "
            "crossings, and enforcement of California orders across the "
            "line."
        ),
        "distance": (
            "Chula Vista is about 20 minutes south of my Mission Valley "
            "office on Interstate 5 outside rush hour. The South County "
            "courthouse is another few minutes into town off Third Avenue. "
            "I appear regularly at the South County calendar and can meet "
            "clients either at the office or, for hearings, at the "
            "courthouse."
        ),
    },
    "carlsbad": {
        "name": "Carlsbad",
        "region": "North County coastal",
        "courthouse_name": "North County Regional Center (Vista Family Courthouse)",
        "courthouse_addr": "325 South Melrose Drive, Vista, CA 92081",
        "courthouse_note": (
            "Carlsbad is one of the North County cities heard at the Vista "
            "Family Courthouse rather than at Downtown Central. Vista is a "
            "separate calendar with its own family-court-services intake "
            "and its own bench. A case for a Carlsbad household should be "
            "filed at Vista from the start — filing at Central for "
            "convenience can trigger a transfer motion and slow the case."
        ),
        "neighborhood": (
            "Carlsbad's population is a mix of coastal-real-estate holders, "
            "biotech and life-sciences professionals in the Bressi Ranch "
            "and Palomar Airport corridor, and long-term families around "
            "Aviara and La Costa. Family law here looks like La Jolla in "
            "some ways — substantial property, retirement, and often "
            "equity comp — and looks like classic North County in "
            "others: two-parent working households where the parenting "
            "schedule has to work around commutes down the I-5 corridor."
        ),
        "distance": (
            "Carlsbad is 30 to 35 minutes north of my Mission Valley office "
            "on I-5 outside rush hour. Vista Courthouse is another 10 "
            "minutes east on Highway 78. Most Carlsbad clients prefer to "
            "meet at Mission Valley when possible, and I appear at Vista "
            "for hearings."
        ),
    },
    "escondido": {
        "name": "Escondido",
        "region": "inland North County",
        "courthouse_name": "North County Regional Center (Vista Family Courthouse)",
        "courthouse_addr": "325 South Melrose Drive, Vista, CA 92081",
        "courthouse_note": (
            "Escondido sits inland in North County, and its family-law "
            "matters are heard at the Vista Family Courthouse. Vista's "
            "family-law calendar handles inland cities from Escondido and "
            "San Marcos through coastal cities like Encinitas and Oceanside "
            "— so a Vista hearing calendar mixes very different kinds "
            "of households in one courtroom."
        ),
        "neighborhood": (
            "Escondido is a classic bedroom-community town: long-term "
            "single-family households, families running small businesses "
            "along the Grand Avenue and East Valley Parkway corridors, and "
            "a share of first-generation Spanish-speaking families. Family "
            "law issues here tend to be practical rather than exotic — "
            "a house that has to be refinanced or sold, a small business "
            "that has to be characterized and divided, a parenting "
            "schedule that has to work around shift work and school "
            "pickup."
        ),
        "distance": (
            "Escondido is about 35 to 45 minutes north of my Mission "
            "Valley office on I-15 outside rush hour. Vista Courthouse is "
            "another 15 minutes west on Highway 78. Meetings can happen "
            "either at the office or by phone/video for Escondido clients "
            "who prefer to skip the drive."
        ),
    },
    "oceanside": {
        "name": "Oceanside",
        "region": "North County coastal / Camp Pendleton area",
        "courthouse_name": "North County Regional Center (Vista Family Courthouse)",
        "courthouse_addr": "325 South Melrose Drive, Vista, CA 92081",
        "courthouse_note": (
            "Oceanside family-law matters are heard at the Vista Family "
            "Courthouse, not at Central Downtown. Vista has its own family "
            "court services intake and its own calendaring rhythm. Filing "
            "for Oceanside households at the wrong courthouse can trigger "
            "a transfer and delay hearings by weeks, so the case should be "
            "filed at Vista from the start."
        ),
        "neighborhood": (
            "Oceanside includes the neighborhoods immediately adjacent to "
            "Marine Corps Base Camp Pendleton, and a meaningful share of "
            "Oceanside family-law cases involve an active-duty Marine, a "
            "veteran spouse, or a family whose parenting plan has to "
            "absorb deployment and PCS orders. That reality shapes almost "
            "every part of a case here: the Servicemembers Civil Relief "
            "Act applies to stays and defaults, deployment schedules drive "
            "custody schedules, and military retirement gets divided "
            "under specific federal rules (USFSPA) that most private-sector "
            "retirement plans do not use."
        ),
        "distance": (
            "Oceanside is about 40 to 50 minutes north of my Mission "
            "Valley office on I-5 outside rush hour. Vista Courthouse is "
            "about 15 minutes east on Highway 78. For military clients on "
            "or near Camp Pendleton, I run consultations by phone or video "
            "when a drive to Mission Valley is not workable."
        ),
    },
}

# --- Practice data -----------------------------------------------------------
# For each practice, we carry: display name, slug, pillar path, one-sentence
# service description, and per-city practice-specific paragraphs.

PRACTICES = {
    "divorce-attorney": {
        "name": "Divorce",
        "singular": "divorce",
        "h1_stub": "Divorce Attorney",
        "pillar": "/practice-areas/divorce/",
        "service_type": "Divorce and dissolution of marriage",
        "service_desc": (
            "Representation of residents through California dissolution of "
            "marriage, from initial petition through final judgment, "
            "including uncontested, contested, and higher-asset divorces."
        ),
        # Per-city practice-specific paragraph (>=140 words each, unique).
        "city_context": {
            "la-jolla": (
                "A La Jolla divorce is almost always a property-division case "
                "as much as it is a dissolution. The typical La Jolla file "
                "has a beach-area primary residence with a substantial "
                "mortgage and years of appreciation, one or more brokerage "
                "accounts, retirement plans that include employer stock or "
                "deferred comp, and often a professional practice or a "
                "partnership interest. Characterization work — sorting "
                "what is community versus separate, and what is a "
                "reimbursement claim under Family Code sections 2640 and "
                "2626 — dominates most La Jolla dissolutions. Higher-"
                "asset cases here regularly need a formal real-estate "
                "appraisal, a business valuation, a QDRO drafter for "
                "retirement division, and sometimes a forensic accountant "
                "to trace pre-marital contributions into commingled "
                "accounts. The six-month waiting period under Family Code "
                "section 2339 is the same as anywhere else; the length of "
                "the file is not."
            ),
            "chula-vista": (
                "Chula Vista divorces frequently involve one spouse with "
                "ties across the border — assets held in Mexico, "
                "residency history that runs both sides of the line, or a "
                "spouse who has already returned to Mexico when the "
                "petition is filed. That changes the practical questions in "
                "the case. Service of process on a spouse in Mexico is "
                "handled through the Hague Service Convention and takes "
                "months longer than domestic service; California courts "
                "still keep jurisdiction over the marriage if either spouse "
                "meets the state and county residency requirements under "
                "Family Code section 2320. Property held in Mexico is "
                "characterized under California community-property rules "
                "if it was acquired during the marriage, though enforcing "
                "an order against a Mexican asset is a separate step. "
                "Working with a bilingual client also matters for "
                "declarations of disclosure — the forms are the same, "
                "but the walk-through takes longer."
            ),
            "carlsbad": (
                "Carlsbad divorces often show up as blended files: a house "
                "in the La Costa or Aviara area with substantial equity, "
                "retirement and brokerage accounts, sometimes a share of "
                "equity comp from a Bressi Ranch-corridor employer, and a "
                "parenting-plan question layered on top. The property side "
                "usually needs disciplined characterization — what "
                "portion of the house down-payment came from separate "
                "funds, how a stock plan vested across the date of "
                "separation, what happens to a 401(k) with pre-marital and "
                "marital contributions. The custody side has its own "
                "wrinkle: many Carlsbad parents commute down the I-5 or I-"
                "15 corridor, and workable parenting plans have to account "
                "for pickup times that survive rush hour. I draft plans "
                "for Carlsbad families in specific, enforceable language "
                "so the schedule itself does not create new arguments each "
                "month."
            ),
            "escondido": (
                "Escondido divorces are often the practical middle of the "
                "county caseload: a long-term marriage, a single-family "
                "house with real equity, one or two retirement accounts, "
                "sometimes a small business run out of the house or off "
                "East Valley Parkway. The community-property analysis is "
                "typically cleaner than a La Jolla file but still requires "
                "care, especially on the small-business side — the "
                "business itself is community, but the goodwill component "
                "and the compensation stream have to be characterized "
                "separately. Support is often the bigger practical issue "
                "in an Escondido dissolution than property, because a "
                "single-earner or shift-worker household leaves a real gap "
                "between the parties post-separation. I handle these cases "
                "with attention to what the six-month timeline actually "
                "means for a household still sharing bills."
            ),
            "oceanside": (
                "Oceanside divorces frequently involve a servicemember, a "
                "veteran, or a spouse who works at or around Camp "
                "Pendleton — which adds a layer of federal law on top "
                "of California's community-property rules. Active-duty "
                "servicemembers can invoke the Servicemembers Civil Relief "
                "Act to stay a divorce during deployment; military "
                "retirement is divided under the Uniformed Services Former "
                "Spouses' Protection Act rather than California statute "
                "alone; the Survivor Benefit Plan election has to be made "
                "in the judgment or it is lost. Housing gets its own "
                "wrinkle — base housing, VA loan entitlement, and "
                "eligibility questions after divorce are all separate "
                "issues. The California six-month waiting period still "
                "runs; the paperwork on top of it is longer."
            ),
        },
        # FAQ set per city (3 Q&A, city+practice specific).
        "city_faqs": {
            "la-jolla": [
                ("Which courthouse hears a La Jolla divorce?",
                 "La Jolla is part of the City of San Diego, so divorces filed for La Jolla residents are heard at the Central Courthouse downtown at 1100 Union Street. That courthouse handles the bulk of the county's family-law calendar."),
                ("Do higher-asset La Jolla divorces take longer?",
                 "The six-month waiting period under Family Code section 2339 is the same regardless of asset level. What takes longer in a higher-asset case is the property-division work — characterization, appraisals, QDROs, and sometimes forensic accounting — all of which happens inside the same case."),
                ("Can we finalize without a trial?",
                 "Yes. Most California divorces, La Jolla included, settle in a written Marital Settlement Agreement rather than going to trial. Even higher-asset cases usually resolve after appraisals and characterization work are done, because at that point the numbers are known and the negotiation gets easier."),
            ],
            "chula-vista": [
                ("Which courthouse hears a Chula Vista divorce?",
                 "Chula Vista family-law matters are heard at the South County Regional Center at 500 Third Avenue, not at Downtown Central. Filing at the correct courthouse from the start avoids a transfer motion and weeks of delay."),
                ("What if my spouse lives in Mexico when I file?",
                 "California courts keep jurisdiction over the marriage if the residency requirements under Family Code section 2320 are met (six months in California and three months in San Diego County by either spouse). Service of process on a spouse in Mexico is handled through the Hague Service Convention and takes noticeably longer than domestic service, so we plan for that in the timeline."),
                ("Is property in Mexico divided by a California court?",
                 "Property acquired during the marriage is community property under California law regardless of where it sits, and a California judgment can order how it gets divided. Actually enforcing that division against a Mexican asset is a separate step and sometimes requires local counsel in Mexico."),
            ],
            "carlsbad": [
                ("Which courthouse hears a Carlsbad divorce?",
                 "Carlsbad is a North County city, so divorces are filed and heard at the Vista Family Courthouse at 325 South Melrose Drive, not at Downtown Central."),
                ("Does the six-month waiting period start when I file?",
                 "No — it starts on the date the other spouse is personally served with the petition, not the filing date, under Family Code section 2339. Delayed service delays the date the marriage can be terminated."),
                ("How is equity comp from a Carlsbad-corridor employer divided?",
                 "Restricted stock, options, and RSUs that vest across the date of separation are apportioned between community and separate property using a time rule (Hug or Nelson formula, depending on why the grant was made). Characterization is done grant by grant, not lumped together."),
            ],
            "escondido": [
                ("Which courthouse hears an Escondido divorce?",
                 "Escondido is North County, so its family-law matters are heard at the Vista Family Courthouse at 325 South Melrose Drive rather than at Downtown Central."),
                ("Do I have to appear in Vista if my divorce is uncontested?",
                 "Genuinely uncontested divorces can often be resolved on paperwork alone — no court appearance needed — by filing a stipulated judgment. Contested Requests for Order and any trial happen at Vista."),
                ("How is a small home-based business divided?",
                 "The business itself, to the extent it was built during the marriage, is community property. Its value is set by the standard California approach (asset-based, income-based, or market-based, whichever fits) and the parties can offset it against other assets or one spouse can buy out the other over time."),
            ],
            "oceanside": [
                ("Which courthouse hears an Oceanside divorce?",
                 "Oceanside is North County, so its divorce matters are heard at the Vista Family Courthouse at 325 South Melrose Drive rather than at Downtown Central."),
                ("Can my spouse file for divorce while I am deployed?",
                 "A spouse can file, but under the Servicemembers Civil Relief Act an active-duty servicemember can request a stay of the proceedings for at least 90 days during deployment. Default judgments entered against a deployed servicemember can be reopened."),
                ("How is military retirement divided in a California divorce?",
                 "Military retired pay is divided under the federal Uniformed Services Former Spouses' Protection Act. The marital portion is generally divisible as community property. The Survivor Benefit Plan election has to be made in the judgment itself — it is not automatic."),
            ],
        },
    },
    "child-custody-attorney": {
        "name": "Child Custody",
        "singular": "child custody",
        "h1_stub": "Child Custody Attorney",
        "pillar": "/practice-areas/child-custody/",
        "service_type": "Child custody and visitation representation",
        "service_desc": (
            "Representation of parents in California child-custody matters "
            "— legal and physical custody, parenting-plan drafting, "
            "modifications, and move-away cases — through Family Court "
            "Services and the San Diego Superior Court."
        ),
        "city_context": {
            "la-jolla": (
                "Custody cases for La Jolla families run into their own set "
                "of pressure points. School enrollment questions matter more "
                "here than in most of the county because a lot of La Jolla "
                "children are in specific public schools, private schools, "
                "or specialty programs that a parenting schedule has to be "
                "written around. Extracurricular calendars — club "
                "sports, music, tutoring — often drive the actual "
                "week-to-week schedule more than the label on the order "
                "does. Higher-earner households also see more requests for "
                "731 or 730 evaluators when the case gets contested, "
                "because the parties can absorb the cost and both sides "
                "want a neutral report on the family. California Family "
                "Code section 3011 best-interest factors are the same "
                "here as anywhere else; the file thickness is not."
            ),
            "chula-vista": (
                "Custody cases in Chula Vista often involve a parenting "
                "schedule that has to be workable across the border. When "
                "one parent lives or spends significant time in Tijuana or "
                "further into Baja, or when a child crosses the border for "
                "extended-family time, the parenting plan has to be "
                "specific about transportation, notarized travel consent, "
                "passports, and what happens if a crossing is delayed or "
                "closed. Move-away analysis under Burgess and LaMusga also "
                "shows up more here than in most of the county — not "
                "always as a request to leave California, sometimes as a "
                "request to relocate primary residence to Mexico while "
                "keeping the California court's custody jurisdiction. "
                "These are not standard files, and the parenting plan has "
                "to be drafted with those realities in view."
            ),
            "carlsbad": (
                "Custody cases in Carlsbad often involve two working "
                "parents whose commutes and workplace schedules directly "
                "drive the parenting schedule. A parent commuting down "
                "I-5 to a Sorrento Valley or downtown employer cannot "
                "realistically do a school-morning pickup in Carlsbad "
                "without adjustments the order has to spell out. Long-"
                "weekend and holiday schedules matter as much as the "
                "weekday schedule here because Carlsbad families "
                "frequently travel for extended weekends. I draft "
                "parenting plans for Carlsbad families in specific "
                "language — which parent handles pickup on which "
                "day, how make-up time works, and how the schedule shifts "
                "for school breaks — rather than the vague language "
                "that creates a new argument each month."
            ),
            "escondido": (
                "Custody cases in Escondido often involve shift-worker "
                "households — first responders, healthcare workers, "
                "and hospitality-industry parents on non-standard schedules "
                "— which means the parenting plan has to be built "
                "around a rotating schedule rather than a standard "
                "weekday/weekend split. A workable Escondido parenting "
                "plan usually gets drafted around the actual rotation "
                "rather than treating shifts as an exception. Language "
                "and communication also matter here — Escondido has a "
                "meaningful bilingual population, and Family Court "
                "Services interviews for parents whose primary language is "
                "Spanish are conducted through an interpreter. I prepare "
                "clients for what FCS mediation looks like in that "
                "setting so the interview does not become a bottleneck."
            ),
            "oceanside": (
                "Custody cases in Oceanside frequently involve an active-"
                "duty parent, a deploying parent, or a household absorbing "
                "PCS (permanent change of station) orders. California has "
                "specific rules for these cases under Family Code section "
                "3047 that protect a servicemember from having a custody "
                "order modified against them because of deployment or "
                "temporary duty. The parenting plan itself has to include "
                "a deployment provision — who has the child while the "
                "servicemember is away, how contact happens during "
                "deployment, and how the schedule snaps back on return. I "
                "draft plans for Oceanside military families with those "
                "specific provisions written in, rather than relying on "
                "the parties to work it out later."
            ),
        },
        "city_faqs": {
            "la-jolla": [
                ("Where does a La Jolla custody case get heard?",
                 "La Jolla is part of the City of San Diego, so custody matters are heard at the Central Family Courthouse downtown, not at Vista or Chula Vista. Family Court Services mediation for La Jolla families is handled through the Central intake."),
                ("Do I have to attend Family Court Services mediation?",
                 "Yes. Family Code section 3170 requires parents in a disputed custody or visitation matter to attend a session with San Diego Family Court Services before the judge will hear the request. San Diego is a recommending county, meaning the mediator can send a written recommendation to the judge."),
                ("What is a 730 evaluation and when does it get ordered?",
                 "A 730 evaluation is a full neutral child-custody evaluation by a licensed psychologist under Evidence Code section 730. San Diego judges order them in high-conflict cases, cases with mental-health or substance-abuse allegations, or where the record is contradictory enough that the court needs a professional read on the family."),
            ],
            "chula-vista": [
                ("Where does a Chula Vista custody case get heard?",
                 "Chula Vista custody matters are heard at the South County Regional Center at 500 Third Avenue. Family Court Services mediation for South County families runs out of that same courthouse."),
                ("Can a parent take a child to Mexico for visits?",
                 "Yes, but the parenting order should authorize it in writing. Border crossings for a minor typically require a notarized letter of consent from the non-traveling parent, plus a valid passport for the child. Vague orders create border-crossing problems; specific orders do not."),
                ("What if one parent wants to move to Mexico with the child?",
                 "That is a move-away request under California law and is evaluated under the Burgess/LaMusga standards — reasons for the move, impact on the child, and how the existing parenting plan would have to change. Cross-border move-away cases usually require a full evidentiary hearing."),
            ],
            "carlsbad": [
                ("Where does a Carlsbad custody case get heard?",
                 "Carlsbad custody matters are heard at the Vista Family Courthouse at 325 South Melrose Drive, not at Downtown Central. Family Court Services mediation for North County families is handled through the Vista intake."),
                ("How does a commuting parent handle school pickups?",
                 "Workable parenting plans for commuting parents build in a realistic pickup delegate for school-morning transitions — usually the other parent, sometimes a designated third party — and specify how that gets handled. The order should say who is the point of contact for the school day-to-day."),
                ("Can the parenting plan change for school breaks?",
                 "Yes — in fact a good plan explicitly addresses winter break, spring break, summer, and school holidays with a schedule that differs from the weekly rhythm. That prevents an argument every school break about whose time it is."),
            ],
            "escondido": [
                ("Where does an Escondido custody case get heard?",
                 "Escondido custody matters are heard at the Vista Family Courthouse at 325 South Melrose Drive. Family Court Services mediation for Escondido families runs through the Vista intake."),
                ("Does Family Court Services provide an interpreter?",
                 "Yes. San Diego Family Court Services provides interpreters for Spanish-speaking parents and other language needs. I make sure the interpreter request is in the file well before the appointment so the mediation is not delayed."),
                ("Can shift work be built into the parenting plan?",
                 "Yes. Parenting plans for shift-worker households are typically drafted around the rotation rather than a fixed weekday/weekend schedule. The plan should specify how the rotation is confirmed each month, what happens with unexpected shift changes, and how make-up time works."),
            ],
            "oceanside": [
                ("Where does an Oceanside custody case get heard?",
                 "Oceanside custody matters are heard at the Vista Family Courthouse at 325 South Melrose Drive rather than at Downtown Central."),
                ("Can custody be modified because a parent is deployed?",
                 "No. Family Code section 3047 protects an active-duty servicemember from a custody order being modified against them because of deployment or temporary duty. A temporary order can shift while the servicemember is away, but the underlying order snaps back on return unless a change of circumstances independently justifies modification."),
                ("What should a parenting plan for a military family include?",
                 "It should include a deployment provision — who has physical custody while the servicemember is away, how contact happens during deployment (video calls, letters, care packages), and how the schedule resumes on return. Vague deployment language creates a new dispute the day the orders come in; specific language does not."),
            ],
        },
    },
    "child-support-attorney": {
        "name": "Child Support",
        "singular": "child support",
        "h1_stub": "Child Support Attorney",
        "pillar": "/practice-areas/child-support/",
        "service_type": "Child support representation",
        "service_desc": (
            "Representation of parents in California child-support "
            "matters, including guideline calculations, modifications, "
            "enforcement, and disputes over income imputation, in San "
            "Diego Superior Court."
        ),
        "city_context": {
            "la-jolla": (
                "Child support in La Jolla households often looks different "
                "from a standard guideline calculation because of how "
                "income is structured. When one parent's compensation is a "
                "mix of base salary, bonus, restricted stock, and deferred "
                "comp, the DissoMaster inputs are not obvious — the "
                "guideline runs on a full income figure, but characterizing "
                "vested-during-marriage stock as income and setting a fair "
                "average bonus for calculation purposes both take work. "
                "Above-guideline questions also come up more here: California "
                "law allows the court to depart from the guideline in "
                "extraordinarily high-income cases where guideline would "
                "exceed the child's needs, and that argument is more common "
                "in La Jolla files than anywhere else in the county. The "
                "principle stays the same — support is set to meet the "
                "child's needs, not to redistribute income."
            ),
            "chula-vista": (
                "Child support in Chula Vista frequently runs into "
                "cross-border income issues — a parent who works or "
                "runs a business in Mexico, cash-based income that does "
                "not show up on U.S. tax returns, or a payor spouse who "
                "has already moved back across the line. California law "
                "uses the same DissoMaster guideline regardless of where "
                "income is earned, but proving that income takes different "
                "documents than a W-2 case: tax returns from both "
                "countries, business bank records, and sometimes forensic "
                "reconstruction. Enforcement across the border adds a "
                "second question — California can enforce its order "
                "against California-based assets and income, but pursuing "
                "a Mexican-based payor typically involves separate steps."
            ),
            "carlsbad": (
                "Child support in Carlsbad often involves a payor with "
                "equity compensation from a Bressi Ranch or Palomar-"
                "corridor employer, and the DissoMaster inputs are not "
                "always obvious. Bonus income has to be averaged over a "
                "realistic window; restricted stock is treated as income "
                "when it vests; RSU proceeds are counted the year they are "
                "constructively received. Getting these inputs right at the "
                "start prevents a modification fight later. Timeshare "
                "assumptions also matter more here than most people expect "
                "— a 30% versus 40% timeshare produces meaningfully "
                "different guideline numbers, and Carlsbad parenting plans "
                "with commuter-driven schedules can land at surprising "
                "percentages when calculated out."
            ),
            "escondido": (
                "Child support in Escondido runs into the practical "
                "questions that shape most County caseloads: what to do "
                "with tip income for a hospitality-industry parent, how to "
                "treat self-employment income where the return understates "
                "cash flow, and how to handle a payor who is between jobs. "
                "California courts can impute income to an under-earning "
                "parent under Family Code section 4058 based on ability "
                "and opportunity to work, but imputation requires evidence "
                "— job searches, comparable local wages, health "
                "history. Support calculations for shift-worker households "
                "also have to account for actual timeshare rather than the "
                "label on the order."
            ),
            "oceanside": (
                "Child support in Oceanside frequently involves an active-"
                "duty parent, and military pay is treated differently on "
                "the DissoMaster than civilian pay. Basic Allowance for "
                "Housing (BAH) and Basic Allowance for Subsistence (BAS) "
                "count as income for guideline purposes even though they "
                "are not taxed as wages. Combat pay, hazardous duty pay, "
                "and other special pays are also generally included. "
                "Deployment does not stop support, but it can affect the "
                "timeshare that drives the guideline, and the order "
                "should address what happens on return. Getting the "
                "military-pay side of the guideline right at the outset "
                "avoids repeat trips to court on modification."
            ),
        },
        "city_faqs": {
            "la-jolla": [
                ("How is guideline support calculated for a high-income La Jolla parent?",
                 "California uses the same statewide DissoMaster guideline regardless of income level, and it applies here. In extraordinarily high-income cases the court can depart from the guideline under Family Code section 4057 if guideline would exceed the child's needs, but the burden is on the party asking to depart."),
                ("How does restricted stock or RSU income get treated?",
                 "Restricted stock and RSUs are typically counted as income when they vest, at the value on vest date. Grants that vest across the date of separation get more careful treatment. Bonus income is generally averaged over a representative window rather than annualized off one year."),
                ("Can support be modified when income changes?",
                 "Yes. A child-support order can be modified on a showing of change of circumstances — significant change in either parent's income, a change in the timeshare, or a change in the child's needs. Modifications are filed with a Request for Order."),
            ],
            "chula-vista": [
                ("Where do Chula Vista child-support matters get heard?",
                 "Chula Vista child-support matters are heard at the South County Regional Center at 500 Third Avenue. Department of Child Support Services (DCSS) matters for Chula Vista families are handled through the local DCSS office."),
                ("What if the paying parent lives in Mexico?",
                 "California can still enter and enforce a child-support order. Enforcement against a Mexican-based payor typically involves the Uniform Interstate Family Support Act framework and cooperation with Mexican authorities. It is slower than domestic enforcement, but not impossible."),
                ("How is cash income proved for support purposes?",
                 "California courts can look at bank deposits, lifestyle evidence, and tax returns to reconstruct income when it is understated. In cash-heavy cases the court can impute income under Family Code section 4058 based on ability and opportunity to work."),
            ],
            "carlsbad": [
                ("Where do Carlsbad child-support matters get heard?",
                 "Carlsbad child-support matters are heard at the Vista Family Courthouse at 325 South Melrose Drive. Local DCSS matters run through the North County DCSS office."),
                ("How is bonus and equity comp handled for guideline?",
                 "Bonus income is generally averaged over a representative window rather than treating one year as gospel. Restricted stock and RSUs are treated as income when they vest at the fair market value on vest date. Getting these inputs right avoids a modification fight the next year."),
                ("Does timeshare on the parenting plan affect support?",
                 "Yes — California guideline is driven in part by the percentage of primary physical responsibility. A shift from a 30% to a 40% timeshare produces a meaningfully different guideline number. The order should reflect the actual timeshare, not an averaged one."),
            ],
            "escondido": [
                ("Where do Escondido child-support matters get heard?",
                 "Escondido child-support matters are heard at the Vista Family Courthouse at 325 South Melrose Drive. The North County DCSS office handles local title IV-D cases."),
                ("Can income be imputed to a parent who is not working?",
                 "Yes. Under Family Code section 4058 the court can impute income based on the parent's ability and opportunity to work. Imputation requires evidence — comparable local wages, work history, health history — not a bare assertion that the parent could earn more."),
                ("How is tip income treated?",
                 "Tip income is included in gross income for support purposes. When tips are cash-based and not fully reported, the court can look at bank deposits, credit-card tips, and lifestyle evidence to reconstruct a realistic figure."),
            ],
            "oceanside": [
                ("Where do Oceanside child-support matters get heard?",
                 "Oceanside child-support matters are heard at the Vista Family Courthouse at 325 South Melrose Drive."),
                ("Do BAH and BAS count as income for support?",
                 "Yes. Basic Allowance for Housing and Basic Allowance for Subsistence are counted as income for guideline support purposes even though they are not taxed as wages. Special pays and combat pay are also generally included."),
                ("What happens to support during deployment?",
                 "Support does not stop during deployment. The parenting timeshare may shift while the servicemember is away, which can affect guideline, but the base support obligation continues. On return, the order should specify how the schedule resumes."),
            ],
        },
    },
    "spousal-support-attorney": {
        "name": "Spousal Support",
        "singular": "spousal support",
        "h1_stub": "Spousal Support Attorney",
        "pillar": "/practice-areas/spousal-support/",
        "service_type": "Spousal support representation",
        "service_desc": (
            "Representation of spouses in California temporary and "
            "long-term spousal support matters, including original "
            "orders, modifications, and terminations, in San Diego "
            "Superior Court."
        ),
        "city_context": {
            "la-jolla": (
                "Spousal support in La Jolla dissolutions is typically a "
                "central issue rather than a residual one. The marital "
                "standard of living — the first factor in the Family "
                "Code section 4320 analysis — is often quite high, "
                "and the paying spouse's income is often complex enough "
                "that a straightforward calculation is misleading. Long-"
                "duration marriages (10+ years) get treated as marriages "
                "of long duration under Family Code section 4336, which "
                "means the court retains jurisdiction over support "
                "indefinitely rather than setting a fixed termination "
                "date. Above-guideline earning and unusual asset "
                "structures both matter here, and the 4320 factor "
                "analysis usually gets a full hearing rather than a "
                "guideline-plug approach. The statute is the same as "
                "anywhere in California; the numbers are not."
            ),
            "chula-vista": (
                "Spousal support in Chula Vista dissolutions has its own "
                "practical questions. When one spouse has cross-border "
                "income — a business in Tijuana, cash-based earnings, "
                "or a payor who has already returned to Mexico — the "
                "temporary-support calculation runs on incomplete "
                "documentation and often requires additional discovery to "
                "establish. Long-term support under Family Code section "
                "4320 is set on a full-factor analysis, and the "
                "supported spouse's ability to become self-supporting "
                "under section 4320(l) is evaluated against local labor-"
                "market realities in South County. Cross-border enforcement "
                "is a separate consideration once the order is entered."
            ),
            "carlsbad": (
                "Spousal support in Carlsbad dissolutions is often "
                "shaped by equity compensation and bonus structures. "
                "Temporary support runs on the DissoMaster guideline "
                "using each spouse's income, and getting the equity-comp "
                "and bonus inputs right at the start prevents a fight "
                "later. Long-term support under Family Code section 4320 "
                "looks at the marital standard of living, the supported "
                "spouse's marketable skills, the time and expense to "
                "acquire education or training, and other factors. In a "
                "Carlsbad long-term marriage with a stay-at-home parent "
                "or a spouse who scaled back a career for the family, "
                "the section 4320(l) analysis — becoming self-"
                "supporting within a reasonable period — has real "
                "teeth on how the order gets structured."
            ),
            "escondido": (
                "Spousal support in Escondido dissolutions often plays "
                "out in longer marriages with a single-earner or "
                "primary-earner household. The Family Code section 4320 "
                "factor analysis matters more than the DissoMaster "
                "guideline for long-term support here, because guideline "
                "is only for temporary support during the case. The "
                "supported spouse's marketable skills, the local labor "
                "market in inland North County, and the time realistically "
                "needed to become self-supporting all shape the term of "
                "the order. In an Escondido long-duration marriage the "
                "court retains jurisdiction indefinitely under Family "
                "Code section 4336, which is different from setting a "
                "fixed termination date."
            ),
            "oceanside": (
                "Spousal support in Oceanside dissolutions frequently "
                "involves military pay on the payor side. Basic Allowance "
                "for Housing, Basic Allowance for Subsistence, and other "
                "non-taxed allowances count as income for support "
                "purposes. Deployment does not suspend a support "
                "obligation. The Family Code section 4320 factor "
                "analysis for long-term support in a military family "
                "often includes weight on the supported spouse's career "
                "history — which can be interrupted by repeated PCS "
                "moves, and that history is treated differently than a "
                "career gap in a civilian marriage."
            ),
        },
        "city_faqs": {
            "la-jolla": [
                ("Is spousal support always ordered in a La Jolla divorce?",
                 "No. Support is not automatic. Temporary support during the case is calculated on DissoMaster and is common when there is a real income disparity. Long-term (post-judgment) spousal support is decided under Family Code section 4320 based on a full-factor analysis; the court can order it, deny it, or set a step-down."),
                ("What is a marriage of long duration?",
                 "Under Family Code section 4336, a marriage of ten years or longer is presumed to be one of long duration. In those cases the court retains jurisdiction over spousal support indefinitely, rather than setting a fixed termination date. Support amounts still change based on circumstances."),
                ("Can support be modified when the paying spouse's income drops?",
                 "Yes. Long-term spousal support can be modified on a material change of circumstances, including a real reduction in the paying spouse's income. The change has to be documented, and voluntary underemployment can trigger income imputation under Family Code section 4058."),
            ],
            "chula-vista": [
                ("Where does a Chula Vista spousal-support matter get heard?",
                 "Chula Vista spousal-support matters are heard at the South County Regional Center at 500 Third Avenue as part of the underlying dissolution or separation case."),
                ("What if the paying spouse works in Mexico?",
                 "A California court can still order and enforce spousal support. Enforcement is stronger against California-based income and assets; pursuing a Mexican-based income stream involves separate steps. The court can also impute income under Family Code section 4058 based on ability and opportunity to earn."),
                ("Does the marital standard of living get proven with lifestyle evidence?",
                 "Yes. The marital standard of living under Family Code section 4320(a) is often proven with a combination of tax returns, expense records, bank statements, and lifestyle evidence — how the family actually lived during the marriage, not just what was reported."),
            ],
            "carlsbad": [
                ("Where does a Carlsbad spousal-support matter get heard?",
                 "Carlsbad spousal-support matters are heard at the Vista Family Courthouse at 325 South Melrose Drive as part of the underlying dissolution."),
                ("How is bonus and equity comp handled for support?",
                 "Bonus income and equity comp are counted as income for support purposes. Bonuses are usually averaged over a representative window; RSUs are counted when they vest. Getting the inputs right at the outset avoids a modification fight the next year."),
                ("Can I be required to go back to work?",
                 "Under Family Code section 4320(l) the goal for the supported spouse is to become self-supporting within a reasonable period — generally treated as about half the length of the marriage in marriages under ten years. In long-duration marriages the analysis is more nuanced and the court retains jurisdiction indefinitely."),
            ],
            "escondido": [
                ("Where does an Escondido spousal-support matter get heard?",
                 "Escondido spousal-support matters are heard at the Vista Family Courthouse at 325 South Melrose Drive as part of the underlying dissolution."),
                ("What if my spouse is voluntarily underemployed?",
                 "California courts can impute income to a spouse who is voluntarily earning less than they could — Family Code section 4058 for support-purpose income imputation. Imputation requires evidence of ability and opportunity, not just an assertion."),
                ("Is spousal support tax-deductible for the paying spouse?",
                 "For orders entered after January 1, 2019, spousal support is neither deductible by the payor nor taxable to the recipient under federal law. That change from the pre-2019 treatment affects how the number gets negotiated."),
            ],
            "oceanside": [
                ("Where does an Oceanside spousal-support matter get heard?",
                 "Oceanside spousal-support matters are heard at the Vista Family Courthouse at 325 South Melrose Drive."),
                ("Do BAH and BAS count for spousal support?",
                 "Yes. Basic Allowance for Housing and Basic Allowance for Subsistence are counted as income for support purposes. Other non-taxed military allowances are generally included as well."),
                ("Can support continue after the servicemember retires?",
                 "Long-term spousal support does not automatically end at retirement, but a genuine retirement can be a material change of circumstances that supports a modification request. Timing matters — mandatory retirement age and voluntary early retirement are treated differently."),
            ],
        },
    },
}

# --- City ordering for consistent output ------------------------------------

CITY_ORDER = ["la-jolla", "chula-vista", "carlsbad", "escondido", "oceanside"]
PRACTICE_ORDER = [
    "divorce-attorney",
    "child-custody-attorney",
    "child-support-attorney",
    "spousal-support-attorney",
]

# --- Templates --------------------------------------------------------------

HEADER = """<!doctype html>
<html lang="en-US">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://childcustodyanddivorce.com{path}">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="https://childcustodyanddivorce.com{path}">
  <meta property="og:image" content="https://childcustodyanddivorce.com/assets/img/brian-burkett-headshot.jpg">
  <meta property="og:site_name" content="Law Office of Brian Burkett">
  <meta name="twitter:card" content="summary_large_image">

  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/favicon.ico" sizes="32x32">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">

  <link rel="preload" as="font" type="font/woff2" href="/assets/fonts/Fraunces-VariableFont_SOFT,WONK,opsz,wght.woff2" crossorigin>
  <link rel="preload" as="font" type="font/woff2" href="/assets/fonts/InterVariable.woff2" crossorigin>

  <link rel="stylesheet" href="/assets/css/tokens.css">
  <link rel="stylesheet" href="/assets/css/base.css">
  <link rel="stylesheet" href="/assets/css/header.css">
  <link rel="stylesheet" href="/assets/css/footer.css">
  <link rel="stylesheet" href="/assets/css/bio.css">
  <link rel="stylesheet" href="/assets/css/practice.css">
  <link rel="stylesheet" href="/assets/css/location.css">

  <!-- GA4 slot — Phase 6. -->
  <!-- GA4-BEGIN
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-BURKETT_ID"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-BURKETT_ID');
  </script>
  GA4-END -->

  <!-- @graph: Service (areaServed City, provider @id → homepage #legalservice, author @id → bio Person) + BreadcrumbList.
       NO LocalBusiness on satellite location pages (PITFALLS §6 fake-NAP risk). -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Service",
        "@id": "https://childcustodyanddivorce.com{path}#service",
        "serviceType": "{service_type}",
        "name": "{h1}",
        "description": "{service_desc}",
        "provider": {{ "@id": "https://childcustodyanddivorce.com/#legalservice" }},
        "areaServed": {{
          "@type": "City",
          "name": "{city_name}",
          "containedInPlace": {{
            "@type": "AdministrativeArea",
            "name": "San Diego County, California"
          }}
        }},
        "audience": {{
          "@type": "PeopleAudience",
          "audienceType": "{city_name} residents seeking {practice_singular} representation"
        }},
        "author": {{ "@id": "https://childcustodyanddivorce.com/about.html#brian-burkett" }}
      }},
      {{
        "@type": "BreadcrumbList",
        "@id": "https://childcustodyanddivorce.com{path}#breadcrumb",
        "itemListElement": [
          {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://childcustodyanddivorce.com/" }},
          {{ "@type": "ListItem", "position": 2, "name": "Practice Areas", "item": "https://childcustodyanddivorce.com/practice-areas/" }},
          {{ "@type": "ListItem", "position": 3, "name": "{pillar_name}", "item": "https://childcustodyanddivorce.com{pillar_path}" }},
          {{ "@type": "ListItem", "position": 4, "name": "{city_name}", "item": "https://childcustodyanddivorce.com{path}" }}
        ]
      }}
    ]
  }}
  </script>
</head>

<body>
  <a href="#main" class="skip-link">Skip to main content</a>

  <header role="banner">
<div class="site-header container-xl">
  <a href="/" class="site-header__logo" aria-label="Law Office of Brian Burkett — Home">
    <span class="site-header__logo-mark">BURKETT</span>
    <span class="site-header__logo-divider" aria-hidden="true">|</span>
    <span class="site-header__logo-caption">family law</span>
  </a>

  <button type="button" class="site-header__hamburger" id="nav-toggle"
          aria-label="Open menu" aria-expanded="false" aria-controls="site-nav">
    <span class="site-header__hamburger-bar" aria-hidden="true"></span>
    <span class="site-header__hamburger-bar" aria-hidden="true"></span>
    <span class="site-header__hamburger-bar" aria-hidden="true"></span>
  </button>

  <nav id="site-nav" class="site-header__nav" aria-label="Primary">
    <ul class="site-header__nav-list">
      <li><a href="/practice-areas/">Practice Areas</a></li>
      <li><a href="/about.html">About</a></li>
      <li><a href="/blog/">Blog</a></li>
      <li><a href="/contact.html">Contact</a></li>
    </ul>
  </nav>

  <a href="tel:+16192502683" class="site-header__phone" aria-label="Call the Law Office of Brian Burkett at (619) 250-2683">
    <svg class="site-header__phone-icon" width="16" height="16" viewBox="0 0 24 24" fill="none"
         stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
    </svg>
    <span>(619) 250-2683</span>
  </a>
</div>

<script defer src="/assets/js/nav.js"></script>
  </header>

  <main id="main">
    <article class="practice">
      <div class="container-xl">
        <nav class="practice__breadcrumb" aria-label="Breadcrumb">
          <ol>
            <li><a href="/">Home</a></li>
            <li><a href="/practice-areas/">Practice Areas</a></li>
            <li><a href="{pillar_path}">{pillar_name}</a></li>
            <li aria-current="page">{city_name}</li>
          </ol>
        </nav>
"""

FOOTER = """      </div>
    </article>
  </main>

  <footer role="contentinfo">
<div class="site-footer container-xl">
  <div class="site-footer__grid">

    <div class="site-footer__col site-footer__col--firm">
      <p class="site-footer__wordmark">
        <span class="site-footer__mark">BURKETT</span>
        <span class="site-footer__caption">family law</span>
      </p>
      <address class="site-footer__nap">
        <span class="site-footer__nap-line">591 Camino De La Reina, Suite 821</span>
        <span class="site-footer__nap-line">San Diego, CA 92108</span>
        <a href="tel:+16192502683" class="site-footer__nap-link">(619) 250-2683</a>
      </address>
      <p class="site-footer__hours">Mon-Fri 9am-6pm</p>
    </div>

    <div class="site-footer__col site-footer__col--practice">
      <p class="site-footer__col-heading">Practice Areas</p>
      <ul class="site-footer__col-list">
        <li><a href="/practice-areas/divorce/">Divorce</a></li>
        <li><a href="/practice-areas/child-custody/">Child Custody</a></li>
        <li><a href="/practice-areas/child-support/">Child Support</a></li>
        <li><a href="/practice-areas/spousal-support/">Spousal Support</a></li>
        <li><a href="/practice-areas/mediation/">Mediation</a></li>
        <li><a href="/practice-areas/domestic-violence/">Domestic Violence</a></li>
        <li><a href="/practice-areas/guardianship/">Guardianship</a></li>
        <li><a href="/practice-areas/family-court/">Family Court</a></li>
      </ul>
    </div>

    <div class="site-footer__col site-footer__col--links">
      <p class="site-footer__col-heading">Firm</p>
      <ul class="site-footer__col-list">
        <li><a href="/about.html">About Brian Burkett</a></li>
        <li><a href="/blog/">Blog</a></li>
        <li><a href="/contact.html">Contact</a></li>
        <li><a href="/privacy.html">Privacy Policy</a></li>
        <li><a href="/terms.html">Terms of Use</a></li>
        <li><a href="/disclaimer.html">Attorney Advertising Disclaimer</a></li>
      </ul>
    </div>

    <div class="site-footer__col site-footer__col--credentials">
      <p class="site-footer__col-heading">Credentials</p>
      <ul class="site-footer__col-list">
        <li>Licensed in California only</li>
        <li>State Bar of California, No. 220343 &mdash; admitted 2002</li>
        <li>San Diego family law focus</li>
      </ul>
    </div>

  </div>

  <div class="site-footer__disclaimer">
    <p>
      This website is attorney advertising. Information on this site is not legal advice.
      Contacting the Law Office of Brian Burkett does not create an attorney-client relationship.
      Past results do not guarantee a similar outcome. Licensed in California only.
    </p>
  </div>

  <div class="site-footer__copyright">
    <p>&copy; 2026 Law Office of Brian Burkett. All rights reserved.</p>
  </div>
</div>
  </footer>
</body>
</html>
"""


def build_page(practice_slug, city_slug):
    p = PRACTICES[practice_slug]
    c = CITIES[city_slug]
    path = f"/san-diego/{practice_slug}/{city_slug}/"
    h1 = f"{c['name']} {p['h1_stub']}"
    title = f"{h1} — Law Office of Brian Burkett"
    description = (
        f"{c['name']}, San Diego County {p['singular']} attorney. "
        f"California {p['singular']} representation with 24 years of "
        f"family-law practice. Call (619) 250-2683."
    )

    header = HEADER.format(
        title=title,
        description=description,
        path=path,
        service_type=p["service_type"],
        service_desc=p["service_desc"].replace('"', '\\"'),
        h1=h1,
        city_name=c["name"],
        pillar_name=p["name"],
        pillar_path=p["pillar"],
        practice_singular=p["singular"],
    )

    # Hero + lead (city + practice specific opening)
    lead = (
        f"If you are looking for a {p['singular']} attorney in {c['name']}, "
        f"your case is in {c['region']} of San Diego County and it will be "
        f"heard at {c['courthouse_name'].split(' (')[0]}. My practice is "
        f"family law only, and I take {p['singular']} matters "
        f"across San Diego County — including regularly for {c['name']} "
        f"families. This page walks through what a {p['singular']} case for "
        f"a {c['name']} household typically looks like and how I handle it."
    )

    hero = f"""
        <section class="practice__hero">
          <p class="practice__eyebrow">San Diego County &middot; {p['name']}</p>
          <h1>{h1}</h1>
          <p class="practice__lead">
            {lead}
          </p>
          <p class="practice__byline">
            Written by <a href="/about.html">Brian Burkett</a>, San Diego family-law
            attorney &middot; California Bar No. 220343
          </p>
        </section>
"""

    # Section 1: local court context (courthouse block)
    court = f"""
        <section class="practice__section">
          <h2>Where a {c['name']} {p['singular']} case is heard</h2>
          <p>
            {c['courthouse_note']}
          </p>
          <aside class="loc__courthouse" aria-label="Courthouse for this city">
            <p class="loc__courthouse-label">San Diego Superior Court</p>
            <p class="loc__courthouse-name">{c['courthouse_name']}</p>
            <address class="loc__courthouse-address">
              {c['courthouse_addr']}
            </address>
            <p class="loc__courthouse-note">
              I appear at this courthouse regularly on {p['singular']} matters.
            </p>
          </aside>
        </section>
"""

    # Section 2: neighborhood
    neighborhood = f"""
        <section class="loc__neighborhood">
          <h2>What family law looks like in {c['name']}</h2>
          <p>
            {c['neighborhood']}
          </p>
        </section>
"""

    # Section 3: practice-specific context
    context = f"""
        <section class="practice__section">
          <h2>{p['name']} cases for {c['name']} households</h2>
          <p>
            {p['city_context'][city_slug]}
          </p>
          <p>
            More on the underlying California procedure is on the
            <a href="{p['pillar']}">San Diego {p['name']} Attorney</a> pillar
            page.
          </p>
        </section>
"""

    # Inline CTA
    inline_cta = f"""
        <aside class="practice__inline-cta">
          <p>
            A {p['singular']} case for a {c['name']} family has its own set
            of practical pressure points — the courthouse it lands in,
            the assets or the parenting schedule that shape it, the way it
            actually runs day to day.
          </p>
          <p>
            Call <a href="tel:+16192502683">(619) 250-2683</a> or
            <a href="/contact.html#booking">book a consultation</a> to walk
            through what your situation looks like as a California family-law
            case.
          </p>
        </aside>
"""

    # Section 4: distance/logistics
    distance = f"""
        <section class="practice__section">
          <h2>From Mission Valley to {c['name']}</h2>
          <p>
            {c['distance']}
          </p>
          <aside class="loc__distance" aria-label="Office logistics">
            <p class="loc__distance-label">Meeting logistics</p>
            <p>
              The office is at 591 Camino De La Reina, Suite 821, San Diego,
              CA 92108 — in Mission Valley off Interstate 8 and
              Interstate 163. Initial consultations for {c['name']} clients
              happen in person, by phone, or by video, whichever fits.
            </p>
          </aside>
        </section>
"""

    # Section 5: what I do (solo attorney identity + practice specific)
    what_i_do = f"""
        <section class="practice__section">
          <h2>How I handle {p['singular']} matters for {c['name']} clients</h2>
          <p>
            My practice is solo, which means the attorney at the first
            consultation is the attorney who runs the case from filing
            through final order. I handle {p['singular']} matters for
            {c['name']} families end to end — drafting the pleadings,
            filing at the correct San Diego County courthouse, appearing at
            Requests for Order, running discovery when needed, and
            negotiating settlement or trying the case. If your situation
            falls outside California family law, I will tell you so at the
            first consultation rather than opening a file.
          </p>
          <p>
            I do not overpromise outcomes. What I do is walk through the
            realistic range of what California law provides for a case like
            yours, the procedural spine of how the case will move through
            San Diego Superior Court, and what the file looks like
            calendar-week by calendar-week from here.
          </p>
        </section>
"""

    # FAQ (city + practice specific)
    faq_items = ""
    for q, a in p["city_faqs"][city_slug]:
        faq_items += f"""
          <details class="practice__faq-item">
            <summary>{q}</summary>
            <p>
              {a}
            </p>
          </details>
"""

    faq_section = f"""
        <section class="practice__faq" aria-labelledby="loc-faq">
          <h2 id="loc-faq">Frequently asked questions about {p['singular']} in {c['name']}</h2>
{faq_items}
        </section>
"""

    # Bottom CTA
    cta = f"""
        <section class="practice__cta">
          <h2>Ready to Talk About Your {p['name']} Case?</h2>
          <p>Three ways to reach me. Pick whichever is easiest and I will follow up.</p>
          <div class="practice__cta-trio">
            <a href="tel:+16192502683" class="cta-card cta-card--phone">
              <p class="cta-card__label">Call Directly</p>
              <p class="cta-card__value">(619) 250-2683</p>
              <p class="cta-card__note">Mon-Fri 9am-6pm</p>
            </a>
            <a href="/contact.html#booking" class="cta-card cta-card--calendar">
              <p class="cta-card__label">Book a Consultation</p>
              <p class="cta-card__value">Schedule online</p>
              <p class="cta-card__note">15-minute intake call</p>
            </a>
            <a href="/contact.html#form" class="cta-card cta-card--form">
              <p class="cta-card__label">Send a Message</p>
              <p class="cta-card__value">Contact form</p>
              <p class="cta-card__note">I respond within one business day</p>
            </a>
          </div>
          <p class="practice__cta-disclaimer">
            Contacting the Law Office of Brian Burkett does not create an
            attorney-client relationship. Please do not include confidential or
            sensitive information in your first message.
          </p>
        </section>
"""

    footer = FOOTER.format(
        pillar_path=p["pillar"],
        pillar_name=p["name"],
        city_name=c["name"],
    )

    body = (
        header
        + hero
        + court
        + neighborhood
        + context
        + inline_cta
        + distance
        + what_i_do
        + faq_section
        + cta
        + footer
    )
    return body


def main():
    written = []
    for pslug in PRACTICE_ORDER:
        for cslug in CITY_ORDER:
            out = ROOT / "san-diego" / pslug / cslug / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            html = build_page(pslug, cslug)
            out.write_text(html, encoding="utf-8")
            written.append(str(out))
    print(f"Wrote {len(written)} pages:")
    for w in written:
        print(f"  {w}")


if __name__ == "__main__":
    main()
