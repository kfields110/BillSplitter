from fpdf import FPDF


class PDF:
    """
    Creates a PDF file that contains information including Flatmate names, bill, and period
    """

    def __init__(self, filename):
        self.filename = filename

    def generator(self, Flatmate1, Flatmate2, bill):

        flatmate1pay = str(round(Flatmate1.pays(bill, Flatmate2),2))
        flatmate2pay = str(round(Flatmate2.pays(bill, Flatmate2),2))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", align='C', ln=1)

        #Insert period label and value
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=300, h=40, txt="Period:", align='C')
        pdf.cell(w=150, h=40, txt=bill.period, align='C', ln=1)

        #Insert name title and value title
        pdf.cell(w=100, h=40, txt="Name", )
        pdf.cell(w=150, h=40, txt="Amount", ln=1)

        #Insert name and due amount from first flatmate
        pdf.set_font(family='Times', size=12, )
        pdf.cell(w=100, h=40, txt=Flatmate1.name,)
        pdf.cell(w=150, h=40, txt=flatmate1pay, ln=1)

        #Insert name and due amount from second flatmate
        pdf.cell(w=100, h=40, txt=Flatmate2.name)
        pdf.cell(w=150, h=40, txt=flatmate2pay, ln=1)

        pdf.output(f'{self.filename}.pdf')

    def export(self):
        pass
