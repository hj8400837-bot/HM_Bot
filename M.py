import numpy as np
import pandas as pd
import streamlit as st

# Try importing yfinance
try:
  import yfinance as yf

  YFINANCE_AVAILABLE = True
except ImportError:
  YFINANCE_AVAILABLE = False

# Page Configuration
st.set_page_config(
    page_title="(4friends+2 couples) - Pro Technical Engine", layout="centered"
)

# Custom Styling
st.markdown(
    """
    <style>
    .main { background-color: #05070b; color: #ffffff; }
    .stApp { background-color: #05070b; }
    .hero-card {
        background: linear-gradient(135deg, #0f172a, #1e1b4b);
        padding: 24px; border-radius: 18px;
        border: 2px solid rgba(0, 255, 204, 0.6);
        text-align: center; box-shadow: 0 0 35px rgba(0, 255, 204, 0.3);
        margin-bottom: 20px;
    }
    .signal-up {
        background: linear-gradient(135deg, #064e3b, #059669); color: white; padding: 24px;
        border-radius: 16px; text-align: center; font-weight: bold; font-size: 18px;
        box-shadow: 0 0 35px rgba(16, 185, 129, 0.8); border: 2px solid #34d399;
    }
    .signal-down {
        background: linear-gradient(135deg, #7f1d1d, #dc2626); color: white; padding: 24px;
        border-radius: 16px; text-align: center; font-weight: bold; font-size: 18px;
        box-shadow: 0 0 35px rgba(239, 68, 68, 0.8); border: 2px solid #f87171;
    }
    .neutral-box {
        background: #0f172a; padding: 20px; border-radius: 16px; text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2); color: #94a3b8;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Header
st.markdown(
    """
    <div class="hero-card">
        <h2 style='color: #00ffcc; margin: 0 0 5px 0;'>⚡ (4friends+2 couples) PRO ENGINE ⚡</h2>
        <p style='color: #94a3b8; font-size: 14px; margin: 0;'>Real Indicator Engine (EMA Crossover + RSI Filter)</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Asset Selection
selected_asset = st.selectbox(
    "🟢 Select Live Market Asset",
    [
        "EUR/USD",
        "GBP/USD",
        "AUD/USD",
        "USD/JPY",
        "EUR/JPY",
    ],
)

ticker_dict = {
    "EUR/USD": "EURUSD=X",
    "GBP/USD": "GBPUSD=X",
    "AUD/USD": "AUDUSD=X",
    "USD/JPY": "USDJPY=X",
    "EUR/JPY": "EURJPY=X",
}

st.markdown("<br>", unsafe_allow_html=True)
signal_slot = st.empty()
signal_slot.markdown(
    """
    <div class="neutral-box">
        Click the analyze button below to compute live EMA and RSI indicators.
    </div>
""",
    unsafe_allow_html=True,
)


# Technical Indicator Calculations
def calculate_rsi(data, window=14):
  delta = data.diff()
  gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
  loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
  rs = gain / loss
  return 100 - (100 / (1 + rs))


if st.button("⚡ RUN ADVANCED TECHNICAL ANALYSIS ⚡"):
  if not YFINANCE_AVAILABLE:
    st.error(
        "yfinance library is missing! Please install it to fetch live data."
    )
  else:
    with st.spinner("Fetching live candles and calculating mathematical"
                    " indicators..."):
      symbol = ticker_dict[selected_asset]
      df = yf.download(symbol, period="5d", interval="1m", progress=False)

      if df.empty:
        st.error(
            "Failed to fetch market data. Please try again or use another asset."
        )
      else:
        # Flatten columns if multi-index
        if isinstance(df.columns, pd.MultiIndex):
          df.columns = df.columns.get_level_values(0)

        # Calculate EMA 9 and EMA 21
        df["EMA_9"] = df["Close"].ewm(span=9, adjust=False).mean()
        df["EMA_21"] = df["Close"].ewm(span=21, adjust=False).mean()

        # Calculate RSI
        df["RSI"] = calculate_rsi(df["Close"], window=14)

        # Get latest values
        last_close = float(df["Close"].iloc[-1])
        last_ema9 = float(df["EMA_9"].iloc[-1])
        last_ema21 = float(df["EMA_21"].iloc[-1])
        last_rsi = float(df["RSI"].iloc[-1])

        # Signal Logic based on real indicators
        if last_ema9 > last_ema21 and last_rsi < 70:
          signal_type = "CALL"
          reason = "Bullish EMA Crossover + RSI Healthy"
        elif last_ema9 < last_ema21 and last_rsi > 30:
          signal_type = "PUT"
          reason = "Bearish EMA Crossover + RSI Healthy"
        else:
          signal_type = "NEUTRAL"
          reason = (
              "Market is consolidating or RSI is in Overbought/Oversold zone."
          )

        if signal_type == "CALL":
          signal_slot.markdown(
              f"""
                        <div class="signal-up">
                            👑 (4friends+2 couples) PRO SIGNAL 👑<br><br>
                            Asset: {selected_asset}<br>
                            Direction: 🟢 BUY / CALL (UP)<br><hr style="border-color: rgba(255,255,255,0.2); margin: 8px 0;">
                            <span style="font-size: 13px; color: #d1fae5;">
                            📈 Price: {last_close:.5f} | EMA 9: {last_ema9:.5f} | EMA 21: {last_ema21:.5f}<br>
                            📊 RSI (14): {last_rsi:.2f} | Setup: {reason}
                            </span>
                        </div>
                    """,
              unsafe_allow_html=True,
          )
        elif signal_type == "PUT":
          signal_slot.markdown(
              f"""
                        <div class="signal-down">
                            👑 (4friends+2 couples) PRO SIGNAL 👑<br><br>
                            Asset: {selected_asset}<br>
                            Direction: 🔴 SELL / PUT (DOWN)<br><hr style="border-color: rgba(255,255,255,0.2); margin: 8px 0;">
                            <span style="font-size: 13px; color: #fee2e2;">
                            📉 Price: {last_close:.5f} | EMA 9: {last_ema9:.5f} | EMA 21: {last_ema21:.5f}<br>
                            📊 RSI (14): {last_rsi:.2f} | Setup: {reason}
                            </span>
                        </div>
                    """,
              unsafe_allow_html=True,
          )
        else:
          signal_slot.markdown(
              f"""
                        <div class="neutral-box">
                            ⚠️ NO CLEAR SIGNAL (SKIPPED)<br>
                            Reason: {reason}<br>
                            RSI Value: {last_rsi:.2f}
                        </div>
                    """,
              unsafe_allow_html=True,
          )
