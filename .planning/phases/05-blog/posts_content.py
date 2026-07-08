"""Post content data for build_posts.py.

Each entry: slug, category, published (ISO), published_pretty, title, h1,
description, breadcrumb_short, body_html, related (list of related-post dicts).

Copy is first-person from Burkett's perspective, California-jurisdiction-specific,
descriptive of statutory procedure. No fabricated numbers, no case counts,
no guarantee language. Passes lint_cal_bar.py + validate_fabrication.py.
"""

POSTS = []

# ---------------------------------------------------------------------------
# 1 — Divorce Mediation in San Diego
# ---------------------------------------------------------------------------
POSTS.append({
    "slug": "divorce-mediation-in-san-diego",
    "category": "Mediation",
    "published": "2024-05-14",
    "published_pretty": "May 14, 2024",
    "title": "Divorce Mediation in San Diego: How the Process Works Under California Law",
    "h1": "Divorce Mediation in San Diego: How the Process Works Under California Law",
    "description": "How California divorce mediation works, what Evidence Code section 1119 confidentiality covers, and when mediation is a better fit than litigation. From a San Diego family-law attorney.",
    "breadcrumb_short": "Divorce Mediation",
    "body_html": """
          <p>
            Most couples I meet at intake want the same two things: they want the
            divorce to end, and they want to get through it without doing
            long-term damage to the co-parenting relationship or the finances.
            Mediation, done well, can deliver both. Done poorly, or done in the
            wrong case, it can turn a manageable dispute into a stalled one.
          </p>
          <p>
            This post walks through what mediation actually looks like in a
            California divorce, how the San Diego Family Court Services process
            differs from private mediation, and how I think about whether
            mediation is the right first move in a case.
          </p>

          <h2>What "mediation" means in a California divorce</h2>
          <p>
            Mediation is a structured settlement conversation with a neutral
            third party. It is not court. There is no judge, no ruling, and no
            binding order unless the parties themselves sign a written
            agreement at the end. What makes mediation work is confidentiality:
            under California Evidence Code section 1119, statements made in a
            mediation are generally inadmissible in later court proceedings,
            which is the reason both sides can talk candidly about what they
            actually want.
          </p>
          <p>
            California family court sees two very different mediation contexts,
            and it helps to know which one is in front of you. The first is
            private mediation &mdash; the parties (usually with counsel) hire
            a neutral to facilitate. The second is court-ordered custody
            mediation through <strong>Family Court Services</strong>, which
            handles disputes about children under Family Code section 3170
            before any contested custody hearing.
          </p>

          <h2>Private mediation: the format</h2>
          <p>
            Private mediation is entirely voluntary. Either spouse can suggest
            it, or it can be scheduled through counsel. The neutral is usually
            a family-law attorney or retired judicial officer. Sessions are
            typically half-day or full-day blocks. The mediator meets with the
            parties together, then more often shuttles between separate rooms
            (a "caucus" model) so each side can talk through options without
            reactive push-back.
          </p>
          <p>
            The end product is a written settlement, either a term sheet the
            attorneys draft into a Marital Settlement Agreement afterward, or a
            more complete stipulated MSA the mediator prepares. That MSA gets
            attached to a proposed judgment (FL-180) and submitted to San Diego
            Superior Court for entry. The court signs the judgment because the
            parties agreed &mdash; the mediation itself has no independent
            power.
          </p>

          <h2>San Diego Family Court Services mediation</h2>
          <p>
            When a custody issue is set for a hearing in San Diego, the court
            almost always routes the parties through Family Court Services
            (FCS) mediation first. FCS is a court-attached department, and the
            mediators are trained counselors. It is not private, it is not
            optional, and in San Diego County the FCS process is
            recommending: the mediator can make a written recommendation to
            the judge if the parents cannot reach an agreement.
          </p>
          <p>
            That last point matters. A parent who walks into FCS thinking of
            it as an informal chat can end up with a written recommendation on
            the judge's desk that they have not read and did not shape. I
            prepare clients for FCS the same way I prepare them for a hearing.
          </p>

          <h2>Where mediation fits (and where it does not)</h2>
          <p>
            Mediation is worth trying first in a lot of San Diego divorce
            cases: two employed spouses, straightforward property, kids where
            neither parent is opposed to reasonable time with the other. The
            fastest, least expensive California divorce I see is a mediated
            settlement in the first ninety days of the case, filed as an
            uncontested judgment.
          </p>
          <p>
            Mediation is not the right first move in every case. Cases with
            active domestic-violence issues need the safety architecture of a
            <a href="/practice-areas/domestic-violence/">restraining
            order</a> first, and often need any custody discussion to happen
            in FCS or in court, not in a private room. Cases where one spouse
            controls the finances and the other spouse has not seen a tax
            return in years need <a href="/blog/preliminary-declaration-of-disclosure-california.html">formal
            disclosure</a> before mediation can produce a fair agreement.
            Cases where one side is not negotiating in good faith &mdash;
            hiding assets, missing sessions, showing up unprepared &mdash;
            can waste months in mediation that a Request for Order would
            resolve in weeks.
          </p>

          <aside class="blog-post__inline-cta">
            <p>
              If you are trying to figure out whether mediation makes sense in
              your case, that assessment is what a first consultation is for.
            </p>
            <p>
              Call <a href="tel:+16192502683">(619) 250-2683</a> or
              <a href="/contact.html#booking">book a consultation</a> and we
              can walk through your facts.
            </p>
          </aside>

          <h2>What a mediation-focused attorney does</h2>
          <p>
            Even in mediation, having your own attorney matters. My role in a
            mediated case looks different from my role in litigation, but it
            is not smaller. Before mediation, I review the disclosures, run
            California guideline support numbers so we know what a court
            would order as a baseline, and identify the two or three issues
            that are actually going to drive the case. During mediation, I
            attend as counsel, which means I am with you in the caucus and
            can pressure-test proposals in real time. After mediation, I turn
            the term sheet into a judgment package that the court will
            actually enter.
          </p>
          <p>
            Where I am the neutral rather than counsel, the format is different
            &mdash; I represent neither spouse, I do not give either party
            legal advice, and I recommend that each party have an independent
            attorney review any written agreement before signing. Whether I
            am serving as neutral or as counsel is set at the outset and
            documented in writing.
          </p>

          <h2>What a mediated settlement covers</h2>
          <p>
            A California mediated divorce settlement is not a limited
            document. To be entered as a judgment, it has to resolve every
            issue in the case: dissolution of the marriage, division of
            community property and debt, characterization of separate
            property, legal and physical custody, a parenting-time schedule,
            child support, spousal support (or a knowing waiver), health
            insurance, life insurance, tax filing status through year of
            separation, and attorneys' fees.
          </p>
          <p>
            Any issue left unresolved has to be argued to the court later.
            The point of a good mediated settlement is that the parties leave
            with a complete package they can live with, not with three
            resolved issues and four still hanging.
          </p>

          <h2>Timing and cost</h2>
          <p>
            A mediated California divorce still has to observe the six-month
            waiting period under Family Code section 2339, which runs from
            the date of service on the respondent. So the shortest possible
            timeline from filing to judgment is roughly six months regardless
            of how quickly the parties settle. What mediation cuts is the
            middle: the discovery motions, the contested Requests for Order,
            the trial preparation. I do not quote average savings figures for
            reasons the California Rules of Professional Conduct take
            seriously, but I will tell you at the first meeting what your
            case looks like as a mediated matter and what it looks like as a
            litigated one.
          </p>

          <h2>Ready to talk it through</h2>
          <p>
            Mediation is a tool, not an outcome. It is worth trying in most
            California divorces where both spouses are willing to negotiate
            in good faith. It is not worth trying &mdash; or is worth
            deferring &mdash; when one side is missing the information they
            need to negotiate on level ground.
          </p>
          <p>
            If you want to think through whether mediation is a fit in your
            case, I am happy to have that conversation. You can reach me at
            <a href="tel:+16192502683">(619) 250-2683</a> or through the
            <a href="/contact.html#form">contact form</a>. I read every
            message and I respond within one business day.
          </p>
""",
    "related": [
        {"url": "/practice-areas/mediation/", "category": "Practice Area", "title": "Divorce Mediation (Practice Area)"},
        {"url": "/blog/how-a-divorce-attorney-navigates-california-process.html", "category": "Divorce", "title": "How a San Diego Divorce Attorney Navigates the California Dissolution Process"},
        {"url": "/blog/domestic-violence-restraining-orders-california.html", "category": "Domestic Violence", "title": "Domestic Violence Restraining Orders in California: How the DVPA Works"},
    ],
})

