# Writing the submission

Two readers, and they need different things from the same page.

**The ten-minute judge** reads the first screen, skims, opens the video, maybe
loads the live URL. They will never clone anything.
**The source-verifying judge** clones, runs your tests, and adds up your tables.

The write-up has to win the first and survive the second. Ours was measured at
**93/100 by the first and 92 by the second** — and the first one's complaint was
length: *"the verification apparatus is longer than the idea, and the idea is
good enough to survive on one page."*

## Structure that tested best

1. **A structural claim, not a persona.** Open on what is capped today and why —
   then land one sentence that is the whole thing. Ours: *"The person who does
   the work mints the tool. The page keeps the veto."* The persona comes second,
   as evidence.
2. **One session, end to end**, numbered, with the exact values a judge can
   retype.
3. **Five numbers, in a table.** The rarity claim, the safety claim, the
   behaviour claim, the assertion count.
4. **How far it goes** — the arithmetic size of the space, the other domains it
   runs on unchanged, the population from a live public API.
5. **Every number with the command that re-derives it**, in one table.
6. **What you got wrong**, naming the entries that beat you.
7. Everything else behind links.

## The sentence that scored highest

> "Move this mechanism to a backend and it does not get slower; it stops
> existing."

Judges are grading *use of the platform*. An explicit argument that your thing
**cannot exist** off it converts "nice product that uses X" into "product that
could not be anything else". Write that sentence for your own project and put
it on the first screen.

## Disarm the sceptic before the flinch, not after

Our rarity claim — "3 of 868" — drew: *"a denominator chosen by the party being
measured."* We did disarm it two paragraphs later (the count was 1, a reader
found the counterexample, here is the script) and that recovery cost one point
instead of five. **Put the self-refutation above the claim, not below it.**

## Length is a real cost

600 lines was called exhausting by a judge told to be patient. Three tables of
the same evidence is where a tired reader closes the tab. Cut to the transcript
and link the rest.

## Devpost mechanics

- **Elevator pitch, 200 chars.** Lead with a capability and an impossibility in
  one breath.
- **Project details** — paste the whole body; no relative links, they break.
- **Built with** — tags are a search surface; include the spec/protocol name.
- **Try it out** — live URL first, repo second.
- **Testing instructions** — assume no account and no special browser. Say
  exactly what a judge without your flag enabled will see, and make that path
  work. Most judges will not enable anything.
- **Gallery** — ~15 images, 3:2, captions written in the same pass as the shots.
- The **"create project" button sits behind a reCAPTCHA**: a person has to do
  the final submission. Have everything paste-ready before that step.
- Keep a `submission-form.md` with every field filled and only the URLs as
  placeholders — and **commit it**, because the folder holding it can vanish.

## Rules that are enforced literally

Public repo · open-source licence file visible in the About section · the
literal registration/API call the rules ask to see, in the source · video under
the cap, public, with audio · everything in English · project created inside the
submission window.

Check the deadline twice: the rules page and the countdown disagreed by twelve
hours in this one. Build to the earlier.
