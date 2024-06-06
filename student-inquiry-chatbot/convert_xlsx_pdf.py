import pandas as pd
from fpdf import FPDF

def xlsx_to_pdf(xlsx_file, pdf_file):
    """
    Converts an Excel file (xlsx) to a PDF file.

    Args:
        xlsx_file (str): The path to the input Excel file.
        pdf_file (str): The path to the output PDF file.
    """

    # Load the Excel file into a Pandas DataFrame
    df = pd.read_excel(xlsx_file)

    # Create a FPDF object
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, f"Excel Data from {xlsx_file}", 0, 1, 'C')
    pdf.set_font('Arial', '', 12)

    # Iterate through the DataFrame and add data to the PDF
    for index, row in df.iterrows():
        for col in df.columns:
            cell_value = str(row[col])  # Convert cell value to string
            pdf.cell(0, 5, f"{col}: {cell_value}", 0, 1)
        pdf.cell(0, 10, '', 0, 1)  # Add empty line between rows

    # Save the PDF
    pdf.output(pdf_file, 'F')

if __name__ == "__main__":
    xlsx_file = 'data/student_cgpa.xlsx'  # Replace with your Excel file path
    pdf_file = 'data/student_cgpa.pdf'  # Replace with your desired PDF file path

    xlsx_to_pdf(xlsx_file, pdf_file)
    print(f"Excel file '{xlsx_file}' converted to PDF '{pdf_file}'")