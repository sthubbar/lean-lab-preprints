# LeanLab: formal checks for two preprints

This repository holds the Lean 4 code behind two preprints. Each `.lean` file under `LeanLab/`
is a byte-for-byte copy of the file in the private working lab it comes from, with the same path
and module name, so every theorem name below is the name used in the papers.

The Lean code was written by an AI, Claude (Anthropic). It is checked only by the Lean kernel.
Nothing here proves binary Goldbach or Chen's theorem.

## Paper A

**Goldbach numbers in intervals of length 4.45 log^2 x under the Riemann Hypothesis**
aiXiv:2610.02672 (aixiv.261025.000001)

### What is proved in Lean

`LeanLab.Routes.U1508.goldbach_445_hsw_gZ` in `LeanLab/Routes/U1508Compose445.lean`. Its type,
as printed by `#check` in the build log:

```
@LeanLab.Routes.U1508.goldbach_445_hsw_gZ : ∀ {Z : ℕ → Finset LeanLab.PNTPort.ExplicitPsi1.Trivial.ZIdx},
  (RiemannHypothesis → ∀ (δ : ℝ), 0 < δ →
      δ ≤ 1 / 10 ^ 13 → LeanLab.ChirreHagen2025.SmoothT2.ExplicitA LeanLab.PNTPort.ExplicitPsi1.Trivial.gZ Z δ) →
    (RiemannHypothesis → LeanLab.ChirreHagen2025.SmoothT2.HadamardK LeanLab.PNTPort.ExplicitPsi1.Trivial.gZ) →
      LeanLab.ChirreHagen2025.SmoothT2.Ordinates14 LeanLab.PNTPort.ExplicitPsi1.Trivial.gZ →
        (RiemannHypothesis → LeanLab.ChirreHagen2025.Lemma26B.BPTN LeanLab.PNTPort.ExplicitPsi1.Trivial.gZ) →
          LeanLab.EvenGoldbachUpTo (4 * 10 ^ 18) →
            LeanLab.Dudek2014.SigmaH.HSWN70 LeanLab.PNTPort.ExplicitPsi1.Trivial.gZ →
              LeanLab.PNTPort.ExplicitPsi1.FirstDiff.HSWHead14 LeanLab.PNTPort.ExplicitPsi1.Trivial.gZ →
                RiemannHypothesis →
                  ∀ (x : ℝ),
                    3 ≤ x → ∃ n, LeanLab.ChirreHagen2025.IsGoldbachNumber n ∧ x < ↑n ∧ ↑n < x + 4.45 * Real.log x ^ 2
```

In words: assume RH. Assume the seven inputs below. Then for every real x ≥ 3 there is a Goldbach
number n, a sum of two odd primes, with x < n < x + 4.45 (log x)^2.

The paper also cites, from `LeanLab/ChirreHagen2025/U6806Theorem2Sp.lean`,
`LeanLab.ChirreHagen2025.SmoothT2.theorem2_u6806` (Theorem 2 with diagonal constant 1.0068) and
`LeanLab.ChirreHagen2025.SmoothT2.diag_u6806_K`, which uses
`LeanLab.ChirreHagen2025.U6806.diag_u6806` from `LeanLab/ChirreHagen2025/U6806DiagCSpS3.lean`.

### What is NOT proved in Lean: the hypotheses

The headline theorem takes these as arguments, besides RH. They are not proved here. The list
is quoted verbatim from the header of `U1508Compose445.lean`:

```
  ExplicitA  : for every 0 < δ ≤ 10^-13 the truncated sums
               Σ_{ρ ∈ Z n} c_ρ(δ) y^ρ, c_ρ(δ) = ((1+δ)^ρ - 1)/ρ, ρ = 1/2 + iγ, γ = gZ,
               converge to -(V_δ(y) - B_δ(y)) for a.e. y ≥ 2, where
               V_δ(y) = ψ((1+δ)y) - ψ(y) - δy; Montgomery-Vaughan (12.1);
  HadamardK  : Σ_{γ' ∈ s} 4/(4 + (γ - γ')²) ≤ log |γ| for every finite set s of zeros;
  Ordinates14: every ordinate has |γ| ≥ 14;
  BPTN       : Brent-Platt-Trudgian Lemma 1 zero counts for T ≥ 10^13;
  HSWN70, HSWHead14 : Hasanalizade-Shen-Wong Corollary 1.2 zero counts, T ≥ 70 and T ≥ 14;
  the even Goldbach check up to 4·10^18.
```

