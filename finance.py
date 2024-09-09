import yfinance as yf

ticker_symbol_apple = "AAPL"


ticker = yf.Ticker(ticker_symbol_apple)


historical_data= ticker.history(period="1y")
print("Apple Historical Data: ")
print(historical_data)

financials= ticker.financials
print("\nApple Financials :")
print(financials)

actions = ticker.actions
print("\nApple Stock Actions: ")
print(actions)


print('********************************************************************************')

ticker_symbol_nike = "NKE"

ticker = yf.Ticker(ticker_symbol_nike)

historical_data_nike = ticker.history(period="1mo")
print(f"Nike Historical data in 1 month :{ticker_symbol_nike}")
print(historical_data_nike[['Open', 'High', 'Low', 'Close', 'Volume']])