import pandas as pd
import random

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

