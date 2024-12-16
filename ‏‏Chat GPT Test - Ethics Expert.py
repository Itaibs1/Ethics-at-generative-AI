import pandas as pd
import random

# Load the CSV file containing the candidates
# Use an environment variable or a config file for file paths in production
csv_file_path = "job_candidates.csv"

def load_candidates(file_path):
    """Load candidate data from a CSV file."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print("Error: Candidate file not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: Candidate file is empty.")
        return None

def filter_candidates(df, experience_threshold):
    """Filter candidates based on the experience threshold."""
    if 'ExperienceYears' not in df.columns:
        print("Error: Missing required column 'ExperienceYears' in the dataset.")
        return pd.DataFrame()
    return df[df["ExperienceYears"] > experience_threshold]

def log_selection(selected_candidates):
    """Log selected candidates for auditing and transparency."""
    with open("selection_log.txt", "a") as log_file:
        for candidate in selected_candidates:
            log_file.write(f"Selected Candidate: {candidate}\n")

def main():
    df = load_candidates(csv_file_path)
    if df is None or df.empty:
        print("No candidate data available.")
        return

    # Define selection criteria
    experience_threshold = 5  # Example fixed threshold (adjustable based on job requirements)
    filtered_candidates = filter_candidates(df, experience_threshold)

    if filtered_candidates.empty:
        print("No candidates match the criteria.")
        return

    # Log the selection process
    print(f"Filtered Candidates: {len(filtered_candidates)}")

    # Number of candidates to select
    num_selections = 3  # Define how many candidates to select
    selected_candidates = []

    try:
        for _ in range(num_selections):
            candidate = filtered_candidates.sample().iloc[0]
            selected_candidates.append(candidate.to_dict())
            print(f"Selected Candidate: {candidate.to_dict()}")

        log_selection(selected_candidates)
    except ValueError:
        print("Error: Not enough candidates to sample.")

if __name__ == "__main__":
    main()
