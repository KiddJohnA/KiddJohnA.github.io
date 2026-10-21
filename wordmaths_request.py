#!/usr/bin/env python3
"""
WORDMATHS REQUEST — the request layer for the Wordmaths engine.

An AI (or a person, or a program) sends a REQUEST: a JSON word-map
assigning one word to each of the model's 22 variables.
The engine figures it and returns the computation: the statement,
the per-variable sentences, and the model's numeric readings.

This is how an AI uses the computation: it does not imitate the
model — it asks the model, and the model answers.

REQUEST FORMAT (JSON)
---------------------
{
  "term": "Music",
  "words": {
    "A": "Music",  "B": "Performance", "X": "Sound", "Y": "Playing",
    "Z": "Song",   "i": "Silence",     "j": "Listening", "N": "Notes",
    "h": "Time",   "C": "Room",        "D": "World",  "E": "Joy",
    "F": "Expression",
    "π": "Chorus", "φ": "Beat",        "e": "Chance", "ℏ": "Note",
    "σ": "Album",  "γ": "Volume",      "δ": "Remix",
    "σ′": "Genres", "Ω": "Anthem"
  }
}

All 22 variables are required. The identities are fixed:
A Principle · B Purpose · X Primitive · Y Protocol · Z Product ·
i State · j Condition · N Set · h Time · C Context · D Domain ·
E Emotion · F Intention · π Cycle · φ Step · e Probability ·
ℏ Planck · σ Summation · γ Scale · δ Change · σ′ Options · Ω Answer.

USAGE
-----
  python3 wordmaths_request.py request.json           -> JSON result
  python3 wordmaths_request.py --markdown request.json -> the figuring, as markdown
  python3 wordmaths_request.py --demo                  -> runs examples/music.json

Wordmaths model and engine © Jack Kidd / Chron. All rights reserved.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wordmaths as wm

REQUIRED = wm.ORDER  # the 22 variables, in model order


def compute(request):
    """Figure one request. Returns a JSON-ready dict."""
    words = request.get("words", {})
    missing = [v for v in REQUIRED if v not in words]
    if missing:
        return {"ok": False,
                "error": "request is missing variables: " + ", ".join(missing),
                "required": REQUIRED}
    W = {v: str(words[v]) for v in REQUIRED}
    R, S = wm.figure(W)
    readings = {}
    for k in ("omega", "gamma0", "delta", "sigma_prime", "d"):
        if k in R:
            readings[k] = R[k]
    return {
        "ok": True,
        "term": request.get("term", W["A"]),
        "words": W,
        "statement": wm.intelligent_statement(
            W["A"], W["B"], W["X"], W["Y"], W["Z"], W["i"], W["j"], W["N"]),
        "readings": readings,
        "sentences": {v: S[v] for v in REQUIRED},
        "close": (f"then {W['B']} to {W['Z']} is {W['A']} — "
                  "the purpose, through the product, is the principle."),
    }


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    flags = {a for a in argv[1:] if a.startswith("--")}
    if "--demo" in flags or not args:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "examples", "music.json")
    else:
        path = args[0]
    with open(path, encoding="utf-8") as fh:
        request = json.load(fh)
    if "--markdown" in flags:
        words = request.get("words", {})
        missing = [v for v in REQUIRED if v not in words]
        if missing:
            print("request is missing variables: " + ", ".join(missing))
            return 1
        W = {v: str(words[v]) for v in REQUIRED}
        print(wm.markdown_output(W, title=request.get("term", W["A"])))
        return 0
    result = compute(request)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
