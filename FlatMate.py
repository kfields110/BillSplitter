class FlatMate:

    """
    Creates a flatmate person who lives in flat and pays portion of the bill.
    """

    def __init__(self, name, days_spent):
        self.name = name
        self.days_spent = days_spent

    def pays(self, bill, flatmate2):
        amount_owed = (self.days_spent / (self.days_spent + flatmate2.days_spent)) * bill
        return amount_owed