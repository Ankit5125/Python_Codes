import requests

# calling apis
apicall = requests.get("http://api.open-notify.org/astros")

# taking statuscode from api
# diffrent statuscode reffres to diffrent respons given from apis
# check online for more status code 
print(type(apicall.status_code))

print(apicall.status_code)

# -------------------------------

# collected data is in json from
# to print data use this method...
print(type(apicall.json()))

print(apicall.json())