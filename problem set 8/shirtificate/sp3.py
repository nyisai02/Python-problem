from fpdf import FPDF

def createPdf():
    pdf=FPDF()
    pdf.add_page()
    pdf.set_text_color(25,222,33)
    pdf.set_font("Arial",size=70)
    pdf.text(50,50,txt="Hello world")
    pdf.output("output.pdf")


if __name__=="__main__":
    createPdf()