# ---------------------------------------------------------------------------
# 2 — How a Divorce Attorney Navigates the California Process
# ---------------------------------------------------------------------------
POSTS.append({
    "slug": "how-a-divorce-attorney-navigates-california-process",
    "category": "Divorce",
    "published": "2024-06-12",
    "published_pretty": "June 12, 2024",
    "title": "How a San Diego Divorce Attorney Navigates the California Dissolution Process",
    "h1": "How a San Diego Divorce Attorney Navigates the California Dissolution Process",
    "description": "The California dissolution process from petition to judgment, the six-month waiting period, disclosures, ATROs, and what an attorney is doing at each stage. Written by San Diego family lawyer Brian Burkett.",
    "breadcrumb_short": "How a Divorce Attorney Navigates the Process",
    "body_html": """
          <p>
            California divorce is a procedure-driven case. There is a fixed
            path from petition to judgment, a mandatory six-month waiting
            period, and a stack of forms the court expects to see in a
            particular order. Most of the value an attorney adds is not
            oratory in a courtroom &mdash; it is knowing where the case is on
            that path, what has to happen next, and what has to be lined up
            before the next hearing.
          </p>
          <p>
            This post walks through the process the way I would walk through
            it with a client at intake, so you can see where an attorney
            attaches at each stage.
          </p>

          <h2>Before you file: the strategic setup</h2>
          <p>
            The most consequential decisions in a California divorce often
            get made before anything is filed. Which spouse files first
            rarely changes the outcome on property (California is a
            community-property state regardless of who filed), but it can
            affect timing on custody, temporary support, and which county
            hears the case.
          </p>
          <p>
            I spend the first meeting understanding the household: dates of
            marriage and separation, whether there are kids and their
            schools, whether either spouse works out of state, whether real
            estate is titled jointly or separately, whether there is a
            business, and whether any restraining-order or safety issues
            need to be addressed first. If a house sale, a job change, or a
            move is imminent, that changes filing strategy.
          </p>

          <h2>Filing and service &mdash; starting the six-month clock</h2>
          <p>
            California divorce begins with a Petition for Dissolution (FL-100)
            and a Summons (FL-110). Once the petition is filed, the summons
            has to be personally served on the other spouse. That service is
            what starts the mandatory six-month waiting period under Family
            Code section 2339 &mdash; the earliest date the marriage itself
            can be legally terminated.
          </p>
          <p>
            Filing also triggers California's <strong>automatic temporary
            restraining orders</strong> (ATROs), which appear on the back of
            the summons. ATROs restrict both spouses from things like
            selling or transferring assets, cashing out or borrowing against
            insurance, taking kids out of state without written agreement or
            a court order, and changing beneficiaries. I walk clients through
            ATROs at the first meeting because inadvertent violations
            (changing an insurance beneficiary, transferring a car to a
            family member) can complicate the case even if they were done
            for reasons that have nothing to do with the divorce.
          </p>

          <h2>Disclosures: the financial spine of the case</h2>
          <p>
            California divorce is built on financial disclosure. Both spouses
            have to serve a <a href="/blog/preliminary-declaration-of-disclosure-california.html">Preliminary
            Declaration of Disclosure</a> early in the case, covering every
            asset and debt each spouse knows about, along with income and
            expenses. A Final Declaration of Disclosure comes before
            judgment, though the parties can waive it by mutual agreement.
          </p>
          <p>
            The disclosure forms are FL-140 (declaration), FL-142 (schedule
            of assets and debts) or FL-160 (property declaration), and
            FL-150 (income and expense declaration). If a spouse's income is
            complicated &mdash; self-employed, commissioned, seasonal,
            equity-comp &mdash; the FL-150 becomes a significant piece of
            drafting work, not a fill-in-the-blank.
          </p>

          <h2>Requests for Order &mdash; getting temporary orders in place</h2>
          <p>
            While the case is pending, most families cannot wait six months
            to figure out custody or support. That is what a <strong>Request
            for Order</strong> (FL-300) is for. An RFO asks the court for
            temporary orders on any issue that needs to be addressed now:
            custody and visitation, temporary child support, temporary
            spousal support, use of the family residence, attorneys' fees,
            and orders about specific assets.
          </p>
          <p>
            The RFO packet includes the request itself, a supporting
            declaration, and (for support requests) an FL-150. It gets
            served on the other spouse with a specific hearing date. That
            hearing is where temporary orders get made. In an urgent
            situation, an ex parte application asks the court to hear the
            issue on shortened notice.
          </p>

          <aside class="blog-post__inline-cta">
            <p>
              Timing on Requests for Order matters. If temporary support is
              set at the wrong number for six months, that money is hard to
              claw back. If a custody schedule gets baseline-established that
              is not workable, changing it later requires a change in
              circumstances.
            </p>
            <p>
              Call <a href="tel:+16192502683">(619) 250-2683</a> if you want
              to walk through your case before the first RFO gets filed.
            </p>
          </aside>

          <h2>Discovery and characterization</h2>
          <p>
            In contested cases, discovery goes beyond the disclosures.
            Standard California discovery devices &mdash; Form
            Interrogatories, Special Interrogatories, Requests for
            Production, Requests for Admission, Depositions &mdash; are all
            available. Higher-asset cases often need business appraisals,
            forensic accounting, and subpoenas to third-party record
            custodians.
          </p>
          <p>
            The other big substantive question at this stage is
            characterization: which assets are community and which are
            separate. California is a community-property state under Family
            Code section 760, and the general rule is that everything
            acquired during marriage from the labor of either spouse is
            community. Property owned before marriage, or received during
            marriage by gift or inheritance, is separate. But hybrid assets
            &mdash; a house bought before marriage that gets paid down with
            marital income, a retirement account with both pre-marital and
            marital contributions, a business started before marriage and
            grown during it &mdash; require tracing analysis to divide
            correctly. I cover
            <a href="/blog/california-community-property-division.html">community
            property in more depth in a separate post</a>.
          </p>

          <h2>Settlement or trial</h2>
          <p>
            Most California divorces end in a Marital Settlement Agreement
            that both spouses sign. The MSA is attached to a proposed
            judgment (FL-180) and submitted to the court. Settlement can
            happen in a mediation session, at a settlement conference the
            court schedules, in email exchanges between counsel, or on the
            courthouse steps the morning of trial. What matters is that the
            agreement resolves every issue in the case.
          </p>
          <p>
            When settlement is not possible, the case goes to trial. Family
            law trials in San Diego Superior Court are bench trials &mdash;
            the judge decides, no jury. The judge issues a Statement of
            Decision, which becomes the judgment. Trial is expensive and
            unpredictable, and I treat it as the option we take when
            negotiation has genuinely failed, not as the default.
          </p>

          <h2>Judgment and after</h2>
          <p>
            Entry of judgment ends the case. It terminates the marriage
            (subject to the six-month clock), divides the property,
            establishes support, and sets a custody and visitation order.
            Post-judgment, either party can bring a motion to modify support
            or custody on a change of circumstances, and enforcement
            mechanisms (wage assignments, contempt, requests for order to
            compel compliance) are available if the other side stops
            following the judgment.
          </p>

          <h2>What an attorney is actually doing</h2>
          <p>
            Reduced to its parts, what I do on a California divorce is:
            (1) map the case at intake so we know what stages it will run
            through and where the pressure points are, (2) draft the pleadings
            so the case is framed correctly from the first filing, (3) get
            timely temporary orders in place through Requests for Order,
            (4) build a complete and accurate financial picture through the
            disclosures and any discovery, (5) negotiate a settlement that
            resolves every issue, and (6) if settlement fails, try the case.
            At each stage, I am also translating the process into plain
            language for the client so they can make good decisions.
          </p>

          <p>
            If you want to talk through where your case is on that path, you
            can reach me at <a href="tel:+16192502683">(619) 250-2683</a> or
            through the <a href="/contact.html#form">contact form</a>. I
            handle divorce matters at all four San Diego County family-law
            courthouses.
          </p>
""",
    "related": [
        {"url": "/practice-areas/divorce/", "category": "Practice Area", "title": "San Diego Divorce (Practice Area)"},
        {"url": "/blog/california-community-property-division.html", "category": "Divorce", "title": "California Community Property: How Marital Assets and Debts Get Divided"},
        {"url": "/blog/preliminary-declaration-of-disclosure-california.html", "category": "Divorce", "title": "The Preliminary Declaration of Disclosure in a California Divorce"},
    ],
})

