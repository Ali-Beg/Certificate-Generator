# def authenticate(password):
#     """ Simple admin authentication """
#     admin_password = "12345"  # Replace with a more secure password
#     return password == admin_password

import os

def authenticate(password):
    """Authenticate admin using environment variable."""
    admin_password = os.getenv("STREAMLIT_ADMIN_PASSWORD")  # Get password from environment variable
    return password == admin_password

