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

# ---------------------------------------------------------------------------
# 11 — Guardianship Under the California Probate Code
# ---------------------------------------------------------------------------
POSTS.append({
    "slug": "guardianship-under-california-probate-code",
    "category": "Guardianship",
    "published": "2025-03-11",
    "published_pretty": "March 11, 2025",
    "title": "Guardianship Under the California Probate Code: A San Diego Overview",
    "h1": "Guardianship Under the California Probate Code: A San Diego Overview",
    "description": "Probate guardianship of the person or estate of a minor under California Probate Code sections 1500-1611, temporary vs permanent orders, and the San Diego Central Courthouse investigation process.",
    "breadcrumb_short": "Guardianship Under California Probate Code",
    "body_html": """
          <p>
            Guardianship of a minor is the legal mechanism that lets an
            adult who is not the parent make care and custody decisions
            for a child. In California, guardianship of a minor is
            primarily handled under the Probate Code (sections 1500
            through 1611) in probate court, though juvenile
            guardianships arising out of dependency proceedings are
            handled separately under Welfare and Institutions Code
            section 360 in juvenile court.
          </p>
          <p>
            This post walks through California probate guardianship of
            a minor: what it does, what it does not do, and how the
            case moves through San Diego Superior Court.
          </p>

          <h2>Guardianship of the person vs. the estate</h2>
          <p>
            California recognizes two kinds of guardianship of a minor,
            and they are decided separately.
          </p>
          <p>
            <strong>Guardianship of the person</strong> gives the
            guardian authority to have the child in their care, to
            make decisions about the child's daily life, and to
            consent to medical care, education, and the child's normal
            activities. It is what most people mean when they say
            "guardianship."
          </p>
          <p>
            <strong>Guardianship of the estate</strong> is separate and
            applies when a minor owns property (an inheritance, a
            settlement, a life-insurance proceed) that has to be
            managed until the minor turns eighteen. A guardian of the
            estate is a fiduciary who has to account to the court for
            the property.
          </p>
          <p>
            The same adult can serve as guardian of both, or the two
            roles can go to different people. When large sums are
            involved, courts sometimes separate the roles.
          </p>

          <h2>What guardianship does not do</h2>
          <p>
            Guardianship is not adoption. It does not terminate the
            parent's rights or the parent-child relationship. Parents
            retain the ability to petition to terminate the
            guardianship on a change of circumstances, and the
            guardianship itself ends automatically when the minor
            turns eighteen (unless the ward is a nonminor dependent
            under special statutes).
          </p>
          <p>
            Guardianship is also not the same as a family-law custody
            order. Custody orders in a family law case set the
            relationship between two parents. Guardianship orders in
            probate court set the relationship between a non-parent
            adult and a minor, usually because neither parent can
            care for the child right now, or because both parents
            consent.
          </p>

          <h2>When guardianship makes sense</h2>
          <p>
            The most common San Diego guardianship cases I see involve:
          </p>
          <ul>
            <li>A grandparent, aunt, or uncle raising a grandchild,
                niece, or nephew because the parents cannot (military
                deployment, incarceration, substance-use treatment,
                serious illness)</li>
            <li>A child living with a family friend whose parent has
                consented to the arrangement and the friend needs
                legal authority to enroll the child in school and
                consent to medical care</li>
            <li>A child whose parents have passed away, where a
                surviving family member is the intended caregiver</li>
            <li>A minor who has received a settlement or inheritance
                and needs a guardian of the estate to manage those
                funds</li>
          </ul>

          <h2>Filing the petition</h2>
          <p>
            A guardianship case starts with a Petition for Appointment
            of Guardian (Judicial Council form GC-210) filed in
            probate court. In San Diego County, probate guardianship
            cases are heard at the Central Courthouse downtown, in
            the probate division. The petition specifies the proposed
            guardian, identifies each parent (with addresses if
            known), states the reason guardianship is needed, and
            attaches a proposed order.
          </p>
          <p>
            Notice has to go to the child's parents, to any adult
            siblings, to grandparents, and to specified relatives
            &mdash; California notice rules for guardianship are
            broader than family-law cases, and defective notice is
            one of the most common reasons a petition gets continued
            or denied on procedural grounds.
          </p>

          <h2>The Probate Court investigator's report</h2>
          <p>
            California requires an investigation of the proposed
            guardianship before an appointment is made. The
            investigation is conducted by the Probate Court
            investigator's office (in San Diego, the Family Court
            Services / Probate Investigator's office). The
            investigator interviews the proposed guardian, the child
            (if old enough), the parents (when possible), and other
            relevant adults, visits the proposed guardian's home,
            reviews the reasons for the guardianship, and files a
            written report with recommendations to the court.
          </p>
          <p>
            The report matters. It is not a formality. A well-prepared
            proposed guardian has documents ready for the
            investigator (letters of consent from parents when
            applicable, school records, health-insurance information,
            proof of adequate housing), and can explain the
            arrangement clearly.
          </p>

          <aside class="blog-post__inline-cta">
            <p>
              Guardianship cases live or die on the investigator's
              report. Preparing for the interview and home visit is
              worth doing carefully.
            </p>
            <p>
              Call <a href="tel:+16192502683">(619) 250-2683</a> to
              walk through your case before the investigation is
              scheduled.
            </p>
          </aside>

          <h2>Temporary guardianship</h2>
          <p>
            When immediate legal authority is needed &mdash; the child
            needs to enroll in school Monday, or there is an urgent
            medical decision &mdash; the court can appoint a temporary
            guardian pending the full hearing. A Petition for
            Appointment of Temporary Guardian (GC-110) can be filed
            with the main petition or shortly after. Temporary
            guardianships last a specific period (usually up to six
            months) and expire unless renewed or replaced by the
            permanent order.
          </p>

          <h2>Objections and contested cases</h2>
          <p>
            A parent (or another interested party) can object to a
            proposed guardianship. When the parents object,
            guardianship is not granted lightly. Under Family Code
            section 3041 (which California courts apply to probate
            guardianship cases as the parental-preference standard),
            granting custody to a non-parent over a parent's
            objection requires a finding that awarding custody to the
            parent would be detrimental to the child, and that
            awarding custody to the non-parent is in the child's best
            interest. The parental-preference standard is a real
            protection for parents.
          </p>

          <h2>Termination of guardianship</h2>
          <p>
            A guardianship of a minor ends automatically at age
            eighteen, but before that, a parent can petition to
            terminate on a change of circumstances. The court applies
            a similar standard: continuing the guardianship must be
            in the child's best interest, or the change back to
            parental custody must not be detrimental. Termination
            cases are their own contested proceeding.
          </p>

          <h2>Guardianship of the estate mechanics</h2>
          <p>
            A guardian of the estate is a court-supervised fiduciary.
            The estate is inventoried and appraised, annual accountings
            are filed with the court, expenditures typically require
            court approval, and the assets are held for the minor's
            benefit until eighteen (or age twenty-five for certain
            structured settlements). Because guardianship of the
            estate is administratively intensive, families sometimes
            choose alternatives (a UTMA account, a special-needs
            trust, a settlement into a court-approved blocked account)
            depending on the size and source of the funds.
          </p>

          <h2>Ready to talk it through</h2>
          <p>
            Guardianship is one of the more procedurally specific
            areas of California family and probate practice, and
            defective filings can add months to the case. If you are
            considering a guardianship &mdash; whether as a
            grandparent, a family friend, or a parent trying to set
            up a stable arrangement for a child &mdash; the intake
            meeting is where we can walk through your specific
            situation.
          </p>
          <p>
            You can reach me at
            <a href="tel:+16192502683">(619) 250-2683</a> or through
            the <a href="/contact.html#form">contact form</a>. See
            also the <a href="/practice-areas/guardianship/">guardianship
            practice area</a> for the broader overview.
          </p>
""",
    "related": [
        {"url": "/practice-areas/guardianship/", "category": "Practice Area", "title": "San Diego Guardianship (Practice Area)"},
        {"url": "/blog/why-hire-a-family-law-attorney-in-california.html", "category": "Family Court", "title": "Why Hire a Family Law Attorney in California (and When You Might Not Need To)"},
        {"url": "/blog/navigating-san-diego-family-court.html", "category": "Family Court", "title": "Navigating San Diego Family Court: A Room-by-Room Guide"},
    ],
})

