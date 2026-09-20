# Making a social-impact claim that survives a judge

The failure mode is not "we didn't mention impact." It is that the impact
paragraph is the only paragraph with nothing checkable in it, and judges read
that as the weakest link in an otherwise strong page. `WINNING-WRITEUPS.md`
measured what the top of two fields actually does instead.

## The rule

**Never write an unanchored magnitude.** "Millions of people struggle with X",
"a huge problem", "the industry loses billions" — these have no source, no
measurement, no institution, no instance. They cost you more than saying nothing,
because they signal that the rest of the numbers may be decorative too.

Every impact claim must sit on one of four anchors. Ranked by cost to obtain:

| # | anchor | what it is | cost | example from the field |
| --- | --- | --- | --- | --- |
| 4 | **Concrete recurring instance** | one specific event, at a specific time, that repeats | free | *"Cancelled appointments go up at 8:00 and are gone by 8:01."* (`cedarfield`) |
| 3 | **Named institution** | a real org that vouches, partners, or supplies the data | an email | California Homeless Youth Project (`haven`) |
| 2 | **Self-measurement** | trials you ran, an ablation, before/after | hours | 95 trials, 41% accuracy decline (`kaiju`) |
| 1 | **Cited public population** | a public dataset, named, with a number a stranger re-fetches | ~1 hour | 20,460 establishments (`placard`); 3,400+ exonerations, National Exoneration Registry (`libertas`) |

Anchor 4 is free and nearly as persuasive as anchor 1. **If you have no data,
you still have no excuse** — you have anchor 4. Two entries in the top 12 of a
2,392-entry field used nothing else.

Stack two anchors and you are above almost everyone.

## The procedure

### 1 · Write the harm as one sentence with a time in it

Not "users find the process difficult." Instead: *who*, doing *what*, at *what
moment*, loses *what*.

> ✗ "Homeless youth struggle to access services."
> ✓ "A 19-year-old is asked for the same intake history at the fourth agency in a
>   week, and each retelling is the reason some of them stop at the third."

The second is anchor 4 and costs nothing. Test it: could a judge picture the
clock? If not, it is still abstract.

### 2 · Find the denominator before you look for a statistic

The mistake is searching for "how big is this problem" and grabbing the largest
number found. Instead decide, in advance, **what population you are entitled to
claim** — then go find its size.

- Too wide: "everyone who uses the web" — a judge discounts it instantly.
- Too narrow: your three interviewees — no magnitude at all.
- Right: the occupational, institutional, or eligibility category your tool
  actually serves, which a public dataset already counts.

`placard` did not claim "chemical safety is a huge problem." It claimed the
number of *establishments that ship placarded hazmat*, because that is exactly
who would open the tool.

### 3 · Get the number from a source a judge can re-fetch, keyless

Reproducible beats impressive. A modest number a stranger re-derives in one
command outscores a big number from a blog post. Candidates, in rough order of
usefulness — **verify keylessness and the exact endpoint yourself before citing,
terms change:**

| domain | source | notes |
| --- | --- | --- |
| employment / occupations | US BLS OEWS (`api.bls.gov/publicAPI`) | v1 is keyless; v2 wants a free key. Counts *jobs*, excludes self-employed |
| EU labour | Eurostat dissemination API | keyless, SDMX/JSON |
| global development | World Bank Indicators API | keyless, very wide coverage |
| health | WHO GHO OData | keyless |
| regulation / legal text | eCFR API, govinfo | keyless; eCFR is editorial, GPO editions are authoritative |
| breaches / security | Have I Been Pwned `/api/v3/breaches` | breach *list* is keyless; account lookup is not |
| research volume | OpenAlex, Crossref | keyless, good for "how much is published on X" |
| US demographics | Census Bureau API | key is free and instant |
| open data | data.gov, national portals | varies |

`build/evidence/population.py` is the worked example: it queries live, sums five
occupations, and **prints its own caveat**.

### 4 · State the caveat yourself, in the same breath

This is where most impact paragraphs are won or lost. An occupation count is an
**upper bound on an audience**, not a count of people who need your thing. Say so.

> "5,996,610 US wage-and-salary jobs sit in the five roles this is for. That is a
> ceiling on the audience, not a count of people who need it — and it excludes
> the self-employed, which is why the Occupational Outlook Handbook puts
> bookkeepers at 1,532,400 where OEWS says 1,373,680. Two federal programs
> counting one occupation. The re-derivable one is cited here."

Disclosing the disagreement scored better than picking the bigger number. Every
judge in our run treated self-correction as a reason to trust the other numbers.

### 5 · Convert magnitude into a per-unit stake

A population alone is inert. Multiply it by what each one loses, and say which
half is measured and which is assumed.

> "N people × T minutes each" — where N is cited and T is *your measurement* from
> anchor 2, not a guess. If T is a guess, say "assumed" and give the range.

### 6 · Close the loop back to the product

The last sentence of the impact section must name what stops happening. Judge
Warren's test — *would I use the finished product* — and Maria's *who pays* both
land here.

> ✓ "The fourth intake becomes the first one that carries forward."

## The paragraph template

Five sentences. Each does one job.

1. **The instance.** One person, one moment, one loss. (anchor 4)
2. **The generalisation.** "Same story for X, Y, Z" — proves it is not an anecdote.
3. **The denominator.** The counted population, with its source named. (anchor 1 or 3)
4. **The caveat.** What that number is *not*, in your own words.
5. **The stake removed.** What stops happening when this exists.

Worked, in the shape `cedarfield` and `placard` each used half of:

> Cancelled clinic appointments are released at 8:00 and gone by 8:01. Course
> seats, visa slots, and concert tickets work the same way. The people who lose
> that race every time are the ones using a switch, a head pointer, or voice
> control — [N] in [source, keyless, re-fetchable]. That figure counts people who
> report using assistive input, not people who have been shut out of a booking,
> which nobody counts. This makes the 8:00 release something they can enter.

## Failure modes, with the fix

| symptom | why it fails | fix |
| --- | --- | --- |
| "Millions of people…" | no anchor of any kind | anchor 4, free, one sentence |
| A big number from a consulting report | judge cannot re-fetch; smells like marketing | swap for a smaller keyless-API number |
| Statistics with no per-unit stake | inert magnitude | step 5 |
| Impact section separate from the product | reads as bolted on | step 6 |
| Every number flattering | reads as selected | step 4 — disclose the disagreement |
| Population = "everyone" | discounted instantly | step 2 — claim only who would open it |
| Personal story only | moving, not sized | keep it, add anchor 1 or 3 beside it |

`haven` and `cedarfield` prove the last row cuts both ways: a personal story with
a named institution beside it won, and a personal story with a *mechanism* beside
it placed top-12. What neither did was leave the story alone and unanchored.

## Where the automation goes

`agents/impact-research.md` should take the product description and return:
the claimable population with two candidate denominators, the keyless endpoint
that counts each, the caveat each number carries, and the anchor-4 sentence if no
dataset fits. The numbers it returns go into `CLAIMS.md` at the rung the ladder
in `WINNING-WRITEUPS.md` assigns them — never higher.
