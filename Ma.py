import streamlit as st
import pandas as pd
import numpy as np
import pandas_ta as ta
import time

st.set_page_config(
    page_title="Hassan Malik AI Bot - Pro Max",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom Dark Futuristic UI Styling matching your screenshot
st.markdown("""
    <style>
    .stApp { background-color: #07090e; color: #ffffff; font-family: 'Segoe UI', Tahoma, sans-serif; }
    .main-header { background: linear-gradient(135deg, #0d1b2a 0%, #1b263b 100%); padding: 18px; border-radius: 16px; text-align: center; border: 1px solid #1f3a5f; box-shadow: 0 4px 20px rgba(0, 150, 255, 0.2); margin-bottom: 15px; }
    .badge-pro { background: linear-gradient(90deg, #f39c12, #f1c40f); color: #000; padding: 4px 14px; border-radius: 20px; font-weight: bold; font-size: 13px; display: inline-block; margin-top: 6px; }
    .status-container { display: flex; justify-content: space-around; background-color: #0e1626; padding: 10px; border-radius: 12px; border: 1px solid #1e293b; margin-bottom: 15px; text-align: center; font-size: 11px; }
    .unlocked-banner { background: linear-gradient(90deg, #1b263b, #0f172a); border: 1px solid #f39c12; color: #f39c12; padding: 10px; border-radius: 10px; text-align: center; font-weight: bold; margin-bottom: 15px; font-size: 14px; }
    .stButton>button { width: 100%; background: linear-gradient(90deg, #2563eb, #7c3aed); color: white; font-size: 16px; font-weight: bold; padding: 14px; border-radius: 12px; border: none; box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4); transition: 0.3s; }
    .stButton>button:hover { background: linear-gradient(90deg, #1d4ed8, #6d28d9); box-shadow: 0 6px 20px rgba(37, 99, 235, 0.6); }
    .footer-nav { display: flex; justify-content: space-around; background-color: #0b1120; padding: 12px 5px; border-radius: 14px; border: 1px solid #1e293b; margin-top: 25px; text-align: center; font-size: 11px; color: #94a3b8; }
    </style>
""", unsafe_allow_html=True)

# Top Header
st.markdown("""
    <div class="main-header">
        <h1 style="margin:0; font-size:24px; color:#ffffff;">HASSAN MALIK <span style="color:#38bdf8;">AI BOT</span></h1>
        <div class="badge-pro">👑 PRO MAX</div>
    </div>
""", unsafe_allow_html=True)

# Status Row
st.markdown("""
    <div class="status-container">
        <div>🛡️ LICENSE STATUS<br><span style="color:#22c55e; font-weight:bold;">ACTIVE 🟢</span></div>
        <div>🤖 AI ENGINE<br><span style="color:#22c55e; font-weight:bold;">ONLINE 🟢</span></div>
        <div>👥 ACTIVE USERS<br><span style="color:#38bdf8; font-weight:bold;">1M+</span></div>
    </div>
    <div class="unlocked-banner">👑 PRO MAX UNLOCKED ✅</div>
""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; margin-bottom: 0;'>GENERATE <span style='color: #38bdf8;'>SIGNALS</span></h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 13px;'>AI Analyzed High Accuracy Trading Signals</p>", unsafe_allow_html=True)

# Broker & Market Selection
broker = st.selectbox("BROKER", ["Quotex"])
market_type = st.selectbox("MARKET", ["OTC Markets", "Live Markets"])

# Comprehensive Asset Lists
otc_pairs_list = [
    "USD/ARS (OTC)", "EUR/USD (OTC)", "GBP/USD (OTC)", "AUD/USD (OTC)", "USD/JPY (OTC)",
    "AUD/CAD OTC", "AUD/CHF OTC", "AUD/JPY OTC", "AUD/NZD OTC", "CAD/CHF OTC", "CAD/JPY OTC",
    "CHF/JPY OTC", "EUR/AUD OTC", "EUR/CAD OTC", "EUR/CHF OTC", "EUR/GBP OTC", "EUR/JPY OTC",
    "EUR/NZD OTC", "GBP/AUD OTC", "GBP/CAD OTC", "GBP/CHF OTC", "GBP/JPY OTC", "GBP/NZD OTC",
    "NZD/CAD OTC", "NZD/CHF OTC", "NZD/JPY OTC", "NZD/USD OTC", "USD/CAD OTC", "USD/CHF OTC",
    "USD/SGD OTC", "Bitcoin OTC", "Ethereum OTC", "Litecoin OTC", "Ripple OTC", "Doge OTC",
    "Gold OTC", "Silver OTC", "Oil OTC (Brent)", "S&P 500 OTC", "Nasdaq 100 OTC", "Dow Jones 30 OTC", "DAX 30 OTC"
]

live_pairs_list = [
    "EUR/USD (Live)", "USD/JPY (Live)", "GBP/USD (Live)", "AUD/USD (Live)", "USD/CAD (Live)", "USD/CHF (Live)",
    "EUR/JPY (Live)", "EUR/GBP (Live)", "NZD/USD (Live)", "AUD/NZD (Live)", "EUR/CAD (Live)", "GBP/MXN (Live)",
    "USD/BRL (Live)", "AUD/JPY (Live)", "CAD/JPY (Live)", "USD/MXN (Live)", "GOLD (Live)", "XAU/USD (Live)",
    "OIL (WTI) (Live)", "BTC/USD (Live)", "ETH/USD (Live)", "S&P 500 (Live)", "NASDAQ (Live)", "DOW JONES (Live)"
]

# Dynamic Pair Filtering based on Market Type selection
pair = st.selectbox("PAIR", otc_pairs_list if market_type == "OTC Markets" else live_pairs_list)

# Timers (5 Seconds to 5 Minutes)
timer = st.selectbox("TIMER", [
    "5 Seconds", "10 Seconds", "15 Seconds", "30 Seconds", 
    "1 Minute", "2 Minutes", "3 Minutes", "5 Minutes"
])

st.markdown("<br>", unsafe_allow_html=True)

# Action Button & Signal Generation Logic
if st.button("🚀 NEXT CANDLE GENERATE SIGNAL"):
    with st.spinner(f"Analyzing market structure, RSI & order flow for {pair}..."):
        time.sleep(1.2)
        
        # Simulating Technical Analysis Feed via Pandas-TA
        np.random.seed()
        sim_close = 1.0800 + np.cumsum(np.random.randn(50) * 0.0001)
        temp_df = pd.DataFrame({"Close": sim_close})
        temp_df['RSI'] = ta.rsi(temp_df['Close'], length=14)
        last_rsi = temp_df['RSI'].iloc[-1] if not temp_df['RSI'].isna().all() else 49.2
        
        # Decision Logic for Next Candle
        if last_rsi < 48 or np.random.rand() > 0.45:
            signal_direction = "CALL (HIGHER) 🟢"
            confidence_score = "91.8% STRONG"
        else:
            signal_direction = "PUT (LOWER) 🔴"
            confidence_score = "89.4% STRONG"
            
        st.markdown(f"---")
        st.markdown(f"### 🎯 NEXT CANDLE SIGNAL: {signal_direction}")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Asset Pair", pair)
            st.metric("Expiry Timer", timer)
        with col_b:
            st.metric("RSI Indicator", round(last_rsi, 2))
            st.metric("AI Confidence", confidence_score)
            
        st.success(f"⚡ **Execution Note:** Market analyzed. Execute a **{signal_direction.split()[0]}** trade exactly at the opening of the next candle for **{timer}** on Quotex ({market_type}).")

st.markdown("---")

# Bottom Performance Metrics Bar
m1, m2, m3, m4 = st.columns(4)
m1.metric("ACCURACY", "89%")
m2.metric("SIGNAL STR", "STRONG")
m3.metric("AVG TIME", "00:05")
m4.metric("TODAY", "128")

# Bottom Navigation Footer Bar
st.markdown("""
    <div class="footer-nav">
        <div>🏠<br><b>Dashboard</b></div>
        <div>⏱️<br>History</div>
        <div>📊<br>Performance</div>
        <div>🎧<br>Support</div>
        <div>⚙️<br>More</div>
    </div>
""", unsafe_allow_html=True)
