"""Using a breakpoint and the debugger, find the problem and fix the following code:

patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

for patient in patients:
    weight, height = patients[0]
    bmi = calculate_bmi(height, weight)
    print("Patient's BMI is: %f" % bmi)
The correct BMIs are 21.604938, 22.160665 and 51.903114."""

patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

for patient in patients:
    weight, height = patient    # This was the logical error as loop must be intended to iterate through each value in the list—patient
    bmi = calculate_bmi(weight, height) # order of parameters defined in the function matters.
    print("Patient's BMI is: %f" % bmi)