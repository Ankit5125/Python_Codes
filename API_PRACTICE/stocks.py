import requests

def stocks():   
    url = "https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata"
    	
    response = requests.get(url)
    
    user_data = response.json()

    print(user_data["statusCode"])


# choice = int(input("1 -> View Stocks \n 0 -> Exit"))
while True :
    choice = int(input("1 -> View Stocks \n0 -> Exit \n Choice : "))
    
    if choice == 1 :
        stocks()
        
    else :
        exit()
