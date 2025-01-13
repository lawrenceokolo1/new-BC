#import libraries
import streamlit as st
import sqlite3
import folium
from streamlit_folium import st_folium
import pandas

#set up my database

def get_db_connecton():
    conn = sqlite3.Connection("home_care.db",)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
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
                   service_name TEXT NOT NULL,
                   patient_id,
                   FOREIGN KEY (patient_id ) REFERENCES patients(patient_id)
                   
                   
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

#initialise_database()

#initialise database, you do this once and uncomment # the initialise button
if "patient_id"  not in st.session_state:
    st.session_state.patient_id = None


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




def save_selected_services(patient_id, selected_services):
    conn = get_db_connecton()
    cursor = conn.cursor()
    try:
            cursor.execute("INSERT INTO services (patient_id, service_name) VALUES (?,?)", (patient_id, selected_services))
            conn.commit()
            return True
    except sqlite3.Error as e:
        return False, str(e)
    finally:
        conn.close()




def save_appointment(patient_id, service_id, health_authority, appointment_date, appointment_time):
    conn = get_db_connecton()
    cursor = conn.cursor()
    try:
        
        cursor.execute("INSERT INTO appointments(patient_id, service_id, health_authority, appointment_date, appointment_time) VALUES(?,?,?,?,?)", (patient_id, service_id, health_authority, appointment_date, appointment_time))
        conn.commit()
        return "saved successfully"
    except sqlite3.IntegrityError:
        return"error occured"
    finally:
        conn.close()


def get_service_id(service_name):
    conn = get_db_connecton()  # Connect to the database
    cursor = conn.cursor()

    try:

        # Query to fetch the service ID based on the service name
        cursor.execute("SELECT service_id FROM services WHERE service_name = ?", (service_name,))
        result = cursor.fetchone()
        return result[0] if result else None  # Return the service ID if found, otherwise None
    except sqlite3.IntegrityError:
            
            return"error occured"
    finally:
        conn.close()

        



st.title("British Columbia Home and Community Care App For Seniors ")
st.caption("by lawrence okolo")
st.image("images/beautiful columbians.webp")

#tab0 = st.columns(1)
#tab1,tab2 = st.columns(2) 
#tab2 = st.columns(1)
#tab3 = st.columns(1)
#tab4 = st.columns(1)
#tab5 = st.columns(1)
st.header("Overview ")
st.subheader('A centralized booking app for seniors')
st.markdown(''' The importance of a user-friendly, centralized home and community care app for seniors cannot be overstated. 
                This web application aims to streamline the appointment booking process by reducing reliance on paper-based systems and significantly speeding up the time it takes to book an appointment. 
                The app consists of five main tabs:  **Overview**,  **Patient Details**,  **Services**, **Booking**, **Health Authorities**, **Database**. 
                All major credit and inspiration for developing this app goes to [HealthBC](https://www2.gov.bc.ca/gov/content/health/accessing-health-care/home-community-care)  
                Feel free to explore the app and test its functionality by filling out the forms with sample or fake details. Please ensure that you save each step of the process to see how the database operates.''')
    
   





#with tab1:
st.header("Patient Details")
        
        # Patient form inside Tab 1
with st.form(key = "patient_form", clear_on_submit=True):
    email = st.text_input("Enter your email:")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=19)
    phone = st.text_input("Phone Number")
    street_address = st.text_input("Street Address")
    city = st.text_input("City")
    province = st.selectbox("Select your province", ("BC", "AB", "SC", "ON", "QC"))

            
            
        # Submit button for form
    save = st.form_submit_button("Save and Continue")
    
        


    if save:
        

            # Step 1: Validate form fields
        if not email or not name or not phone or not street_address or not city or province == "":
            
        
            st.error("Please fill out all required fields.")
        

    
        else:
            
            
                 # Step 2: Check if patient already exists
            existing_patient = check_patient_exists(email)
        
            if existing_patient:
                
                    # Notify user if patient already exists
                st.info("You already have an account. Proceed to Services.")
                st.session_state.patient_id = existing_patient["patient_id"]
            else:
                save_patient_details(name, age, email, phone, street_address, city, province)
                new_patient = check_patient_exists(email)
                st.session_state.patient_id = new_patient["patient_id"]
                st.success("successfully registered, select and save service")
                
            st.write("Current Patient ID:", st.session_state.patient_id)
            
                 
