import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode

# Take input the phonenumber along with the country code
number = input("Enter the PhoneNumber with the country code : ")

# Parse the phonenumber string to convert it into phonenumber format
phoneNumber = phonenumbers.parse(number)

# Generate API Key
key = "fd596bb7478048bea7fda3633e70ba5b" # generate your api https://opencagedata.com/api

# Use the geocoder module of phonenumbers to print the Location in console
location = geocoder.description_for_number(phoneNumber, "en")
print(f"Location: {location}")

# Use the carrier module of phonenumbers to print the service provider name in console
service_provider = carrier.name_for_number(phoneNumber, "en")
print(f"Service Provider: {service_provider}")

# Use opencage to get the latitude and longitude of the location
geocoder = OpenCageGeocode(key)
query = location
results = geocoder.geocode(query)

# Assigning the latitude and longitude values to the lat and lng variables
latitude = results[0]['geometry']['lat']
longitude = results[0]['geometry']['lng']

# Get the map for the given latitude and longitude
my_map = folium.Map(location=[latitude, longitude], zoom_start=9)

# Add a Marker on the map to show the location name
folium.Marker([latitude, longitude], popup=location).add_to(my_map)
# Save the Map as HTML file
my_map.save('star.html')