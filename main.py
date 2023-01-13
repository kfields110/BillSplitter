from Bill import Bill
from FlatMate import FlatMate


new_bill = Bill(120, "March 2020")
Flat1 = FlatMate("John", 20)
Flat2 = FlatMate("Kenny", 25)

print(Flat1.pays(bill=new_bill.amount, flatmate2= Flat2))
