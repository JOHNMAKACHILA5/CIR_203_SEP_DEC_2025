patient = ("John Doe", 45, "120/80", 72)
print("Age:", patient[1])
print("Heart Rate:", patient[3])
patient_list = list(patient)
patient_list[3] = 75  # Updated heart rate
updated_patient = tuple(patient_list)
print(updated_patient)
patients = (
    ("Alice", 30, "110/70", 68),
    ("Bob", 50, "130/85", 80),
    ("Carol", 40, "120/78", 72),
    ("David", 35, "115/75", 70),
    ("Eve", 28, "108/65", 65)
)

names = [patient[0] for patient in patients]
print("Patient Names:", names)
#
# 3. Why Tuples Are Suitable for Patient Vitals (4 marks)

# Tuples are ideal for storing patient vitals because:
#
# Immutability: Vitals should not be accidentally changed; tuples prevent modification.
#
# Data Integrity: Ensures consistent and reliable records.
#
# Performance: Tuples are faster than lists for fixed data.
#
# Structured Storage: Each element has a defined position (e.g., name, age), making access predictable.