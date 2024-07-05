
#The objective of this project is to compile a list of schedule options for a department of middle school language teachers 
#The teachers must teach 4 sections of 8th grade, 4 sections of 7th grade and 3 sections of 6th grade
#There are 3 teachers J, C and V
# J and C must teach 4 classes while V will only teach 3  

#This is essenrialy a combinatorics problem 

import itertools
from collections import Counter

# Define the variables
J = "Jorge"
C = "Colleen"
V = "Victor"

# Create a list with the desired number of instances
teachers_list = [J] * 4 + [C] * 4 + [V] * 3


# Create 3 places to store 4 variables each
classes = [
    [None] * 4,  # 8th grade
    [None] * 4,  # 7th grade
    [None] * 3   # 6th grade
]

# Function to check if a place has at least two kinds of variables
def has_two_kinds(place):
    return len(set(place)) >= 2

# Generate all possible ways to assign 4 variables to each of the 2 places and 3 variables to the last place
def generate_assignments(variables):
    assignments = set()
    # Get all possible combinations of 4 variables for the first place
    for first_place in itertools.combinations(variables, 4):
        if not has_two_kinds(first_place):
            continue
        remaining_after_first = list(variables)
        for var in first_place:
            remaining_after_first.remove(var)
        
        # Get all possible combinations of 4 variables for the second place
        for second_place in itertools.combinations(remaining_after_first, 4):
            if not has_two_kinds(second_place):
                continue
            remaining_after_second = list(remaining_after_first)
            for var in second_place:
                remaining_after_second.remove(var)
            
            # The remaining 3 variables go to the third place
            third_place = tuple(remaining_after_second)
            if not has_two_kinds(third_place):
                continue
            
            # Create a sorted tuple of the assignment to ensure uniqueness
            sorted_assignment = tuple(sorted([tuple(sorted(first_place)), tuple(sorted(second_place)), tuple(sorted(third_place))]))
            
            # Add the sorted assignment to the set
            assignments.add(sorted_assignment)
    
    return assignments

# Generate all unique assignments
unique_assignments = generate_assignments(teachers_list)

# Function to count the number of places each variable is present in
def count_variable_places(assignment):
    count = Counter()
    for place in assignment:
        unique_vars = set(place)
        for var in unique_vars:
            count[var] += 1
    return count

# Prepare data for the text file
output_lines = []

for i, assignment in enumerate(unique_assignments):
    # Identify the place with 3 variables
    places = list(assignment)
    place_with_3_vars = next(place for place in places if len(place) == 3)
    places.remove(place_with_3_vars)
    place_with_4_vars1, place_with_4_vars2 = places

    # Count the number of places each variable is present in
    variable_count = count_variable_places(assignment)
    variable_count_str = ", ".join([f"{var}: {count} preps" for var, count in variable_count.items()])

    # Append the assignment details to the output lines
    output_lines.append(f"Assignment {i+1}:")
    output_lines.append(f"  8th grade: {place_with_4_vars1}")
    output_lines.append(f"  7th grade: {place_with_4_vars2}")
    output_lines.append(f"  6th: {place_with_3_vars}")
    output_lines.append(f"  Class preps needed: {variable_count_str}\n")

# Write the output to a text file
with open('ClassAssignments3.txt', 'w') as f:
    f.write("\n".join(output_lines))

print("Assignments have been exported to 'ClassAssignments3.txt'.")