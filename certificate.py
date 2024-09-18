# import uuid
# from docx import Document
# import os

# def generate_unique_id():
#     """ Generate a unique certificate ID """
#     return str(uuid.uuid4())

# def generate_certificate(name, period):
#     """ Generate and save the certificate based on the template """
#     cert_id = generate_unique_id()
    
#     # Load the DOCX template
#     doc = Document('certificate_template.docx')
    
#     # Replace placeholders with actual values
#     for paragraph in doc.paragraphs:
#         if '[Intern_Name]' in paragraph.text:
#             paragraph.text = paragraph.text.replace('[Intern_Name]', name)
#         if '[Certificate_ID]' in paragraph.text:
#             paragraph.text = paragraph.text.replace('[Certificate_ID]', cert_id)
#         if '[Period]' in paragraph.text:
#             paragraph.text = paragraph.text.replace('[Period]', period)
    
#     # Save the certificate in the certificates folder
#     if not os.path.exists('certificates'):
#         os.makedirs('certificates')
        
#     certificate_path = f"certificates/{cert_id}.docx"
#     doc.save(certificate_path)
    
#     return cert_id, certificate_path




import uuid
from docx import Document
import os

def generate_unique_id():
    """Generate a unique certificate ID"""
    return str(uuid.uuid4())

def replace_placeholder_in_run(runs, placeholder, replacement):
    """Replace placeholder text in a run while preserving formatting"""
    for run in runs:
        if placeholder in run.text:
            run.text = run.text.replace(placeholder, replacement)

def generate_certificate(name, period):
    """Generate and save the certificate based on the template"""
    cert_id = generate_unique_id()
    
    # Load the DOCX template
    doc = Document('certificate_template.docx')
    
    # Replace placeholders with actual values while preserving formatting
    for paragraph in doc.paragraphs:
        replace_placeholder_in_run(paragraph.runs, '[Intern_Name]', name)
        replace_placeholder_in_run(paragraph.runs, '[Certificate_ID]', cert_id)
        replace_placeholder_in_run(paragraph.runs, '[Period]', period)
    
    # Save the certificate in the certificates folder
    if not os.path.exists('certificates'):
        os.makedirs('certificates')
        
    certificate_path = f"certificates/{cert_id}.docx"
    doc.save(certificate_path)
    
    return cert_id, certificate_path