# ---------------------------------------------------------------------------
# 12 — Domestic Violence Restraining Orders
# ---------------------------------------------------------------------------
POSTS.append({
    "slug": "domestic-violence-restraining-orders-california",
    "category": "Domestic Violence",
    "published": "2025-04-08",
    "published_pretty": "April 8, 2025",
    "title": "Domestic Violence Restraining Orders in California: How the DVPA Works",
    "h1": "Domestic Violence Restraining Orders in California: How the DVPA Works",
    "description": "Emergency protective orders, temporary restraining orders, long-term DVROs under the California DVPA, and the Family Code section 3044 custody presumption. San Diego family attorney.",
    "breadcrumb_short": "DV Restraining Orders in California",
    "body_html": """
          <p>
            Domestic Violence Restraining Orders (DVROs) are one of the
            fastest-moving areas of California family law. The California
            Domestic Violence Prevention Act (Family Code sections 6200
            through 6460) creates a specific set of orders designed to
            give immediate protection while a case is investigated and
            heard. Understanding the layers &mdash; and how each order
            fits with the others &mdash; is important whether you are
            seeking protection or responding to a request.
          </p>
          <p>
            This post walks through the four kinds of orders California
            uses in a DV situation, how the DVPA defines "abuse," and
            the Family Code section 3044 custody presumption that
            attaches once a DVRO issues.
          </p>

          <h2>What "abuse" means under the DVPA</h2>
          <p>
            The DVPA definition of abuse is broader than physical
            violence. Under Family Code section 6203, abuse includes
            intentionally or recklessly causing or attempting to cause
            bodily injury; sexual assault; placing a person in
            reasonable apprehension of imminent serious bodily injury
            to that person or another; and behavior that has been or
            could be enjoined under Family Code section 6320.
          </p>
          <p>
            Section 6320, in turn, covers a broad range of conduct
            including molesting, attacking, striking, stalking,
            threatening, harassing, disturbing the peace of the other
            party, and other conduct. The California Supreme Court has
            explained that "disturbing the peace" means conduct that
            destroys the mental or emotional calm of the other party
            &mdash; a standard that reaches non-physical conduct
            including coercive control.
          </p>
          <p>
            The DVPA applies to specific relationships listed in
            Family Code section 6211: spouses and former spouses,
            cohabitants and former cohabitants, dating or engaged
            partners, parents of a common child, and family members
            related by blood or marriage within specified degrees.
            It does not apply to co-workers, neighbors, or strangers
            &mdash; those situations may need a civil harassment
            restraining order (a separate statute).
          </p>

          <h2>Layer 1: Emergency Protective Orders (EPO)</h2>
          <p>
            An Emergency Protective Order is issued by a judicial
            officer at the request of law enforcement, usually in
            response to an on-scene call. An EPO can be requested at
            any hour, is issued verbally and then reduced to writing,
            and lasts up to seven calendar days or five court days,
            whichever is shorter. It is the immediate protection
            layer.
          </p>
          <p>
            An EPO gives law enforcement authority to arrest for
            violation, and provides the protected person time to seek
            a longer restraining order without leaving them
            unprotected. Not every DV situation involves an EPO
            &mdash; only situations where law enforcement is called
            and requests one.
          </p>

          <h2>Layer 2: Temporary Restraining Orders (TRO)</h2>
          <p>
            A Temporary Restraining Order under the DVPA is what the
            protected party requests directly from the court. A TRO
            application (Judicial Council form DV-100 and related
            forms) is filed with a supporting declaration describing
            the incidents and requesting specific orders (stay-away,
            move-out, no-contact, temporary custody, temporary
            visitation, firearms surrender).
          </p>
          <p>
            The court typically decides the TRO on the same day the
            application is filed, based on the declaration. If
            granted, the TRO issues and remains in effect until the
            noticed hearing on the long-term restraining order,
            usually within 21 to 25 days.
          </p>
          <p>
            The TRO gets personally served on the restrained party.
            It is not effective until service &mdash; enforceability
            depends on proof the restrained party had notice of the
            order.
          </p>

          <aside class="blog-post__inline-cta">
            <p>
              A well-prepared TRO application includes a detailed
              declaration, specific requested orders, and any
              supporting exhibits (photos, medical records, text
              messages). The declaration is the case at the TRO
              stage.
            </p>
            <p>
              Call <a href="tel:+16192502683">(619) 250-2683</a> to
              walk through your DVRO application before it goes to
              court.
            </p>
          </aside>

          <h2>Layer 3: The long-term hearing</h2>
          <p>
            Within 21 to 25 days of the TRO, the court holds a
            noticed hearing on whether to issue a long-term
            restraining order (Family Code section 6345, up to five
            years, renewable). Both parties can appear, present
            evidence, testify, and cross-examine.
          </p>
          <p>
            At the long-term hearing, the burden is on the party
            seeking the order to prove abuse by a preponderance of
            the evidence. That is a lower standard than a criminal
            trial, but the evidence still has to be admissible and
            credible. Photos, medical records, texts, witnesses, and
            recorded incidents are all standard exhibits.
          </p>
          <p>
            The responding party can present their own evidence and
            can testify. Cross-examination is available (subject to
            California's specific rules for DVROs). This is a real
            evidentiary hearing, not a formality.
          </p>

          <h2>Layer 4: renewal</h2>
          <p>
            A five-year DVRO can be renewed at the request of the
            protected party under Family Code section 6345. Renewal
            does not require a new incident of abuse. Under the
            California Supreme Court's <em>Ritchie v. Konrad</em>
            decision, the standard is whether the protected party has
            a reasonable apprehension of future abuse. That is
            frequently satisfied by the original abuse plus
            circumstances since (continued contact attempts,
            proximity, ongoing custody disputes). Renewal can be for
            five years or permanent.
          </p>

          <h2>The Family Code section 3044 custody presumption</h2>
          <p>
            When a DVRO issues, Family Code section 3044 creates a
            rebuttable presumption that awarding sole or joint
            physical or legal custody to the restrained parent is
            detrimental to the child. The presumption applies for
            five years after the finding of abuse.
          </p>
          <p>
            The presumption is rebuttable but the restrained parent
            has to affirmatively address specific statutory factors:
            best-interest of the child, completion of a batterer's
            intervention program, completion of any court-ordered
            substance-use program, compliance with any probation or
            parole, and non-commission of further acts of DV. Section
            3044 is a substantial thumb on the scale in the custody
            analysis, and it is one of the most consequential
            downstream effects of a DVRO.
          </p>

          <h2>Firearm surrender under section 6389</h2>
          <p>
            A person subject to a DVRO is prohibited from owning or
            possessing firearms and ammunition under Family Code
            section 6389 for the duration of the order. Any firearms
            in the restrained party's possession have to be
            surrendered to law enforcement or sold to a licensed
            dealer within 24 hours of service, with proof of
            compliance filed with the court within 48 hours. This is
            not optional, and non-compliance is a criminal offense.
          </p>

          <h2>Responding to a DVRO request</h2>
          <p>
            If you have been served with a TRO, the response you file
            for the long-term hearing (form DV-120 and supporting
            declaration) is the case. Being able to explain the
            incidents in context, produce corroborating documents,
            and present witnesses is what shapes the outcome. This is
            not the moment for a lengthy narrative about the other
            party; it is the moment for a specific, factual
            response.
          </p>

          <h2>Ready to talk it through</h2>
          <p>
            California DVRO cases move fast, and the DVPA gives real
            protection when it applies. If you need to file a request
            or are responding to one, the intake meeting is where we
            walk through the incidents, the evidence, and the
            downstream custody and firearm consequences. You can
            reach me at <a href="tel:+16192502683">(619) 250-2683</a>
            or through the <a href="/contact.html#form">contact
            form</a>. See also the
            <a href="/practice-areas/domestic-violence/">domestic
            violence practice area</a>.
          </p>
""",
    "related": [
        {"url": "/practice-areas/domestic-violence/", "category": "Practice Area", "title": "San Diego Domestic Violence (Practice Area)"},
        {"url": "/blog/navigating-san-diego-family-court.html", "category": "Family Court", "title": "Navigating San Diego Family Court: A Room-by-Room Guide"},
        {"url": "/blog/protecting-parental-rights-in-california-custody.html", "category": "Child Custody", "title": "Protecting Parental Rights in California Custody Cases"},
    ],
})

