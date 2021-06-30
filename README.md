# Binance (Market)Sell Script

## Disclaimer
By using this script, you give it access to your Binance account. I do not take any responsibility of bugs which could cause loss of funds.

## What it does

This simple script will sell a user-specified amount of DOT tokens for EUR as a market-sell-order. Before doing so, it first shows your DOT balance and the current DOT price. After a successful trade it provides you the information about your profit and the paid fees. Note: To reduce trading fees it is advised to have BNB tokens in your account.

## Tip
If you are planning to frequently sell stake-rewards, it might be convenient to set your Binance address as your staking destination address. Thereby, you just need to run the script from time to time and sell your tokens. There are currently **no deposit fees** on binance which makes this a viable strategy. Things can always change and you are responsible for checking that.

## Installation

### Set your API keys as environmental variables
* Get your Binance API keys.
* Set your API keys as environmental variables. Use `binance_api` for your public key and `binance_secret` for your secret key.
* Install the binance python library with `pip install python-binance`.

## Running
Open the folder containing the script with your terminal and type:
`python3 auto_sell.py`

