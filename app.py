import streamlit as st
from auth import authenticate
from certificate import generate_certificate 
from database import store_certificate_data, get_certificate_by_id
from database import create_table

# Initialize database table
create_table()

# Title
st.title("Internship Certificate Generator and Verifier")

# Admin login for generating certificates
st.header("Admin Login")

admin_password = st.text_input("Enter admin password", type="password")
is_authenticated = authenticate(admin_password)

if is_authenticated:
    st.success("Logged in as Admin.")
    
    # Certificate Generation Section
    st.header("Generate Certificate")

    with st.form("certificate_form"):
        intern_name = st.text_input("Intern's Name", max_chars=50)
        internship_period = st.text_input("Internship Period", max_chars=50)
        submit_button = st.form_submit_button(label='Generate Certificate')

    if submit_button:
        if intern_name and internship_period:
            cert_id, cert_path = generate_certificate(intern_name, internship_period)
            store_certificate_data(cert_id, intern_name, internship_period, cert_path)
            st.success(f"Certificate generated successfully with ID: {cert_id}")
            
            # Provide download link
            with open(cert_path, "rb") as file:
                st.download_button(
                    label="Download Certificate",
                    data=file,
                    file_name=f"{intern_name}_certificate.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
        else:
            st.error("Please fill in all the details.")
else:
    st.error("Invalid password. Only administrators can generate certificates.")

# Certificate Verification Section
st.header("Verify Certificate")

cert_id_to_verify = st.text_input("Enter Certificate ID to Verify")

if st.button("Verify Certificate"):
    certificate = get_certificate_by_id(cert_id_to_verify)
    if certificate:
        st.success(f"Certificate is valid for {certificate['name']}.")
        st.write(f"Internship Period: {certificate['period']}")
        # Optionally, allow to download the certificate
        with open(certificate['path'], "rb") as file:
            st.download_button(
                label="Download Certificate",
                data=file,
                file_name=f"{certificate['name']}_certificate.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
    else:
        st.error("Invalid Certificate ID.")
