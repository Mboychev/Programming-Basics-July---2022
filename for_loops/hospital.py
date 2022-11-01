period = int(input())
doctors_total = 7
treated_patients = 0
untreated_patients = 0

for current_day in range(1, period + 1):

    patients_per_day = int(input())

    if current_day % 3 == 0 and untreated_patients > treated_patients:
        doctors_total += 1

    if patients_per_day > doctors_total:
        current_untreated_patients = patients_per_day - doctors_total
        untreated_patients += current_untreated_patients
        treated_patients += doctors_total


    else:
        treated_patients += patients_per_day


print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")




