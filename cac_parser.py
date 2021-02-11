class CACBarcode:
    branch_list = {
        'A': 'USA',
        'C': "USCG",
        "D": "DOD",
        "F": "USAF",
        "H": "USPHS",
        "M": "USMC",
        "N": "USN",
        "O": "NOAA",
        "1": "Foreign Army",
        "2": "Foreign Navy",
        "3": "Foreign Marine Corps",
        "4": "Foreign Air Force",
        "X": "Other"
    }

    category_list = {
        "A": "Active Duty member",
        "B": "Presidential Appointee",
        "C": "DoD civil service employee",
        "D": "100% disabled American veteran",
        "E": "DoD contract employee",
        "F": "Former member",
        "N": "National Guard member",
        "G": "National Guard member",
        "H": "Medal of Honor recipient",
        "I": "Non-DoD Civil Service Employee",
        "J": "Academy student",
        "K": "non-appropriated fund (NAF) DoD employee",
        "L": "Lighthouse service",
        "M": "Non-Government agency personnel",
        "O": "Non-DoD contract employee",
        "Q": "Reserve retiree not yet eligible for retired pay",
        "R": "Retired Uniformed Service member eligible for retired pay",
        "V": "Reserve",
        "S": "Reserve",
        "T": "Foreign military member",
        "U": "Foreign national employee",
        "W": "DoD Beneficiary",
        "Y": "Retired DoD Civil Service Employees"
    }

    def _getbranch(self, code) -> str:
        return self.branch_list.get(code, 'N/A')

    def _getcategory(self, code) -> str:
        return self.category_list.get(code, "N/A")


class PDF417Barcode(CACBarcode):
    def __init__(self, data):
        if len(data) == 99:
            # parse with new method
            self.branch = self._getbranch(data[71])
            self.category = self._getcategory(data[70])
            self.edipi = int(data[1:8], 32)
            self.fname = data[16:36]
            self.lname = data[37:63]
            self.rank = data[74:80]

        if len(data) == 89 or len(data) == 88:
            # parse with old method
            self.branch = self._getbranch(data[66])
            self.category = self._getcategory(data[65])
            self.edipi = int(data[8:15], 32)
            self.fname = data[15:35]
            self.lname = data[35:61]
            self.rank = data[69:75]
