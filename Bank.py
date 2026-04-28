from Account import Account
from Branch import Branch
from Payroll import Payroll
from Staff import Staff


class Bank:
    def __init__(self):
        self.accounts = []
        self.customers = []
        self.branches = []
        self.payroll = None

    def setup_branch(self, branch: Branch):
        self.branches.append(branch)

    def close_branch(self, branch: Branch, transfer_branch: Branch):
        branch.transfer_all_staff_to(transfer_branch)
        self.branches.remove(branch)

    def transfer_staff_member(self, from_branch: Branch, to_branch: Branch, staff: Staff):
        from_branch.transfer_staff_member(to_branch, staff)

    def setup_new_account(self, account: Account, customer):
        account.open_for(customer)
        self.accounts.append(account)

        if customer not in self.customers:
            self.customers.append(customer)

    def obtain_balance(self, account: Account):
        return account.get_balance()

    def add_interest(self, account: Account):
        account.add_interest()

    def add_funds(self, account: Account, amount: float):
        account.add_funds(amount)

    def close_account(self, account: Account):
        account.close()
        self.accounts.remove(account)

    def add_staff_member(self, branch: Branch, staff: Staff):
        branch.add_staff_member(staff)

    def change_opening_time(self, branch: Branch, time: str):
        branch.change_opening_time(time)

    def change_payroll_date(self, payroll: Payroll, date: str, staff_category: str):
        self.payroll = payroll
        self.payroll.change_payroll_date(date, staff_category)