# ---------------------------------------------------------------------------
# 3 — California Community Property Division
# ---------------------------------------------------------------------------
POSTS.append({
    "slug": "california-community-property-division",
    "category": "Divorce",
    "published": "2024-07-09",
    "published_pretty": "July 9, 2024",
    "title": "California Community Property: How Marital Assets and Debts Get Divided",
    "h1": "California Community Property: How Marital Assets and Debts Get Divided",
    "description": "California is a community-property state under Family Code section 760. How the community/separate line is drawn, how hybrid assets get traced, and how debt gets divided in a San Diego divorce.",
    "breadcrumb_short": "California Community Property",
    "body_html": """
          <p>
            "California is a community-property state" is the sentence I say
            most often at intake, and it is also the sentence that opens the
            most follow-up questions. What is community. What is separate.
            What happens to the house we bought before we married but have
            been paying off together. What about the retirement account. What
            about the credit card debt in his name.
          </p>
          <p>
            This post is a plain-language walk through California
            community-property rules for divorce. It is descriptive, not
            legal advice for your specific case &mdash; characterization
            is often fact-heavy and small details change the analysis.
          </p>

          <h2>The general rule</h2>
          <p>
            Under Family Code section 760, everything acquired by either
            spouse during the marriage is presumed to be community property.
            That includes wages, salary, retirement contributions, real
            estate purchased with marital income, business interests built
            during the marriage, and everyday household assets. Community
            property is divided equally between the spouses at divorce.
          </p>
          <p>
            Property that is not community is separate. Under Family Code
            section 770, separate property is anything a spouse owned
            before marriage, anything received during marriage by gift or
            inheritance, and the rents, issues, and profits of separate
            property. Separate property stays with the spouse who owns it.
          </p>
          <p>
            The date of separation matters. Property acquired after the
            date of separation from earnings or accumulations of either
            spouse is that spouse's separate property. Which is why the
            date of separation is often litigated when the numbers are
            large &mdash; a bonus paid three months after separation for
            work performed six months before separation is community, but
            a bonus paid three months after separation for work performed
            two months after separation is separate.
          </p>

          <h2>Community property in practice</h2>
          <p>
            In a typical San Diego divorce, the community-property inventory
            includes:
          </p>
          <ul>
            <li>Real estate purchased during the marriage from marital
                income</li>
            <li>Bank and brokerage accounts funded during the marriage</li>
            <li>Retirement accounts (401(k), IRA, pension) to the extent
                contributions were made during the marriage</li>
            <li>Vehicles, furniture, jewelry, and household goods acquired
                during marriage</li>
            <li>Business interests to the extent value was built during
                marriage</li>
            <li>Stock options and RSUs (vesting analysis matters &mdash; the
                <em>Marriage of Hug</em> and <em>Marriage of Nelson</em> time
                rules divide these depending on grant and vesting dates)</li>
            <li>Debts incurred during the marriage for community
                purposes</li>
          </ul>

          <h2>Separate property in practice</h2>
          <p>
            Separate property, by contrast, generally includes:
          </p>
          <ul>
            <li>Real estate a spouse owned before marriage (subject to
                reimbursement rules if community funds paid it down &mdash;
                more below)</li>
            <li>Bank accounts a spouse had before marriage, if they can be
                traced and were not commingled beyond recognition</li>
            <li>Retirement account balances that predate the marriage</li>
            <li>Inheritances and gifts, whether received before or during
                the marriage</li>
            <li>Personal injury settlements (with some California-specific
                rules that split economic and non-economic damages)</li>
            <li>Debts incurred by a spouse before marriage or for separate
                purposes</li>
          </ul>

          <h2>Hybrid assets: where cases actually get argued</h2>
          <p>
            The straightforward cases divide themselves. What takes time,
            and is usually where an attorney adds real value, is the hybrid
            asset &mdash; an asset that has both community and separate
            components mixed together.
          </p>

          <h3>The house bought before marriage</h3>
          <p>
            One of the most common hybrid assets is a house one spouse
            bought before marriage that both spouses paid off during the
            marriage. Under a line of California cases going back to
            <em>Marriage of Moore</em> and clarified in <em>Marriage of
            Marsden</em>, the community gets a pro-rata share of the
            appreciation attributable to community payments on the mortgage
            principal. The Moore/Marsden calculation traces the amount of
            community principal reduction, applies it to the appreciation
            during marriage, and gives the community a proportional
            interest. It is arithmetic-heavy, and it is where I frequently
            bring in a forensic accountant when the numbers matter.
          </p>

          <h3>The retirement account with a pre-marital balance</h3>
          <p>
            A 401(k) or IRA with contributions both before and during the
            marriage is divided using a "time rule" (for defined-benefit
            pensions) or a direct tracing (for defined-contribution
            accounts). The pre-marital balance and its earnings stay
            separate; the marital contributions and their earnings are
            community. A Qualified Domestic Relations Order (QDRO) is
            usually needed to divide qualified retirement accounts
            without triggering tax and penalty.
          </p>

          <h3>The business started before marriage and grown during it</h3>
          <p>
            A business one spouse owned before marriage but grew during the
            marriage requires a Van Camp or Pereira analysis (from
            California cases of the same name). Van Camp values the spouse's
            services at reasonable market compensation and treats the rest
            of the growth as return on separate capital. Pereira applies a
            reasonable rate of return to the separate capital and treats the
            excess as community. Which framework applies depends on where
            the business's growth actually came from.
          </p>

          <aside class="blog-post__inline-cta">
            <p>
              Hybrid-asset cases are usually where the difference between
              "we handled this ourselves" and "we hired an attorney" shows
              up in dollars.
            </p>
            <p>
              Call <a href="tel:+16192502683">(619) 250-2683</a> to walk
              through your asset picture at a first meeting.
            </p>
          </aside>

          <h2>Reimbursements under Family Code section 2640</h2>
          <p>
            California has a specific statute, Family Code section 2640,
            that lets a spouse recover their separate-property
            contributions to community property. A common example: one
            spouse used separate savings as a down payment on a house
            titled jointly during the marriage. At divorce, that spouse can
            claim a 2640 reimbursement for the down payment (without
            interest, and capped at the value of the property) before the
            community equity is divided. 2640 rights can be waived only in
            a written signed statement, and courts read that requirement
            strictly.
          </p>

          <h2>How debt gets divided</h2>
          <p>
            Debt follows similar characterization rules. Debt incurred
            during marriage is presumed to be community, and is divided
            equally at divorce. Debt incurred before marriage is separate.
            Debt incurred during marriage for a spouse's non-community
            purpose (a girlfriend's rent, a personal legal problem) can
            sometimes be characterized as separate under Family Code
            sections 2621 through 2627. The court can allocate
            community debt to one spouse if the other spouse assumes a
            corresponding community asset, so the net division stays
            equal.
          </p>

          <h2>What happens after characterization</h2>
          <p>
            Once assets and debts have been characterized, the court (or
            the parties in a settlement) has to divide them equally in
            value. California does not require every single asset to be
            split down the middle &mdash; the equal division applies to the
            <em>net community estate</em>. One spouse can take the house
            and refinance out the community interest; the other spouse can
            take the retirement account and other liquid assets of
            equivalent value. What matters is that the numbers balance.
          </p>

          <h2>Where to go from here</h2>
          <p>
            California community property looks simple in the general
            principle and complicated in the specific fact. Most contested
            divorces I handle in San Diego have at least one hybrid asset,
            and often the difference of tens of thousands of dollars turns
            on a tracing analysis that has to be done carefully.
          </p>
          <p>
            If you want to walk through your asset picture, call
            <a href="tel:+16192502683">(619) 250-2683</a> or reach out
            through the <a href="/contact.html#form">contact form</a>. You
            can also read the <a href="/practice-areas/divorce/">divorce
            practice area</a> for the broader dissolution overview or the
            <a href="/blog/preliminary-declaration-of-disclosure-california.html">disclosure
            post</a> for the forms side.
          </p>
""",
    "related": [
        {"url": "/practice-areas/divorce/", "category": "Practice Area", "title": "San Diego Divorce (Practice Area)"},
        {"url": "/blog/preliminary-declaration-of-disclosure-california.html", "category": "Divorce", "title": "The Preliminary Declaration of Disclosure in a California Divorce"},
        {"url": "/blog/how-a-divorce-attorney-navigates-california-process.html", "category": "Divorce", "title": "How a San Diego Divorce Attorney Navigates the California Dissolution Process"},
    ],
})

# ---------------------------------------------------------------------------
# 4 — Spousal Support: What to Expect
# ---------------------------------------------------------------------------
POSTS.append({
    "slug": "spousal-support-in-california-what-to-expect",
    "category": "Spousal Support",
    "published": "2024-08-06",
    "published_pretty": "August 6, 2024",
    "title": "Spousal Support in California: What to Expect at Every Stage of a Case",
    "h1": "Spousal Support in California: What to Expect at Every Stage of a Case",
    "description": "Temporary spousal support during a California divorce, long-term post-judgment support under Family Code section 4320, and the standards judges apply. San Diego family attorney Brian Burkett.",
    "breadcrumb_short": "Spousal Support: What to Expect",
    "body_html": """
          <p>
            "Am I going to have to pay spousal support?" and "Am I going to
            get spousal support?" are two of the questions I hear most often
            in the first ten minutes of an intake meeting. The honest answer
            is: it depends on which stage of the case you are asking about,
            and on a set of factors that California family court weighs
            differently at different stages.
          </p>
          <p>
            This post walks through spousal support in a California divorce
            from filing through post-judgment, and shows how the standard
            changes as the case moves forward.
          </p>

          <h2>Temporary spousal support during the case</h2>
          <p>
            While a divorce is pending, either spouse can ask the court for
            temporary spousal support. Temporary support is designed to
            preserve the pre-separation standard of living while the case
            works its way toward judgment. It is not a permanent number
            and it does not become permanent by default.
          </p>
          <p>
            In San Diego family court, temporary spousal support is
            typically calculated using DissoMaster software (or a similar
            computer program the court accepts), which uses a formula
            keyed to each spouse's gross income. The DissoMaster number is
            not statutory &mdash; there is no California statewide
            guideline for temporary spousal support the way there is for
            child support &mdash; but San Diego local rules and practice
            treat the DissoMaster output as the presumptive temporary
            number. Deviations can be argued, but the practitioner asking
            for the deviation has to explain why.
          </p>
          <p>
            Temporary support is set by a Request for Order (FL-300)
            supported by an Income and Expense Declaration (FL-150).
            Because temporary support runs from the date of the order (or
            arguably from the date of filing the RFO if the court makes
            it retroactive) until judgment, the DissoMaster inputs matter.
            An inaccurate FL-150 in the first month of the case can lock
            in an under- or over-stated temporary number for many months.
          </p>

          <h2>Long-term (post-judgment) spousal support</h2>
          <p>
            Long-term spousal support is a different animal. It is decided
            under Family Code section 4320, which lists fourteen factors
            the court has to weigh. Unlike temporary support, long-term
            support is <strong>not</strong> a formula. DissoMaster output
            is expressly not admissible for setting long-term support
            (<em>Marriage of Schulze</em> is the case usually cited). The
            court has to work through the 4320 factors on the record.
          </p>
          <p>
            The 4320 factors, paraphrased, are: the marital standard of
            living; each spouse's earning capacity; whether the supported
            spouse contributed to the supporting spouse's education,
            training, or career; the supporting spouse's ability to pay
            (income, assets, standard of living); the needs of each spouse
            based on the marital standard of living; each spouse's assets
            and debts; the duration of the marriage; the ability of the
            supported spouse to work outside the home without unduly
            interfering with children's interests; each spouse's age and
            health; documented history of domestic violence; the immediate
            and specific tax consequences to each spouse; the balance of
            hardships; the goal that the supported spouse be
            self-supporting within a reasonable period of time; and any
            other factors the court determines are just and equitable.
          </p>

          <h2>The duration question</h2>
          <p>
            For marriages of fewer than ten years, Family Code section
            4336 sets a general presumption that "a reasonable period of
            time" for the supported spouse to become self-supporting is
            about half the length of the marriage. That is a starting
            presumption, not a hard rule, and it can be rebutted on the
            record.
          </p>
          <p>
            For marriages of ten years or more &mdash; what section 4336
            calls a "marriage of long duration" &mdash; the court retains
            jurisdiction over spousal support indefinitely, unless the
            parties waive that jurisdiction in writing. Retaining
            jurisdiction does not mean support continues forever; it means
            the court keeps the power to set, modify, or terminate support
            based on future circumstances.
          </p>

          <h2>The Gavron warning</h2>
          <p>
            California courts routinely issue a "Gavron warning" (from
            <em>Marriage of Gavron</em>) at judgment. A Gavron warning
            tells the supported spouse, on the record, that they are
            expected to take reasonable steps to become self-supporting
            within a reasonable period of time. If the supported spouse
            does not, that failure can be used later to reduce or
            terminate support on a modification.
          </p>
          <p>
            A Gavron warning is not a hostile move by the paying spouse.
            It is a standard piece of the record on any long-term spousal
            support order. In fact, the court can be reversed for failing
            to issue one where duration justifies it.
          </p>

          <aside class="blog-post__inline-cta">
            <p>
              What temporary support looks like at your first RFO and what
              long-term support looks like at judgment are often very
              different numbers.
            </p>
            <p>
              Call <a href="tel:+16192502683">(619) 250-2683</a> to walk
              through your numbers before the first hearing.
            </p>
          </aside>

          <h2>Modification and termination</h2>
          <p>
            Spousal support in California is generally modifiable on a
            change of circumstances after judgment &mdash; the paying
            spouse loses a job, the supported spouse's income grows,
            either party's health changes, or a Gavron-related failure to
            become self-supporting. Both temporary and long-term support
            are modifiable unless the parties expressly agreed in writing
            that the number is non-modifiable.
          </p>
          <p>
            Support also terminates by operation of law on the death of
            either party, or on the remarriage of the supported spouse
            under Family Code section 4337 (unless the parties agreed
            otherwise in writing). Cohabitation with a non-marital
            partner does not automatically terminate support, but under
            Family Code section 4323, cohabitation creates a rebuttable
            presumption of decreased need &mdash; which is often enough
            to reduce support on a subsequent Request for Order.
          </p>

          <h2>Tax treatment (post-2018)</h2>
          <p>
            For divorces finalized after December 31, 2018, spousal
            support is <strong>not deductible by the paying spouse for
            federal income tax purposes and not taxable to the receiving
            spouse</strong>. This is a significant change from prior law
            and affects the after-tax math on any support number. Older
            California judgments entered before that date generally
            retain the pre-2018 tax treatment unless expressly modified
            to follow current rules. California state tax treatment
            differs from federal &mdash; California still allows the
            paying-spouse deduction and treats support as income to the
            receiving spouse for California returns.
          </p>

          <h2>Settling spousal support</h2>
          <p>
            Most spousal support gets resolved by agreement rather than by
            contested hearing. A typical settlement might specify a
            dollar amount (or a formula), a duration (or a "step-down"
            schedule), a modifiability provision, and a jurisdiction-
            termination date for marriages of long duration. Every one of
            those variables has real cash consequences, and the drafting
            has to be precise. Ambiguous spousal-support language is a
            leading reason people come back to court a year or two after
            judgment.
          </p>

          <p>
            If you want to talk through where your case is on any of this,
            you can reach me at <a href="tel:+16192502683">(619) 250-2683</a>
            or through the <a href="/contact.html#form">contact form</a>. You
            can also read the <a href="/practice-areas/spousal-support/">spousal
            support practice area</a> for the broader overview or the
            <a href="/blog/alimony-in-california-a-practical-guide.html">alimony
            guide</a> for a deeper dive on the 4320 factors.
          </p>
""",
    "related": [
        {"url": "/practice-areas/spousal-support/", "category": "Practice Area", "title": "San Diego Spousal Support (Practice Area)"},
        {"url": "/blog/alimony-in-california-a-practical-guide.html", "category": "Spousal Support", "title": "Alimony in California: A Practical Guide Under Family Code Section 4320"},
        {"url": "/blog/how-a-divorce-attorney-navigates-california-process.html", "category": "Divorce", "title": "How a San Diego Divorce Attorney Navigates the California Dissolution Process"},
    ],
})

