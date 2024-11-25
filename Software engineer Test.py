import pandas as pd
import random

# Path to the CSV file containing the candidates
csv_file_path = "C:/Project/job_candidates.csv"

# Load the CSV file into a DataFrame
def load_csv_file(csv_file_path):
    try:
        df = pd.read_csv(csv_file_path)
        return df
    except FileNotFoundError:
        print(f"Error: The file '{csv_file_path}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{csv_file_path}' is empty.")
    except pd.errors.ParserError:
        print(f"Error: The file '{csv_file_path}' contains parsing errors.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Define the selection criteria
experience_threshold = random.randint(0, 20)

df = load_csv_file(csv_file_path)

# Filter candidates based on criteria
filtered_candidates = df[(df["ExperienceYears"] > experience_threshold)]

# Number of runs for selecting a random candidate
runs = 1000
loop = 40
male = 0
woman = 0
for j in range(loop):
    for i in range(runs):  # Loop should run `runs` times
        # Check if there are any matching candidates
        if not filtered_candidates.empty:
            # Randomly select a candidate from the filtered list
            selected_candidate = filtered_candidates.sample()

            # Check gender statistics
            if "Gender" in selected_candidate.columns:
                if selected_candidate["Gender"].iloc[0] == "Male":  # Use `iloc[0]` for the single row
                    male += 1
                else:
                    woman += 1
            else:
                print("The 'Gender' column is not available in the dataset.")
        else:
            print("No candidates match the criteria.")
            break

    # Calculate and display gender statistics
    total_selected = male + woman
    if total_selected > 0:
        if abs((male / total_selected)/(woman / total_selected)) > 5: 
            print(f"Male statistics: {male / total_selected:.2%}")
            print(f"Female statistics: {woman / total_selected:.2%}")
            print("The program has bias issue")
            break
    else:
        print("No candidates were selected.")
print("There is no issue found")    

