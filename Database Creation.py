import csv
import random
import faker

# Initialize the faker generator
fake = faker.Faker()

# Define the number of records
num_records = 100000

# List of possible skills
skills_list = ["Python", "Java", "C++", "JavaScript", "SQL", "Ruby", "Go", "HTML", "CSS", "React", "Angular", "Django", "Flask", "AWS", "Azure"]

# List of possible genders
gender_list = ["Male", "Female"]

# List of possible origins (countries)
country_list = ["United States", "Canada", "United Kingdom", "Germany", "France", "India", "China", "Japan", "Australia", "Brazil"]

# CSV file path
csv_file_path = "C:\Project\job_candidates.csv"

# Function to generate a list of random skills
def generate_random_skills():
    num_skills = random.randint(1, 5)
    return ", ".join(random.sample(skills_list, num_skills))

# Open the CSV file for writing
with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(["CandidateID", "FirstName", "LastName", "Gender", "Origin", "Email", "PhoneNumber", "ExperienceYears", "Skills", "Location"])
    
    # Generate candidate data
    for i in range(1, num_records + 1):
        candidate_id = i
        first_name = fake.first_name()
        last_name = fake.last_name()
        gender = random.choice(gender_list)
        origin = random.choice(country_list)
        email = fake.email()
        phone_number = fake.phone_number()
        experience_years = random.randint(0, 20)
        skills = generate_random_skills()
        location = fake.city()
        
        # Write the candidate row
        writer.writerow([candidate_id, first_name, last_name, gender, origin, email, phone_number, experience_years, skills, location])

print(f"{num_records} job candidates have been written to {csv_file_path}.")
