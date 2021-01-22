import datetime

_1_jan_1000 = datetime.datetime(1000, 1, 1)


class CACBarcode:

    def read(self, data, start, finish=None):
        pass

    def _getbranch(self, code) -> str:
        """
        Called by constructor, don't call this method
        http://www.cac.mil/docs/DoD-ID-Bar-Code_SDK-Formats_v7-5-0_Sep2012.pdf, page 50
        :param code: Branch Code
        :return: Branch Service String
        """
        # Series of ifs for speed since this is a one way conversion
        if code == "A": return "USA"
        if code == "C": return "USCG"
        if code == "D": return "DOD"
        if code == "F": return "USAF"
        if code == "H": return "USPHS"
        if code == "M": return "USMC"
        if code == "N": return "USN"
        if code == "O": return "NOAA"
        if code == "1": return "Foreign Army"
        if code == "2": return "Foreign Navy"
        if code == "3": return "Foreign Marine Corps"
        if code == "4": return "Foreign Air Force"
        if code == "X": return "Other"
        return "N/A"

    def _getcategory(self, code):
        """
        Called by constructor, don't call this method
        http://www.cac.mil/docs/DoD-ID-Bar-Code_SDK-Formats_v7-5-0_Sep2012.pdf, page 51
        :param code: Personnel Category Code
        :return: String of category description
        """
        # Series of ifs for speed since this is a one way conversion
        if code == "A": return "Active Duty member"
        if code == "B": return "Presidential Appointee"
        if code == "C": return "DoD civil service employee"
        if code == "D": return "100% disabled American veteran"
        if code == "E": return "DoD contract employee"
        if code == "F": return "Former member"
        if code == "N" or code == "G": return "National Guard member"
        if code == "H": return "Medal of Honor recipient"
        if code == "I": return "Non-DoD Civil Service Employee"
        if code == "J": return "Academy student"
        if code == "K": return "non-appropriated fund (NAF) DoD employee"
        if code == "L": return "Lighthouse service"
        if code == "M": return "Non-Government agency personnel"
        if code == "N": return "National Guard member"
        if code == "O": return "Non-DoD contract employee"
        if code == "Q": return "Reserve retiree not yet eligible for retired pay"
        if code == "R": return "Retired Uniformed Service member eligible for retired pay"
        if code == "V" or code == "S": return "Reserve"
        if code == "T": return "Foreign military member"
        if code == "U": return "Foreign national employee"
        if code == "V": return "Reserve member"
        if code == "W": return "DoD Beneficiary"
        if code == "Y": return "Retired DoD Civil Service Employees"
        return "N/A"


class PDF417Barcode(CACBarcode):

    def __init__(self, data):
        # self.data = data

        # 2D barcode Version "1" and Version "N" have 88 and 89 chars
        # VN's 89'th char is middle initial
        if len(data) != 88 and len(data) != 89:
            raise Exception

        self.barcode_version = data[1]

        # Only version 1 and N supported
        # if self.barcode_version != "1" and self.barcode_version != "N":
        #     print('************************')
        #     print("Version", self.barcode_version, "not recognized!")
        #     raise Exception

        self.branch = self._getbranch(data[66])
        self.category = self._getcategory(data[65])
        self.edipi = int(data[8:15], 32)
        self.fname = data[15:35]
        self.lname = data[35:61]
        self.rank = data[69:75]