# ---------------------------------------------------------------------------
# 5 — Alimony in California: A Practical Guide
# ---------------------------------------------------------------------------
POSTS.append({
    "slug": "alimony-in-california-a-practical-guide",
    "category": "Spousal Support",
    "published": "2024-09-10",
    "published_pretty": "September 10, 2024",
    "title": "Alimony in California: A Practical Guide Under Family Code Section 4320",
    "h1": "Alimony in California: A Practical Guide Under Family Code Section 4320",
    "description": "How California family court applies the fourteen Family Code section 4320 factors to set long-term spousal support, and what the record needs to look like. San Diego family attorney Brian Burkett.",
    "breadcrumb_short": "Alimony: A Practical Guide",
    "body_html": """
          <p>
            "Alimony" is not a term California family law actually uses in
            the statute &mdash; the Family Code calls it spousal support.
            The word is close enough that I use it interchangeably in
            conversations with clients, and the concept is the same:
            court-ordered payments from one spouse to the other after a
            divorce.
          </p>
          <p>
            This post goes deeper on how the fourteen factors in Family
            Code section 4320 actually play out in a contested spousal
            support ruling, and what a well-prepared record looks like on
            each factor.
          </p>

          <h2>Why section 4320 carries the weight</h2>
          <p>
            Temporary spousal support during the case is largely formulaic
            in San Diego (DissoMaster). Long-term spousal support &mdash;
            the number that survives judgment and follows the parties for
            years &mdash; is not. It is set by the judge weighing the
            fourteen factors in section 4320.
          </p>
          <p>
            A long-term spousal support order that does not go through
            4320 on the record can get reversed on appeal. And in
            practice, the party asking for support (or for less support)
            has to build a factual record on the factors that matter
            most to their position. That is what an attorney is really
            doing on a long-term spousal support case: shaping the record.
          </p>

          <h2>Walking through the fourteen factors</h2>

          <h3>1. Marital standard of living</h3>
          <p>
            The court is required to consider the standard of living
            established during the marriage. What did the family spend on
            housing, on vehicles, on vacations, on discretionary items.
            This is fact-heavy and turns on documentation &mdash; tax
            returns, credit-card statements, and the FL-150 income and
            expense declaration.
          </p>

          <h3>2 &amp; 4. Earning capacity and ability to pay</h3>
          <p>
            The court considers each spouse's earning capacity, including
            marketable skills, the job market for those skills, the time
            and expense required to acquire training, and whether the
            supported spouse's marketable skills have declined during
            marriage due to unemployment or a period of homemaking. On the
            paying side, the court considers ability to pay &mdash; income,
            assets, and standard of living.
          </p>
          <p>
            Earning capacity is where a vocational examination under
            Family Code section 4331 sometimes gets ordered. A vocational
            evaluator examines the supported spouse's skills and reports on
            what jobs and earning ranges are available in the local market.
            The report is admissible and often carries weight.
          </p>

          <h3>3. Contribution to the supporting spouse's career</h3>
          <p>
            If the supported spouse contributed to the other spouse's
            attainment of education, training, career position, or a
            professional license, that goes on the record. A common
            example is a spouse who worked to pay the other spouse's way
            through medical school or law school.
          </p>

          <h3>5. Needs based on the marital standard of living</h3>
          <p>
            Each spouse's needs are measured against the marital standard
            of living. This is where the FL-150 expenses matter. Inflated
            expenses do not help credibility; deflated expenses can
            undercut a support claim. Documented expenses tied to real
            monthly cash-flow work best.
          </p>

          <h3>6. Assets and debts</h3>
          <p>
            The court considers each spouse's assets (including separate
            property, when relevant to support) and debts. A spouse whose
            property division includes substantial liquid assets may need
            less support than a spouse whose share is illiquid.
          </p>

          <h3>7. Duration of the marriage</h3>
          <p>
            The length of the marriage is central. Under Family Code
            section 4336, a marriage of ten years or more is a "marriage
            of long duration," and the court retains jurisdiction over
            support indefinitely. In shorter marriages, the presumption is
            that support runs for about half the length of the marriage,
            though that presumption can be rebutted.
          </p>

          <h3>8. Working outside the home with children present</h3>
          <p>
            The court considers whether the supported spouse can engage in
            gainful employment without unduly interfering with the
            interests of dependent children in the spouse's custody. A
            supported spouse with young children and demanding custody
            responsibilities is not treated the same as a supported
            spouse whose children are grown.
          </p>

          <h3>9. Age and health</h3>
          <p>
            Both spouses' age and health matter. Health conditions that
            affect earning capacity are relevant, and can be documented
            through medical records if disputed.
          </p>

          <h3>10. Documented history of domestic violence</h3>
          <p>
            Family Code section 4320(i) requires the court to consider any
            documented history of domestic violence between the parties,
            including emotional distress from violence perpetrated by the
            supporting party and any history of violence by the supported
            party. Section 4325 goes further &mdash; a spouse convicted
            of an act of domestic violence against the other spouse within
            five years before dissolution is subject to a rebuttable
            presumption against being awarded support. If restraining
            orders are part of the case history, that goes on the record.
          </p>

          <aside class="blog-post__inline-cta">
            <p>
              4320 is a fourteen-factor test the court has to actually
              apply. Which factors matter most in your case is a strategic
              call.
            </p>
            <p>
              Call <a href="tel:+16192502683">(619) 250-2683</a> or
              <a href="/contact.html#booking">book a consultation</a> to
              walk through the factors that fit your facts.
            </p>
          </aside>

          <h3>11. Tax consequences</h3>
          <p>
            The court considers the immediate and specific tax consequences
            to each party. As noted in the
            <a href="/blog/spousal-support-in-california-what-to-expect.html">temporary/permanent
            support post</a>, post-2018 divorces have federal tax
            treatment very different from earlier cases &mdash; support
            is neither deductible to the payer nor taxable to the
            recipient federally, though California state tax treatment
            still follows the old rules.
          </p>

          <h3>12. Balance of hardships</h3>
          <p>
            The court balances the hardships to each spouse. This factor
            is broad and is often where a judge factors in things that
            do not fit neatly under the other factors.
          </p>

          <h3>13. Goal of self-support within a reasonable time</h3>
          <p>
            Section 4320(l) codifies the policy that a supported spouse is
            expected to become self-supporting within a reasonable period
            of time. This is where the Gavron warning I discuss elsewhere
            comes in. A judge who orders long-term support usually gives
            the supported spouse a specific timeline expectation on the
            record.
          </p>

          <h3>14. Any other just and equitable factor</h3>
          <p>
            A catch-all. Judges use this when the facts of a case have a
            wrinkle that does not fit under 1-13 but bears on what a
            fair support number looks like.
          </p>

          <h2>How the factors get built into a hearing</h2>
          <p>
            In a contested spousal support hearing, the record on the
            factors typically comes from: (1) the FL-150 income and
            expense declaration and supporting documents, (2) tax returns
            for the last three to five years, (3) declarations from each
            spouse addressing standard of living, contribution, and
            circumstances, (4) a vocational report if earning capacity is
            disputed, (5) testimony if the hearing goes evidentiary, and
            (6) a proposed statement of decision each side submits.
          </p>
          <p>
            Getting a good long-term support order is largely about
            preparation. The 4320 factors are the outline; the exhibits
            are how the outline gets filled in.
          </p>

          <h2>Ready to talk through your case</h2>
          <p>
            Long-term spousal support cases turn on facts. If you have
            questions about how the 4320 factors would apply to yours,
            you can reach me at <a href="tel:+16192502683">(619)
            250-2683</a> or through the
            <a href="/contact.html#form">contact form</a>. See also the
            <a href="/practice-areas/spousal-support/">spousal support
            practice area</a> for the broader overview.
          </p>
""",
    "related": [
        {"url": "/practice-areas/spousal-support/", "category": "Practice Area", "title": "San Diego Spousal Support (Practice Area)"},
        {"url": "/blog/spousal-support-in-california-what-to-expect.html", "category": "Spousal Support", "title": "Spousal Support in California: What to Expect at Every Stage of a Case"},
        {"url": "/blog/how-a-divorce-attorney-navigates-california-process.html", "category": "Divorce", "title": "How a San Diego Divorce Attorney Navigates the California Dissolution Process"},
    ],
})

