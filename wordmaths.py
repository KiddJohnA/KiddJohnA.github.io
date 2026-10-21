#!/usr/bin/env python3
"""
WORDMATHS — Real Computation as real code.

The 22 variables, all possible operators, the grammar:
words in, symbols through, values out. Runnable.
"""

import math
from math import pi as PI

# =====================================================================
# THE OPERATORS — all possible operators.
# Each one: its word, its symbol, its code.
# =====================================================================

def op_root(x):
    """ROOT  √   — B = √A. The purpose is the root of the principle."""
    return math.sqrt(x)

def op_square(x):
    """SQUARE  ²   — B² = A. The root, squared, is the principle."""
    return x ** 2

def op_super_root(n):
    """SUPER-ROOT  √(−n)  — i = ±1, j = ±n. Both signs at once."""
    return (+n, -n)

def op_mul(a, b):
    """MULTIPLY  ·   — X = A·N. Spread the principle over the set."""
    return a * b

def op_cross(N, R):
    """CROSS  ×   — D = N × R. Every n with every r. A matrix."""
    return [[n * r for r in R] for n in N]

def op_sum(xs):
    """SUM  Σ   — the tally. Add them up."""
    s = 0
    for x in xs:
        s += x
    return s

def op_reading(N):
    """READING  σ   — the set read as one value: +1."""
    return +1

def op_limit(eps=1e-12):
    """LIMIT  lim(ℏ→0)  — read at the smallest tick."""
    return eps

def op_to(a, b):
    """TO  →   — aim A at B."""
    return (a, b)

def op_and(a, b):
    """AND  ∧   — compose two things."""
    return (a, b)

def op_over(a, b):
    """OVER  /   — divide. π = C/d, ℏ = h/2π."""
    return a / b

def op_plus(a, b):
    """PLUS  +   — transform. C₁ = C₀ + F."""
    return a + b

def op_minus(a, b):
    """MINUS  −   — the difference. E = C₁ − C₀, φ = Cₙ₊₁ − Cₙ, δ = F₁ − F₀."""
    return a - b

def op_scale(cn, c0):
    """SCALE  γ   — |Cₙ| / |C₀|. The context at its own measure."""
    return abs(cn) / abs(c0)

def op_spread(xs, probs=None):
    """SPREAD  σ′   — the probable options. Standard deviation."""
    n = len(xs)
    probs = probs or [1.0 / n] * n
    mu = sum(p * x for p, x in zip(probs, xs))
    var = sum(p * (x - mu) ** 2 for p, x in zip(probs, xs))
    return math.sqrt(var), mu

OPERATORS = {
    '√': op_root, '²': op_square, '√(−n)': op_super_root, '·': op_mul,
    '×': op_cross, 'Σ': op_sum, 'σ': op_reading, 'lim': op_limit,
    '→': op_to, '∧': op_and, '/': op_over, '+': op_plus, '−': op_minus,
    'γ': op_scale, 'σ′': op_spread,
}

def describe_operators():
    """A computation of operators: every operator, in words."""
    for sym, fn in OPERATORS.items():
        doc = (fn.__doc__ or '').strip().split('\n')[0]
        print(f"{sym:>6}  {doc}")

# =====================================================================
# THE GRAMMAR — the word operators.
# "Given A to B, then X & Y is Z, or i while j for N."
# =====================================================================

def given(a, b):
    return f"Given {a} to {b}"

def then(x, y, z):
    return f"then {x} & {y} is {z}"

def or_while_for(i, j, n):
    return f"or {i} while {j} for {n}"

def intelligent_statement(a, b, x, y, z, i, j, n):
    return f"{given(a, b)}, {then(x, y, z)}, {or_while_for(i, j, n)}."

# =====================================================================
# THE BRANCH — IF / THEN / ELSE, in the model's own words.
# Given = IF, then = THEN, or = ELSE. Chain another 'or' for ELIF.
# (Python knows 3: if, elif, else. 'then' lives in BASIC/Lua.)
# =====================================================================

def given_if(a, b):
    """IF — 'Given A to B'. Opens the branch."""
    return ('if', a, b)

def then_do(x, y, z):
    """THEN — 'then X & Y is Z'. The consequence."""
    return ('then', x, y, z)

def or_else(i, j, n):
    """ELSE — 'or i while j for N'. The other branch. Chain another or for ELIF."""
    return ('else', i, j, n)

