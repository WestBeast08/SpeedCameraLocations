import csv

# Input csv data (for now manually locally) and extract street names with suburbs and put them in a list
def getCsvData():
    filePath = 'Mobile-Camera-Locations-November-2024.csv'
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


# Function testing
locations = getCsvData()
for street, suburb in locations:
    print(f"Street: {street}, Suburb: {suburb}")