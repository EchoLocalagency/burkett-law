#!/usr/bin/env python3
"""Fix meta title/description violations from Phase 6 audit.

Approach: swap sitewide title tail from ' — Law Office of Brian Burkett' to
' | Burkett Family Law' (saves 9 chars) — that alone doesn't cover blog
posts, so blog + pillar titles get bespoke shorter titles. Descriptions get
per-page curated ≤160 rewrites.

Also rewrites og:title/og:description so social snippets stay tight.
"""
from __future__ import annotations
import pathlib
import re

ROOT = pathlib.Path("/Users/brianegan/Desktop/burkett-law")

# Curated titles + descriptions per page. Every value ≤60 (title) and ≤160 (desc).
FIXES: dict[str, dict[str, str]] = {
    "about.html": {
        "title": "About Brian Burkett | San Diego Family Law Attorney",
        "description": "Brian Burkett — solo San Diego family law attorney, California Bar No. 220343, 24 years practicing at all four SDSC family-law courthouses.",
    },
    "disclaimer.html": {
        "title": "Attorney Advertising Disclaimer | Burkett Family Law",
        "description": "California Bar attorney advertising disclaimer for the Law Office of Brian Burkett — childcustodyanddivorce.com. Rule 7.1 compliant.",
    },
    "practice-areas/index.html": {
        "title": "San Diego Family Law Practice Areas | Burkett",
        "description": "San Diego family law practice areas: divorce, custody, support, mediation, DVROs, guardianship, and family court navigation. 24 years practicing.",
    },
    "practice-areas/divorce/index.html": {
        "title": "San Diego Divorce Attorney | Burkett Family Law",
        "description": "San Diego divorce lawyer. California dissolution process, six-month waiting period, disclosures, and judgment. 24 years of family-law practice.",
    },
    "practice-areas/child-custody/index.html": {
        "title": "San Diego Child Custody Attorney | Burkett Family Law",
        "description": "San Diego child custody lawyer. Legal and physical custody, parenting plans, and modifications under the California Family Code by Brian Burkett.",
    },
    "practice-areas/child-support/index.html": {
        "title": "San Diego Child Support Attorney | Burkett Family Law",
        "description": "San Diego child support lawyer. Guideline calculation under Family Code § 4055, initial orders, modification, and enforcement by Brian Burkett.",
    },
    "practice-areas/spousal-support/index.html": {
        "title": "San Diego Spousal Support Attorney | Burkett Family Law",
        "description": "San Diego spousal support (alimony) lawyer. Temporary and long-term orders under California Family Code section 4320. 24 years of family-law practice.",
    },
    "practice-areas/mediation/index.html": {
        "title": "San Diego Family Law Mediation Attorney | Burkett",
        "description": "San Diego family law mediation. Private mediation, Family Court Services mediation (Family Code § 3170), representation, and neutral service.",
    },
    "practice-areas/domestic-violence/index.html": {
        "title": "San Diego Domestic Violence Attorney | Burkett",
        "description": "San Diego domestic violence restraining orders under California DVPA (Family Code §§ 6200-6460). EPO, TRO, permanent orders, and custody effects.",
    },
    "practice-areas/guardianship/index.html": {
        "title": "San Diego Guardianship Attorney | Burkett Family Law",
        "description": "San Diego guardianship of minors. Probate guardianship under California Probate Code §§ 1500-1611 and juvenile guardianship in dependency.",
    },
    "practice-areas/family-court/index.html": {
        "title": "San Diego Family Court Attorney | Burkett Family Law",
        "description": "Navigating San Diego family court. RFOs, ex parte, judgments, enforcement, and appeals across all four SDSC family-law courthouses.",
    },
    "blog/index.html": {
        "title": "San Diego Family Law Blog | Burkett Family Law",
        "description": "Plain-language California family law explainers from San Diego attorney Brian Burkett. Divorce, custody, support, mediation, DVROs, and guardianship.",
    },
    "blog/alimony-in-california-a-practical-guide.html": {
        "title": "Alimony in California: A Practical Guide (§ 4320)",
        "description": "How California family court applies the fourteen Family Code section 4320 factors to set long-term spousal support, and what the record needs to look like.",
    },
    "blog/california-community-property-division.html": {
        "title": "California Community Property: How Assets Get Divided",
        "description": "California is a community-property state under Family Code § 760. How the community/separate line is drawn, tracing hybrid assets, and dividing debt.",
    },
    "blog/child-support-in-california-what-attorneys-do.html": {
        "title": "Child Support in California: What an Attorney Adds",
        "description": "California guideline child support is a formula. What an attorney adds around it: income imputation, add-ons, DissoMaster inputs, and modification.",
    },
    "blog/child-visitation-in-california.html": {
        "title": "Child Visitation in California: Plans and Enforcement",
        "description": "How California parenting-time schedules get built, common patterns, and enforcement options when the other parent will not follow the court order.",
    },
    "blog/divorce-mediation-in-san-diego.html": {
        "title": "Divorce Mediation in San Diego: How It Works",
        "description": "How California divorce mediation works, what Evidence Code § 1119 confidentiality covers, and when mediation fits better than litigation.",
    },
    "blog/domestic-violence-restraining-orders-california.html": {
        "title": "Domestic Violence Restraining Orders in California",
        "description": "EPOs, temporary restraining orders, and long-term DVROs under the California DVPA, plus the Family Code § 3044 custody presumption.",
    },
    "blog/guardianship-under-california-probate-code.html": {
        "title": "Guardianship Under the California Probate Code",
        "description": "Probate guardianship of the person or estate of a minor under California Probate Code §§ 1500-1611 and the San Diego Central Courthouse investigation.",
    },
    "blog/how-a-divorce-attorney-navigates-california-process.html": {
        "title": "How a San Diego Divorce Attorney Navigates the Process",
        "description": "The California dissolution process from petition to judgment: the six-month waiting period, disclosures, ATROs, and what an attorney does at each stage.",
    },
    "blog/navigating-san-diego-family-court.html": {
        "title": "Navigating San Diego Family Court: A Room-by-Room Guide",
        "description": "The four San Diego family-law courthouses, Requests for Order, ex parte applications, and what a day of hearing actually looks like.",
    },
    "blog/preliminary-declaration-of-disclosure-california.html": {
        "title": "Preliminary Declaration of Disclosure in California",
        "description": "The FL-140, FL-142, and FL-150 that make up a California Preliminary Declaration of Disclosure, why it exists, and what happens if a spouse hides an asset.",
    },
    "blog/protecting-parental-rights-in-california-custody.html": {
        "title": "Protecting Parental Rights in California Custody Cases",
        "description": "Legal and physical custody, the best-interest standard under Family Code § 3011, and the moves that erode a parent's position in a California case.",
    },
    "blog/spousal-support-in-california-what-to-expect.html": {
        "title": "Spousal Support in California: What to Expect",
        "description": "Temporary spousal support during a California divorce, long-term post-judgment support under Family Code § 4320, and the standards judges apply.",
    },
    "blog/what-a-california-custody-attorney-does.html": {
        "title": "What a California Custody Attorney Actually Does",
        "description": "Family Court Services mediation prep, section 3111 evaluations, minor's counsel, and the day-to-day work of a California custody attorney.",
    },
    "blog/why-hire-a-family-law-attorney-in-california.html": {
        "title": "Why Hire a Family Law Attorney in California",
        "description": "When a California family-law attorney adds value, when a self-help center is enough, and the middle-ground option of unbundled representation.",
    },
    "blog/working-with-a-child-support-attorney.html": {
        "title": "Working With a San Diego Child Support Attorney",
        "description": "The FL-150 Income and Expense Declaration, the DissoMaster print-out, and how a Request for Order becomes an initial California child support order.",
    },
    "thanks.html": {
        # thanks.html is noindex, but populate meta+OG so social previews are clean.
        "description": "Your message reached the Law Office of Brian Burkett. Response within one business day.",
    },
}