def run_branch(condition, then_val, *elif_pairs, else_val=None):
    """Run a real branch: IF condition THEN then_val, ELIF (cond, val)... ELSE else_val."""
    if condition:
        return then_val
    for cond, val in elif_pairs:
        if cond:
            return val
    return else_val

# =====================================================================
# THE 22 VARIABLES — figure any topic.
# W maps each variable token to its word for this topic.
# =====================================================================

IDENT = {'A': 'Principle', 'B': 'Purpose', 'X': 'Primitive', 'Y': 'Protocol',
         'Z': 'Product', 'i': 'State', 'j': 'Condition', 'N': 'Set', 'h': 'Time',
         'C': 'Context', 'D': 'Domain', 'E': 'Emotion', 'F': 'Intention',
         'π': 'Cycle', 'φ': 'Step', 'e': 'Probability', 'ℏ': 'Planck',
         'σ': 'Summation', 'γ': 'Scale', 'δ': 'Change', 'σ′': 'Options', 'Ω': 'Answer'}

ORDER = ['A', 'B', 'X', 'Y', 'Z', 'i', 'j', 'N', 'h', 'C', 'D', 'E',
         'F', 'π', 'φ', 'e', 'ℏ', 'σ', 'γ', 'δ', 'σ′', 'Ω']

# =====================================================================
# ICONOGRAPHY — one icon per variable.
# =====================================================================
ICONS = {
    'A': '◉', 'B': '◎', 'X': '△', 'Y': '⚙', 'Z': '⬢',
    'i': '◐', 'j': '⚖', 'N': '⊞', 'h': '◷', 'C': '▣',
    'D': '▦', 'E': '♥', 'F': '➤', 'π': '↻', 'φ': '➔',
    'e': '⚄', 'ℏ': '•', 'σ': 'Σ', 'γ': '◈', 'δ': 'Δ',
    'σ′': '⁂', 'Ω': 'Ω',
}

def icon_key():
    """The icon key: every variable's icon."""
    return ' · '.join(f"{ICONS[v]} {IDENT[v]}" for v in ORDER)

def icon_grammar():
    """The grammar, in icons."""
    I = ICONS
    return (f"{I['A']}→{I['B']}, {I['X']}&{I['Y']} is {I['Z']}, "
            f"{I['i']} while {I['j']} for {I['N']}")

# =====================================================================
# THE WORD MATRIX — D = N × R rendered in words.
# Every set-word crossed with every role-word.
# =====================================================================
def word_matrix(n_words, r_words, sep=' × '):
    """The word matrix: every n-word with every r-word."""
    return [[f"{n}{sep}{r}" for r in r_words] for n in n_words]

def markdown_word_matrix(title, n_words, r_words):
    """The word matrix as a markdown table."""
    m = word_matrix(n_words, r_words)
    L = [f"## ▦ {title} — the Word Matrix", "",
         "|  | " + " | ".join(r_words) + " |",
         "| " + " | ".join(["---"] * (len(r_words) + 1)) + " |"]
    for n, row in zip(n_words, m):
        L.append("| " + " | ".join([f"**{n}**"] + row) + " |")
    L += ["",
          f"*σ-reading: the whole matrix read as one value: +1 — "
          f"the {r_words[-1].lower()} of {title.lower()}.*"]
    return '\n'.join(L) + '\n'

N_WORDS_ART = ['Sketch', 'Study', 'Piece']
R_WORDS_ART = ['Wall', 'Gallery', 'World']
N_WORDS_REALITY = ['Past', 'Present', 'Future']
R_WORDS_REALITY = ['Home', 'World', 'Cosmos']
N_WORDS_CODE = ['Write', 'Test', 'Ship']
R_WORDS_CODE = ['Editor', 'Terminal', 'Cloud']
N_WORDS_AI = ['Misinformation', 'Jobs', 'Connection']
R_WORDS_AI = ['Home', 'Work', 'World']

