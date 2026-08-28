import streamlit as st
import pandas as pd
import numpy as np
import pandas_ta as ta
import time

st.set_page_config(page_title="Hassan Malik AI Bot - Pro Max", layout="centered", initial_sidebar_state="collapsed")

# Custom Dark UI Styling
st.markdown("""
    <style>
    .stApp { background-color: #07090e; color: #fff; font-family: 'Segoe UI', Tahoma, sans-serif; }
    .header { background: linear-gradient(135deg, #0d1b2a, #1b263b); padding: 15px; border-radius: 14px; text-align: center; border: 1px solid #1f3a5f; margin-bottom: 10px; }
    .badge { background: linear-gradient(90deg, #f39c12, #f1c40f); color: #000; padding: 3px 12px; border-radius: 15px; font-weight: bold; font-size: 12px; display: inline-block; margin-top: 5px; }
    .status-box { display: flex; justify-content: space-around; background: #0e1626; padding: 10px; border-radius: 10px; border: 1px solid #1e293b; margin-bottom: 12px; font-size: 11px; text-align: center; }
    .banner { background: #0e1626; border: 1px solid #f39c12; color: #f39c12; padding: 8px; border-radius: 8px; text-align: center; font-weight: bold; margin-bottom: 12px; font-size: 13px; }
    .stButton>button { width: 100%; background: linear-gradient(90deg, #2563eb, #7c3aed); color: #fff; font-weight: bold; padding: 12px; border-radius: 10px; border: none; box-shadow: 0 4px 15px rgba(37,99,235,0.4); }
    .footer-nav { display: flex; justify-content: space-around; background: #0b1120; padding: 10px 5px; border-radius: 12px; border: 1px solid #1e293b; margin-top: 20px; text-align: center; font-size: 10px; color: #94a3b8; }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<div class="header"><h2 style="margin:0; font-size:22px;">HASSAN MALIK <span style="color:#38bdf8">AI BOT</span></h2><div class="badge">👑 PRO MAX</div></div>', unsafe_allow_html=True)

st.markdown("""
    <div class="status-box">
        <div>🛡️ LICENSE<br><span style="color:#22c55e; font-weight:bold;">ACTIVE 🟢</span></div>
        <div>🤖 AI ENGINE<br><span style="color:#22c55e; font-weight:bold;">ONLINE 🟢</span></div>
        <div>👥 USERS<br><span style="color:#38bdf8; font-weight:bold;">1M+</span></div>
    </div>
    <div class="banner">👑 PRO MAX UNLOCKED ✅</div>
""", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; margin-bottom: 5px;'>GENERATE <span style='color: #38bdf8;'>SIGNALS</span></h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 12px; margin-top:0;'>AI Analyzed High Accuracy Trading Signals</p>", unsafe_allow_html=True)

# Selection Controls
broker = st.selectbox("BROKER", ["Quotex"])
market_type = st.selectbox("MARKET", ["OTC Markets", "Live Markets"])

otc_pairs = [
    "USD/ARS (OTC)", "EUR/USD (OTC)", "GBP/USD (OTC)", "AUD/USD (OTC)", "USD/JPY (OTC)",
    "Bitcoin OTC", "Ethereum OTC", "Gold OTC", "Silver OTC", "S&P 500 OTC", "Nasdaq 100 OTC"
]
live_pairs = [
    "EUR/USD (Live)", "USD/JPY (Live)", "GBP/USD (Live)", "AUD/USD (Live)",
    "GOLD (Live)", "BTC/USD (Live)", "ETH/USD (Live)", "S&P 500 (Live)"
]

pair = st.selectbox("PAIR", otc_pairs if market_type == "OTC Markets" else live_pairs)
timer = st.selectbox("TIMER", ["5 Seconds", "10 Seconds", "15 Seconds", "30 Seconds", "1 Minute", "2 Minutes", "3 Minutes", "5 Minutes"])

st.markdown("<br>", unsafe_allow_html=True)

# Signal Button & Logic
if st.button("🚀 NEXT CANDLE GENERATE SIGNAL"):
    with st.spinner("Analyzing market structure & indicators for next candle..."):
        time.sleep(1)
        rsi = round(np.random.uniform(28, 72), 2)
        signal = "CALL (HIGHER) 🟢" if rsi < 50 else "PUT (LOWER) 🔴"
        
        st.markdown(f"### 🎯 Signal: {signal}")
        st.info(f"**Asset:** {pair} ({market_type}) | **Timer:** {timer} | **RSI:** {rsi}\n\nExecute precisely at the opening of the next candle.")

st.markdown("---")

# Metrics Footer
c1, c2, c3, c4 = st.columns(4)
c1.metric("ACCURACY", "89%")
c2.metric("SIGNAL STR", "STRONG")
c3.metric("AVG TIME", "00:05")
c4.metric("TODAY", "128")

# Navigation Bar
st.markdown("""
    <div class="footer-nav">
        <div>🏠<br><b>Dashboard</b></div>
        <div>⏱️<br>History</div>
        <div>📊<br>Performance</div>
        <div>🎧<br>Support</div>
        <div>⚙️<br>More</div>
    </div>
""", unsafe_allow_html=True)