# ---------------------------------------------------------------------------
# 6 — Protecting Parental Rights in California Custody
# ---------------------------------------------------------------------------
POSTS.append({
    "slug": "protecting-parental-rights-in-california-custody",
    "category": "Child Custody",
    "published": "2024-10-08",
    "published_pretty": "October 8, 2024",
    "title": "Protecting Parental Rights in California Custody Cases",
    "h1": "Protecting Parental Rights in California Custody Cases",
    "description": "Legal and physical custody, the best-interest standard under Family Code section 3011, and the moves that erode a parent's role. San Diego family attorney Brian Burkett.",
    "breadcrumb_short": "Protecting Parental Rights",
    "body_html": """
          <p>
            Parental rights in California custody cases do not get lost in
            one big ruling. They get chipped away in small, easy-to-miss
            moves &mdash; a temporary order that quietly becomes the
            baseline, an FCS session where one parent shows up with a
            proposal and the other does not, a Request for Order the other
            side files while a parent is still trying to figure out what
            venue this all lives in.
          </p>
          <p>
            This post is about what parental rights actually are under
            California law, how the best-interest standard gets applied,
            and the moves that quietly erode a parent's role in a case if
            they are not addressed early.
          </p>

          <h2>Legal custody versus physical custody</h2>
          <p>
            California distinguishes two kinds of custody, and they are
            decided separately. <strong>Legal custody</strong> is
            decision-making authority over the child's education, medical
            care, religious upbringing, and other major life decisions.
            <strong>Physical custody</strong> is where the child lives and
            spends time. Either kind can be joint (shared between the
            parents) or sole (to one parent), and the two do not have to
            match. Joint legal with primary physical to one parent is a
            common San Diego outcome.
          </p>
          <p>
            "Sole legal custody" is not a symbolic label. It changes who
            gets to enroll a child in school, who signs medical consent
            forms, who chooses a therapist. Losing joint legal custody in
            a case is a real reduction in a parent's role, and it can be
            hard to reverse once the order is entered.
          </p>

          <h2>The best-interest standard under section 3011</h2>
          <p>
            California family court decides custody using the best-interest
            standard in Family Code section 3011. The statute lists
            factors the court is required to consider: the health, safety,
            and welfare of the child; any history of abuse by a parent;
            the nature and amount of contact with each parent; and habitual
            or continual illegal use of controlled substances or alcohol
            abuse by either parent.
          </p>
          <p>
            Section 3011 is the framework. Section 3020 layers on the
            state's policy statement: the court's primary concern is the
            health, safety, and welfare of the child; frequent and
            continuing contact with both parents is favored where consistent
            with the child's best interest; and where those goals conflict,
            the child's health, safety, and welfare wins.
          </p>

          <h2>The moves that erode parental rights</h2>

          <h3>Not appearing at the first hearing</h3>
          <p>
            The most common way a parent's role gets reduced early in a
            case is by not being present, on paper or in person, when
            initial orders are set. A Request for Order the other parent
            files while a parent is between jobs, moving, or simply
            unrepresented can produce a "temporary" custody order that
            functions as the status quo for months. Courts are cautious
            about changing custody arrangements the child has adapted to.
          </p>

          <h3>Not preparing for Family Court Services mediation</h3>
          <p>
            San Diego routes custody disputes through Family Court Services
            mediation under Family Code section 3170 before the contested
            hearing. FCS in San Diego County is a recommending
            jurisdiction &mdash; the mediator can make a written
            recommendation to the judge if the parents do not agree.
            Walking into FCS unprepared, without a proposed parenting
            plan, can result in a recommendation that reflects the other
            parent's proposal by default.
          </p>

          <h3>Consenting to a substantial deviation "just for now"</h3>
          <p>
            "Let's just do it your way for the next three months and
            revisit" sounds like flexibility. In practice, a three-month
            arrangement often becomes the baseline the court asks each
            parent to justify departing from. Written agreements between
            parents, and any court-adopted temporary orders, deserve real
            attention even when they are described as short-term.
          </p>

          <h3>Miscommunication with the other parent, in writing</h3>
          <p>
            Text messages and email are admissible. A parent who vents in
            writing &mdash; even in response to genuinely provocative
            behavior &mdash; is creating exhibits. In an active custody
            case, treating written communication with the other parent as
            if it will end up attached to a declaration is a habit worth
            forming.
          </p>

          <aside class="blog-post__inline-cta">
            <p>
              If you are in the first ninety days of a custody dispute, the
              early moves matter more than the eventual hearing.
            </p>
            <p>
              Call <a href="tel:+16192502683">(619) 250-2683</a> to walk
              through your case before the next Request for Order or FCS
              date.
            </p>
          </aside>

          <h2>The Family Code section 3044 presumption</h2>
          <p>
            Family Code section 3044 creates a rebuttable presumption
            against awarding sole or joint physical or legal custody to a
            parent who has committed domestic violence against the other
            parent, the child, or the child's sibling within the previous
            five years. The presumption can be rebutted with clear evidence
            addressing the enumerated statutory factors, but it is a
            substantial thumb on the scale. If a restraining order has
            issued in the case, section 3044 will structure the custody
            analysis.
          </p>

          <h2>Section 3111 evaluations and minor's counsel</h2>
          <p>
            In cases where the custody dispute is contested and the
            evidence about the child is not straightforward, the court can
            order a Family Code section 3111 child custody evaluation. An
            evaluator (a licensed mental-health professional) interviews
            each parent, the child, and collaterals, reviews records, and
            submits a written report with recommendations. A 3111
            evaluation is expensive and time-consuming, but the resulting
            report often carries substantial weight.
          </p>
          <p>
            Family Code section 3150 lets the court appoint minor's
            counsel &mdash; a separate attorney for the child &mdash; in
            appropriate cases. Minor's counsel represents the child's
            interests independently of either parent, and can present
            evidence, cross-examine, and argue at the hearing.
          </p>

          <h2>Move-away requests</h2>
          <p>
            A parent with a custody order who wants to relocate the child
            has to give notice and, if the other parent objects, may need
            court permission. Under <em>Marriage of LaMusga</em> and its
            progeny, the court weighs a set of move-away factors: the
            child's interest in stability, the distance of the move, the
            child's age, the child's relationship with each parent, the
            move's likely impact on the child, and the reasons for the
            move. Move-away cases are among the highest-stakes custody
            disputes California family court hears.
          </p>

          <h2>Modification after the order</h2>
          <p>
            An existing California custody order can be modified on a
            substantial change of circumstances that affects the child's
            best interest. That standard is meaningful &mdash; the court
            does not modify custody just because a parent is unhappy with
            the order. But real changes in a child's life (school changes,
            a parent's relocation, a work-schedule shift, a safety issue)
            can support a modification. A well-prepared modification
            motion identifies the change, ties it to the child's best
            interest, and proposes a specific new order.
          </p>

          <h2>Protecting your role in the case</h2>
          <p>
            Protecting parental rights in a California custody case is
            mostly about being present and prepared at the moments that
            matter &mdash; the first hearing, the FCS session, any
            evaluation, and any modification. It also means being
            realistic. The best-interest standard is a real standard, and
            a proposal that is clearly better for the child usually wins.
          </p>
          <p>
            If you want to talk through your custody case, you can reach
            me at <a href="tel:+16192502683">(619) 250-2683</a> or through
            the <a href="/contact.html#form">contact form</a>. See also
            the <a href="/practice-areas/child-custody/">child custody
            practice area</a> for the broader overview.
          </p>
""",
    "related": [
        {"url": "/practice-areas/child-custody/", "category": "Practice Area", "title": "San Diego Child Custody (Practice Area)"},
        {"url": "/blog/child-visitation-in-california.html", "category": "Child Custody", "title": "Child Visitation in California: Parenting Plans, Schedules, and Enforcement"},
        {"url": "/blog/what-a-california-custody-attorney-does.html", "category": "Child Custody", "title": "What a California Custody Attorney Actually Does (Beyond the Hearing)"},
    ],
})