# ---------------------------------------------------------------------------
# 13 — Navigating San Diego Family Court
# ---------------------------------------------------------------------------
POSTS.append({
    "slug": "navigating-san-diego-family-court",
    "category": "Family Court",
    "published": "2025-05-13",
    "published_pretty": "May 13, 2025",
    "title": "Navigating San Diego Family Court: A Room-by-Room Guide",
    "h1": "Navigating San Diego Family Court: A Room-by-Room Guide",
    "description": "The four San Diego family-law courthouses, Requests for Order, ex parte applications, and what a day of hearing actually looks like. San Diego family attorney Brian Burkett.",
    "breadcrumb_short": "Navigating San Diego Family Court",
    "body_html": """
          <p>
            San Diego family court is not one building. It is four
            courthouses, each with its own calendar, its own judicial
            officers, and its own way of doing things. Add on the
            various satellite functions &mdash; Family Court Services,
            the self-help center, the family-law facilitator's office,
            the family-law clerk's window &mdash; and even people who
            work in the legal system regularly can get turned around.
          </p>
          <p>
            This post walks through the San Diego family-court
            geography and the practical mechanics of a Request for
            Order, an ex parte application, and a hearing day.
          </p>

          <h2>The four family-law courthouses</h2>
          <p>
            San Diego County has four courthouses that hear family-law
            matters, and which one hears a case depends on where the
            parties live:
          </p>
          <ul>
            <li><strong>Central Courthouse</strong> &mdash; 1100 Union
                Street, San Diego. Downtown. Handles cases from most
                of the City of San Diego and central-county
                communities. Also home to the Probate Division that
                hears probate guardianship of minors.</li>
            <li><strong>North County Regional Center</strong> &mdash;
                325 South Melrose Drive, Vista. Handles cases from
                North County: Oceanside, Carlsbad, Encinitas, San
                Marcos, Escondido, Vista, Fallbrook, and adjacent
                communities.</li>
            <li><strong>East County Regional Center</strong> &mdash;
                250 East Main Street, El Cajon. Handles cases from
                East County: El Cajon, La Mesa, Lakeside, Santee,
                Spring Valley, Alpine, and adjacent communities.</li>
            <li><strong>South County Regional Center</strong> &mdash;
                500 Third Avenue, Chula Vista. Handles cases from
                South County: Chula Vista, National City, Imperial
                Beach, Bonita, and adjacent communities.</li>
          </ul>
          <p>
            I appear on family-law matters at all four courthouses. If
            a client's residence is on the border between two
            courthouse jurisdictions, we look at where each party
            lives and where the child is enrolled in school to decide
            filing venue.
          </p>

          <h2>The Family Court Services calendar</h2>
          <p>
            Whenever custody or visitation is contested, San Diego
            routes the case through Family Court Services (FCS)
            mediation under Family Code section 3170 before the
            contested hearing. FCS sessions are scheduled at the
            courthouse where the case is filed, and the FCS
            counselor works from that same courthouse.
          </p>
          <p>
            FCS in San Diego is a recommending mediation, which means
            the counselor can send a written recommendation to the
            judge if the parents cannot reach agreement. Preparing for
            FCS is one of the most impactful things a custody
            attorney does &mdash; walking into FCS with a proposed
            parenting plan, a school calendar, and specific
            behavioral examples is much stronger than showing up
            without them.
          </p>

          <h2>Request for Order &mdash; how it moves</h2>
          <p>
            The workhorse motion in California family court is the
            Request for Order (RFO) &mdash; Judicial Council form
            FL-300. An RFO asks the court for orders on any issue in
            the case: custody, visitation, temporary support,
            attorneys' fees, use of the family residence, orders
            about specific assets. The RFO packet includes the
            request itself, a supporting declaration, any FL-150
            required (for support requests), and a proposed order.
          </p>
          <p>
            After the RFO is filed, the family-law clerk assigns a
            hearing date, typically six to ten weeks out depending on
            the department calendar. The moving party has to
            personally serve the RFO on the other party (or their
            attorney of record) with at least the minimum statutory
            notice. The responding party can file a responsive
            declaration and their own supporting exhibits.
          </p>
          <p>
            When the hearing day comes, the judge has read the
            filings before the hearing. The oral argument focuses on
            the two or three disputed issues, and the court makes
            orders on the record. A written Findings and Order After
            Hearing (FL-340 and any subject-specific attachments)
            memorializes the ruling.
          </p>

          <h2>Ex parte applications</h2>
          <p>
            When something needs to be addressed on shortened notice
            &mdash; a child is about to be taken out of state, a
            house is about to be sold, there is an urgent safety
            issue &mdash; an ex parte application (California Rules
            of Court 5.151) asks the court to hear the matter within
            days rather than weeks.
          </p>
          <p>
            Ex parte relief in family court is not a lower bar. The
            application has to show, on the declaration, an
            irreparable harm to be prevented or an immediate danger
            or other statutory basis for shortened notice. Notice
            still has to go to the other side (either the day before
            the ex parte hearing or a specific number of hours,
            depending on department rules), and the other side can
            appear and be heard.
          </p>
          <p>
            When ex parte relief is not appropriate, the court can
            still convert the application into an "order to show
            cause" on a longer timeline than an ex parte but shorter
            than a standard RFO calendar.
          </p>

          <aside class="blog-post__inline-cta">
            <p>
              Knowing which motion to file and which courthouse to
              file it in is a real part of San Diego family-law
              practice. Getting either wrong can add weeks to a
              case.
            </p>
            <p>
              Call <a href="tel:+16192502683">(619) 250-2683</a> or
              <a href="/contact.html#booking">book a consultation</a>
              to walk through your case.
            </p>
          </aside>

          <h2>A hearing day, start to finish</h2>
          <p>
            Family-law calendars in San Diego typically start at 8:30
            a.m. Show up at least 20 minutes early to get through
            courthouse security, find the department, and check in
            with the courtroom clerk. Bring photo ID for security,
            two copies of any exhibits you plan to reference, and
            proof of service if applicable.
          </p>
          <p>
            When the calendar is called, the courtroom clerk usually
            reads through the matters set for that morning and takes
            attendance. Some cases resolve on stipulation in the
            hallway before the calendar is called; those get set
            aside for the stipulation to be reduced to writing.
            Contested matters get argued in the order the department
            takes them, sometimes by 9:00 a.m. for the shortest
            matters, sometimes later for cases that need a longer
            record.
          </p>
          <p>
            Family-law hearings are on the record but not always
            recorded for later transcript purposes unless a court
            reporter is present. If you want a record for a possible
            appeal, arranging a court reporter (or an electronic
            recording if the department allows it) is a step to
            take before the hearing.
          </p>

          <h2>The self-help center and the family-law facilitator</h2>
          <p>
            Every San Diego family-law courthouse has a self-help
            center and a family-law facilitator's office. These are
            court-attached programs that help parties without
            attorneys prepare specific forms, understand basic
            procedure, and file the right paperwork. They cannot give
            legal advice, and they are not counsel for either party,
            but for straightforward matters (uncontested judgments,
            simple modifications) they can be enough to get a
            filing done.
          </p>
          <p>
            The self-help center is not a substitute for counsel in
            contested cases. If your case involves any of a serious
            custody dispute, complex property, or a substantial
            support number, an attorney adds value the self-help
            staff cannot provide. See
            <a href="/blog/why-hire-a-family-law-attorney-in-california.html">the
            post on when to hire an attorney</a> for more on the
            trade-offs.
          </p>

          <h2>Ready to talk it through</h2>
          <p>
            San Diego family court is workable once you know the
            layout. If you have a case coming up at one of the four
            courthouses and want to walk through the mechanics, you
            can reach me at
            <a href="tel:+16192502683">(619) 250-2683</a> or through
            the <a href="/contact.html#form">contact form</a>. See
            also the <a href="/practice-areas/family-court/">family
            court practice area</a>.
          </p>
""",
    "related": [
        {"url": "/practice-areas/family-court/", "category": "Practice Area", "title": "San Diego Family Court (Practice Area)"},
        {"url": "/blog/why-hire-a-family-law-attorney-in-california.html", "category": "Family Court", "title": "Why Hire a Family Law Attorney in California (and When You Might Not Need To)"},
        {"url": "/blog/domestic-violence-restraining-orders-california.html", "category": "Domestic Violence", "title": "Domestic Violence Restraining Orders in California: How the DVPA Works"},
    ],
})

