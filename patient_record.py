# COP 5230 Object-Oriented Programming Module 2 Assignment (Class Based Vaccine Records List)
# Ryan Stapf
# 5/26/2023

# ***MAIN FILE***

# Import Classes from supporting documents
from patient_details import patient_details
from patient_symptom_records import patient_symptom_record
from patient_vax_records import patient_vax_record


# Create a class for the manager object "patient_record"
# MANAGER OBJECT
class patient_record():
    # The class creates objects of all supporting classes listed above and puts them in a tuple called pList
    def __init__(self):
        self.pDetails = patient_details()
        self.pVaccines = patient_vax_record()
        self.pSymptoms = patient_symptom_record()
        self.pList = (self.pDetails, self.pVaccines, self.pSymptoms)

    # The method of the object manager creates a full patient record combining methods from all 3 classes and storing their data in the tuple
    def new_patient_record(self, pID, pFirst, pLast, pPhone, pAddress, vac_A,
                           vac_B, vac_C, syp_A, syp_B, syp_C):
        self.pDetails.new_details(pID, pFirst, pLast, pPhone, pAddress)
        self.pVaccines.new_vax_record(pID, vac_A, vac_B, vac_C)
        self.pSymptoms.new_syp_record(pID, syp_A, syp_B, syp_C)
        print("Record Added")


# Import Exception Handlers
from exception_handlers import value_checker_YN
from exception_handlers import value_checker_options

# Create an object called new_record based off of the patient_record class to be used in the execution
new_record = patient_record()

# Initializing counter variable for patient number when entering patient data
num_patients = 1

# All user input prompts are inserted into a loop that remains recurrent until the user decides to quit
while True:
    # Prints options for user to input
    print()
    print("-" * 84)
    print("Options Available:")
    print("Press 'i' to input a new patient record")
    print("Press 'r' to report the vaccination status of an individual")
    print("Press 'v' to report the vaccination totals of all patients for each vaccine type")
    print("Press 's' to report the symptom totals of all patients for each vaccine type")
    print("Press 't' to clear all vaccine and symptom data")
    print("Press 'q' to quit program")
    print("-" * 84)

    # Storage variable for the input option representing the action the user intends to take
    action = input("Enter your option: ")
    action = action.lower()
    action = action[0]
    action = value_checker_options(action)
    print()

    # (i) prompts the user to input the first/last name, phone number, address, vaccination statuses, and symptom reports of a new patient
    if action == 'i':
        if num_patients <= 15:
            print("Patient #{0}:".format(num_patients))

            patientFirstName = input("Enter patient first name: ").upper()
            patientLastName = input("Enter patient last name: ").upper()
            patientPhoneNum = input("Enter patient phone number: ")
            patientAddress = input("Enter patient address: ").upper()

            # Vaccine Statuses
            vax_A = input("Did the patient take vac_A? (Y/N) ").upper()
            vax_A = value_checker_YN(vax_A)

            vax_B = input("Did the patient take vac_B? (Y/N) ").upper()
            vax_B = value_checker_YN(vax_B)

            vax_C = input("Did the patient take vac_C? (Y/N) ").upper()
            vax_C = value_checker_YN(vax_C)

            # Symptom report
            # If the vaccine status was previously entered as N, the symptom report is set to N by default. You can't have symptoms from a vaccine you haven't taken.
            if vax_A == 'Y':
                smp_A = input(
                    "Did the patient experience symptoms after taking vac_A? (Y/N) "
                ).upper()
                smp_A = value_checker_YN(smp_A)
            else:
                smp_A = 'N'

            if vax_B == 'Y':
                smp_B = input(
                    "Did the patient experience symptoms after taking vac_B? (Y/N) "
                ).upper()
                smp_B = value_checker_YN(smp_B)
            else:
                smp_B = 'N'

            if vax_C == 'Y':
                smp_C = input(
                    "Did the patient experience symptoms after taking vac_C? (Y/N) "
                ).upper()
                smp_C = value_checker_YN(smp_C)
            else:
                smp_C = 'N'

            # Generates a new patient record by calling the method from patient_record
            new_record.new_patient_record(num_patients, patientFirstName,
                                          patientLastName, patientPhoneNum,
                                          patientAddress, vax_A, vax_B, vax_C,
                                          smp_A, smp_B, smp_C)
            print()
        else:
            print("Maximum number of patients entered for this record.")
        num_patients += 1

    # (r) prompts the user to enter a patient last name, and will return the vaccine status for all 3 vaccines the patient has/hasn't recieved. The methods are called from patient_details.py and patient_vax_records.py
    if action == 'r':
        inputPatientLastName = input("Enter patient last name: ").upper()
        patient_PIN = new_record.pDetails.get_PIN_via_LastName(
            inputPatientLastName)
        new_record.pList[1].get_vax_record(patient_PIN)

    # (v) returns the total number of vaccines of each type recieved within the group of patients. The method is called from patient_vax_records.py
    if action == 'v':
        new_record.pList[1].vax_totals()

    # (s) returns the total number of symptoms reported for each vaccine type recieved within the group of patients. The method is called from patient_symptom_records.py
    if action == 's':
        new_record.pList[2].symptom_totals()

    # (t) resets all vaccine and symptom totals to 0. The methods are called from patient_vax_records.py and patient_symptom_records.py.
    if action == 't':
        new_record.pList[1].vax_reset()
        new_record.pList[2].symptoms_reset()
        print()
        new_record.pList[1].vax_totals()
        print()
        new_record.pList[2].symptom_totals()

    # (q) quits program
    if action == 'q':
        break
