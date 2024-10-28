def test_data_integrity():
    df = pd.read_csv(csv_file_path)
    assert not df.empty, "CSV file is empty"
    assert "ExperienceYears" in df.columns, "ExperienceYears column is missing"
    assert df["ExperienceYears"].dtype == int, "ExperienceYears should be integers"

def test_threshold_integrity():
    assert 0 <= experience_threshold <= 20, "Experience threshold is out of valid range"


def test_demographic_bias():
    df = pd.read_csv(csv_file_path)
    gender_ratio = df["Gender"].value_counts(normalize=True)
    assert abs(gender_ratio["Male"] - gender_ratio["Female"]) < 0.1, "Gender imbalance detected"

def test_age_bias():
    df = pd.read_csv(csv_file_path)
    age_groups = pd.cut(df["Age"], bins=[0, 30, 50, 100], labels=["Young", "Middle", "Senior"])
    age_ratio = age_groups.value_counts(normalize=True)
    assert max(age_ratio) - min(age_ratio) < 0.2, "Age group imbalance detected"

def test_equal_opportunity():
    runs = 1000
    selected_candidates = []
    for _ in range(runs):
        if not filtered_candidates.empty:
            selected_candidates.append(filtered_candidates.sample().index[0])
    unique_selections = len(set(selected_candidates))
    assert unique_selections / len(filtered_candidates) > 0.9, "Selection process may not be providing equal opportunities"

    def test_fairness_across_attributes():
        df = pd.read_csv(csv_file_path)
        protected_attributes = ["Gender", "Ethnicity"]
        for attr in protected_attributes:
            group_selection_rates = {}
            for group in df[attr].unique():
                group_df = df[df[attr] == group]
                group_selection_rate = len(filtered_candidates[filtered_candidates[attr] == group]) / len(group_df)
                group_selection_rates[group] = group_selection_rate
            assert max(group_selection_rates.values()) - min(
                group_selection_rates.values()) < 0.1, f"Unfair selection rates across {attr} groups"
