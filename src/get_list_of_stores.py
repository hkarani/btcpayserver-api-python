import requests
import os
from dotenv import load_dotenv

load_dotenv()
btc_pay_server_api_key = os.getenv("BTCPAYSERVER_API")
btc_pay_server_url = "https://testnet.demo.btcpayserver.org"
btc_pay_server_api_endpoint = "/api/v1/stores"

##  List stores  ###

def list_stores():
    url = f"{btc_pay_server_url}{btc_pay_server_api_endpoint}"
    headers = {
        "Authorization": f"token {btc_pay_server_api_key}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

stores = list_stores()
print("---- List of stores ------\n")
print(stores)