and, by name and kind:

```
  RiemannHypothesis   RH, the antecedent of the conclusion.
  hE  ExplicitA gZ Z  cited analytic input, MV (12.1) truncated explicit formula; under RH.
  hH  HadamardK gZ    cited analytic input, Hadamard product bound; under RH.
  h14 Ordinates14 gZ  cited numeric fact, first zero at 14.1347; a computation, not done here.
  hB  BPTN gZ         cited numeric input, Brent-Platt-Trudgian JNT 238 2022 Lemma 1, T ≥ 10^13.
  hN  HSWN70 gZ       cited numeric input, Hasanalizade-Shen-Wong arXiv 2107.06506 Cor 1.2, T ≥ 70.
  hHd HSWHead14 gZ    cited numeric input, same corollary, head clause, T ≥ 14.
  hEv EvenGoldbachUpTo (4·10^18)  cited computation, Oliveira e Silva, Herzog, Pardi 2014.
```

Some imported files (for example `ChirreHagen2025/Statements.lean`, `Tao2012/Statements.lean`,
`DERZ1997/Statements.lean`, `RamareSaouter2003/Statements.lean`, `KadiriLumley2014/Statements.lean`)
state cited results of other papers with `sorry`. They are in the import closure, so the build
prints `declaration uses 'sorry'` warnings for them. The headline theorems do not use them:
`#print axioms` on each headline lists only `propext`, `Classical.choice` and `Quot.sound`, with
no `sorryAx`.

## Paper B

**A lower explicit threshold for Chen's theorem under GRH**
aiXiv:2610.02760 (aixiv.261026.000001)

### Headline, added for v1.3: the threshold theorem, conditional

`LeanLab.BS2022GRH.Cert1575.chenThreshold13375_of_deep_closed` in `LeanLab/BS2022GRH/Cert1575Closed.lean`:

```
theorem chenThreshold13375_of_deep_closed (h5 : Thm5J) (h6 : Thm6J) (h7 : Thm7J)
    (hT4 : LinearSieveT4 (1 / 8349) 112 114) : ChenThreshold13375
```

with, in `LeanLab/BS2022GRH/ChenThresholdGRH.lean`,

```
def ChenThreshold13375 : Prop :=
  GRH → ∀ N : ℕ, Even N → exp (exp 13.375) ≤ (N : ℝ) → ChenSqfreeRep N
```

`ChenSqfreeRep N`: N = p + m, p prime, m > 1 square-free with at most two prime factors.
In words: assume the four cited inputs below. Then under GRH every even N ≥ exp(exp 13.375) is a
prime plus such an m. Axioms: `propext`, `Classical.choice`, `Quot.sound` only, build log
`logs/paperB/20261027T0807Z-9485-U-1575.log`, final entry; earlier entries in that log are failed
attempts fixed before the final build.

Proved inside, no hypotheses: `lemma9J_holds`, the journal's Lemma 9, from `U7153.lemma10`;
`section55_step` and `rep_of_pi2'`, Section 5.5; `Cert1567.bracket13375_holds`, the exact
brackets of Theorems 5, 6, 7 at the new parameters are at least K3J − 10⁻⁵ for every N ≥ X₂;
`Cert1575.eps1500`, ε(1500) < 1/8349 by a kernel certificate, `decide +kernel`, 11 windows, no
`native_decide`; `error_13375`; `cond19_13375`, `cond25_13375`, `X2_ranges`.

### What is NOT proved in Lean: the hypotheses

* GRH, an explicit argument.
* `Thm5J`, `Thm6J`, `Thm7J`: Theorems 5, 6, 7 of Bordignon and Starichkova, transcribed by hand
  and stated as Lean propositions, with GRH and the linear sieve as arguments. They use the
  normalisation U_N = 2e^{-γ}∏_{p>2}(1 − (p−1)^{-2})∏_{p|N, p>2}(p−1)/(p−2); the journal prints
  it without the factor 2. A transcription error here would not be caught by Lean.
