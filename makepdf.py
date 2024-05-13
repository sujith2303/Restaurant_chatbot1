from fpdf import FPDF

def text_to_pdf(input_file, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(input_file, "r") as file:
        for line in file:
            pdf.cell(200, 10, txt=line, ln=True)

    pdf.output(output_file)

# Usage
input_text_file = "file.txt"  # Change this to your input text file
output_pdf_file = "output.pdf"  # Change this to your output PDF file

text_to_pdf(input_text_file, output_pdf_file)
