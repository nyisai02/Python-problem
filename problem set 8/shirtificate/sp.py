from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_text_color(25,222,33)
pdf.set_font("Arial",size=70)
pdf.text(50,50,txt="Hello world")
pdf.image("shirtificate.png", 60,120,w=120 )
pdf.output("pdf-with-image.pdf")
