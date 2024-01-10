# This class governs the patient symptom record object containing their ID number and reports of whether or not the patient experienced symptoms from any of the 3 vaccines. It effectively operates the same way as the vax_records file.

class patient_symptom_record():
  def __init__(self):
    self.sypList = []

  def new_syp_record(self, pID, syp_A, syp_B, syp_C):
    self.pID = pID
    self.syp_A = syp_A
    self.syp_B = syp_B
    self.syp_C = syp_C
    self.sypDict = {'Patient ID_Symptoms': pID, 'Symptoms A': syp_A, 'Symptoms B': syp_B, 'Symptoms C': syp_C}
    self.sypList.append(self.sypDict)
    #print("Symptom Record Added")

  def get_symptom_record(self, pID):
    PIN = 0
    while PIN < len(self.sypList):
      if pID == self.sypList[PIN]['Patient ID_Symptoms']:
        print("\nSymptoms from Vaccine A: {0}\nSymptoms from Vaccine B: {1}\nSymptoms from Vaccine C: {2}\n".format(self.sypList[PIN]['Symptoms A'], self.sypList[PIN]['Symptoms B'], self.sypList[PIN]['Symptoms C']))
      PIN += 1

  def symptom_totals(self):
    PIN = 0
    num_syp_A = 0
    num_syp_B = 0
    num_syp_C = 0
    while PIN < len(self.sypList):
      if self.sypList[PIN]['Symptoms A'] == 'Y':
        num_syp_A += 1
      if self.sypList[PIN]['Symptoms B'] == 'Y':
        num_syp_B += 1
      if self.sypList[PIN]['Symptoms C'] == 'Y':
        num_syp_C += 1
      PIN += 1
    print("Number of Symptoms reported from each vaccine type taken in this group:\nPatients Reporting Symptoms from Vaccine A: {0}\nPatients Reporting Symptoms from Vaccine B: {1}\nPatients Reporting Symptoms from Vaccine C: {2}".format(num_syp_A, num_syp_B, num_syp_C))

  # Sets all symptom values to 'N' which then sets the total sum for each to 0
  def symptoms_reset(self):
    PIN = 0
    while PIN < len(self.sypList):
      self.sypList[PIN]['Symptoms A'] = 'N'
      self.sypList[PIN]['Symptoms B'] = 'N'
      self.sypList[PIN]['Symptoms C'] = 'N'
      PIN += 1
    print("Symptom Records Reset")