'''
from pandas_datareader import data as pdr

"""Retrieve stock historical financial pricing information from Yahoo! Finance."""

# Example 3.1: Download Data from Yahoo
def test_yfinance():
    for symbol in ["AAPL", "MSFT", "VFINX", "BTC-USD"]:
        print(">>", symbol, end=" ... ")
        data = pdr.get_data_yahoo(symbol, start="2020-09-25", end="2020-10-02")
        print(data)


if __name__ == "__main__":
    # if script called directly
    test_yfinance()
'''
"""
It seems like you’re getting an AttributeError because the pandas_datareader library is having trouble accessing Yahoo Finance’s data.

This issue is usually related to a change on Yahoo Finance’s side that might have broken the older code. Here’s a possible solution:

1. Use yfinance library instead

Instead of pandas_datareader, you can use yfinance, which is a more robust and up-to-date library for pulling Yahoo Finance data. Here’s how you can modify your code to use yfinance:

First, install yfinance:

!pip install yfinance

Then modify your code like this:

import yfinance as yf

# Example 3.1: Download Data from Yahoo
def test_yfinance():
    for symbol in ["AAPL", "MSFT", "VFINX", "BTC-USD"]:
        print(">>", symbol, end=" ... ")
        data = yf.download(symbol, start="2020-09-25", end="2020-10-02")
        print(data)

if __name__ == "__main__":
    # if script called directly
    test_yfinance()

The yfinance.download() method works similarly to pandas_datareader.get_data_yahoo(), and it should resolve the issue you’re facing with pandas_datareader.

2. If you still prefer using pandas_datareader

There may be an update or fix for the pandas_datareader library in future versions. You can try updating it with:

!pip install --upgrade pandas-datareader

Let me know if that works or if you need more assistance!
"""

!pip install yfinance

### Then modify your code like this:

import yfinance as yf

# Example 3.1: Download Data from Yahoo
def test_yfinance():
    for symbol in ["AAPL", "MSFT", "VFINX", "BTC-USD"]:
        print(">>", symbol, end=" ... ")
        data = yf.download(symbol, start="2020-09-25", end="2020-10-02")
        print(data)

if __name__ == "__main__":
    # if script called directly
    test_yfinance()



