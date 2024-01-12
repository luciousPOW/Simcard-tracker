import phonenumbers
import opencage
from phonenumbers import geocoder, carrier

def get_phone_info():
    number = input("Enter number: ")
    
    try:
        pepnumber = phonenumbers.parse(number, "PH")
        location = geocoder.description_for_number(pepnumber, "en")
        print(f"Location: {location}")

        services_pro = phonenumbers.parse(number, "PH")
        service_provider = carrier.name_for_number(services_pro, "en")
        print(f"Service Provider: {service_provider}")

    except phonenumbers.NumberParseException as e:
        print(f"Error: {e}")
        
from opencage.geocoder import OpenCageGeocode

# Call the function to get phone information
get_phone_info()
