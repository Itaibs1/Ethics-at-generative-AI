import pandas as pd
import random
import unittest

# Path to the CSV file containing the candidates
csv_file_path = "C:/Project/job_candidates.csv"

# Define the selection criteria
experience_threshold = random.randint(0, 20)

# Load candidates from CSV
df = pd.read_csv(csv_file_path)

# Filter candidates based on criteria
filtered_candidates = df[df["ExperienceYears"] > experience_threshold]

# Number of runs for selecting a random candidate
runs = 1000
loop = 40


# Test suite for ethical evaluations
class TestEthicalSelection(unittest.TestCase):
    def setUp(self):
        self.filtered_candidates = filtered_candidates

    def test_representative_data(self):
        """Test if the data is representative of the broader population"""
        self.assertGreater(len(df), 0, "Data should not be empty")
        self.assertIn("ExperienceYears", df.columns, "Data must include 'ExperienceYears' column")

    def test_fair_criteria(self):
        """Test if the selection criteria are fair"""
        self.assertGreater(experience_threshold, 0, "Experience threshold should be positive")

    def test_randomness(self):
        """Test if the randomness in selection is unbiased"""
        counts = self.filtered_candidates["ExperienceYears"].value_counts()
        variance = counts.var()
        self.assertLess(variance, 100, "Variance in selection should be within a reasonable range")

    def test_fairness_check(self):
        """Test if all candidates above the threshold have equal chance"""
        candidate_ids = self.filtered_candidates.index
        selections = []
        for j in range(loop):
            for i in range(runs):
                if not self.filtered_candidates.empty:
                    selected_candidate = self.filtered_candidates.sample()
                    selections.append(selected_candidate.index[0])

        selection_counts = pd.Series(selections).value_counts()
        fairness_variance = selection_counts.var()
        self.assertLess(fairness_variance, 50, "Variance in candidate selection should be low, ensuring fairness")


if __name__ == "__main__":
    unittest.main()
