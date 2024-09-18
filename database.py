import sqlite3
# from database import store_certificate_data


# Connect to the SQLite database
conn = sqlite3.connect('certificates.db', check_same_thread=False)
c = conn.cursor()

def create_table():
    """ Create the certificates table if it doesn't exist """
    c.execute('''
        CREATE TABLE IF NOT EXISTS certificates (
            cert_id TEXT PRIMARY KEY, 
            name TEXT, 
            period TEXT, 
            cert_path TEXT
        )
    ''')
    conn.commit()

def store_certificate_data(cert_id, name, period, cert_path):
    """ Store generated certificate data in the database """
    c.execute("INSERT INTO certificates (cert_id, name, period, cert_path) VALUES (?, ?, ?, ?)",
              (cert_id, name, period, cert_path))
    conn.commit()

def get_certificate_by_id(cert_id):
    """ Retrieve certificate data by its ID """
    c.execute("SELECT * FROM certificates WHERE cert_id=?", (cert_id,))
    result = c.fetchone()
    
    if result:
        return {"cert_id": result[0], "name": result[1], "period": result[2], "path": result[3]}
    else:
        return None
