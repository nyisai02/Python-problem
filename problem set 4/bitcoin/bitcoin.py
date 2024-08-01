import requests
import sys

if len(sys.argv)==2:
    try:
         value=float(sys.argv[1])
    except:
        exit("Command-line argument is not a number")

if len(sys.argv)!=2:
    exit("Missing command-line argument")


try:
    req=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    respons=req.json()
    coin=respons['bpi']['USD']['rate_float']
    amount=coin * value
    print(f"${amount:,.4f}")
except requests.RequestException:
    print("RequestException")
    sys.exit(1)
