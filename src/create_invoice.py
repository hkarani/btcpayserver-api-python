import requests
import os
from dotenv import load_dotenv

load_dotenv()
btc_pay_server_api_key = os.getenv("BTCPAYSERVER_API")

print(f"API Key: {btc_pay_server_api_key}")