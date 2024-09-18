# def authenticate(password):
#     """ Simple admin authentication """
#     admin_password = "12345"  # Replace with a more secure password
#     return password == admin_password

# import os

# def authenticate(password):
#     """Authenticate admin using environment variable."""
#     admin_password = os.getenv("STREAMLIT_ADMIN_PASSWORD")  # Get password from environment variable
#     return password == admin_password


import streamlit as st
import os

def authenticate(password):
    """Authenticate admin using Streamlit secrets or environment variables."""
    try:
        # Use Streamlit secrets in production
        admin_password = st.secrets["general"]["admin_password"]
    except KeyError:
        # Fallback to environment variable or .env for local testing
        admin_password = os.getenv("STREAMLIT_ADMIN_PASSWORD")
    
    return password == admin_password