* `LinearSieveT4 (1/8349) 112 114`: their Theorem 4, the linear sieve, with Table 1 row 6100.
* `theorems567_of_inputs`, deriving Theorems 5 to 7 from GRH, Lemma 3 and Lemma 7, is an open
  `sorry` in `ChenThresholdGRH.lean`; `Cert1567.eps1500_cert` is a superseded `sorry`. Neither is
  used by the headline, as its axiom list shows.

One file is not a byte-for-byte copy: in `LeanLab/AlmostPrimeSums/Statements.lean` the cited
statement `bordignonStarichkova_GRH` is a `def ... : Prop` here, the form that
`ChenThresholdGRH.lean` uses, instead of a `theorem ... := by sorry` in an older lab copy. It is not
used by the headline. This repository was built from a clean clone with these files,
`lake build LeanLab.BS2022GRH.Cert1575Closed Papers.ChenGRH13375`, Build completed successfully
(9103 jobs), log `logs/paperB/20261027-public-repo-build-Cert1575Closed.log`.

### Earlier checks, v1 to v1.2, still valid

In `LeanLab/BS2022GRH/`, namespace `LeanLab.BS2022GRH.Journal`:

* `K3J` (`JournalMargin.lean`): the main-term constant of Section 5.4, as a real-valued function.
* `theorem3_positive_main` (`JournalPositive.lean`):
  `0.0001 < K3J 0.00256 (exp eulerMascheroniConstant) (1 / 8349) 112 114 LeanLab.ChenExplicit.BJS.cbar`.
* `conditions_13375`, `params_ok_13375`, and `RangeCheck13375.lean`: the parameter ranges at 13.375.
* `theorem3_journal_main`: `0.0045 < K3J` at the journal's own parameters.
* `theorem3_lower_main`, `conditions_1345` (`JournalLower.lean`): the checks at log log X₂ = 13.45.

The Python script `scripts/i0088_numerics.py` remains as a numerical cross-check of ε(1500) and
the total.

## Layout

```
lakefile.toml, lean-toolchain, lake-manifest.json   Lean v4.35.0, Mathlib v4.35.0
LeanLab/...                                          the import closure, unchanged
Papers/GoldbachRH445.lean                            #check and #print axioms, Paper A
Papers/ChenGRH13375.lean                             #check and #print axioms, Paper B
logs/paperA/, logs/paperB/                           original build logs from the lab
scripts/i0088_numerics.py, .out                      Python numerics for Paper B
```

The toolchain and Mathlib pin are the same as in the lab: `leanprover/lean4:v4.35.0`, Mathlib
tag `v4.35.0`, commit `56a005855ea17e0b0958f73ec801ae140b0a1679` in `lake-manifest.json`.

## Building

Install elan (https://github.com/leanprover/elan), then from the repository root:

```
lake exe cache get
lake build Papers.ChenGRH13375
lake build Papers.GoldbachRH445
```

`lake build` with no target builds both. Each `Papers` file prints the statement and the axioms of
every headline theorem. Expected output for every headline: `depends on axioms: [propext,
Classical.choice, Quot.sound]`.

Paper B builds in a few minutes on two cores after the Mathlib cache is in place. Paper A is much
heavier: the `ChirreHagen2025/U6743Diag*`, `U6759*` and `U6806Diag*` files are large interval
certificates (about 9 MB of Lean in total) and need several GB of memory per file; the lab's
build took more than an hour of wall time and had to be resumed after a memory kill and a
timeout, see `logs/paperA/`.

To count `sorry` warnings in a build log: `grep -c "declaration uses .sorry." build.log`.

## Build logs

* `logs/paperA/20261025T0416Z-19415-U-1508.log`: lab build of `LeanLab.Routes.U1508Compose445`,
  ending `Build completed successfully (9183 jobs)` and `EXIT 0`.
* `logs/paperB/20261020T0802Z-20406-JournalPositive.log`, `20261020T1303Z-22201.log`,
  `20261020T0403Z-27388-U1166.log`: lab builds of `JournalPositive`, `RangeCheck13375` and
  `JournalLower`, each `EXIT 0` with 0 `sorry`.

## License

Apache License 2.0, see `LICENSE`.
