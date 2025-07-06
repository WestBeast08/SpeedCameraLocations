import csv
import folium
from geopy.geocoders import Nominatim
import time

# Input csv data (for now manually locally) and extract street names with suburbs and put them in a list
def getCsvData():
    filePath = 'Mobile-Camera-Locations-July-2025.csv'
    with open(filePath, 'r') as csvFile:
        csvReader = csv.reader(csvFile)
        locations = []
        
		# Skip header rows
        for i in range(2):
            next(csvReader)
        
		# Add each location's street and suburb to the locations list
        for row in csvReader:
            # First two columns are street and suburb, respectively
            locations.append((row[0], row[1]))
    return locations

# Change location format to full address format for use with Map API
def getFullAddresses(locations):
    fullAddresses = [f"{street}, {suburb}, Victoria, Australia" for street, suburb in locations]
    return fullAddresses



geolocator = Nominatim(user_agent="camera-map")

def get_coordinates(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return (location.latitude, location.longitude)
        return None
    except:
        return None



# Testing for street name to coordinates
coords = get_coordinates("123 Smith St, Fitzroy, VIC, Australia")
# Remember that Nomintim has a general rate limit of 1 Request/second so when looping we should add a time delay between get_coordinate calls
print(coords)


# Testing map on melbourne
map_obj = folium.Map(location=[-37.8136, 144.9631], zoom_start=12)

# Example locations
locations = [
    (-37.8136, 144.9631, "Melbourne CBD"),
    (-37.8200, 145.0000, "South Yarra"),
    (-37.8000, 144.9500, "North Melbourne"),
    (coords[0], coords[1], "123 Smith St, Fitzroy, VIC, Australia")
]

# Add basic markers
for lat, lon, label in locations:
    folium.Marker(location=[lat, lon], popup=label).add_to(map_obj)

# Save to HTML
map_obj.save("map_with_pins.html")