#with tab2:

#if st.session_state.patient_id:




st.header("please select and save service below")


services = {


    "community nursing" : {
    "description" : "Community nursing services are provided by a licensed nursing professional to clients in the community who require acute, chronic, palliative or rehabilitative support. Services include assessment and nursing interventions such as education, wound care, medication management, chronic disease management, care management, post-surgical care and palliative care. Generally, community nursing services will be provided on a short-term basis and the community nurses will assist you and your family to be confident in taking over your care at home.", 
    "links":"https://www2.gov.bc.ca/gov/content/health/accessing-health-care/home-community-care/care-options-and-cost/community-nursing"
    },
    "community rehabilitation" : {
    "description" : "Community rehabilitation services are provided by a licensed physical therapist or occupational therapist to clients who require acute, chronic, palliative or rehabilitative support. The main goals of rehabilitation therapy are to help improve or maintain physical and functional abilities and to provide assessment and treatment to ensure a client’s home is suitably arranged for their needs and safety. Generally, community rehabilitation services will be provided on a short-term basis and the community rehabilitation therapists will assist you and your family to be confident in taking over your care at home.Community rehabilitation services, which include physical therapy and occupational therapy, may be provided in a variety of settings such as clinics, the client’s home, assisted living residences, family care homes, group homes, or other community settings.  ", 
    "links":"https://www2.gov.bc.ca/gov/content/health/accessing-health-care/home-community-care/care-options-and-cost/community-rehabilitation"
    },
    "Adult Day Services" : {
    "description" : "Adult day services assist seniors and adults with disabilities to continue to live in their own homes by providing supportive group programs and activities in the community.Clients receiving adult day services travel to a location in their community usually 1-2 days per week where they may receive a variety of services, including: personal assistance;health care services including nursing and/or rehabilitation services; an organized program of therapeutic social and recreational activities in a protective group setting; health education and promotion, nutrition and bathing programs, blood pressure and podiatry clinics, telephone checking, and counselling; and caregiver support, including respite, activities such as caregiver support groups, information and education programs.", 
    "links":"https://www2.gov.bc.ca/gov/content/health/accessing-health-care/home-community-care/care-options-and-cost/adult-day-services"
    }, 

    "Home Support" : {
    "description" : "Home support services help you to remain independent and to live in your own home as long as possible.Home support services are direct care services provided by community health workers to clients who require personal assistance with activities of daily living, such as: mobility; nutrition;lifts and transfers; bathing and dressing; cueing (providing prompts to assist with the completion of tasks); and grooming and toileting. Home support services may also include safety maintenance activities as a supplement to personal assistance when appropriate. These activities may include clean-up, laundry of soiled bedding or clothing, and meal preparation. In addition, community health workers may perform some specific nursing and rehabilitation tasks that have been delegated by health care professionals.", 
    "links":"https://www2.gov.bc.ca/gov/content/health/accessing-health-care/home-community-care/care-options-and-cost/home-support"
    },  
    "End Of Life Care" : {
    "description" : "End-of-life care is supportive and compassionate care that focuses on comfort,quality of life, respect for personal health care treatment decisions, support for the family, and psychological, cultural and spiritual concerns for dying people and their families. Palliative care is specialized medical care for people with serious illness – whatever the diagnosis. Care can be provided wherever the client is living, whether at home, in hospice, an assisted living residence or a long-term care home. End-of-life and palliative care services aim to preserve an individual’s comfort, dignity and quality of life as their needs change, and to offer on-going support for family and friends. These services include the following: care co-ordination and consultation, pain and symptom management, community nursing services, community rehabilitation services, home support, respite for the caregiver and hospice care.", 
    "links":"https://www2.gov.bc.ca/gov/content/health/accessing-health-care/home-community-care/care-options-and-cost/end-of-life-care"
    }, 
        
    }
        
   
selected_services = st.selectbox(label= "select services ",options= list(services.keys()))
if selected_services:
        
        

    st.subheader(selected_services)
    st.write(services[selected_services]["description"])
    st.markdown(f"[Learn more about {selected_services} from HealthBC]({services[selected_services]['links']})", unsafe_allow_html=True)


if selected_services and st.button("Save Service Here!"):
    result = save_selected_services(st.session_state.patient_id, selected_services)
    if result is True:
        st.success("service Saved! go to Booking ")
    else:
            
        st.error(f"An error occurred: {result[1]}")
