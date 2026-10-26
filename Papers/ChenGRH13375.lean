/-
Paper B: "A lower explicit threshold for Chen's theorem under GRH".
aiXiv:2610.02760 (aixiv.261026.000001).

This file only re-exports the headline results and prints their statements and axioms.
These are arithmetic and parameter-range checks for Section 5.4 of Bordignon and Starichkova;
Chen's theorem itself is not stated or proved here.
-/
import LeanLab.BS2022GRH.JournalPositive
import LeanLab.BS2022GRH.JournalMargin
import LeanLab.BS2022GRH.RangeCheck13375
import LeanLab.BS2022GRH.JournalLower

-- The main-term constant K3J used in Section 5.4.
#check @LeanLab.BS2022GRH.Journal.K3J

-- Threshold log N ≥ e^13.375, alpha = 0.00256.
#check @LeanLab.BS2022GRH.Journal.theorem3_positive_main
#print axioms LeanLab.BS2022GRH.Journal.theorem3_positive_main
#check @LeanLab.BS2022GRH.Journal.conditions_13375
#print axioms LeanLab.BS2022GRH.Journal.conditions_13375
#check @LeanLab.BS2022GRH.Journal.params_ok_13375
#print axioms LeanLab.BS2022GRH.Journal.params_ok_13375

-- Parameter ranges at the 13.375 threshold.
#check @LeanLab.BS2022GRH.Journal.sieve_ranges_13375
#print axioms LeanLab.BS2022GRH.Journal.sieve_ranges_13375
#check @LeanLab.BS2022GRH.Journal.mono_range_13375
#print axioms LeanLab.BS2022GRH.Journal.mono_range_13375
#check @LeanLab.BS2022GRH.Journal.lemma7_range
#print axioms LeanLab.BS2022GRH.Journal.lemma7_range
#check @LeanLab.BS2022GRH.Journal.remark1_H_vacuity
#print axioms LeanLab.BS2022GRH.Journal.remark1_H_vacuity

-- The journal parameters (alpha = 0.001) margin.
#check @LeanLab.BS2022GRH.Journal.theorem3_journal_main
#print axioms LeanLab.BS2022GRH.Journal.theorem3_journal_main

-- The more conservative threshold e^13.45, alpha = 0.0024.
#check @LeanLab.BS2022GRH.Journal.theorem3_lower_main
#print axioms LeanLab.BS2022GRH.Journal.theorem3_lower_main
#check @LeanLab.BS2022GRH.Journal.conditions_1345
#print axioms LeanLab.BS2022GRH.Journal.conditions_1345