# ---------------------------------------------------------------------------
# 14 — Preliminary Declaration of Disclosure
# ---------------------------------------------------------------------------
POSTS.append({
    "slug": "preliminary-declaration-of-disclosure-california",
    "category": "Divorce",
    "published": "2025-06-17",
    "published_pretty": "June 17, 2025",
    "title": "The Preliminary Declaration of Disclosure in a California Divorce",
    "h1": "The Preliminary Declaration of Disclosure in a California Divorce",
    "description": "The FL-140, FL-142, and FL-150 that make up a California Preliminary Declaration of Disclosure, why it exists, and what happens if a spouse hides an asset. San Diego family attorney.",
    "breadcrumb_short": "Preliminary Declaration of Disclosure",
    "body_html": """
          <p>
            Every California divorce runs on financial disclosure.
            Whether the case is uncontested and heading for a
            stipulated judgment, or contested and heading for trial,
            both spouses have to disclose their assets, debts, income,
            and expenses to each other. That obligation is not
            optional and it is not paperwork &mdash; it is the
            foundation the court builds a fair division on.
          </p>
          <p>
            This post explains the Preliminary Declaration of
            Disclosure (PDOD) in a California divorce: what forms it
            includes, why California requires it, what a good PDOD
            looks like, and what happens when a spouse hides an
            asset.
          </p>

          <h2>Why California requires disclosure</h2>
          <p>
            The California Legislature codified fiduciary duties
            between spouses in Family Code section 721. Spouses have
            the highest good-faith duty to each other in their
            financial dealings, on par with a business partner's
            duty to another partner. That duty extends into the
            divorce process. Family Code section 2100 declares the
            state's policy: the divorcing parties are required to
            fully and accurately disclose the identity and value of
            all assets and debts, and to update those disclosures as
            circumstances change.
          </p>
          <p>
            The mechanism the Family Code uses to enforce that duty
            is the disclosure regime in sections 2100 through 2113:
            a Preliminary Declaration of Disclosure early in the
            case, a Final Declaration of Disclosure before judgment
            (with limited waivability), and remedies (up to
            set-aside of the judgment) if the disclosure obligation
            is violated.
          </p>

          <h2>The forms that make up a PDOD</h2>
          <p>
            The Preliminary Declaration of Disclosure is a package of
            four Judicial Council forms:
          </p>
          <ul>
            <li><strong>FL-140 &mdash; Declaration of Disclosure.</strong>
                The cover form. It confirms that the party has served
                the other required disclosure documents.</li>
            <li><strong>FL-142 &mdash; Schedule of Assets and Debts</strong>
                (or, in some cases, FL-160 Property Declaration). A
                comprehensive itemization of every asset and every
                debt the party knows about, including retirement
                accounts, real estate, bank accounts, brokerage
                accounts, business interests, vehicles, jewelry, and
                credit-card balances.</li>
            <li><strong>FL-150 &mdash; Income and Expense Declaration.</strong>
                Detailed income for the past twelve months, current
                monthly income and expenses, and information about
                assets. FL-150 is also the form used for support
                calculations.</li>
            <li>The <strong>tax returns</strong> for the two years
                preceding the disclosure &mdash; complete returns
                with all schedules and attachments, not just the
                summary pages.</li>
          </ul>
          <p>
            All four elements are served on the other party (or their
            attorney) and the FL-140 is filed with the court to
            document that service occurred. The FL-142 and FL-150
            themselves are typically not filed &mdash; they are
            exchanged between the parties.
          </p>

          <h2>What a well-prepared FL-142 looks like</h2>
          <p>
            An FL-142 is not filled in from memory. It is filled in
            with documents. For a straightforward case, that means
            recent statements for every bank account, brokerage
            account, retirement account, and credit card, plus a
            recent mortgage statement, vehicle titles or DMV
            registration, and life-insurance and health-insurance
            declaration pages.
          </p>
          <p>
            For a higher-asset case, the FL-142 gets more work:
            business valuations (or at least business tax returns
            for the last few years and current profit-and-loss
            statements), appraisals of real estate, statements for
            stock plans (RSUs, ISOs, ESPPs), and documentation of
            any separate-property claims (pre-marital account
            balances traced forward, gift or inheritance documents).
          </p>

          <h2>What a well-prepared FL-150 looks like</h2>
          <p>
            The FL-150 is the income and expense declaration. For a
            W-2 employee, the income section is anchored by pay
            stubs and the most recent W-2. For a self-employed
            party, the income section is a considerably more
            substantial drafting exercise &mdash; business gross
            income, deductible business expenses, and personal
            (non-deductible) draws all have to be broken out
            clearly.
          </p>
          <p>
            The expense section on the FL-150 has to reflect actual
            monthly cash flow. Inflated expenses hurt credibility;
            deflated expenses can undercut a support claim.
            Well-prepared FL-150 expenses come from three months of
            bank and credit card statements analyzed carefully.
          </p>

          <aside class="blog-post__inline-cta">
            <p>
              The PDOD is not a formality. In every California
              divorce I handle, we treat the PDOD as the foundation
              of the property division and the support order.
            </p>
            <p>
              Call <a href="tel:+16192502683">(619) 250-2683</a> to
              walk through what your PDOD should look like.
            </p>
          </aside>

          <h2>Timing</h2>
          <p>
            The petitioner is supposed to serve the Preliminary
            Declaration of Disclosure within 60 days of filing the
            Petition. The respondent is supposed to serve within 60
            days of filing the Response. In practice, the deadlines
            are often missed by both sides &mdash; the case moves at
            the pace of the case &mdash; but the earlier the PDOD
            gets served, the sooner both parties know what the
            picture actually is, and the sooner meaningful
            settlement conversations become possible.
          </p>

          <h2>The Final Declaration of Disclosure</h2>
          <p>
            California also requires a Final Declaration of Disclosure
            before entry of judgment (Family Code section 2105). The
            final version updates the PDOD to current information
            and confirms nothing has been left off. The parties can
            <strong>mutually waive</strong> the Final Declaration by
            executing a written waiver on Judicial Council form
            FL-144, which is common in cases where the PDOD is
            recent and both sides are comfortable it is complete.
            Waiver requires both sides to sign; it cannot be
            unilateral.
          </p>

          <h2>What happens if a spouse hides an asset</h2>
          <p>
            The remedy for a failed or fraudulent disclosure is
            significant. Family Code section 2107 authorizes the
            court to impose monetary sanctions and attorney's fees
            for a party's failure to comply with disclosure
            obligations. Family Code section 1101 governs breaches
            of the fiduciary duty between spouses and, in the case
            of a fraudulent breach, permits the court to award 100%
            of the value of the undisclosed asset to the injured
            spouse.
          </p>
          <p>
            The California Supreme Court's decision in <em>Marriage
            of Rossi</em> is the classic example: a wife who won a
            $1.3 million lottery jackpot and concealed it during
            the divorce lost the entire jackpot to her ex-husband
            under section 1101. The section is a real deterrent.
          </p>

          <h2>Set-aside after judgment</h2>
          <p>
            Family Code section 2122 permits the court to set aside
            a judgment in specific circumstances, including
            fraud, perjury, and failure to comply with the
            disclosure requirements of Chapter 9. Discovery of a
            hidden asset after judgment is a significant post-
            judgment matter that can, in the right case, reopen the
            property division. The time limits for a set-aside vary
            depending on which ground applies, so timing matters.
          </p>

          <h2>Ready to talk it through</h2>
          <p>
            The Preliminary Declaration of Disclosure is one of the
            most important documents in a California divorce, and
            it is worth doing right. If you want to talk through
            what your PDOD should look like, you can reach me at
            <a href="tel:+16192502683">(619) 250-2683</a> or through
            the <a href="/contact.html#form">contact form</a>. See
            also the <a href="/practice-areas/divorce/">divorce
            practice area</a> and
            <a href="/blog/california-community-property-division.html">community
            property post</a>.
          </p>
""",
    "related": [
        {"url": "/practice-areas/divorce/", "category": "Practice Area", "title": "San Diego Divorce (Practice Area)"},
        {"url": "/blog/california-community-property-division.html", "category": "Divorce", "title": "California Community Property: How Marital Assets and Debts Get Divided"},
        {"url": "/blog/how-a-divorce-attorney-navigates-california-process.html", "category": "Divorce", "title": "How a San Diego Divorce Attorney Navigates the California Dissolution Process"},
    ],
})

