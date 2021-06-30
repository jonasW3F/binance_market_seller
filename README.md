# Binance (Market)Sell Script

## Disclaimer
By using this script, you give it access to your Binance account. I do not take any responsibility of bugs which could cause loss of funds.

## What it does

This simple script will sell a user-specified amount of DOT tokens for EUR as a market-sell-order. Before doing so, it first shows your DOT balance and the current DOT price. After a successful trade it provides you the information about your profit and the paid fees. Note: To reduce trading fees it is advised to have BNB tokens in your account.

## Installation

### Set your API keys as environmental variables
* Get your Binance API keys.
* Set your API keys as environmental variables. Use `binance_api` for your public key and `binance_secret` for your secret key.
* Install the binance python library with `pip install python-binance`.

## Running
Open the folder containing the script with your terminal and type:
`python3 auto_sell.py`

