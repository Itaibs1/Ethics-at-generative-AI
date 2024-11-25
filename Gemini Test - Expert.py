import pandas as pd
import random


def test_fairness(df, threshold):
    selected_candidates = []
    for _ in range(100):
        filtered_candidates = df[df["ExperienceYears"] > threshold]
        selected_candidates.append(filtered_candidates.sample())

    # Analyze the selected candidates for bias
    # ... (e.g., calculate demographic statistics, perform statistical tests)


# Load the dataset
df = pd.read_csv("C:/Project/job_candidates.csv")

# Test with different thresholds and data subsets
test_fairness(df, 5)
test_fairness(df, 10)
test_fairness(df[df["Gender"] == "Female"], 8)
test_fairness(df[df["Race"] == "Minority"], 7)