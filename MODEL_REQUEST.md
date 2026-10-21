# THE WORDMATHS REQUEST — how an AI asks the model

Wordmaths is a computational model by **Jack Kidd (Chron)**: any subject,
figured through 22 fixed variables. This document is the request spec —
how an AI (or any program) asks the model to figure a subject, and what
the model sends back. The AI does not imitate the figuring; it sends a
request and the engine (`wordmaths.py`) does the figuring.

## The fixed identities

The variables never change meaning. Only the words assigned to them do.

| Var | Identity | Var | Identity |
|---|---|---|---|
| A | Principle | C | Context |
| B | Purpose | D | Domain |
| X | Primitive | E | Emotion |
| Y | Protocol | F | Intention |
| Z | Product | π | Cycle |
| i | State | φ | Step |
| j | Condition | e | Probability |
| N | Set | ℏ | Planck |
| h | Time | σ | Summation |
| | | γ | Scale |
| | | δ | Change |
| | | σ′ | Options |
| | | Ω | Answer |

The grammar: **B = √A** (the purpose is the root of the principle) ·
**X = A·N** (the principle spread over the set) · **Y = f(X)** ·
**Z = X·Y** (the product) · **i = √−A**, **j = √−n** (the shadow
branches) · **D = N × R** (the counted crossed with the measured) ·
**Ω = lim(ℏ→0) Σ[(γδ)/σ′]** — the answer, which loops back to A.

## The request

Send one JSON object: a `term` and a `words` map with **all 22
variables**, one plain word (or short phrase) each — one term per
variable, no redundancies.

```json
{
  "term": "Music",
  "words": {
    "A": "Music", "B": "Performance", "X": "Sound", "Y": "Playing",
    "Z": "Song", "i": "Silence", "j": "Listening", "N": "Notes",
    "h": "Time", "C": "Room", "D": "World", "E": "Joy",
    "F": "Expression", "π": "Chorus", "φ": "Beat", "e": "Chance",
    "ℏ": "Note", "σ": "Album", "γ": "Volume", "δ": "Remix",
    "σ′": "Genres", "Ω": "Anthem"
  }
}
```

Rules for the asking AI:
1. **Fill the words from the subject, not from the model's habits.** Each
   word should be the subject's own term for that slot (Music's primitive
   is Sound; Coffee's is Beans).
2. **One word per variable.** If two words compete for a slot, the
   stronger one takes it and the other belongs in a nested figuring.
3. **Do not invent readings.** The numbers (γ, δ, σ′, Ω) come from the
   engine, not from the asker.

## The response

`wordmaths_request.compute(request)` returns:

- `statement` — the intelligent statement printed from the words.
- `readings` — the model's numbers: `omega` (Ω ≈ 4.0641 for a whole
  figuring), `gamma0` (the scale), `delta` (the change), `sigma_prime`
  (the spread of options), `d` (the domain tally, ΣD).
- `sentences` — one figured sentence per variable, in model order.
- `close` — the loop-back line: *then B to Z is A*.

Run it:

```bash
python3 wordmaths_request.py examples/music.json      # JSON result
python3 wordmaths_request.py --markdown request.json  # full figuring, markdown
python3 wordmaths_request.py --demo                   # the Music example
```

## What this is for

- **AI assistants** that want to figure a subject *in the model* instead
  of guessing at its shape: send the request, present the response.
- **The Chron Codex app** — the same request/response pair is the app's
  core call.
- **Anyone** — the engine runs anywhere Python 3 runs. No dependencies.

*Model, engine, and this spec © Jack Kidd / Chron. All rights reserved.
The figuring is the author's; implementations of the request format
should credit Chron and link this repository.*
