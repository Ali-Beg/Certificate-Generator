import uuid
from docx import Document
import os

def generate_unique_id():
    """ Generate a unique certificate ID """
    return str(uuid.uuid4())

def generate_certificate(name, period):
    """ Generate and save the certificate based on the template """
    cert_id = generate_unique_id()
    
    # Load the DOCX template
    doc = Document('certificate_template.docx')
    
    # Replace placeholders with actual values
    for paragraph in doc.paragraphs:
        if '[Intern_Name]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[Intern_Name]', name)
        if '[Certificate_ID]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[Certificate_ID]', cert_id)
        if '[Period]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[Period]', period)
    
    # Save the certificate in the certificates folder
    if not os.path.exists('certificates'):
        os.makedirs('certificates')
        
    certificate_path = f"certificates/{cert_id}.docx"
    doc.save(certificate_path)
    
    return cert_id, certificate_path