# Location pages: title needs 3-5 char trim. Suffix swap does it uniformly.
LOCATION_SUFFIX_OLD = " — Law Office of Brian Burkett"
LOCATION_SUFFIX_NEW = " | Burkett Family Law"


def fix_page(path: pathlib.Path, rel: str) -> tuple[bool, list[str]]:
    text = path.read_text(encoding="utf-8")
    orig = text
    changes: list[str] = []

    curated = FIXES.get(rel)
    if curated:
        if "title" in curated:
            new_title = curated["title"]
            text, n = re.subn(r"<title>.*?</title>", f"<title>{new_title}</title>", text, count=1, flags=re.S)
            if n:
                changes.append(f"title -> {len(new_title)} chars")
            # OG title
            text, n = re.subn(
                r'(<meta[^>]+property=["\']og:title["\'][^>]+content=["\']).*?(["\'])',
                lambda m: m.group(1) + new_title + m.group(2), text, count=1,
            )
            if n:
                changes.append("og:title synced")

        if "description" in curated:
            new_desc = curated["description"]
            # meta description
            text, n = re.subn(
                r'(<meta[^>]+name=["\']description["\'][^>]+content=["\']).*?(["\'])',
                lambda m: m.group(1) + new_desc + m.group(2), text, count=1,
            )
            if n == 0 and rel == "thanks.html":
                # Inject after <meta name="robots"> line for thanks page
                inject = f'\n  <meta name="description" content="{new_desc}">'
                text = text.replace(
                    '<meta name="robots" content="noindex, follow">',
                    '<meta name="robots" content="noindex, follow">' + inject, 1,
                )
                n = 1
            if n:
                changes.append(f"description -> {len(new_desc)} chars")
            # OG description
            text, n = re.subn(
                r'(<meta[^>]+property=["\']og:description["\'][^>]+content=["\']).*?(["\'])',
                lambda m: m.group(1) + new_desc + m.group(2), text, count=1,
            )
            if n:
                changes.append("og:description synced")

    else:
        # Algorithmic path — location pages.
        # Rewrite the trailing branding suffix on <title>, og:title.
        for pat in [
            (r"<title>(.*?)" + re.escape(LOCATION_SUFFIX_OLD) + r"</title>",
             lambda m: f"<title>{m.group(1)}{LOCATION_SUFFIX_NEW}</title>"),
            (r'(<meta[^>]+property=["\']og:title["\'][^>]+content=["\'])(.*?)' + re.escape(LOCATION_SUFFIX_OLD) + r'(["\'])',
             lambda m: m.group(1) + m.group(2) + LOCATION_SUFFIX_NEW + m.group(3)),
        ]:
            text, n = re.subn(pat[0], pat[1], text, count=1, flags=re.S)
            if n:
                changes.append("suffix swapped")

    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True, changes
    return False, changes


def main():
    # Target files: any page in FIXES + every location page (san-diego/**).
    targets = set(FIXES.keys())
    for p in ROOT.glob("san-diego/**/*.html"):
        targets.add(str(p.relative_to(ROOT)))

    count = 0
    for rel in sorted(targets):
        p = ROOT / rel
        if not p.exists():
            print(f"MISS {rel}")
            continue
        changed, changes = fix_page(p, rel)
        if changed:
            count += 1
            print(f"FIX  {rel}: {', '.join(changes)}")
        else:
            print(f"skip {rel}")
    print(f"\nModified {count} files")


if __name__ == "__main__":
    main()
