from fpdf import FPDF
name=input("Name ")
pdf = FPDF()
pdf.add_page()

pdf.set_text_color(25,222,33)
pdf.set_font("helvetica", "B", 50)
pdf.cell(0, 10, "CS50 Shirtificate",new_x="LMARGIN",new_y="NEXT",align="C")
pdf.image("shirtificate.png",w=pdf.epw )
pdf.set_font("helvetica", "B", 40)
pdf.text(x=47.5,y=110,txt=f"{name} took cs50")
pdf.output("shirtificate.pdf")