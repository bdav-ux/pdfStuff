import fpdf

new = fpdf.FPDF()
new.add_page()
new.set_font("Arial")
new.cell(200, 10, "Hey there", align="C")
new.output("newPdf.pdf")