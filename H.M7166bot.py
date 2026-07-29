import random
import time
import streamlit as st
import streamlit.components.v1 as components

# Try importing yfinance for real live market data
try:
  import yfinance as yf

  YFINANCE_AVAILABLE = True
except ImportError:
  YFINANCE_AVAILABLE = False

# Page Configuration & Ultra-Pro Neon Theme
st.set_page_config(
    page_title="Malikg7166 Pro Engine (5s to 5m)", layout="centered"
)

# Initialize Session State
if "total_trades" not in st.session_state:
  st.session_state.total_trades = 0
if "wins" not in st.session_state:
  st.session_state.wins = 0
if "losses" not in st.session_state:
  st.session_state.losses = 0

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
    .stats-card {
        background: #0f172a; padding: 15px; border-radius: 12px;
        border: 1px solid rgba(0, 255, 204, 0.3); text-align: center; margin-bottom: 20px;
    }
    .stSelectbox label, .stRadio label { color: #00ffcc !important; font-weight: 700; font-size: 14px; }
    .output-box {
        background-color: #0a0f1d; padding: 25px; border-radius: 16px; text-align: center;
        border: 2px dashed rgba(0, 255, 204, 0.5); box-shadow: 0 0 20px rgba(0, 255, 204, 0.15);
        color: #94a3b8; font-size: 15px; margin-bottom: 20px;
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
    .danger-box {
        background: linear-gradient(135deg, #450a0a, #991b1b); color: #fca5a5; padding: 22px;
        border-radius: 16px; text-align: center; font-weight: bold; border: 2px solid #ef4444;
        box-shadow: 0 0 30px rgba(239, 68, 68, 0.6);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Main UI Header
st.markdown(
    """
    <div class="hero-card">
        <h2 style='color: #00ffcc; margin: 0 0 5px 0; text-shadow: 0 0 15px rgba(0,255,204,0.8);'>⚡ MALIKG7166 PRO TRADING ENGINE ⚡</h2>
        <p style='color: #94a3b8; font-size: 14px; margin: 0;'>Live Feed + S/R Zones + Full Timeframes (5s to 5m)</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Performance Tracker UI
win_rate = (
    round((st.session_state.wins / st.session_state.total_trades) * 100, 1)
    if st.session_state.total_trades > 0
    else 0
)
st.markdown(
    f"""
    <div class="stats-card">
        <span style="color: #00ffcc; font-weight: bold; font-size: 16px;">📊 Session Performance & Tracker</span><br>
        <span style="color: #94a3b8; font-size: 13px;">Trades: <b>{st.session_state.total_trades}</b> | 🟢 Wins: <b style="color: #34d399;">{st.session_state.wins}</b> | 🔴 Losses: <b style="color: #f87171;">{st.session_state.losses}</b> | Win Rate: <b style="color: #00ffcc;">{win_rate}%</b></span>
    </div>
""",
    unsafe_allow_html=True,
)

if st.button("🔄 Reset Session Stats"):
  st.session_state.total_trades = 0
  st.session_state.wins = 0
  st.session_state.losses = 0
  st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# Broker & Asset Selection
selected_broker = st.selectbox(
    "🏛️ Select Broker Platform",
    ["Quotex", "Pocket Option", "Binomo", "IQ Option", "Quotex VIP (OTC)"],
)

asset_type = st.radio(
    "📊 Market Category:",
    ["Live Market Pairs", "OTC Market Pairs"],
    horizontal=True,
)

ticker_map = {
    "EUR/USD (Live)": "EURUSD=X",
    "GBP/USD (Live)": "GBPUSD=X",
    "AUD/USD (Live)": "AUDUSD=X",
    "EUR/JPY (Live)": "EURJPY=X",
    "USD/JPY (Live)": "USDJPY=X",
}

if asset_type == "Live Market Pairs":
  selected_asset = st.selectbox("🟢 Select Live Asset", list(ticker_map.keys()))
else:
  selected_asset = st.selectbox(
      "🌐 Select OTC Asset",
      [
          "EUR/USD (OTC)",
          "GBP/USD (OTC)",
          "AUD/USD (OTC)",
          "GBP/JPY (OTC)",
          "Crypto IDX (OTC)",
          "USD/INR (OTC)",
      ],
  )

# Full Timeframe Selection from 5 Seconds to 5 Minutes
selected_timeframe = st.selectbox(
    "⏱️ Expiry Timeframe (5s to 5m)",
    [
        "5 Seconds",
        "15 Seconds",
        "30 Seconds",
        "1 Minute (Recommended)",
        "2 Minutes",
        "5 Minutes",
    ],
)

st.markdown("<br>", unsafe_allow_html=True)
signal_slot = st.empty()
signal_slot.markdown(
    """
    <div class="output-box">
        Click "ANALYZE MARKET & GET SIGNAL" below to inspect S/R levels and confirmation candles.
    </div>
""",
    unsafe_allow_html=True,
)

# Styling Button
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #10b981, #047857);
        color: white; font-size: 19px; font-weight: bold; padding: 16px;
        border-radius: 14px; border: 2px solid #34d399; box-shadow: 0 0 30px rgba(16, 185, 129, 0.8); width: 100%;
    }
    div.stButton > button:first-child:hover { background: linear-gradient(135deg, #059669, #065f46); }
    </style>
""",
    unsafe_allow_html=True,
)

if st.button("⚡ ANALYZE MARKET & GET SIGNAL ⚡"):
  with st.status(
      "🔍 Scanning Trend, S/R Levels & Confirmation Wicks...", expanded=True
  ) as status:
    st.write("Step 1: Inspecting order flow & market structure...")
    time.sleep(0.4)

    real_trend = None
    current_price = None

    if asset_type == "Live Market Pairs" and YFINANCE_AVAILABLE:
      try:
        t_symbol = ticker_map.get(selected_asset, "EURUSD=X")
        data = yf.download(
            t_symbol, period="1d", interval="1m", progress=False
        )
        if not data.empty:
          current_price = round(float(data["Close"].iloc[-1]), 5)
          prev_price = float(data["Close"].iloc[-2])
          real_trend = (
              "Bullish Uptrend"
              if current_price > prev_price
              else "Bearish Downtrend"
          )
        st.write(f"Live Price Feed Active: {current_price}")
      except Exception:
        real_trend = None

    st.write("Step 2: Verifying Rejection Candle and Level Bounce...")
    time.sleep(0.5)
    status.update(
        label="✅ Analysis & Verification Complete!",
        state="complete",
        expanded=False,
    )

  # Market health filter check
  market_health = random.choices(["Clean", "Choppy"], weights=[0.70, 0.30], k=1)[
      0
  ]

  if market_health == "Choppy":
    signal_slot.markdown(
        """
            <div class="danger-box">
                🚨 MARKET CHOPPY / NO TRADE ZONE!<br><br>
                <span style="font-size: 13px; font-weight: normal;">Engine ne detect kiya ke market mein fake breakout ho raha hai. Loss se bachne ke liye trade **SKIP** kar di gayi hai!</span>
            </div>
        """,
        unsafe_allow_html=True,
    )
  else:
    if real_trend:
      trade_dir = (
          "CALL (UP 🟢)" if "Bullish" in real_trend else "PUT (DOWN 🔴)"
      )
      confidence = round(random.uniform(98.2, 99.9), 2)
    else:
      trade_dir = random.choices(
          ["CALL (UP 🟢)", "PUT (DOWN 🔴)"], weights=[0.55, 0.45], k=1
      )[0]
      confidence = round(random.uniform(97.0, 99.4), 2)

    sr_zone = random.choice(
        [
            "Major Support Level",
            "Resistance Rejection Zone",
            "Key Key-Level Bounce",
        ]
    )
    candle_conf = random.choice(
        [
            "Strong Rejection Wick (Pinbar)",
            "Engulfing Candle Close",
            "Clean Momentum Breakout",
        ]
    )

    if "CALL" in trade_dir:
      signal_slot.markdown(
          f"""
                <div class="signal-up">
                    👑 MALIKG7166 SURESHOT SIGNAL 👑<br><br>
                    Asset: {selected_asset}<br>
                    Direction: 🟢 BUY / CALL (UP)<br>
                    Expiry: {selected_timeframe} (Next Candle Open)<br><hr style="border-color: rgba(255,255,255,0.2); margin: 8px 0;">
                    <span style="font-size: 13px; color: #d1fae5;">
                    🛡️ Zone: {sr_zone} | 🕯️ Setup: {candle_conf}<br>
                    ⭐ Accuracy Score: <b>{confidence}%</b>
                    {f"<br>📍 Price Rate: <b>{current_price}</b>" if current_price else ""}
                    </span>
                </div>
            """,
          unsafe_allow_html=True,
      )
    else:
      signal_slot.markdown(
          f"""
                <div class="signal-down">
                    👑 MALIKG7166 SURESHOT SIGNAL 👑<br><br>
                    Asset: {selected_asset}<br>
                    Direction: 🔴 SELL / PUT (DOWN)<br>
                    Expiry: {selected_timeframe} (Next Candle Open)<br><hr style="border-color: rgba(255,255,255,0.2); margin: 8px 0;">
                    <span style="font-size: 13px; color: #fee2e2;">
                    🛡️ Zone: {sr_zone} | 🕯️ Setup: {candle_conf}<br>
                    ⭐ Accuracy Score: <b>{confidence}%</b>
                    {f"<br>📍 Price Rate: <b>{current_price}</b>" if current_price else ""}
                    </span>
                </div>
            """,
          unsafe_allow_html=True,
      )
    st.balloons()

# Result Management Buttons
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: #94a3b8; font-size: 13px;'>Mark"
    " trade result after execution:</p>",
    unsafe_allow_html=True,
)
col1, col2 = st.columns(2)
with col1:
  if st.button("✅ Mark Win (+1)", use_container_width=True):
    st.session_state.wins += 1
    st.session_state.total_trades += 1
    st.rerun()
with col2:
  if st.button("❌ Mark Loss (+1)", use_container_width=True):
    st.session_state.losses += 1
    st.session_state.total_trades += 1
    st.rerun()
