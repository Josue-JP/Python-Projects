# Note: This script is not optimzed meaning that it is not good enough to use
# Please feel free to optimize this code to get a better result.
import phonenumbers
from phonenumbers import geocoder, carrier, timezone 

# ==============
#   Section 1                       \
# ==============

phoneNumber = input("Enter phonenumber with a Country code and a National Number\nExample: +1 (717) 550-1675 or +15716593756\n  Enter phonenumber\n  ")

parsedNumber = phonenumbers.parse(phoneNumber)
print(parsedNumber) # This prints the Country Code and the National number

phoneNumberLocation = geocoder.description_for_number(parsedNumber, 'en')
print(f"Location: {phoneNumberLocation}") # this prints the City and State of the phone number

phoneTimezones = timezone.time_zones_for_number(parsedNumber)
print(f"Timezone: {phoneTimezones}")

phoneNumberType = phonenumbers.number_type(parsedNumber)
# This prints the phone number type
if phoneNumberType == phonenumbers.PhoneNumberType.MOBILE:
    print("Type: Mobile")
elif phoneNumberType == phonenumbers.PhoneNumberType.FIXED_LINE:
    print("Type: Fixed Line")
elif phoneNumberType == phonenumbers.PhoneNumberType.TOLL_FREE:
    print("Type: Toll-Free")
elif phoneNumberType == phonenumbers.PhoneNumberType.PREMIUM_RATE:
    print("Type: Premium Rate")
elif phoneNumberType == phonenumbers.PhoneNumberType.SHARED_COST:
    print("Type: Shared Cost")
elif phoneNumberType == phonenumbers.PhoneNumberType.VOIP:
    print("Type: VOIP")
elif phoneNumberType == phonenumbers.PhoneNumberType.UNKNOWN:
    print("Type: Unknown")
else:
    print("Type: Not recognized")

# You can try to get the carrier with this code but 9/10 it will not find it
# if phonenumbers.is_valid_number(parsedNumber):
#     # Get the carrier name (it may be empty if the number is a landline or VoIP)
#     phoneCarrier = carrier.name_for_number(parsedNumber, 'en')
#     if phoneCarrier:
#         print(f"Carrier: {phoneCarrier}")
#     else:
#         print("Carrier: Not Found")
