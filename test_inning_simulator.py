#!/usr/bin/env python

# Author: Syd Polk

import unittest

from inning_simulator import Inning, out, k, single, double, triple, hr, e, bb, hbp

class TestInningSimulator(unittest.TestCase):

    def test_str(self):
        inning = Inning(True, False, True, 1, 3)
        desc = inning.__str__()
        self.assertEqual(desc, "Bases: 101, Outs: 1, Runs: 3")

    def test_incr_outs_zero_outs(self):
        inning = Inning(False, False, False, 0, 0)
        inning.incr_outs()
        self.assertFalse(inning.first_base, "Should be nobody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 1, "Should be one out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_incr_outs_two_outs(self):
        # Test clearing of bases as well
        inning = Inning(True, True, True, 2, 0)
        inning.incr_outs()
        self.assertFalse(inning.first_base, "Should be nobody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 3, "Should be three outs")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_advance_runners_from_third(self):
        inning = Inning(False, False, True, 0, 0)
        inning.advance_runners()
        self.assertFalse(inning.first_base, "Should be nobody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 1, "Should be one runs")

    def test_advance_runners_from_second(self):
        inning = Inning(False, True, False, 0, 0)
        inning.advance_runners()
        self.assertFalse(inning.first_base, "Should be nobody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertTrue(inning.third_base, "Should be somebody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_advance_runners_from_first(self):
        inning = Inning(True, False, False, 0, 0)
        inning.advance_runners()
        self.assertFalse(inning.first_base, "Should be nobody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_advance_runners_nobody_on(self):
        inning = Inning(False, False, False, 0, 0)
        inning.advance_runners()
        self.assertFalse(inning.first_base, "Should be nobody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_batter_to_first_non_forcing(self):
        inning = Inning(False, True, False, 0, 0)
        inning.batter_to_first_non_forcing()
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertTrue(inning.third_base, "Should be somebody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_batter_to_first_forcing_runner_on_first(self):
        inning = Inning(True, False, False, 0, 0)
        inning.batter_to_first_forcing()
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_batter_to_first_forcing_runner_on_second(self):
        inning = Inning(False, True, False, 0, 0)
        inning.batter_to_first_forcing()
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_batter_to_first_runners_on_first_and_second(self):
        inning = Inning(True, True, False, 0, 0)
        inning.batter_to_first_forcing()
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertTrue(inning.third_base, "Should be somebody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_batter_to_first_bases_loaded(self):
        inning = Inning(True, True, True, 0, 0)
        inning.batter_to_first_forcing()
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertTrue(inning.third_base, "Should be somebody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 1, "Should be one run")

    def test_out(self):
        inning = Inning(False, False, False, 0, 0)
        out(inning)
        self.assertFalse(inning.first_base, "Should be nobody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 1, "Should be one out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_out_nobody_out_bases_loaded(self):
        inning = Inning(True, True, True, 0, 0)
        out(inning)
        self.assertFalse(inning.first_base, "Should be nobody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertTrue(inning.third_base, "Should be somebody on third")
        self.assertEqual(inning.outs, 1, "Should be one out")
        self.assertEqual(inning.runs, 1, "Should be one runs")

    def test_out_two_outs_bases_loaded(self):
        inning = Inning(True, True, True, 2, 0)
        out(inning)
        self.assertFalse(inning.first_base, "Should be nobody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 3, "Should be three outs")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_k(self):
        inning = Inning(True, True, True, 0, 0)
        k(inning)
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertTrue(inning.third_base, "Should be somebody on third")
        self.assertEqual(inning.outs, 1, "Should be one out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_single_nobody_on(self):
        inning = Inning(False, False, False, 0, 0)
        single(inning)
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_single_man_on_first(self):
        inning = Inning(True, False, False, 0, 0)
        single(inning)
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_single_man_on_third(self):
        inning = Inning(False, False, True, 0, 0)
        single(inning)
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 1, "Should be one run")

    def test_double_nobody_on(self):
        inning = Inning(False, False, False, 0, 0)
        double(inning)
        self.assertFalse(inning.first_base, "Should be nobody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_double_man_on_first(self):
        inning = Inning(True, False, False, 0, 0)
        double(inning)
        self.assertFalse(inning.first_base, "Should be nobody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertTrue(inning.third_base, "Should be somebody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_double_men_on_second_and_third(self):
        inning = Inning(False, True, True, 0, 0)
        double(inning)
        self.assertFalse(inning.first_base, "Should be nobody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 2, "Should be two runs")

    def test_triple_nobody_on(self):
        inning = Inning(False, False, False, 0, 0)
        triple(inning)
        self.assertFalse(inning.first_base, "Should be nobody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertTrue(inning.third_base, "Should be somebody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_triple_men_on_first_and_third(self):
        inning = Inning(True, False, True, 0, 0)
        triple(inning)
        self.assertFalse(inning.first_base, "Should be nobody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertTrue(inning.third_base, "Should be somebody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 2, "Should be two runs")

    def test_home_run_nobody_on(self):
        inning = Inning(False, False, False, 0, 0)
        hr(inning)
        self.assertFalse(inning.first_base, "Should be nobody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 1, "Should be one run")

    def test_grand_slam(self):
        inning = Inning(True, True, True, 0, 0)
        hr(inning)
        self.assertFalse(inning.first_base, "Should be nobody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 4, "Should be four runs")

    def test_error_nobody_on(self):
        inning = Inning(False, False, False, 0, 0)
        e(inning)
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_error_man_on_first(self):
        inning = Inning(True, False, False, 0, 0)
        e(inning)
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_error_man_on_third(self):
        inning = Inning(False, False, True, 0, 0)
        e(inning)
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 1, "Should be one run")

    def test_walk_bases_empty(self):
        inning = Inning(False, False, False, 0, 0)
        bb(inning)
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_walk_man_on_first(self):
        inning = Inning(True, False, False, 0, 0)
        bb(inning)
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_walk_man_on_second(self):
        inning = Inning(False, True, False, 0, 0)
        bb(inning)
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_walk_bases_loaded(self):
        inning = Inning(True, True, True, 0, 0)
        bb(inning)
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertTrue(inning.third_base, "Should be somebody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 1, "Should be one runs")

    def test_hbp_bases_empty(self):
        inning = Inning(False, False, False, 0, 0)
        hbp(inning)
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertFalse(inning.second_base, "Should be nobody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_hbp_man_on_first(self):
        inning = Inning(True, False, False, 0, 0)
        hbp(inning)
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_hbp_man_on_second(self):
        inning = Inning(False, True, False, 0, 0)
        hbp(inning)
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertFalse(inning.third_base, "Should be nobody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 0, "Should be no runs")

    def test_hbp_bases_loaded(self):
        inning = Inning(True, True, True, 0, 0)
        hbp(inning)
        self.assertTrue(inning.first_base, "Should be somebody on first")
        self.assertTrue(inning.second_base, "Should be somebody on second")
        self.assertTrue(inning.third_base, "Should be somebody on third")
        self.assertEqual(inning.outs, 0, "Should be nobody out")
        self.assertEqual(inning.runs, 1, "Should be one runs")


if __name__ == '__main__':
    unittest.main()

