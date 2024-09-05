import requests

def apicall():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response = requests.get(url)
    data = response.json()
    
    
    if data["success"] and "data" in data :
        print(data["message"] + "\n")
        
        contents = data["data"]

        joke = contents[0]["contents"]

        print(joke)

    '''
    if data["statusCode"] == 200 :
        print("Done ✅")
    '''

apicall() 