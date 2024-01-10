# This class governs the patient details object containing their ID number, first and last name, phone number, and address.

class patient_details():
  def __init__(self):
    self.detailsList = []

  # Creates a new record of details which are added to a dictionary, which said dictionary is then appended to detailsList
  def new_details(self, pID, pFirst, pLast, pPhone, pAddress):
    self.pID = pID
    self.pFirst = pFirst
    self.pLast = pLast
    self.pPhone = str(pPhone)
    self.pAddress = str(pAddress)
    self.pDetailsDict = {'Patient ID': pID, 'Patient First Name': pFirst, 'Patient Last Name': pLast, 'Patient Phone Number': str(pPhone), 'Patient Address': str(pAddress)}
    self.detailsList.append(self.pDetailsDict)
    #print("Details Added")

  # Returns first name
  def get_FirstName(self, pID):
    PIN = 0
    while PIN < len(self.detailsList):
      if pID == self.detailsList[PIN]['Patient ID']:
        return self.detailsList[PIN]['Patient First Name']
      PIN += 1

  # Returns last name
  def get_LastName(self, pID):
    PIN = 0
    while PIN < len(self.detailsList):
      if pID == self.detailsList[PIN]['Patient ID']:
        return self.detailsList[PIN]['Patient Last Name']
      PIN += 1

  # Returns phone number
  def get_PhoneNumber(self, pID):
    PIN = 0
    while PIN < len(self.detailsList):
      if pID == self.detailsList[PIN]['Patient ID']:
        return self.detailsList[PIN]['Patient Phone Number']
      PIN += 1

  # Returns address
  def get_Address(self, pID):
    PIN = 0
    while PIN < len(self.detailsList):
      if pID == self.detailsList[PIN]['Patient ID']:
        return self.detailsList[PIN]['Patient Address']
      PIN += 1

  # Returns ID number through the entry of the patient's last name
  def get_PIN_via_LastName(self, pLast):
    PIN = 0
    while PIN < len(self.detailsList):
      if pLast == self.detailsList[PIN]['Patient Last Name']:
        return self.detailsList[PIN]['Patient ID']
      else:
        print("Patient Not Found in Records")
      PIN += 1

  # Returns ID number through the entry of the patient's last name and phone number
  def get_PIN_via_LastName_PhoneNum(self, pLast, pPhone):
    PIN = 0
    while PIN < len(self.detailsList):
      if pLast == self.detailsList[PIN]['Patient Last Name']:
        if pPhone == self.detailsList[PIN]['Patient Phone Number']:
          return self.detailsList[PIN]['Patient ID']
      PIN += 1