#else:
    #st.warning("Please fill in Patient Details to select or update your services.")    
                    
                  


#with tab3:
#if st.session_state.patient_id:
st.header("book appointment")

with st.form(key = "appointment_form"):
    
    health_authority = st.selectbox("select your health authority",("interior health", "Fraser Health","Vancouver Coastal Health", "Island Health", "Northern Health"  ))
    appointment_date = st.date_input("select appointment date")
    appointment_time = st.time_input("select appointment time")
            
    save= st.form_submit_button("save appointment")

    if save:
        if not health_authority or not appointment_date or not appointment_time:
            st.write("please select the feilds")
        else:
            if not selected_services:
                st.error("please save your selected service")
            else:                    
                service_id = get_service_id(selected_services)
                save_appointment(st.session_state.patient_id,service_id, health_authority, str(appointment_date), str(appointment_time))
                st.snow()
                st.success("successfully booked an appointment!")
                    
    #else:
        #st.warning("Please fill in Patient Details to select or update your appointment.")







with tab4:
    health_authorities = {


        "Interior Health": [


            {"name": "100 Mile District General Hospital", "coords": [51.6426, -121.2998], "address": "D–555 Cedar Ave, 100 Mile House, BC V0K 2E0"},
            {"name": "Armstrong Health Centre", "coords": [50.4489, -119.1941], "address": "3800 Patten Dr, Armstrong, BC V0E 1B2"},
            {"name": "Ashcroft Community Health Centre", "coords": [50.7256, -121.2824], "address": "700 Ash-Cache Creek Hwy, Ashcroft, BC V0K 1A0"},
            {"name": "Barriere Health Centre", "coords": [51.1848, -120.1238], "address": "4537 Barriere Town Rd, Barriere, BC V0E 1E0"},
            {"name": "Castlegar and District Community Health Centre", "coords": [49.3233, -117.6593], "address": "709 10th St, Castlegar, BC V1N 2H7"},
            {"name": "Chase Health Centre", "coords": [50.8190, -119.6833], "address": "825 Thompson Ave, Chase, BC V0E 1M0"},
            {"name": "Dr Helmcken Memorial Hospital", "coords": [51.6512, -120.0342], "address": "640 Park Dr RR#1, Clearwater, BC V0E 1N0"},
            {"name": "Clinton Health and Wellness Centre", "coords": [51.0937, -121.5854], "address": "1510 Cariboo Hwy 97 N, Clinton, BC V0K 1K0"},
            {"name": "East Kootenay Regional Hospital (Cranbrook)", "coords": [49.5120, -115.7694], "address": "20 23rd Ave S, Cranbrook, BC V1C 5V1"},
            {"name": "Crawford Bay Health Centre", "coords": [49.6333, -116.8167], "address": "15985 Hwy 3A, Crawford Bay, BC V0B 1E0"},
            {"name": "Creston Valley Hospital", "coords": [49.0956, -116.5131], "address": "312 15th Ave N, Creston, BC V0B 1G0"},
            {"name": "Enderby Community Health Centre", "coords": [50.5500, -119.1392], "address": "707 3rd Ave W, Enderby, BC V0E 1V5"},
            {"name": "Elk Valley Hospital (Fernie)", "coords": [49.5040, -115.0631], "address": "1501 5th Ave, Fernie, BC V0B 1M0"},
            {"name": "Golden and District Hospital", "coords": [51.2986, -116.9829], "address": "835 9th Ave S RR#4 Golden BC V0A 1H2"},
            {"name": "Boundary District Hospital (Grand Forks)", "coords": [49.0306, -118.4415], "address": "7649 22nd St RR#3 Grand Forks BC V0H 1H2"},
            {"name": "Invermere and District Hospital", "coords": [50.5047, -116.0306], "address": "850 10th Ave S RR#4 Invermere BC V0A 1K4"},
            {"name": "(Downtown) Kamloops Home and Community Care", "coords": [50.6745, -120.3273], "address": "37–450 Lansdowne St Kamloops BC V2C 1Y3"},
            {"name": "Kelowna General Hospital", "coords": [49.8817, -119.4779]},
            {"name": "Penticton Regional Hospital", "coords": [49.4911, -119.5896]},
            {"name": "Kamloops Royal Inland Hospital", "coords": [50.6745, -120.3273]},
        ],

        "Fraser Health":[

            {"name": "Abbotsford Home Health", "coords": [49.0500, -122.3294], "address": "103-34194 Marshall Road, Abbotsford, BC V2S 0C2"},
            {"name": "Agassiz Home Health", "coords": [49.2380, -121.7693], "address": "7040 Cheam Avenue, Agassiz, BC V0M 1A0"},
            {"name": "Burnaby Home Health", "coords": [49.2481, -123.0046], "address": "400-4946 Canada Way, Burnaby, BC V5G 4H7"},
            {"name": "Chilliwack Home Health", "coords": [49.1570, -121.9515], "address": "45470 Menholm Road, Chilliwack, BC V2P 1M6"},
            {"name": "South Delta Home Health", "coords": [49.0906, -123.0593], "address": "#1826 – 4949 Canoe Pass Way, Delta, BC V4K 5B6"},
            {"name": "Hope Home Health", "coords": [49.3828, -121.4414], "address": "1275A 7th Avenue, Hope, BC V0X 1L4"},
            {"name": "Langley Home Health", "coords": [49.1049, -122.6604], "address": "101-20651 56 Avenue, Langley, BC V3A 3Y9"},
            {"name": "Maple Ridge Home Health", "coords": [49.2191, -122.6017], "address": "400-11762 Laity Street, Maple Ridge, BC V2X 5A3"},
            {"name": "Mission Home Health", "coords": [49.1358, -122.3088], "address": "7298 Hurd Street (2nd Floor), Mission, BC V2V 3H5"},
            {"name": "New Westminster Home Health", "coords": [49.2057, -122.9110], "address": "218-610 Sixth Street, New Westminster, BC V3L 3C2"},
            {"name": "Tri-Cities Home Health", "coords": [49.2827, -122.8279], "address": "700-220 Brew Street, Port Moody, BC V3H 0H6"},
            {"name": "Newton Home Health", "coords": [49.1836, -122.8490], "address": "#1009-7495 132 Street, Surrey, BC V3W 1J8"},
            {"name": "Gateway Home Health", "coords": [49.1913, -122.8500], "address": "#1500-13401 108th Avenue, Surrey, BC V3T 5T3"},
            {"name": "White Rock Home Health", "coords": [49.0266, -122.8028], "address": "#15476 Vine Avenue, White Rock, BC V4B 2R4"},
            {"name": "Surrey Memorial Hospital", "coords": [49.1837, -122.8490]},
            {"name": "Burnaby Hospital", "coords": [49.2488, -122.9805]},
            {"name": "Abbotsford Regional Hospital", "coords": [49.0504, -122.2856]},
            
        ],
    

        "Vancouver Coastal Health": [

            {"name": "Evergreen Community Health Centre", "coords": [49.2489, -123.0311], "address": "3425 Crowley Drive, Vancouver, BC V5R 6G3"},
            {"name": "South Community Health Centre", "coords": [49.2204, -123.0766], "address": "6405 Knight Street, Vancouver, BC V5P 2V9"},
            {"name": "Richmond Community Health Access Centre", "coords": [49.1706, -123.1360], "address": "7671 Alderbridge Way, Richmond, BC V6X 1Z9"},
            {"name": "North Shore Community Health Centre", "coords": [49.3270, -123.0720], "address": "132 West Esplanade, North Vancouver, BC V7M 1A2"},
            {"name": "Powell River Home and Community Care", "coords": [49.8352, -124.5248], "address": "5000 Joyce Avenue, Powell River, BC V8A 5R3"},
            {"name": "Sechelt Home and Community Care", "coords": [49.4728, -123.7613], "address": "5630 Inlet Avenue, Sechelt, BC V0N 3A0"},
            {"name": "Squamish Home and Community Care", "coords": [49.7016, -123.1558], "address": "1140 Hunter Place, Squamish, BC V8B 0G8"},
            {"name": "Bella Coola General Hospital (Home Care Services)", "coords": [52.3702, -126.7534], "address": "1025 Elcho Street, Bella Coola, BC V0T 1C0"},
            {"name": "Bella Bella Community Health Centre", "coords": [52.1633, -128.1454], "address": "Hospital Road, Bella Bella, BC V0T 1Z0"},
            {"name": "Vancouver General Hospital", "coords": [49.2636, -123.1246]},
            {"name": "Richmond Hospital", "coords": [49.1700, -123.1368]},
            {"name": "Lions Gate Hospital", "coords": [49.3163, -123.0726]},
        ],

        "Island Health": [

            {"name": "South Island Community Access Centre", "coords": [48.4284, -123.3656], "address": "Victoria, BC (Serving all communities south of Mill Bay, including Greater Victoria and Southern Gulf Islands)"},
            {"name": "Centre Island Community Access Centre", "coords": [49.1659, -123.9401], "address": "Nanaimo, BC (Serving all communities from Mill Bay to Deep Bay, including Gabriola Island)"},
            {"name": "North Island Community Access Centre", "coords": [49.6923, -124.9905], "address": "Courtenay, BC (Serving all communities north of Deep Bay, including North Vancouver Island and adjacent Gulf Islands)"},
            {"name": "Evergreen Seniors Home Health", "coords": [48.8482, -123.4980], "address": "Cowichan Valley, Duncan, BC V9L 1N8"},
            {"name": "Gabriola Island Nursing Office", "coords": [49.1667, -123.8167], "address": "Gabriola Island, BC V0R 1X0"},
            {"name": "Powell River Home and Community Care", "coords": [49.8352, -124.5248], "address": "5000 Joyce Avenue, Powell River, BC V8A 5R3"},
            {"name": "Sechelt Home and Community Care", "coords": [49.4728, -123.7613], "address": "5630 Inlet Avenue, Sechelt, BC V0N 3A0"},
            {"name": "Port Alberni Home and Community Care", "coords": [49.2339, -124.8052], "address": "3999 Redford Street, Port Alberni, BC V9Y 3R9"},
            {"name": "Tofino Home and Community Care", "coords": [49.1528, -125.9066], "address": "265 First Street South, Tofino, BC V0R 2Z0"},
            {"name": "Bella Coola General Hospital (Home Care Services)", "coords": [52.3702, -126.7534], "address": "1025 Elcho Street, Bella Coola, BC V0T 1C0"},
            {"name": "Bella Bella Community Health Centre", "coords": [52.1633, -128.1454], "address": "Hospital Road, Bella Bella, BC V0T 1Z0"},
            {"name": "Royal Jubilee Hospital (Victoria)", "coords": [48.4359, -123.3381]},
            {"name": "Nanaimo Regional General Hospital", "coords": [49.1659, -123.9401]},
            {"name": "Campbell River Hospital", "coords": [50.0271, -125.2446]},
        ],

        "Northern Health": [

            {"name": "Atlin Health Centre", "coords": [59.5800, -133.7070], "address": "188 Discovery Avenue, Atlin, BC V0W 1A0"},
            {"name": "Burns Lake Primary Care Clinic", "coords": [54.2173, -125.7564], "address": "741 Center Street, Burns Lake, BC V0J 1E0"},
            {"name": "Chetwynd Hospital and Health Centre", "coords": [55.6979, -121.6365], "address": "5125 50th Street Southwest, Chetwynd, BC V0C 1J0"},
            {"name": "Dawson Creek Health Unit", "coords": [55.7606, -120.2356], "address": "1101-103 Avenue, Dawson Creek, BC V1G 2G7"},
            {"name": "Fort Nelson Health Unit", "coords": [58.8052, -122.6972], "address": "5315 Liard Street, Fort Nelson, BC V0C 1R0"},
            {"name": "Fort St. James Health Unit", "coords": [54.4439, -124.2557], "address": "720 4th Avenue West, Fort St. James, BC V0J 1P0"},
            {"name": "Fort St. John Health Unit", "coords": [56.2528, -120.8466], "address": "10115 110 Avenue, Fort St. John, BC V1J 6M9"},
            {"name": "Fraser Lake Community Health Centre", "coords": [54.0625, -124.8528], "address": "130 Chowsunket Street, Fraser Lake, BC V0J 1S0"},
            {"name": "Granisle Community Health Centre", "coords": [54.8844, -126.2245], "address": "34 McDonald Avenue, Granisle, BC V0J 1W0"},
            {"name": "Haida Gwaii Hospital and Health Centre", "coords": [53.2544, -132.0733], "address": "3209 Oceanview Drive, Daajing Giids (Queen Charlotte), BC V0T 1S0"},
            {"name": "Houston Health Centre", "coords": [54.3989, -126.6483], "address": "3202 14th Street, Houston, BC V0J 1Z0"},
            {"name": "Hudson's Hope Health Centre", "coords": [56.0317, -121.9078], "address": "10309 Kyllo Street, Hudson's Hope, BC V0C 1V0"},
            {"name": "Kitimat General Hospital and Health Centre", "coords": [54.0523, -128.6538], "address": "920 Lahakas Boulevard South, Kitimat, BC V8C 2S3"},
            {"name": "Mackenzie and District Hospital and Health Centre", "coords": [55.3372, -123.0964], "address": "45 Centennial Drive West Box 546 Mackenzie BC V0J 2C0"},
            {"name": "McBride Health Unit", "coords": [53.3027, -120.1666], "address": "#1136 Frontage Road McBride BC V0J-2E0"},
            {"name": "Northern Haida Gwaii Hospital and Health Centre","coords":[54.000, -132.1467],"address":"PO Box #88 Masset Haida Gwaii BC V0T 1M0"},
            {"name":"University Hospital of Northern BC (Prince George)","coords":[53.9171, -122.7497],"address":"1475 Edmonton Street Prince George BC V2M 1S2"},  
            {"name":"Fort St John Hospital","coords":[56.252, -120.8467]," address":"8407-112 Ave Fort St John"} , 
            
        ],
    }

    # write the streamlit folium code for the map
    st.title("Home and Community care Map of BC")

    # Dropdown for selecting a health authority
    selected_authority = st.selectbox(

        label="Select a Health Authority",
        options=list(health_authorities.keys()),
    )

    # Create a Folium map centered on BC
    m = folium.Map(location=[54.226669, -126.647621], zoom_start=5)

    # Add markers for the selected health authority
    if selected_authority:

        locations = health_authorities[selected_authority]
        for location in locations:

            folium.Marker(
                location=location["coords"],
                popup=f"<b>{location['name']}</b>",
                tooltip=location["name"],
                icon=folium.Icon(color="blue")
            ).add_to(m)

    # Render the map in Streamlit
    st.write(f"Showing Home Health locations under: {selected_authority}")
    st_folium(m, width=725, height=500)

