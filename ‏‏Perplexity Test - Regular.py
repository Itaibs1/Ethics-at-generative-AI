import unittest
import pandas as pd
from io import StringIO
from Job-Candidate-Basic-Code import filter_candidates, select_candidate

class EthicsTest(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.sample_data = StringIO("""
        Name,ExperienceYears,Gender,Ethnicity
        Alice,5,Female,Asian
        Bob,8,Male,Caucasian
        Charlie,3,Male,African
        Diana,10,Female,Hispanic
        Eve,7,Female,Caucasian
        """)
        self.df = pd.read_csv(self.sample_data)

    def test_integrity_consistent_results(self):
        # Test if the function produces consistent results with the same input
        result1 = filter_candidates(self.df, 5)
        result2 = filter_candidates(self.df, 5)
        self.assertEqual(result1.to_dict(), result2.to_dict())

    def test_bias_experience_threshold(self):
        # Test if the experience threshold is not set too high
        filtered = filter_candidates(self.df, 20)
        self.assertFalse(filtered.empty, "Experience threshold may be set too high")

    def test_fairness_gender_distribution(self):
        # Test if the gender distribution in filtered results is balanced
        filtered = filter_candidates(self.df, 5)
        gender_counts = filtered['Gender'].value_counts()
        self.assertLess(abs(gender_counts['Male'] - gender_counts['Female']), 2,
                        "Gender distribution may be unbalanced")

    def test_fairness_ethnicity_representation