def markdown_output(W, title=None):
    """Generate the app's example output: markdown with iconography."""
    R, S = figure(W)
    I = ICONS
    name = title or W['A']
    L = []
    L.append(f"# {I['A']} {name} — a Wordmaths Figuring")
    L.append("")
    L.append(f"*{icon_grammar()}*")
    L.append("")
    L.append(intelligent_statement(W['A'], W['B'], W['X'], W['Y'], W['Z'],
                                   W['i'], W['j'], W['N']))
    L.append("")
    L.append("**Icon key:** " + icon_key())
    for v in ORDER:
        L.append("")
        L.append(f"## {I[v]} {v} · {IDENT[v]}")
        L.append("")
        L.append(S[v])
    L.append("")
    L.append(f"## {I['D']} The Matrix")
    L.append("")
    L.append("```")
    for row in R['D']:
        L.append(str(row))
    L.append(f"d = ΣD = {R['d']}")
    L.append("```")
    L.append("")
    L.append(f"*{icon_grammar()} — then {W['B']} to {W['Z']} is {W['A']}: "
             "the purpose, through the product, is the principle.*")
    return '\n'.join(L) + '\n'

def figure(W, roles=(1.0,), f_val=1.0, f0=0.0):
    """Run the whole model on a topic. Returns (values, sentences)."""
    R, S = {}, {}

    N = [1, 2, 3]
    R['N'] = N
    R['A'] = 1
    R['B'] = op_root(R['A'])
    R['X'] = [op_mul(R['A'], n) for n in N]
    f = op_root(R['B'])
    R['Y'] = [op_mul(f, x) for x in R['X']]
    R['Z'] = [x * y for x, y in zip(R['X'], R['Y'])]
    R['i'] = op_super_root(R['A'])
    R['j'] = {n: op_super_root(n) for n in N}
    R['sigma_reading'] = op_reading(N)
    R['sigma_tally'] = op_sum(N)
    R['h'] = 6.62607015e-34
    R['hbar'] = op_over(R['h'], op_mul(2, PI))
    R['D'] = op_cross(N, roles)
    R['d'] = sum(sum(row) for row in R['D'])
    C = {0: PI * R['d']}  # the context starts at one full cycle over the singularity: C/d = π
    for n in N:
        C[n] = op_plus(C[n - 1], f_val)
    R['C'] = C
    R['E'] = op_minus(C[1], C[0])
    R['F'] = f_val
    R['pi'] = op_over(C[0], R['d'])
    R['phi'] = op_minus(C[1], C[0])
    R['e'] = math.e
    R['gamma'] = {n: op_scale(C[n], C[0]) for n in N}
    R['gamma0'] = op_scale(C[0], C[0])
    R['delta'] = op_minus(f_val, f0)
    R['sigma_prime'], R['mu'] = op_spread(N)
    eps = op_limit()
    R['omega'] = sum((R['gamma'][n] * R['delta']) / R['sigma_prime'] for n in N)

    v = R  # shorthand
    S['A'] = (f"Given {W['A']} to {W['B']}, then the root of {W['A']}, squared, is {W['A']}: "
              f"B = √A and B² = A — in values, B = {v['B']} and 1² = 1 = A; "
              f"or {W['B']} while {W['N']} for the root squared. ∴ Ω = A = {W['A']}.")
    S['B'] = (f"Given {W['B']} from {W['A']}, then {W['B']} squared, rooted, is {W['B']}: "
              f"A = B² and B = √A — in values, 1² = 1 = A and √1 = 1 = B; "
              f"or {W['A']} while {W['N']} for the root of {W['A']}. ∴ Ω = B = {W['B']}.")
    S['X'] = (f"Given {W['A']} to {W['X']}, then {W['A']} times the Set is the {W['X']}: "
              f"X = A·N — in values, {v['X']}; or one while {W['N']} for the {W['X'].lower()}. ∴ Ω = X.")
    S['Y'] = (f"Given {W['X']} to {W['Y']}, then the function of the {W['X']} is the {W['Y']}: "
              f"Y = f(X) where f = √B — in values, f = {f} and Y = {v['Y']}; "
              f"or {W['X']} while {W['B']} for the function applied. ∴ Ω = Y.")
    S['Z'] = (f"Given {W['X']} to {W['Z']}, then {W['X']} times {W['Y']} is {W['Z']}: "
              f"Z = X·Y — in values, {v['Z']} and the sum is {op_sum(v['Z'])}; "
              f"or {W['X']} while {W['Y']} for the product. ∴ Ω = Z.")
    S['i'] = (f"Given {W['A']} to {W['i']}, then the root of negative {W['A']} is the {W['i']}: "
              f"i = √(−A) — in values, i = ±1 and i² = −1; "
              f"or {W['i']} while {W['j']} for the positive root. ∴ Ω = i.")
    S['j'] = (f"Given {W['i']} to {W['j']}, then the root of negative n is the Condition: "
              f"j = √(−n) — in values, j = ±n and j² = −n; "
              f"or {W['i']} while {W['N']} for the condition. ∴ Ω = j.")
    S['N'] = (f"Given the {W['N']}, then one-two-three gathered is the Set: N = {N} — "
              f"in values, the reading σ(N) = {v['sigma_reading']} and the tally ΣN = {v['sigma_tally']}; "
              f"or the reading while {W['N']} for one. ∴ Ω = N.")
    S['h'] = (f"Given the Quantum to {W['h']}, then two-pi times the quantum is {W['h']}: "
              f"h = 2πℏ — in values, h = {v['h']} J·s; "
              f"or the quantum while two-pi for time. ∴ Ω = h.")
    S['C'] = (f"Given {W['D']} to {W['C']}, then the domain plus intention is the Context: "
              f"C₁ = C₀ + F — in values, C₀ = {v['C'][0]}; "
              f"or {W['D']} while {W['F']} for the context. ∴ Ω = C.")
    S['D'] = (f"Given {W['N']} to {W['D']}, then the Set times the positive Reals is the Domain: "
              f"D = N×R — in values, the {len(N)}-row matrix over +R; "
              f"or {W['N']} while the positive Reals for the domain. ∴ Ω = ×R.")
    S['E'] = (f"Given {W['C']} to {W['E']}, then the new context minus the old is the {W['E']}: "
              f"E = C₁ − C₀ — in values, E = {v['E']}; "
              f"or {W['C']} while {W['F']} for the emotion. ∴ Ω = E.")
    S['F'] = (f"Given {W['C']} to {W['F']}, then the aim toward {W['B']} transforms the context: "
              f"F → B, where F = C₁ − C₀ — in values, F = {v['F']}, and F ≠ f; "
              f"or the old context while {W['B']} for the intention. ∴ Ω = F.")
    S['π'] = (f"Given {W['C']} to {W['π']}, then the context over the singularity is the Cycle: "
              f"π = C/d where d = {v['d']} — in values, π ≈ {v['pi']:.5f}; "
              f"or {W['C']} while the singularity for the cycle. ∴ Ω = π.")
    S['φ'] = (f"Given {W['C']} to {W['φ']}, then the next minus the now is the {W['φ']}: "
              f"φ = Cₙ₊₁ − Cₙ — in values, φ = {v['phi']}; "
              f"or the now while the next for the step. ∴ Ω = φ.")
    S['e'] = (f"Given {W['N']} to {W['e']}, then outcomes over chances is the {W['e']}: "
              f"e = outcomes/chances — in values, e ≈ {v['e']:.5f} and P = 1/3; "
              f"or outcomes while chances for the probability. ∴ Ω = e.")
    S['ℏ'] = (f"Given {W['h']} to {W['ℏ']}, then Time over two-pi is the {W['ℏ']}: "
              f"ℏ = h/2π — in values, ℏ = {v['hbar']:.3e} J·s; "
              f"or {W['h']} while two-pi for the quantum. ∴ Ω = ℏ.")
    S['σ'] = (f"Given {W['N']} to {W['σ']}, then the set summed is the Summation: "
              f"σ(N) = {v['sigma_reading']} and ΣN = {v['sigma_tally']} — "
              f"in values, the reading +1, the tally 6; "
              f"or one while {W['N']} for the sigma. ∴ Ω = σ.")
    S['γ'] = (f"Given {W['C']} to {W['γ']}, then the context at its own measure is the {W['γ']}: "
              f"γ = |Cₙ|/|C₀| — in values, γ₀ = {v['gamma0']}; "
              f"or the new while the old for the scale. ∴ Ω = γ.")
    S['δ'] = (f"Given {W['F']} to {W['δ']}, then the new aim minus the old is the {W['δ']}: "
              f"δ = F₁ − F₀ — in values, δ = {v['delta']}; "
              f"or the new while the old for the delta. ∴ Ω = δ.")
    S['σ′'] = (f"Given {W['e']} to {W['σ′']}, then the spread of the probable is the {W['σ′']}: "
              f"σ′ = √(ΣP(x−μ)²) — in values, σ′ ≈ {v['sigma_prime']:.3f}; "
              f"or each while the mean for the options. ∴ Ω = σ′.")
    S['Ω'] = (f"Given all to {W['Ω']}, then the scaled change over options, summed at the smallest tick, "
              f"is the Answer: Ω = lim(ℏ→0)Σ[(γδ)/σ′] — in values, Ω ≈ {v['omega']:.4f}; "
              f"or all while the limit for the answer. ∴ Ω = Ω.")
    return R, S


