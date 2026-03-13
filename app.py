from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    quote = None
    error = None
    ticker = None

    if request.method == "POST":
        ticker = request.form.get("ticker", "").strip().upper()
        if not ticker:
            error = "请输入要查询的股票代码 (例如: AAPL, 000001.SZ, 600000.SS)"
        else:
            try:
                stock = yf.Ticker(ticker)
                info = stock.info

                if not info or info.get("regularMarketPrice") is None:
                    raise ValueError("无法获取该股票的数据，可能代码不正确。")

                quote = {
                    "symbol": ticker,
                    "name": info.get("shortName") or info.get("longName") or "",
                    "price": info.get("regularMarketPrice"),
                    "previous_close": info.get("regularMarketPreviousClose"),
                    "open": info.get("regularMarketOpen"),
                    "day_high": info.get("regularMarketDayHigh"),
                    "day_low": info.get("regularMarketDayLow"),
                    "currency": info.get("currency"),
                }
            except Exception as e:
                error = f"查询失败: {e}"

    return render_template("index.html", quote=quote, error=error, ticker=ticker)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