# ---------------------------------------------------------------------------
# 7 — Child Visitation in California
# ---------------------------------------------------------------------------
POSTS.append({
    "slug": "child-visitation-in-california",
    "category": "Child Custody",
    "published": "2024-11-05",
    "published_pretty": "November 5, 2024",
    "title": "Child Visitation in California: Parenting Plans, Schedules, and Enforcement",
    "h1": "Child Visitation in California: Parenting Plans, Schedules, and Enforcement",
    "description": "How California parenting-time schedules get built, the difference between typical schedules, and enforcement options when the other parent will not follow the order. San Diego family attorney.",
    "breadcrumb_short": "Child Visitation in California",
    "body_html": """
          <p>
            "Visitation" is what people call it in conversation. California
            family court has largely moved on to the language of "parenting
            time" or "parenting plans," because the older word implied one
            parent was less of a real parent. The change is not just
            semantic &mdash; parenting-time orders in California are
            expected to be specific enough that both parents can actually
            follow them, and generic enough to accommodate normal life.
          </p>
          <p>
            This post is about how a workable California parenting plan
            gets built, what a typical San Diego schedule looks like, and
            what to do when the other parent stops following the order.
          </p>

          <h2>What a good parenting plan actually specifies</h2>
          <p>
            A workable California parenting-time order covers, at minimum:
          </p>
          <ul>
            <li>The regular weekly schedule (which parent has the child on
                which days, and when exchanges happen)</li>
            <li>The holiday schedule (Thanksgiving, winter break,
                three-day weekends, Mother's Day and Father's Day, each
                parent's birthday, the child's birthday)</li>
            <li>Summer vacation (block time, or continued regular
                schedule, or a modified schedule)</li>
            <li>School breaks (spring break, fall break, back-to-school
                night attendance)</li>
            <li>Exchange location and mechanics (curbside, at school, at
                the child's activity)</li>
            <li>Communication (phone, text, video calls with the child
                during the other parent's time)</li>
            <li>Travel (advance notice for out-of-county travel,
                passports, international travel)</li>
            <li>Third-party care (which non-parent caregivers can
                supervise the child during a parent's time)</li>
          </ul>
          <p>
            A parenting plan that specifies only "every other weekend and
            one weekday evening" leaves too much to interpretation. A plan
            that specifies each holiday and each school break down to the
            hour reduces the number of disputes that require a return to
            court.
          </p>

          <h2>Typical San Diego schedules</h2>
          <p>
            There is no "standard" California parenting plan &mdash; the
            court decides based on the best interest of the child in each
            case &mdash; but a handful of formats come up over and over
            in San Diego family court.
          </p>
          <p>
            <strong>Every other weekend, one weekday visit.</strong> Common
            when one parent is the primary residential parent and the
            child's school schedule is stable. The visiting parent
            typically has Friday after school through Sunday evening every
            other week, plus a weekday visit for dinner (or, in some
            plans, an overnight midweek).
          </p>
          <p>
            <strong>2-2-3.</strong> A 50/50 schedule with two nights with
            parent A, two nights with parent B, and a three-night stretch
            that alternates each week. Popular with younger children
            because neither parent goes more than a few days without a
            visit, but the number of exchanges each week is high.
          </p>
          <p>
            <strong>2-2-5-5.</strong> Also a 50/50 schedule, with each
            parent having the same two weekday nights every week and the
            weekends alternating in five-night blocks. Fewer exchanges;
            more predictable for older kids.
          </p>
          <p>
            <strong>Week-on / week-off.</strong> A 50/50 schedule where
            each parent has the child for a full week at a time. Works
            when the child is old enough to tolerate a longer stretch
            between visits, and when the parents live close enough to the
            same schools and activities to make it seamless.
          </p>

          <h2>Building a schedule that fits the case</h2>
          <p>
            The right parenting plan depends on the child's age, school,
            activities, and health; each parent's work schedule and
            geographic proximity; the co-parenting relationship; and any
            safety issues in the case. A schedule that would be perfect
            for a school-age child with two parents living six blocks
            apart is not workable for a toddler with parents thirty miles
            apart in different school districts.
          </p>
          <p>
            In San Diego, Family Court Services mediation is usually where
            the schedule discussion happens first, on any case where
            custody is in dispute. Coming to FCS with a proposal &mdash;
            not just "more time," but a specific week-by-week schedule
            with holidays &mdash; is much stronger than showing up
            without one. I cover this in more detail in the post on
            <a href="/blog/what-a-california-custody-attorney-does.html">what
            a California custody attorney actually does</a>.
          </p>

          <aside class="blog-post__inline-cta">
            <p>
              A parenting plan is the operating manual for the next several
              years of your family. It is worth building carefully.
            </p>
            <p>
              Call <a href="tel:+16192502683">(619) 250-2683</a> or
              <a href="/contact.html#booking">book a consultation</a> to
              walk through what a workable schedule looks like for your
              family.
            </p>
          </aside>

          <h2>What happens when the other parent will not follow the order</h2>
          <p>
            California parenting-time orders are court orders. When a
            parent unilaterally deviates from the order &mdash; keeping
            the child on non-scheduled days, refusing to allow exchanges,
            withholding phone or video contact &mdash; there are several
            enforcement paths.
          </p>

          <h3>Meet-and-confer, in writing</h3>
          <p>
            Before returning to court, most judges expect the parents to
            have tried to resolve the issue directly. A calm written
            message from a parent (or from counsel) documenting the
            specific violation and asking for compliance serves two
            purposes: it may actually work, and it creates a paper record
            if a court filing is later needed.
          </p>

          <h3>Request for Order to modify or enforce</h3>
          <p>
            A Request for Order (FL-300) can ask the court to enforce the
            existing parenting plan (compensatory time, warnings), to
            modify the plan if the pattern of violation has effectively
            changed the schedule, or to clarify ambiguous language that
            is being used as a pretext.
          </p>

          <h3>Contempt</h3>
          <p>
            California family court can hold a parent in contempt for
            willful violation of a court order. Contempt in family court
            is a serious remedy &mdash; the party seeking contempt has to
            allege the specific order violated, the party's knowledge of
            it, and the ability to comply with it, and prove each element
            beyond a reasonable doubt. Contempt is not the right tool for
            every parenting-time dispute, but for a pattern of egregious
            violations it can be effective.
          </p>

          <h3>Family Code section 3028 &mdash; monetary sanctions</h3>
          <p>
            California Family Code section 3028 authorizes the court to
            order a parent who denies the other parent's court-ordered
            time to pay financial compensation to the aggrieved parent
            &mdash; costs actually incurred as a result of the missed
            time. It is not commonly ordered, but it is on the books, and
            in the right case it can be a useful tool.
          </p>

          <h2>Modifying the schedule as kids grow</h2>
          <p>
            A schedule that fits a five-year-old will not fit a
            fourteen-year-old. As kids grow, their activities, school
            demands, and preferences shift. A modification of the
            parenting plan on a substantial change of circumstances is
            available, and pre-planning the modification when the
            original order is entered &mdash; e.g., "the schedule
            transitions to 2-2-5-5 when the child enters middle school"
            &mdash; can reduce future court filings.
          </p>

          <h2>Ready to talk through your case</h2>
          <p>
            Whether you are trying to build a first parenting plan,
            modify an existing one, or address a pattern of the other
            parent's non-compliance, the moves are specific and the
            process is workable. If you want to walk through your case,
            you can reach me at
            <a href="tel:+16192502683">(619) 250-2683</a> or through the
            <a href="/contact.html#form">contact form</a>. See also the
            <a href="/practice-areas/child-custody/">child custody
            practice area</a>.
          </p>
""",
    "related": [
        {"url": "/practice-areas/child-custody/", "category": "Practice Area", "title": "San Diego Child Custody (Practice Area)"},
        {"url": "/blog/protecting-parental-rights-in-california-custody.html", "category": "Child Custody", "title": "Protecting Parental Rights in California Custody Cases"},
        {"url": "/blog/what-a-california-custody-attorney-does.html", "category": "Child Custody", "title": "What a California Custody Attorney Actually Does (Beyond the Hearing)"},
    ],
})