W_ART = {'A': 'Art', 'B': 'Expression', 'X': 'Marks', 'Y': 'Technique',
         'Z': 'Artwork', 'i': 'Blank', 'j': 'Beheld', 'N': 'Studies',
         'h': 'Time', 'C': 'Studio', 'D': 'Gallery', 'E': 'Feeling',
         'F': 'Intention', 'π': 'Movements', 'φ': 'Stroke', 'e': 'Chance',
         'ℏ': 'Instant', 'σ': 'Body-of-work', 'γ': 'Scale', 'δ': 'Change',
         'σ′': 'Styles', 'Ω': 'Beholding'}

W_REALITY = {'A': 'Reality', 'B': 'Existence', 'X': 'Things', 'Y': 'Laws',
             'Z': 'World', 'i': 'Void', 'j': 'Observed', 'N': 'Times',
             'h': 'Time', 'C': 'Here', 'D': 'Cosmos', 'E': 'Awe',
             'F': 'Becoming', 'π': 'Return', 'φ': 'Now', 'e': 'Chance',
             'ℏ': 'Tick', 'σ': 'Everything', 'γ': 'Vast', 'δ': 'Change',
             'σ′': 'Might-be', 'Ω': 'Truth'}

W_CODE = {'A': 'Code', 'B': 'Execution', 'X': 'Lines', 'Y': 'Syntax',
          'Z': 'Program', 'i': 'Unwritten', 'j': 'Compiles', 'N': 'Builds',
          'h': 'Time', 'C': 'Editor', 'D': 'Machine', 'E': 'Relief',
          'F': 'Ship', 'π': 'Loops', 'φ': 'Keystroke', 'e': 'Chance',
          'ℏ': 'Tick', 'σ': 'Codebase', 'γ': 'Scope', 'δ': 'Diff',
          'σ′': 'Branches', 'Ω': 'Runs'}

