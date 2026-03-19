import fpdf
import pdfplumber
#crea un pdf e scrive qualcosa

'''new = fpdf.FPDF()
new.add_page()
#style= italic, underlined, strikethrough, bold
new.set_font("Arial", style="U", size=16)
new.set_text_color(255,0,0)
new.cell(200, 10, "Hey there", align="C")

new.output("newPdf.pdf")
'''

#legge pdf e ne crea uno nuovo
final = fpdf.FPDF()

final.add_font("dejavu-sans", style="", fname="DejaVuSans.ttf")
final.add_font("bold-sans", style="", fname="DejaVuSans-Bold.ttf")

final.set_font("dejavu-sans", style="", size=10)


counter = 1
lineHeight=8

def conditionalWrite(text, destination):
    if len(text.split(" "))<=5 and text[-2]!=".":
        destination.set_text_color(0,0,0)
        destination.set_font("bold-sans", style="", size=14)
        destination.multi_cell(200, 10, text+"\n", align="C")
        destination.set_font("dejavu-sans", style="", size=10)
    else:
        destination.write(lineHeight, text)



with pdfplumber.open("Relazione.pdf") as pdf:
    for page in pdf.pages:
        final.add_page()
        text=page.extract_text()
        lines=text.splitlines()
        for line in lines:
            if len(line)>1:
                printable=line+" "
                if counter%3==1:
                    final.set_text_color(220, 50, 50)
                    conditionalWrite(printable, final)
                elif counter%3==2:
                    final.set_text_color(0, 0, 0)
                    conditionalWrite(printable, final)
                elif counter%3==0:
                    final.set_text_color(30, 80, 200)
                    conditionalWrite(printable, final)
                counter+=1

final.output("final2.pdf")