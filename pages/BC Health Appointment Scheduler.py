#import libraries
import streamlit as st
import sqlite3
from streamlit_folium import st_folium
import folium

#set up my database

def get_db_connecton():
    conn = sqlite3.Connection("bc_home_care.db")
    conn.row_factory = sqlite3.Row
    return conn

#intialise database- run only once to create tables

def initialise_database():
    conn = get_db_connecton()
    cursor = conn.cursor()

    #create tables using cursor.execute
    cursor.execute('''
CREATE TABLE IF NOT EXISTS patients(
                   patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   patient_name TEXT NOT NULL,
                   age INTEGER NOT NULL,
                   patient_email TEXT UNIQUE NOT NULL,
                   phone TEXT NOT NULL,
                   street_address TEXT NOT NULL,
                   city TEXT NOT NULL,
                   province Text NOT NULL
                   )
                   
''')
    cursor.execute('''
CREATE TABLE IF NOT EXISTS  services(
                   service_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   service_name TEXT NOT NULL
                   
                   )

''' )
    cursor.execute('''
CREATE TABLE IF NOT EXISTS  appointments(
                   appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   patient_id INTEGER NOT NULL,
                   service_id INTEGER NOT NULL,
                   health_authority TEXT NOT NULL,
                   appointment_date DATE NOT NULL,
                   appointment_time TIME NOT NULL,
                   FOREIGN KEY (patient_id ) REFERENCES patients(patient_id ),
                   
                   FOREIGN KEY (service_id) REFERENCES services (service_id )
                     )
''' )
    cursor.execute('''
CREATE TABLE IF NOT EXISTS  feedback(
                   feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   patient_id INTEGER NOT NULL,
                   service_id INTEGER NOT NULL,
                   rating  INTEGER,
                   comment TEXT,
                   FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
                   
                   FOREIGN KEY (service_id) REFERENCES services (service_id )
                     
                   
                   )

''' )
    conn.commit()
    conn.close()

#initialise database, you do this once and uncomment # the initialise button

#initialise_database()

def check_patient_exists(email):
    conn=get_db_connecton()
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM patients WHERE patient_email=?", (email,))
    patient = cursor.fetchone()
    conn.close()
    return patient
def save_patient_details(name, age, email, phone, street_address, city, province):
    conn = get_db_connecton()
    cursor = conn.cursor()

    try:
        cursor.execute(""" INSERT INTO patients(patient_name, age, patient_email, phone, street_address, city, province)
                       VALUES(?,?,?,?,?,?,?)""",
                       (name, age,email, phone, street_address, city, province)) 
        conn.commit()
        return "saved successfully"
    except sqlite3.IntegrityError:
        return"email already exist"
    finally:
        conn.close()

st.title("BC Home and Community Care App")



with tab1:
    st.header("Patient Details")
        
        # Patient form inside Tab 1
    with st.form("patient_form"):
        email = st.text_input("Enter your email:")
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=19)
        phone = st.text_input("Phone Number")
        street_address = st.text_input("Street Address")
        city = st.text_input("City")
        province = st.selectbox("Select your province", ("BC", "AB", "SC", "ON", "QC"))

            
            
        # Submit button for form
        save_button = st.form_submit_button("Save and Continue")
        

        
        
with tab2:
    st.header("Services")
    st.write("This is where you can select services.")