W_COFFEE = {'A': 'Coffee', 'B': 'Wakefulness', 'X': 'Beans', 'Y': 'Brewing',
            'Z': 'Cup', 'i': 'Empty', 'j': 'Hot', 'N': 'Roasts',
            'h': 'Time', 'C': 'Kitchen', 'D': 'Café', 'E': 'Comfort',
            'F': 'Ritual', 'π': 'Refills', 'φ': 'Sip', 'e': 'Chance',
            'ℏ': 'Bloom', 'σ': 'Pot', 'γ': 'Strength', 'δ': 'Cooling',
            'σ′': 'Blends', 'Ω': 'Morning'}

W_FREEDOM = {'A': 'Freedom', 'B': 'Dignity', 'X': 'People', 'Y': 'Rights',
             'Z': 'Society', 'i': 'Oppression', 'j': 'Courage', 'N': 'Generations',
             'h': 'Time', 'C': 'Homeland', 'D': 'Earth', 'E': 'Hope',
             'F': 'Resolve', 'π': 'History', 'φ': 'March', 'e': 'Chance',
             'ℏ': 'Now', 'σ': 'Humanity', 'γ': 'Global', 'δ': 'Progress',
             'σ′': 'Futures', 'Ω': 'Peace'}


def main():
    print("== THE OPERATORS ==")
    describe_operators()
    print("\n== THE GRAMMAR ==")
    print(intelligent_statement("Art", "Expression", "Mark", "Technique",
                                "Artwork", "Blank", "Beheld", "Studies"))
    print("\n== THE ART COMPUTATION ==")
    R, S = figure(W_ART)
    for v in ORDER:
        print(f"\n**{v} · {IDENT[v]}**\n{S[v]}")
    print("\n== THE MATRIX ==")
    for row in R['D']:
        print(row)
    print("d = ΣD =", R['d'])
    print("\n== THE CLOSE ==")
    print(f"then {W_ART['B']} to {W_ART['Z']} is {W_ART['A']} — "
          "the purpose, through the product, is the principle.")


