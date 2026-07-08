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

