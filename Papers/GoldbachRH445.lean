/-
Paper A: "Goldbach numbers in intervals of length 4.45 log^2 x under the Riemann Hypothesis".
aiXiv:2610.02672 (aixiv.261025.000001).

This file only re-exports the headline results and prints their statements and axioms.
The proofs live in the LeanLab modules imported below.
-/
import LeanLab.Routes.U1508Compose445
import LeanLab.ChirreHagen2025.U6806Theorem2Sp

-- Headline: under RH and the named inputs, a Goldbach number in (x, x + 4.45 log^2 x) for x ≥ 3.
#check @LeanLab.Routes.U1508.goldbach_445_hsw_gZ
#print axioms LeanLab.Routes.U1508.goldbach_445_hsw_gZ

-- Variant with a general ordinate family for the J step.
#check @LeanLab.Routes.U1508.goldbach_445_hsw
#print axioms LeanLab.Routes.U1508.goldbach_445_hsw

-- Theorem 2 with the sharpened diagonal constant 1.0068.
#check @LeanLab.ChirreHagen2025.SmoothT2.theorem2_u6806
#print axioms LeanLab.ChirreHagen2025.SmoothT2.theorem2_u6806

-- The diagonal bound used by Theorem 2.
#check @LeanLab.ChirreHagen2025.U6806.diag_u6806
#print axioms LeanLab.ChirreHagen2025.U6806.diag_u6806
#check @LeanLab.ChirreHagen2025.SmoothT2.diag_u6806_K
#print axioms LeanLab.ChirreHagen2025.SmoothT2.diag_u6806_K