# ---------------------------------------------------------------------------
# 8 — What a California Custody Attorney Actually Does
# ---------------------------------------------------------------------------
POSTS.append({
    "slug": "what-a-california-custody-attorney-does",
    "category": "Child Custody",
    "published": "2024-12-03",
    "published_pretty": "December 3, 2024",
    "title": "What a California Custody Attorney Actually Does (Beyond the Hearing)",
    "h1": "What a California Custody Attorney Actually Does (Beyond the Hearing)",
    "description": "Family Court Services mediation prep, section 3111 evaluations, minor's counsel, discovery, and the everyday work between hearings on a California custody case.",
    "breadcrumb_short": "What a Custody Attorney Does",
    "body_html": """
          <p>
            When most people picture a custody attorney, they picture the
            hearing &mdash; the courtroom, the judge, the argument at the
            podium. That is a real part of the job, but on a typical
            California custody case it is a small part. The work that
            actually shapes the outcome usually happens in the weeks
            between the courtroom appearances.
          </p>
          <p>
            This post is about what a California custody attorney is
            doing when they are not standing in front of the judge.
          </p>

          <h2>Intake and the first strategic map</h2>
          <p>
            The first meeting on a custody case is not just a
            question-and-answer session. It is the strategic map for the
            case: who has the child now, what the schools and activities
            look like, whether either parent works out of the county,
            whether there are safety issues that need a separate
            restraining-order track, and whether the current status quo
            was reached through a written agreement, an oral agreement, or
            just habit.
          </p>
          <p>
            That map drives everything that follows. A case where one
            parent has been the primary caregiver for a year and the other
            parent is asking for 50/50 time looks different from a case
            where the parents had been sharing time roughly equally until
            the day one of them filed.
          </p>

          <h2>Drafting the initial pleadings correctly</h2>
          <p>
            A California custody case usually opens with a Petition (in a
            divorce) or a Request for Order (FL-300) attaching a specific
            proposed parenting plan. The specificity matters. A Request
            for Order that asks for "reasonable visitation" is meaningfully
            weaker than one that attaches a written proposed schedule with
            holidays, exchanges, and travel provisions.
          </p>
          <p>
            Drafting the supporting declaration is where I spend most of
            my time in the pleading stage. A declaration should be
            specific, factual, and short. It should recount the concrete
            history that supports the requested schedule, not the parent's
            frustration with the other side. Judges read a lot of
            declarations. The ones that get remembered are the ones that
            are tight.
          </p>

          <h2>Family Court Services mediation prep</h2>
          <p>
            San Diego routes contested custody through Family Court
            Services (FCS) mediation under Family Code section 3170
            before the contested hearing. FCS is recommending &mdash; the
            mediator can send a written recommendation to the judge if the
            parents cannot reach agreement.
          </p>
          <p>
            Preparing a parent for FCS is one of the most impactful pieces
            of work I do on a custody case. That preparation covers: what
            to bring (the proposed parenting plan, the child's school
            calendar, the parents' work schedules), how to talk about the
            child (specific and behavioral, not global and characterological
            about the other parent), what the FCS mediator will ask, and
            what a productive proposal looks like.
          </p>

          <h2>Section 3111 evaluations</h2>
          <p>
            In cases where FCS mediation cannot resolve the dispute and
            the child's specific circumstances need deeper examination,
            the court can order a Family Code section 3111 custody
            evaluation. A section 3111 evaluator (a licensed
            mental-health professional trained in family evaluations)
            interviews each parent, the child, and collaterals (teachers,
            pediatrician, therapist, other relevant adults), reviews
            records, and prepares a written report with recommendations to
            the court.
          </p>
          <p>
            My role during a section 3111 evaluation is to prepare the
            client for the interviews, coordinate document production for
            the evaluator, ensure the evaluator has access to the
            collaterals the client wants heard, and, once the report is
            issued, evaluate whether to accept the recommendations, argue
            them at hearing, or (in rare cases) challenge the
            evaluation itself.
          </p>

          <aside class="blog-post__inline-cta">
            <p>
              A section 3111 evaluation is a significant undertaking. How
              you prepare for it, and what documents the evaluator sees,
              often drives the recommendation.
            </p>
            <p>
              Call <a href="tel:+16192502683">(619) 250-2683</a> if a
              section 3111 evaluation has been ordered or is on the
              table in your case.
            </p>
          </aside>

          <h2>Minor's counsel appointments</h2>
          <p>
            Family Code section 3150 allows the court to appoint a
            separate attorney for the child &mdash; "minor's counsel"
            &mdash; in appropriate cases. Minor's counsel represents the
            child's interests independently, interviews the child, and
            can present evidence, cross-examine, and argue.
          </p>
          <p>
            When minor's counsel is appointed, I work closely with them:
            providing the case history, coordinating information about the
            child's school and activities, and ensuring the client is
            available to speak with minor's counsel professionally.
            Minor's counsel is not the opposing side, but they are also
            not aligned with either parent by default. How the parents
            interact with them matters.
          </p>

          <h2>Discovery in a custody case</h2>
          <p>
            Discovery in a custody case looks different from discovery in
            a property case. Standard California discovery devices are
            available (interrogatories, requests for production,
            depositions), but the substantive focus is different:
            school and medical records, communications between the
            parents, third-party witness statements, and, in rare cases,
            subpoenas to therapists (subject to privilege) or law
            enforcement.
          </p>

          <h2>Preparing exhibits for hearing</h2>
          <p>
            When a contested custody hearing actually gets set, exhibit
            preparation is a real amount of work. A well-prepared
            evidentiary hearing has: the FCS report, any section 3111
            evaluation, school records, key text-message excerpts, the
            parents' calendars, and specific incident-based documents. A
            hearing is not the moment to introduce your entire case in
            one motion; it is the moment to present the two or three
            documents that show the pattern the court needs to see.
          </p>

          <h2>Post-hearing follow-through</h2>
          <p>
            After the hearing, the actual custody order has to be
            reduced to a written Findings and Order After Hearing
            (FL-340 / FL-341(D)). That drafting matters. Ambiguous
            language in the written order becomes future disputes. A
            well-drafted order specifies each element of the schedule
            with enough precision that both parents can follow it, and
            includes standard provisions (exchanges, communication
            during the other parent's time, travel notice) that fill in
            the ordinary edge cases.
          </p>

          <h2>Modification, enforcement, and the long tail</h2>
          <p>
            A custody case does not close at judgment; it just goes
            dormant. Kids grow. Parents' work changes. Second households
            form. Every one of those changes can support a modification
            of the custody order on a substantial change of circumstances.
            A parent who returns to court on the same theory that was
            argued a year ago rarely succeeds; a parent who returns with
            a specific new circumstance and a specific proposed
            adjustment usually gets a hearing.
          </p>
          <p>
            Enforcement is the other half of post-judgment work. When
            the other parent stops following the order, an attorney can
            issue meet-and-confer letters, file a Request for Order to
            enforce or modify, and in the right case pursue contempt.
            See the <a href="/blog/child-visitation-in-california.html">post
            on child visitation</a> for more on enforcement options.
          </p>

          <h2>Ready to talk it through</h2>
          <p>
            Custody attorneys are not just courtroom advocates. Most of
            the value in a well-handled case comes from the preparation,
            the FCS session, the evaluation, and the drafting &mdash; the
            work that never shows up as a courtroom highlight but shapes
            what the child's life looks like for the next several years.
          </p>
          <p>
            If you want to talk about your custody case, you can reach me
            at <a href="tel:+16192502683">(619) 250-2683</a> or through
            the <a href="/contact.html#form">contact form</a>. See also
            the <a href="/practice-areas/child-custody/">child custody
            practice area</a>.
          </p>
""",
    "related": [
        {"url": "/practice-areas/child-custody/", "category": "Practice Area", "title": "San Diego Child Custody (Practice Area)"},
        {"url": "/blog/protecting-parental-rights-in-california-custody.html", "category": "Child Custody", "title": "Protecting Parental Rights in California Custody Cases"},
        {"url": "/blog/child-visitation-in-california.html", "category": "Child Custody", "title": "Child Visitation in California: Parenting Plans, Schedules, and Enforcement"},
    ],
})

# ---------------------------------------------------------------------------
# 9 — Child Support in California: What Attorneys Add
# ---------------------------------------------------------------------------
POSTS.append({
    "slug": "child-support-in-california-what-attorneys-do",
    "category": "Child Support",
    "published": "2025-01-14",
    "published_pretty": "January 14, 2025",
    "title": "Child Support in California: What an Attorney Adds to the Guideline Number",
    "h1": "Child Support in California: What an Attorney Adds to the Guideline Number",
    "description": "California guideline child support is a formula. What an attorney adds around the formula — income imputation, add-ons, DissoMaster inputs, and modification. San Diego family attorney.",
    "breadcrumb_short": "Child Support: What Attorneys Add",
    "body_html": """
          <p>
            California child support is one of the more formula-driven
            areas of family law. There is a statewide guideline, a
            software calculator most judges use (DissoMaster), and a set
            of statutory inputs. So a fair question at the intake meeting
            is: if this is a formula, why do I need an attorney at all?
          </p>
          <p>
            The formula is real. What an attorney adds is what goes into
            the formula &mdash; and, on the back end, how add-ons,
            enforcement, and modification get handled.
          </p>

          <h2>The California guideline</h2>
          <p>
            California child support is set under the statewide guideline
            in Family Code section 4055. The formula uses each parent's
            net disposable income and the approximate percentage of time
            each parent has with the child. In San Diego, judges
            calculate the guideline number using DissoMaster or a similar
            court-accepted calculator. The formula is presumptively
            correct under Family Code section 4057 &mdash; the court is
            required to order the guideline number unless it makes
            findings under one of the enumerated statutory exceptions.
          </p>
          <p>
            Because the formula is presumptive, deviations from the
            guideline are the exception, not the rule. In practice, the
            fight in most California child support cases is not "should
            we deviate from guideline." It is "what are the correct
            inputs to the guideline formula."
          </p>

          <h2>Inputs one: income</h2>
          <p>
            Each parent's income is the biggest input. For W-2 employees,
            income is usually straightforward &mdash; the FL-150 Income
            and Expense Declaration, backed by pay stubs and tax returns,
            establishes the number.
          </p>
          <p>
            For self-employed parents, commissioned parents, seasonal
            workers, and parents with significant equity comp, the
            income picture is more work. A self-employed parent's
            business net income is not the same as their taxable income,
            and the two rarely match without careful analysis of
            personal expenses run through the business. A parent whose
            income spikes twice a year on commission or bonuses cannot
            be evaluated on a single month's paycheck. RSUs and stock
            options have vesting schedules that affect what portion is
            income for support purposes.
          </p>
          <p>
            The FL-150 asks for the last twelve months' income. A
            well-prepared FL-150 attaches supporting documents and
            explains any unusual line items. A poorly prepared FL-150
            invites the other side (and the court) to fill in blanks
            with assumptions.
          </p>

          <h2>Inputs two: imputed income</h2>
          <p>
            California courts have discretion under Family Code section
            4058 to impute income to a parent based on earning capacity,
            not just actual income. The classic case: a parent who quits
            a job or takes a substantial pay cut around the time a
            support case starts. If the court finds the parent has the
            ability and opportunity to earn more, it can calculate
            support as if the parent were earning that higher number.
          </p>
          <p>
            Imputation cases usually involve a vocational examination
            under Family Code section 4331 &mdash; a licensed vocational
            evaluator reports on what jobs and earning ranges are
            available to the parent given their skills and the local
            market. Imputation is not automatic; the party requesting it
            has to build a record.
          </p>

          <h2>Inputs three: time share</h2>
          <p>
            The percentage of time each parent has with the child is the
            second big input to the guideline formula. Higher timeshare
            for the paying parent reduces the support order; higher
            timeshare for the receiving parent increases it.
          </p>
          <p>
            "Timeshare" for guideline purposes is a specific concept.
            It refers to the percentage of primary physical
            responsibility &mdash; the time during which each parent is
            the responsible caretaker, not just "any time the child
            physically spends with the parent." Overnight time, school
            hours, and third-party care are handled specifically by
            case law. In a case where the parenting-time schedule is
            still being litigated, the timeshare input can change
            substantially as the custody order changes, which is why
            child support and custody hearings are often set together.
          </p>

          <aside class="blog-post__inline-cta">
            <p>
              A child-support order is only as good as its inputs. Get the
              FL-150 wrong and the guideline number will be wrong.
            </p>
            <p>
              Call <a href="tel:+16192502683">(619) 250-2683</a> to walk
              through your case before the first support hearing.
            </p>
          </aside>

          <h2>Add-ons under section 4062</h2>
          <p>
            The guideline number covers basic child support. Family Code
            section 4062 lists specific additional costs that get
            allocated on top of the guideline number:
          </p>
          <ul>
            <li><strong>Mandatory add-ons:</strong> child care costs
                related to employment or job-related training; and
                reasonable uninsured health-care costs for the child</li>
            <li><strong>Discretionary add-ons:</strong> educational or
                other special needs of the child; and travel expenses
                for visitation</li>
          </ul>
          <p>
            Section 4061 sets the default that add-ons are allocated
            equally between the parents, but the court can allocate
            them in proportion to each parent's net disposable income.
            Well-drafted support orders specify how add-ons will be
            paid (reimbursement mechanism, tracking) so the parents do
            not end up back in court over private-school tuition or
            an orthodontia bill.
          </p>

          <h2>Modification under section 3651</h2>
          <p>
            California child support is modifiable on a change of
            circumstances under Family Code section 3651. Common triggers
            for modification include a job loss or change, a significant
            income increase, a change in the custody schedule, a change
            in health-care coverage, or the child's emancipation. A
            modification runs from the date of filing the Request for
            Order (or, in some cases, from a slightly earlier date if
            the parties agree). It does not run retroactive to the
            actual change of circumstances, which is why filing timely
            matters.
          </p>

          <h2>Enforcement</h2>
          <p>
            California child-support orders are enforced through a
            variety of tools: wage assignments (mandatory on every new
            order unless waived under Family Code section 5260),
            interception of state and federal tax refunds, license
            suspensions in cases of chronic non-payment, and, in the
            right case, contempt. San Diego County has a Department of
            Child Support Services that can enforce orders at no cost
            to the receiving parent, though the enforcement path and
            control over the case differs from private counsel.
          </p>

          <h2>What an attorney adds</h2>
          <p>
            Around a formula, an attorney adds preparation and
            precision. That means: an accurate FL-150 with the
            supporting documents attached; the correct imputation
            argument when it applies; a timeshare input that matches
            the actual schedule; add-on allocations that are specific;
            and modification and enforcement work when the case
            changes. It is not glamorous. It is what determines whether
            the number that comes out of DissoMaster is a number the
            client can live with.
          </p>
          <p>
            If you want to walk through your child support case, you can
            reach me at <a href="tel:+16192502683">(619) 250-2683</a> or
            through the <a href="/contact.html#form">contact form</a>.
            See also the <a href="/practice-areas/child-support/">child
            support practice area</a> and the
            <a href="/blog/working-with-a-child-support-attorney.html">first-six-weeks
            walkthrough</a>.
          </p>
""",
    "related": [
        {"url": "/practice-areas/child-support/", "category": "Practice Area", "title": "San Diego Child Support (Practice Area)"},
        {"url": "/blog/working-with-a-child-support-attorney.html", "category": "Child Support", "title": "Working With a San Diego Child Support Attorney: What the First Six Weeks Look Like"},
        {"url": "/blog/protecting-parental-rights-in-california-custody.html", "category": "Child Custody", "title": "Protecting Parental Rights in California Custody Cases"},
    ],
})

