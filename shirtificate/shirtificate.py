# import required libaray
from fpdf import FPDF, Align

# define class PDF with relavent methods which is a inherited class of FPDF
class PDF(FPDF):
    def header(self):
        self.set_font("Times", "B", size=40)
        self.set_y(25)
        self.cell(w=0, h=0, text="CS50 Shirtificate", align="C")

    def shirt(self):
        self.image("shirtificate.png", x=Align.C, y=50, w=200, h=220)

    def text(self):
        self.set_y(125)
        self.set_font("Helvetica", size=20)
        self.set_text_color(r=255,g=255,b=255)
        self.cell(w=0, h=0, text=f"{input("Name: ").title()} took CS50", align="C")


# define main function to create shirtificate PDF
def main():
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.shirt()
    pdf.text()
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
