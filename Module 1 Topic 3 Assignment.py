# COP 5230 Object-Oriented Programming Module 1 Topic 3 Assignment (Class Based Vaccine Records List)
# Ryan Stapf
# 5/19/2023

# Vaccination Records

# Create a class for the record which starts out with a list attribute
class vax_record():
  def __init__(self):
    self.pList = []

  # The first method is to create a new record which returns a dictionary of a patient's name, their vaccine statuses, and appends said dictionary to pList
  def new_record(self, pName, vac_A, vac_B, vac_C):
    self.pName = pName
    self.vac_A = vac_A
    self.vac_B = vac_B
    self.vac_C = vac_C
    self.pDict = {'Patient Name': pName, 'vac_A': vac_A, 'vac_B': vac_B, 'vac_C': vac_C}
    self.pList.append(self.pDict)
    print("Record Added")
    
  # The second method is used to look up a patient record with their name as an input. Functionally, this method is no different than what I used in the previous assginment, the only difference is the reference to pList.
  def patientLookup(self, input_name):
    PIN = 0
    while PIN < len(self.pList):
      if input_name == self.pList[PIN]['Patient Name']:
        print("Vaccine Data for {0}:\nvac_A: {1}\nvac_B: {2}\nvac_C: {3}".format(self.pList[PIN]['Patient Name'], self.pList[PIN]['vac_A'], self.pList[PIN]['vac_B'], self.pList[PIN]['vac_C']))
        return
      PIN += 1
    # If input_name doesn't match any existing names in the records
    print("Patient Not Found")

  # The third method is used to look up the total number of vaccinations among the group. Likewise with the previous method, the only difference is the reference to pList.
  def vaccineTotals(self):
    PIN = 0
    num_vac_A = 0
    num_vac_B = 0
    num_vac_C = 0
    while PIN < len(self.pList):
      if self.pList[PIN]['vac_A'] == 'Y':
        num_vac_A += 1
      if self.pList[PIN]['vac_B'] == 'Y':
        num_vac_B += 1
      if self.pList[PIN]['vac_C'] == 'Y':
        num_vac_C += 1
      PIN += 1
    print("Number of Vaccines of each type taken in this group:\nvac_A: {0}\nvac_B: {1}\nvac_C: {2}".format(num_vac_A, num_vac_B, num_vac_C))


print("Vaccination Status Lookup")

# Create an object called new_record based off of the vax_record class to be used in the execution
new_record = vax_record()

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
  print("Press 'v' to report the vaccination totals of all 15 patients for each vaccine type")
  print("Press 'q' to quit program")
  print("-" * 84)

  # Storage variable for the input option representing the action the user intends to take
  action = input("Enter your option: ")
  action = action.lower()
  action = action[0]
  print()

  # (i) prompts the user to input the names and vaccination statuses of 15 patients
  if action == 'i':
    if num_patients <= 15:
      print("Patient #{0}:".format(num_patients))
      patientName = input("Enter full patient name: ").upper()
      status_A = input("Enter vaccine status for vac_A (Y/N): ").upper()
      status_B = input("Enter vaccine status for vac_B (Y/N): ").upper()
      status_C = input("Enter vaccine status for vac_C (Y/N): ").upper()
      new_record.new_record(patientName, status_A, status_B, status_C)
      print()
    else:
      print("Maximum number of patients entered for this record.")
    num_patients += 1

  # (r) prompts the user to enter a patient name, and will return the vaccine status for all 3 vaccines the patient has/hasn't recieved
  if action == 'r':
    inputPatientName = input("Enter full patient name: ").upper()
    new_record.patientLookup(inputPatientName)

  # (v) returns the total number of vaccines of each type recieved within the group of 15 patients
  if action == 'v':
    new_record.vaccineTotals()

  # (q) quits program
  if action == 'q':
    break