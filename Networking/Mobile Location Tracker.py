import phonenumbers
from phonenumbers import geocoder
number = input("Enter the Phone Number : ")
phone_number1 = phonenumbers.parse(number)
print(geocoder.description_for_number(phone_number1,'en'))