# ---------------------------------------------------------------------------
# 15 — Why Hire a Family Law Attorney
# ---------------------------------------------------------------------------
POSTS.append({
    "slug": "why-hire-a-family-law-attorney-in-california",
    "category": "Family Court",
    "published": "2025-08-19",
    "published_pretty": "August 19, 2025",
    "title": "Why Hire a Family Law Attorney in California (and When You Might Not Need To)",
    "h1": "Why Hire a Family Law Attorney in California (and When You Might Not Need To)",
    "description": "An honest look at when a California family-law attorney adds value, when a self-help center is enough, and the middle-ground option of unbundled representation. San Diego attorney Brian Burkett.",
    "breadcrumb_short": "Why Hire a Family Law Attorney",
    "body_html": """
          <p>
            "Do I even need an attorney?" is a fair question, and it
            deserves an honest answer. Not every California family-law
            matter requires representation. The self-help center at
            each San Diego courthouse exists because a lot of
            family-law paperwork is straightforward, and the family-
            law facilitator's office can help pro-per parties get
            uncontested filings across the finish line.
          </p>
          <p>
            That said, plenty of cases do call for an attorney. This
            post lays out the honest version: when I think an
            attorney genuinely adds value, when the self-help route
            is enough, and the middle-ground option most people do
            not know exists.
          </p>

          <h2>When an attorney genuinely adds value</h2>

          <h3>Contested custody</h3>
          <p>
            A contested custody case &mdash; where the parents
            disagree on legal custody, physical custody, or the
            parenting-time schedule &mdash; is the case where I most
            often think representation makes the biggest difference.
            The moves in the first ninety days shape the case:
            preparing for Family Court Services mediation, drafting
            a specific proposed parenting plan, drafting the
            declaration for the initial hearing, and (if it comes
            to it) preparing for a section 3111 evaluation or a
            minor's counsel appointment.
          </p>
          <p>
            These are not paperwork moves. They are strategic and
            evidentiary, and they compound &mdash; the FCS session
            in month one shapes the recommendation in month two,
            which shapes the hearing in month three, which shapes
            the parenting plan the family lives with for years.
          </p>

          <h3>Contested support with complex income</h3>
          <p>
            California child and spousal support calculations start
            with each spouse's income. If either party is
            self-employed, commissioned, seasonal, has equity comp
            (RSUs, options), or has income that runs through
            multiple LLCs, the FL-150 becomes a substantial drafting
            exercise. Getting the FL-150 wrong locks in an incorrect
            support number for months.
          </p>

          <h3>Higher-asset divorces</h3>
          <p>
            Cases with a house bought before marriage, a business
            started before marriage, retirement accounts with
            pre-marital and marital contributions, or any hybrid
            asset benefit from someone who can perform (or coordinate)
            the tracing analysis. A community-property division that
            ignores a Moore/Marsden calculation or a Van Camp
            /Pereira analysis can move six-figure sums in one
            direction or the other.
          </p>

          <h3>Any case with a domestic-violence issue</h3>
          <p>
            DVRO cases move fast. The TRO application, the response,
            the noticed hearing within three weeks, and the downstream
            Family Code section 3044 custody presumption all
            happen in a short window and each has a real record to
            build. This is not a case where the self-help center is
            enough.
          </p>

          <h3>Any move-away case</h3>
          <p>
            Custody move-away requests (under <em>Marriage of
            LaMusga</em>) are among the highest-stakes contested
            hearings California family court sees. Preparing the
            record on the move-away factors &mdash; distance,
            reasons, impact on the child, existing relationship
            with each parent &mdash; is a substantial undertaking.
          </p>

          <h3>Guardianship of a minor</h3>
          <p>
            California guardianship of a minor is procedurally
            specific, requires notice to a broader set of relatives
            than family-law cases, and involves an investigator's
            report the court relies on. A defective filing can set
            the case back months.
          </p>

          <h2>When you might not need an attorney</h2>
          <p>
            On the other end of the spectrum, there are cases where
            the self-help center and the family-law facilitator's
            office are enough.
          </p>

          <h3>Fully uncontested divorces with no minor children and modest assets</h3>
          <p>
            If both spouses agree on every issue, have limited
            community property, no minor children, and no support
            claims, the self-help center can help walk both parties
            through an uncontested judgment. The FL-100 petition,
            the response, the FL-140/142/150 disclosures, a
            stipulated Marital Settlement Agreement, and the FL-180
            proposed judgment are all forms the self-help center
            regularly assists with.
          </p>

          <h3>Simple modifications by agreement</h3>
          <p>
            If both parents agree to modify a custody schedule or a
            support number, and the modification is straightforward,
            a Stipulation and Order (FL-350 for custody or a
            comparable form for support) can be prepared without
            counsel. What both parties are signing has to be
            understood, but the drafting is not always heavy.
          </p>

          <h3>Enforcement of a clear order</h3>
          <p>
            If a support order is being violated and the paying
            party is a W-2 employee, the San Diego County Department
            of Child Support Services can enforce the order at no
            cost. DCSS uses wage assignments, tax intercepts, and
            license suspensions. The trade-off is that DCSS controls
            the pace and priorities of the case, not the receiving
            parent.
          </p>

          <aside class="blog-post__inline-cta">
            <p>
              I would rather have a fifteen-minute conversation with
              you and honestly tell you an attorney is not necessary
              in your case than take on a matter that would be a
              waste of your money.
            </p>
            <p>
              Call <a href="tel:+16192502683">(619) 250-2683</a> or
              <a href="/contact.html#booking">book a consultation</a>
              &mdash; the first meeting is the right place to make
              that call.
            </p>
          </aside>

          <h2>The middle ground: unbundled representation</h2>
          <p>
            California allows attorneys to provide "unbundled" or
            "limited scope" representation, where the attorney is
            engaged for specific tasks rather than the entire case.
            California Rules of Court 5.425 governs limited-scope
            representation in family law. Common unbundled tasks
            include:
          </p>
          <ul>
            <li>Reviewing draft documents the client has prepared</li>
            <li>Drafting a Request for Order and declaration for a
                client who will file and appear on their own</li>
            <li>Coaching a client through a mediation session or FCS
                appointment</li>
            <li>Preparing the client for a single hearing (a
                document walkthrough, a talking-points outline, a
                mock cross-examination)</li>
            <li>Drafting the written Findings and Order After
                Hearing after a client wins on their own</li>
          </ul>
          <p>
            Unbundled representation costs meaningfully less than
            full representation, because you are paying for specific
            hours rather than a full retainer, and it can be a good
            fit for clients who can handle most of the case
            themselves but want professional help at a specific
            pressure point.
          </p>

          <h2>What a first consultation is actually for</h2>
          <p>
            An intake consultation is the right way to make the
            decision. In thirty to sixty minutes, we can walk
            through the case: what issues are on the table, what
            the other side has done, what the schedule of upcoming
            court dates looks like, and honestly whether the case
            needs full representation, unbundled help, or nothing.
          </p>
          <p>
            The consultation itself is not a commitment. If the case
            does not need me, I say so. If a specific piece of it
            would benefit from limited-scope help, I say so. If the
            case needs full representation, we talk through what
            that engagement would look like, and you decide.
          </p>

          <h2>Ready to talk it through</h2>
          <p>
            California family court is workable, and the moves are
            specific. Sometimes an attorney is the right investment,
            and sometimes the self-help center will do the job. The
            way to know which one your case needs is to sit down and
            look at it.
          </p>
          <p>
            You can reach me at
            <a href="tel:+16192502683">(619) 250-2683</a> or through
            the <a href="/contact.html#form">contact form</a>. See
            also the <a href="/practice-areas/family-court/">family
            court practice area</a> and the
            <a href="/blog/navigating-san-diego-family-court.html">room-by-room
            guide to San Diego family court</a>.
          </p>
""",
    "related": [
        {"url": "/practice-areas/family-court/", "category": "Practice Area", "title": "San Diego Family Court (Practice Area)"},
        {"url": "/blog/navigating-san-diego-family-court.html", "category": "Family Court", "title": "Navigating San Diego Family Court: A Room-by-Room Guide"},
        {"url": "/blog/how-a-divorce-attorney-navigates-california-process.html", "category": "Divorce", "title": "How a San Diego Divorce Attorney Navigates the California Dissolution Process"},
    ],
})



