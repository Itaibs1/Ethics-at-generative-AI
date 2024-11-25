
import pandas as pd
import random

# Test DataFrame for testing ethical aspects
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "ExperienceYears": [5, 10, 15, 20, 25],
    "Gender": ["Female", "Male", "Male", "Female", "Female"],
}

df = pd.DataFrame(data)

def test_integrity():
    try:
        # Test if the data load and filter process are consistent
        experience_threshold = 10  # Fixed threshold for testing
        filtered_candidates = df[df["ExperienceYears"] > experience_threshold]
        assert not filtered_candidates.empty, "Integrity Issue: No candidates found despite valid data."
        print("Integrity Test Passed")
    except Exception as e:
        print(f"Integrity Test Failed: {e}")

def test_bias():
    try:
        # Simulate multiple runs with random thresholds
        thresholds = [random.randint(0, 20) for _ in range(1000)]
        results = []
        for threshold in thresholds:
            filtered_candidates = df[df["ExperienceYears"] > threshold]
            results.append(len(filtered_candidates))
        
        # Check if the results are disproportionately skewed
        assert len(set(results)) > 1, "Bias Issue: Selection process is too deterministic."
        print("Bias Test Passed")
    except Exception as e:
        print(f"Bias Test Failed: {e}")

def test_fairness():
    try:
        # Check if the selection process unfairly excludes a group
        experience_threshold = 10  # Fixed threshold for simplicity
        filtered_candidates = df[df["ExperienceYears"] > experience_threshold]
        female_candidates = filtered_candidates[filtered_candidates["Gender"] == "Female"]
        male_candidates = filtered_candidates[filtered_candidates["Gender"] == "Male"]
        
        # Ensure no gender is disproportionately excluded
        assert len(female_candidates) > 0 and len(male_candidates) > 0, "Fairness Issue: Gender exclusion detected."
        print("Fairness Test Passed")
    except Exception as e:
        print(f"Fairness Test Failed: {e}")

# Run the tests
test_integrity()
test_bias()
test_fairness()
