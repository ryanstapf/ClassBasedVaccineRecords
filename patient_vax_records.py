# This class governs the patient vaccine record object containing their ID number and statuses of all 3 vaccines

class patient_vax_record():
  def __init__(self):
    self.vaxList = []

  # Creates a new record for vaccine statuses which are added to a dictionary, which said dictionary is then appended to vaxList
  def new_vax_record(self, pID, vac_A, vac_B, vac_C):
    self.pID = pID
    self.vac_A = vac_A
    self.vac_B = vac_B
    self.vac_C = vac_C
    self.vaxDict = {'Patient ID_Vax': pID, 'Vaccine A': vac_A, 'Vaccine B': vac_B, 'Vaccine C': vac_C}
    self.vaxList.append(self.vaxDict)
    #print("Vaccine Record Added")

  # Returns vaccine record of a patient via their ID number
  def get_vax_record(self, pID):
    PIN = 0
    while PIN < len(self.vaxList):
      if pID == self.vaxList[PIN]['Patient ID_Vax']:
        print("\nVaccine A: {0}\nVaccine B: {1}\nVaccine C: {2}\n".format(self.vaxList[PIN]['Vaccine A'], self.vaxList[PIN]['Vaccine B'], self.vaxList[PIN]['Vaccine C']))
      else:
        print("Patient Not Found in Records")
      PIN += 1

  # Returns the total number of vaccines of each type taken that are recorded in vaxList
  def vax_totals(self):
    PIN = 0
    num_vac_A = 0
    num_vac_B = 0
    num_vac_C = 0
    while PIN < len(self.vaxList):
      if self.vaxList[PIN]['Vaccine A'] == 'Y':
        num_vac_A += 1
      if self.vaxList[PIN]['Vaccine B'] == 'Y':
        num_vac_B += 1
      if self.vaxList[PIN]['Vaccine C'] == 'Y':
        num_vac_C += 1
      PIN += 1
    print("Number of Vaccines of each type taken in this group:\nvac_A: {0}\nvac_B: {1}\nvac_C: {2}".format(num_vac_A, num_vac_B, num_vac_C))

  # Sets all vaccine values to 'N' which then sets the total sum for each to 0
  def vax_reset(self):
    PIN = 0
    while PIN < len(self.vaxList):
      self.vaxList[PIN]['Vaccine A'] = 'N'
      self.vaxList[PIN]['Vaccine B'] = 'N'
      self.vaxList[PIN]['Vaccine C'] = 'N'
      PIN += 1
    print("Vaccine Records Reset")