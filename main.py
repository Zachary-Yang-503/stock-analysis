print("hello stock project")

import yfinance as yf
data = yf.download("NVDA TSLA PLTR MSFT", period="6mo")
print(data.head())
print(data["Close"])
print(data["Close"]["NVDA"])

import matplotlib.pyplot as plt
plt.plot(data["Close"]["NVDA"])
plt.show()

import pandas

print("ok")