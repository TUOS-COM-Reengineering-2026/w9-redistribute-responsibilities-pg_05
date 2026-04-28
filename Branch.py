from Staff import Staff


class Branch:

    def __init__(self, location):
        self._location = location
        self._staff = []
        self._opening_time = "9:00"

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_staff(self):
        return self._staff

    def get_opening_time(self):
        return self._opening_time

    def change_opening_time(self, time):
        self._opening_time = time

    def add_staff_member(self, staff: Staff):
        self._staff.append(staff)

    def transfer_staff_member(self, transfer_branch, staff: Staff):
        self._staff.remove(staff)
        transfer_branch.add_staff_member(staff)

    def transfer_all_staff_to(self, transfer_branch):
        for staff in list(self._staff):
            self.transfer_staff_member(transfer_branch, staff)