# ---------------------------------------------------------------------------
# 10 — Working with a Child Support Attorney: First Six Weeks
# ---------------------------------------------------------------------------
POSTS.append({
    "slug": "working-with-a-child-support-attorney",
    "category": "Child Support",
    "published": "2025-02-11",
    "published_pretty": "February 11, 2025",
    "title": "Working With a San Diego Child Support Attorney: What the First Six Weeks Look Like",
    "h1": "Working With a San Diego Child Support Attorney: What the First Six Weeks Look Like",
    "description": "The FL-150 Income and Expense Declaration, the DissoMaster print-out, and how a Request for Order becomes an initial California child support order. San Diego family attorney.",
    "breadcrumb_short": "Working with a Child Support Attorney",
    "body_html": """
          <p>
            "How long until we have a support order?" is one of the first
            practical questions on a new child-support case. The honest
            answer is that a lot depends on when the FL-150 gets
            completed and how quickly a hearing date comes up in the
            San Diego Superior Court calendar. But the shape of the
            first six weeks is fairly consistent.
          </p>
          <p>
            This post walks through what actually happens between the
            intake meeting and the initial support order, so you can
            see how the case moves and where your work is needed.
          </p>

          <h2>Week 1: intake and document collection</h2>
          <p>
            The first meeting covers the basics: whether there is an
            existing family-law case open, whether the other parent is
            represented, whether the parents are married, whether there
            is a custody order, and what the timeshare with the child
            looks like today. If there is no open family-law case, we
            usually need to open one &mdash; either as part of a
            divorce, as a paternity (parentage) case under the Uniform
            Parentage Act if the parents were not married, or in some
            cases through San Diego DCSS.
          </p>
          <p>
            After intake, the first task is document collection. The
            client leaves the meeting with a specific list: the last
            three years' tax returns; the last two months of pay stubs
            (or year-to-date income statements if self-employed);
            monthly household expense figures; the current cost of
            health insurance for the child and any child-care costs;
            and, if a business is involved, its recent profit-and-loss
            statement and any recent business tax return.
          </p>

          <h2>Weeks 2-3: drafting the FL-150 and the Request for Order</h2>
          <p>
            The FL-150 Income and Expense Declaration is the core
            support document. It has to be accurate, complete, and
            supported by attached documents. Drafting a good FL-150 is
            not "fill in the blank." A W-2 employee's FL-150 might
            take an hour if the pay stubs are clean; a self-employed
            parent's FL-150 might take considerably longer.
          </p>
          <p>
            While the FL-150 is being drafted, we also draft the
            Request for Order (FL-300) itself, the proposed order
            (FL-343 or a custom order), and the supporting declaration.
            The Request for Order specifies exactly what we are asking
            for: child support in a specific amount (or "guideline"),
            add-ons allocated a specific way, retroactivity, and any
            related orders (health insurance, wage assignment).
          </p>

          <h2>Week 3: filing and service</h2>
          <p>
            Once the FL-150, RFO, and declaration are drafted, we file
            with the San Diego Superior Court and get a hearing date.
            The RFO packet is then personally served on the other
            parent (or their attorney of record if they have one),
            with at least the minimum statutory notice before the
            hearing. Service is what starts the other side's clock for
            filing a responsive declaration and their own FL-150.
          </p>

          <h2>Weeks 4-5: the other side responds; DissoMaster preview</h2>
          <p>
            After service, the other parent files a responsive
            declaration and their own FL-150. That is when both sides
            first see the actual income picture from both households.
            I run a preview DissoMaster calculation using both
            FL-150s and the current parenting-time schedule so we know
            what the guideline number looks like heading into the
            hearing.
          </p>
          <p>
            This is often the moment a settlement becomes possible.
            When both sides know the guideline number, and it lines up
            with expectations on both sides, the case can resolve by
            stipulation without a contested hearing. When it does not
            &mdash; because the FL-150 inputs are disputed, or because
            income imputation is on the table &mdash; we head into the
            hearing.
          </p>

          <aside class="blog-post__inline-cta">
            <p>
              The FL-150 is the biggest lever in the first six weeks. Get
              the FL-150 right and the case gets easier from there.
            </p>
            <p>
              Call <a href="tel:+16192502683">(619) 250-2683</a> to walk
              through the FL-150 before it gets filed.
            </p>
          </aside>

          <h2>Week 6: the hearing</h2>
          <p>
            San Diego family-law hearings on Requests for Order are
            usually short. The court has read the pleadings before the
            hearing, and the argument at the podium focuses on the
            two or three disputed inputs to the guideline calculation
            &mdash; income imputation, add-ons, timeshare percentage,
            or the retroactivity of the order. The court then runs
            DissoMaster on the record (or the parties do it on the
            record) and orders the guideline number, plus specific
            allocations of add-ons.
          </p>
          <p>
            After the hearing, the order has to be reduced to a
            written Findings and Order After Hearing (FL-340) with a
            child support attachment (FL-342). Judges sometimes hand
            over drafting to counsel, sometimes prepare their own. The
            written order is what gets served on the other side, gets
            entered as an enforceable court order, and generates the
            wage assignment.
          </p>

          <h2>What happens after the order</h2>
          <p>
            Wage assignments are mandatory on every new California
            child-support order unless waived under Family Code section
            5260 (and the waiver requires specific findings). Once the
            written order is entered, a wage assignment (FL-195) issues
            and gets served on the paying parent's employer, so the
            support comes directly from the paycheck.
          </p>
          <p>
            The order also specifies how add-ons will be paid &mdash;
            typically an equal share or an income-proportional share
            &mdash; and often has a reimbursement mechanism (usually
            30 days after the requesting parent produces a receipt).
          </p>

          <h2>Modifying or enforcing later</h2>
          <p>
            Once the initial order is entered, later work is
            modification (on a change of circumstances) or enforcement
            (when the paying parent falls behind). The modification and
            enforcement mechanics are covered in the
            <a href="/blog/child-support-in-california-what-attorneys-do.html">what-an-attorney-adds
            post</a> and the
            <a href="/practice-areas/child-support/">child support
            practice area</a>. The relevant point here is that the
            initial order is a starting point, not a permanent number
            &mdash; the case can be reopened when circumstances
            genuinely change.
          </p>

          <h2>Ready to talk it through</h2>
          <p>
            Getting an initial California child-support order takes
            preparation and follow-through, but the moves are
            specific. If you want to walk through your case, you can
            reach me at <a href="tel:+16192502683">(619) 250-2683</a>
            or through the <a href="/contact.html#form">contact
            form</a>. I appear on child-support matters at all four
            San Diego County family-law courthouses.
          </p>
""",
    "related": [
        {"url": "/practice-areas/child-support/", "category": "Practice Area", "title": "San Diego Child Support (Practice Area)"},
        {"url": "/blog/child-support-in-california-what-attorneys-do.html", "category": "Child Support", "title": "Child Support in California: What an Attorney Adds to the Guideline Number"},
        {"url": "/blog/protecting-parental-rights-in-california-custody.html", "category": "Child Custody", "title": "Protecting Parental Rights in California Custody Cases"},
    ],
})


