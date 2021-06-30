import os
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

# Initialize Client
client = Client(api_key, api_secret)

# Get DOT Balance
dot_balance = client.get_asset_balance(asset='DOT')
dot_balance = float(dot_balance["free"])

# Get BNB Balance (using that for paying fees is cheaper, so it is adviced to have some in the account)
bnb_balance = client.get_asset_balance(asset='BNB')
bnb_balance = float(bnb_balance["free"])

# Get the prices in EUR
bnb_price = float(client.get_symbol_ticker(symbol="BNBEUR")["price"])
dot_price = float(client.get_symbol_ticker(symbol="DOTEUR")["price"])

# Get the BNB amount in EUR
bnb_amount = bnb_balance*bnb_price

# Information to the user
print("You currently have " + str(dot_balance) + " DOT as balance. And you have " + str(bnb_amount) + " EUR in BNB tokens to pay fees")
print("The DOT price is currently " + str(dot_price) + "EUR")

# How much does the user want to sell?
sell_amount_dot = float(input("How many DOT to you want to sell? "))

# There seems to be a minimum of 0.8 DOT which can be sold
if(sell_amount_dot >= 0.8):
    try:
        market_order = client.order_market_sell(
        symbol='DOTEUR',
        quantity = sell_amount_dot
        )
    except BinanceAPIException as e:
    # error handling goes here
        print(e)
    except BinanceOrderException as e:
    # error handling goes here
        print(e)
    print("You successfully sold " + market_order["executedQty"] + " DOT and earned " + market_order["cummulativeQuoteQty"] + "EUR")
    if(market_order["fills"][0]["commissionAsset"] == "BNB"):
        print("This order cost " + str(float(market_order["fills"][0]["commission"]) * bnb_price) + " fees in EUR")
else:
    print("Sell amount must be greater or equal to 0.8")