with tab5:
    st.header("BC HOME CARE DATABASE ")
    st.text(" The Database tab demonstrates how we queried our tables to extract important information. This database is designed to facilitate analysis of the data provided by patients. By leveraging this data, we can apply machine learning techniques to build models that identify the most sought-after services. This insight will allow us to focus on enhancing expertise in those areas of specialization, ensuring better resource allocation and improved service delivery.  ")
    st.markdown("##### click button below to view interactive database ")
  
    def print_table():
        conn = get_db_connecton()
        cursor = conn.cursor()

        try:
            # Query all rows and columns from the `services` table
            query = '''SELECT patient_name, patient_email, service_name, health_authority, appointment_date, appointment_time 
                           FROM patients p
                           INNER JOIN services s
                           ON p.patient_id = s.patient_id
                           INNER JOIN appointments a
                           ON s.service_id = a.service_id
                           ;'''
            
            cursor.execute(query)
            rows = cursor.fetchall()
            
            
            column_names = [description[0] for description in cursor.description]
            df = pandas.DataFrame(rows, columns=column_names)
            return df
        except sqlite3.Error as e:
            st.error(f"An error occurred while fetching data: {e}")
            return None

        finally:
            conn.close()
          

    if st.button("Show appointment in dataframe "):
       data = print_table()

       if data is not None and not data.empty:

        st.dataframe(data)  # Display data as an interactive table
       else:

        st.info("No appointment data found.")



    










#def reset_auto_increment():
    #conn = get_db_connecton()
    #cursor = conn.cursor()

    #Ensure the patients table is empty
    #cursor.execute("DELETE FROM patients;")

    # Reset auto-increment counter for the patients table
    #cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name='patients';")

    #conn.commit()
    #conn.close()

#reset_auto_increment()


#def drop():
    #conn = get_db_connecton()
    #cursor = conn.cursor()

    #Ensure the patients table is empty
    #cursor.execute("DROP TABLE IF EXISTS services")

    # Reset auto-increment counter for the patients table
    #cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name='patients';")

    #conn.commit()
    #conn.close()

#drop()
