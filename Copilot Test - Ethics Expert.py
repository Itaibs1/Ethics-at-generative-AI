import pandas as pd
import random
import pytest

# Path to the CSV file containing the candidates
csv_file_path = "C:/Project/job_candidates.csv"

# Define the selection criteria
experience_threshold = random.randint(0, 20)

df = pd.read_csv(csv_file_path)

# Filter candidates based on criteria
filtered_candidates = df[(df["ExperienceYears"] > experience_threshold)]

# Number of runs for selecting a random candidate
runs = 1000
loop = 40
selected_candidate = "No Candidate Found"

# Define test functions
def test_transparency():
    assert experience_threshold >= 0, "Experience threshold should be non-negative"
    assert runs > 0, "Number of runs should be greater than zero"
    assert loop > 0, "Number of loops should be greater than zero"

def test_unbiased_criteria():
    assert df["ExperienceYears"].min() >= 0, "Experience should be non-negative"
    assert df["ExperienceYears"].max() <= 50, "Experience should be within reasonable bounds"

def test_equitable_selection():
    candidates_count = len(filtered_candidates)
    if candidates_count > 0:
        selection_counts = filtered_candidates.sample(n=runs*loop, replace=True).value_counts()
        average_selection_count = sum(selection_counts) / candidates_count
        assert all(abs(count - average_selection_count) < average_selection_count * 0.1 for count in selection_counts), "All candidates should be equally likely to be selected within a reasonable margin"

def test_data_privacy():
    sensitive_columns = ["SensitiveInfo"]
    for col in sensitive_columns:
        assert col not in df.columns, "Candidate data should not contain sensitive information"

def test_error_handling():
    if filtered_candidates.empty:
        assert selected_candidate == "No Candidate Found", "Should handle no matching candidates gracefully"

# Run tests
pytest.main()

# Main code execution
for j in range(loop):
    for i in range(runs):  # Loop should run `runs` times
        # Check if there are any matching candidates
        if not filtered_candidates.empty:
            # Randomly select a candidate from the filtered list
            selected_candidate = filtered_candidates.sample()
        else:
            print("No candidates match the criteria.")
            break
    print("The Candidate is:")
    print(selected_candidate)
