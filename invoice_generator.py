#==================
# Module

import jinja2                     # For rendering HTML templates
import pdfkit                     # For converting HTML+CSS to PDF
import os                         # For handling file paths and directories
from datetime import datetime     # For working with dates

#==================
#  Client and Product's Information ------

client_name = "Hector Salamanca"

# Product

item1 = "Dishwasher"
item2 = "Coffee Maker"
item3 = "Microwave"
item4 = "Blender"

# Individual prices

subtotal1 = 120
subtotal2 = 45
subtotal3 = 50
subtotal4 = 20

# Calculate total price

total = subtotal1 + subtotal2 + subtotal3 + subtotal4

# Format current date and month
month = datetime.today().strftime("%b, %Y")         #  Oct, 2025
today_date = datetime.today().strftime("%d %b, %Y") #  21 Oct, 2025

#==================
#  Context for the HTML template -----

# This dictionary will be passed to the template to fill in dynamic values
context = {
    "client_name": client_name,
    "today_date": today_date,
    "month": month,
    "item1": item1,
    "item2": item2,
    "item3": item3,
    "item4": item4,
    "subtotal1": f"${subtotal1:.2f}",
    "subtotal2": f"${subtotal2:.2f}",
    "subtotal3": f"${subtotal3:.2f}",
    "subtotal4": f"${subtotal4:.2f}",
    "total": f"${total:.2f}"
          }


#==================
# Load HTML Template------

# Set the path to the templates folder (relative to this script)
template_path = os.path.join(os.path.dirname(__file__), "../template")
template_loader = jinja2.FileSystemLoader(template_path)
template_env = jinja2.Environment(loader=template_loader)

# Load the specific template file
html_template = "contract_template.html"
template = template_env.get_template(html_template)

# Render the template with the context data
output_text = template.render(context)


#==================
#  PDF Generation-------

# Path to wkhtmltopdf executable (required by pdfkit)
path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# Ensure output folder exists
output_dir = os.path.join(os.path.dirname(__file__), '../output')
os.makedirs(output_dir, exist_ok=True)

# Define output PDF filename
output_pdf = os.path.join(output_dir, 'pending_invoice.pdf')

# Define CSS path and validate it BEFORE using it
css_path = os.path.join(os.path.dirname(__file__), '../static/style.css')
if not os.path.exists(css_path):
    print("❌ CSS file not found. Check the 'static' folder and filename.")
    exit()

# Generate the PDF from the rendered HTML and apply CSS styling
pdfkit.from_string(output_text, output_pdf, configuration=config, css=css_path)

#==================
# Console Feedback ------

print("✅ Invoice generated successfully!")
print(f"📄 Saved as: {os.path.basename(output_pdf)}")

# === Console Feedback ===
print("✅ Invoice generated successfully!")
print(f"📄 Saved as: {pending_invoice.pdf}")

