import streamlit as st
st.title("Can we play with big boys in potato production")


import pandas as pd

# Clinic data
data = {
    "lat": [49.2827, 49.2488, 49.1666],
    "lon": [-123.1207, -122.9805, -123.1336],
    "name": ["Vancouver Clinic", "Burnaby Clinic", "Richmond Clinic"]
}
df = pd.DataFrame(data)

# Display the map
st.title("Health Resource Locator")
st.map(df)



import streamlit as st
from streamlit_folium import st_folium
import folium
st.image("images/beautiful columbians.webp")
# Title of the app
st.title("Interactive Map with Folium")


# Create a Folium map centered on Vancouver, BC
m = folium.Map(location=[49.2827, -123.1207], zoom_start=12)

# Add a marker to the map
folium.Marker(
    location=[49.2827, -123.1207],
    popup="Vancouver, BC",
    tooltip="Click for more info"
).add_to(m)

st.write("Below is an interactive map centered on Vancouver:")
st_folium(m, width=725, height=500)


patient_id = st.number_input("Enter your Patient ID:", min_value=1, step=1)


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

# Streamlit app
st.title("Health Authorities Map of BC")

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
st.write(f"Showing locations for: {selected_authority}")
st_folium(m, width=725, height=500)