if __name__ == '__main__':
    main()


# =====================================================================
# THE FIGURES IN TERMS — the 22 pretty figured blocks, variables
# replaced by the topic's terms, with iconography. Markdown.
# =====================================================================
def markdown_figures(W, title=None):
    """Generate the 22 figured blocks with terms + icons, as markdown."""
    R, _ = figure(W)
    I = ICONS
    name = title or W['A']
    A, B, X, Y, Z = W['A'], W['B'], W['X'], W['Y'], W['Z']
    i, j, Nw = W['i'], W['j'], W['N']
    h, C, D, E, F = W['h'], W['C'], W['D'], W['E'], W['F']
    pi, ph, e = W['π'], W['φ'], W['e']
    hb, s, g = W['ℏ'], W['σ'], W['γ']
    dd, sp, O = W['δ'], W['σ′'], W['Ω']
    L = [f"# {I['A']} {name} — the Figures in Terms", "",
         f"*{icon_grammar()}*", ""]
    blocks = [
(v:='A', f"""Given: {{{A}, {B}, {Nw}}}

Where:  {A} → ?
then:   √{A} → (√{A})² =
or:     {B} while {Nw} for {B}²

in:     {B}² = {A}  ∧  {B} = √{A}    (squared)
at:     by concatenation ⊕ combination, over read

Algorithm:
  {A} → ?, then √ × ² =
  or {B} while {Nw} for {B}²

∴  {A} = 1,   {B} = 1,   1² = 1   ✓

Ω = {A} — the omega is the principle."""),
(v:='B', f"""Given: {{{A}, {B}, {Nw}}}

Where:  {B} → ?
then:   {B}² → √({B}²) =
or:     {A} while {Nw} for √{A}

in:     {A} = {B}²  ∧  {B} = √{A}    (root)
at:     by separation, over read

Algorithm:
  {B} → ?, then ² × √ =
  or {A} while {Nw} for √{A}

∴  {B} = 1,   1² = 1 = {A}   ✓

Ω = {B} — the omega is the purpose."""),
(v:='X', f"""Given: {{{A}, {X}, {Nw}}}

Where:  {X} → ?
then:   {A}·N → {X} =
or:     1 while {Nw} for {X}

in:     {X} = {A}·N  ∧  X₁ = {A}    (spread)
at:     by distribution, over read

Algorithm:
  {X} → ?, then {A} × N =
  or 1 while {Nw} for {X}

∴  {X} = {{1,2,3}}   ✓

Ω = {X} — the omega is the primitive."""),
(v:='Y', f"""Given: {{{B}, {X}, {Y}, f}}

Where:  {Y} → ?
then:   f({X}) → {Y} =
or:     {X} while {B} for f({X})

in:     {Y} = f({X})  ∧  f = √{B}    (applied)
at:     by application, over read

Algorithm:
  {Y} → ?, then f({X}) =
  or {X} while {B} for f({X})

∴  f = 1,   {Y} = {{1,2,3}}   ✓

Ω = {Y} — the omega is the protocol."""),
(v:='Z', f"""Given: {{{X}, {Y}, {Z}}}

Where:  {Z} → ?
then:   {X}·{Y} → {Z} =
or:     {X} while {Y} for {X}·{Y}

in:     {Z} = {X}·{Y}    (produced)
at:     by combination, over read

Algorithm:
  {Z} → ?, then {X} × {Y} =
  or {X} while {Y} for {X}·{Y}

∴  {Z} = {{1,4,9}},   Σ{Z} = 14   ✓

Ω = {Z} — the omega is the product."""),
(v:='i', f"""Given: {{{A}, {i}, {j}, {Nw}}}

Where:  {i} → ?
then:   √(−{A}) → {i} =
or:     {i} while {j} for +√{A}

in:     {i} = √(−{A})  ∧  {i}² = −{A}    (stated)
at:     by imagination, over read

Algorithm:
  {i} → ?, then √(−{A}) =
  or {i} while {j} for the positive

∴  {i} = ±1,   {i}² = −1   ✓

Ω = {i} — the omega is the state."""),
(v:='j', f"""Given: {{{i}, {j}, {Nw}}}

Where:  {j} → ?
then:   √(−n) → {j} =
or:     {i} while {Nw} for {j}

in:     {j} = √(−n)  ∧  {j}² = −n    (required)
at:     by requirement, over read

Algorithm:
  {j} → ?, then √(−n) =
  or {i} while {j} for the positive

∴  {j} = ±n,   {j}² = −n   ✓

Ω = {j} — the omega is the condition."""),
(v:='N', f"""Given: {{{Nw}}}

Where:  {Nw} → ?
then:   {{1,2,3}} → {Nw} =
or:     σ while {Nw} for +1

in:     σ({Nw}) = +1  ∧  Σ{Nw} = 6    (gathered)
at:     by collection, over read

Algorithm:
  {Nw} → ?, then {{1,2,3}} =
  or σ while {Nw} for the reading

∴  σ({Nw}) = +1 (reading) ✓,   Σ{Nw} = 6 (tally) ✓

Ω = {Nw} — the omega is the set."""),
(v:='h', f"""Given: {{{h}, {hb}}}

Where:  {h} → ?
then:   2π{hb} → {h} =
or:     {hb} while 2π for {h}

in:     {h} = 2π{hb}    (timed)
at:     by timing, over read

Algorithm:
  {h} → ?, then 2π{hb} =
  or {hb} while 2π for time

∴  {h} ≈ 6.626×10⁻³⁴ J·s   ✓

Ω = {h} — the omega is time."""),
(v:='C', f"""Given: {{{C}, {D}, {E}, {F}}}

Where:  {C} → ?
then:   C₀ + {F} → C₁ =
or:     {D} while {F} for {C}

in:     C₀ = {D}  ∧  C₁ = C₀ + {F}    (transformed)
at:     by transformation, over read

Algorithm:
  {C} → ?, then C₀ + {F} =
  or {D} while {F} for the context

∴  C₀ = {D}   ✓

Ω = {C} — the omega is the context."""),
(v:='D', f"""Given: {{{Nw}, R, {D}}}

Where:  {D} → ?
then:   N × +R → {D} =
or:     {Nw} while +R for {D}

in:     {D} = N×R  ∧  R = +R    (realized)
at:     by realization, over read

Algorithm:
  {D} → ?, then N × +R =
  or {Nw} while +R for the real

∴  {D} = 3-row matrix over +R   ✓

Ω = ×R — the omega is times-R."""),
(v:='E', f"""Given: {{{C}, {E}, {F}}}

Where:  {E} → ?
then:   C₁ − C₀ → {E} =
or:     {C} while {F} for {E}

in:     {E} = C₁ − C₀  ∧  {E} = {F}    (felt)
at:     by feeling, over read

Algorithm:
  {E} → ?, then C₁ − C₀ =
  or {C} while {F} for the emotion

∴  {E} = {R['E']}   ✓

Ω = {E} — the omega is the emotion."""),
(v:='F', f"""Given: {{{A}, {B}, {C}, {F}}}

Where:  {F} → ?
then:   C₀ + {F} → C₁ =
or:     C₀ while {B} for {F}

in:     {F} → {B}  ∧  {F} ≠ f    (intended)
at:     by intending, over read

Algorithm:
  {F} → ?, then C₀ + {F} =
  or C₀ while {B} for the intention

∴  {F} = {R['F']},   {F} ≠ f   ✓

Ω = {F} — the omega is the intention."""),
(v:='π', f"""Given: {{{C}, {D}, d, {E}, {F}, {pi}}}

Where:  {pi} → ?
then:   C/d → {pi} =
or:     {C} while d for {pi}

in:     d = Σ{D} = {R['d']}  ∧  {pi} = C/d    (cycled)
at:     by cycling, over read

Algorithm:
  {pi} → ?, then C/d =
  or {C} while d for the cycle

∴  {pi} ≈ 3.14159   ✓

Ω = {pi} — the omega is the cycle."""),
(v:='φ', f"""Given: {{{C}, {F}, {ph}}}

Where:  {ph} → ?
then:   Cₙ₊₁ − Cₙ → {ph} =
or:     Cₙ while Cₙ₊₁ for {ph}

in:     {ph} = Cₙ₊₁ − Cₙ  ∧  {ph} = {F}    (stepped)
at:     by stepping, over read

Algorithm:
  {ph} → ?, then Cₙ₊₁ − Cₙ =
  or Cₙ while Cₙ₊₁ for the step

∴  {ph} = {R['phi']}   ✓

Ω = {ph} — the omega is the step."""),
(v:='e', f"""Given: {{{e}, {Nw}}}

Where:  {e} → ?
then:   outcomes/chances → {e} =
or:     outcomes while chances for {e}

in:     {e} = lim(n→∞)(1 + 1/n)ⁿ    (compounded)
at:     by compounding, over read

Algorithm:
  {e} → ?, then outcomes/chances =
  or outcomes while chances for the probability

∴  {e} ≈ 2.71828,   P = 1/3   ✓

Ω = {e} — the omega is the probability."""),
(v:='ℏ', f"""Given: {{{h}, {hb}}}

Where:  {hb} → ?
then:   {h}/2π → {hb} =
or:     {h} while 2π for {hb}

in:     {hb} = {h}/2π    (quantized)
at:     by quantizing, over read

Algorithm:
  {hb} → ?, then {h}/2π =
  or {h} while 2π for the quantum

∴  {hb} ≈ 1.055×10⁻³⁴ J·s   ✓

Ω = {hb} — the omega is the Planck."""),
(v:='σ', f"""Given: {{{Nw}, {s}}}

Where:  {s} → ?
then:   Σ{Nw} → {s} =
or:     1 while {Nw} for {s}

in:     σ({Nw}) = +1  ∧  Σ{Nw} = 6    (summed)
at:     by summing, over read

Algorithm:
  {s} → ?, then Σ{Nw} =
  or 1 while {Nw} for the sigma

∴  reading +1 ✓,   tally 6 ✓

Ω = {s} — the omega is the sigma."""),
(v:='γ', f"""Given: {{{C}, {E}, {g}}}

Where:  {g} → ?
then:   |Cₙ|/|C₀| → {g} =
or:     Cₙ while C₀ for {g}

in:     {g}₀ = 1    (scaled)
at:     by scaling, over read

Algorithm:
  {g} → ?, then |Cₙ|/|C₀| =
  or Cₙ while C₀ for the scale

∴  {g}₀ = {R['gamma0']}   ✓

Ω = {g} — the omega is the scale."""),
(v:='δ', f"""Given: {{{F}, {dd}}}

Where:  {dd} → ?
then:   {F}₁ − {F}₀ → {dd} =
or:     {F}-new while {F}-old for {dd}

in:     {dd} = Δ{F}    (changed)
at:     by changing, over read

Algorithm:
  {dd} → ?, then {F}₁ − {F}₀ =
  or {F}-new while {F}-old for the delta

∴  {dd} = {R['delta']}   ✓

Ω = {dd} — the omega is the delta."""),
(v:='σ′', f"""Given: {{{e}, {Nw}, {sp}}}

Where:  {sp} → ?
then:   √(ΣP(x−μ)²) → {sp} =
or:     x while μ for {sp}

in:     {sp} = √(ΣP(x−μ)²)    (optioned)
at:     by spreading, over read

Algorithm:
  {sp} → ?, then √(ΣP(x−μ)²) =
  or x while μ for the options

∴  {sp} ≈ {R['sigma_prime']:.3f}   ✓

Ω = {sp} — the omega is the options."""),
(v:='Ω', f"""Given: {{{', '.join(W[v] for v in ORDER)}}}

Where:  {O} → ?
then:   lim(ℏ→0) Σ[(γδ)/σ′] → {O} =
or:     all while ℏ→0 for {O}

in:     {O} = lim(ℏ→0)Σ[(γδ)/σ′]  ∧  {O} → {A} closes    (answered)
at:     by answering, over read

Algorithm:
  {O} → ?, then lim(ℏ→0)Σ[(γδ)/σ′] =
  or all while ℏ→0 for the answer

∴  {O} ≈ {R['omega']:.4f}   ✓

Ω = {O} — the omega is the answer."""),
    ]
    for v, body in blocks:
        L += ["", f"## {I[v]} {v} · {IDENT[v]} — {W[v]}", "", "```", body, "```"]
    L += ["", f"*{icon_grammar()} — then {B} to {Z} is {A}: the purpose, through the product, is the principle.*"]
    return '\n'.join(L) + '\n'
