# 📈 Stock Tracker (Streamlit + yfinance)

A simple web app built with [Streamlit](https://streamlit.io/) and [yfinance](https://github.com/ranaroussi/yfinance) that lets you look up any stock and see its price history and trading volume.

## Features

- Choose a **start date** and **end date**
- Enter any **stock ticker symbol** (e.g. `AAPL`, `MSFT`, `TSLA`, `RELIANCE.NS`)
- View the full historical data table (Open, High, Low, Close, Volume, Dividends, Stock Splits)
- Line chart of the **daily closing price**
- Line chart of the **daily trading volume**

## Tech Stack

- Python 3.9+
- Streamlit
- yfinance

## Installation

1. Clone the repository

   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. (Optional) Create and activate a virtual environment

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. Install the dependencies

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the app with:

```bash
streamlit run stock_analysis_demo.py
```

Streamlit will open the app in your browser at `http://localhost:8501`.

1. Pick the start and end dates.
2. Type a ticker symbol in the text box and press Enter.
3. Scroll down to see the data table and the charts.

> **Tip:** For Indian stocks, add the exchange suffix, e.g. `TCS.NS` (NSE) or `TCS.BO` (BSE).

## Project Structure

```
.
├── stock_analysis_demo.py   # Main Streamlit app
├── requirements.txt         # Python dependencies
└── README.md
```

## Future Improvements

- Moving averages and technical indicators
- Candlestick charts
- Compare multiple stocks
- Error handling for invalid tickers

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

**Arnav**
B.Tech Computer Engineering, MIT Academy of Engineering, Pune
