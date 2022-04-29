import os 
from PIL import Image
from fpdf import FPDF

fpdf = FPDF()

# image folder
sdir = "C:/Users/..."

width, height = 0, 0

for i in range(1, 7):
    fname = sdir + "Screenshot_%.d.png" % i
    if os.path.exists(fname):
        if i == 1:
            page = Image.open(fname)
            width, height = page.size
            pdf = FPDF(unit='pt', format = [width, height])
        image = fname
        pdf.add_page()
        pdf.image(image, 0,0, width, height)
    else:
        print("File could not found: ", fname)
    #print("Processed %d" %i)
pdf.output("Converted_output.pdf", "F")
#print("Successfully Converted")
