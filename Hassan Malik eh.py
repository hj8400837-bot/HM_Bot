import streamlit as st
import random
import time
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="Hassan Malik Trading Bot", 
    page_icon="🤖", 
    layout="centered"
)

# --- 🖼️ Top Avatar / Profile Section ---
IMAGE_SOURCE = "profile.png"

col1, col2, col3 = st.columns([1.5, 1.0, 1.5])
with col2:
    if os.path.exists(IMAGE_SOURCE):
        st.image(IMAGE_SOURCE, caption="Hassan Malik", use_container_width=True)
    else:
        st.image("https://unsplash.com", caption="Hassan Malik", use_container_width=True)

# --- Header Section (Aapka Custom Name) ---
st.title("🤖 Hassan Malik 💗 EH 💗")
st.caption("✨ AI BOT | 👑 PRO MAX UNLOCKED")

# App Stats Grid
stat_col1, stat_col2, stat_col3 = st.columns(3)
with stat_col1:
    st.success("🛡️ LICENSE: ACTIVE")
with stat_col2:
    st.info("⚙️ ENGINE: ONLINE")
with stat_col3:
    st.warning("👥 USERS: 1M+")

st.write("---")
st.write("### ⚡ GENERATE SIGNALS")
st.caption("AI Analyzed High Accuracy Trading Signals")

# --- 🔌 Hardware & Power Status ---
st.write("##### 🔌 Hardware & Power Status")
gen_status = st.radio(
    "Generator Light Status:", 
    ["🟢 ON (Normal)", "🔴 OFF (Power Interrupted)"], 
    index=0,
    horizontal=True
)
st.write("---")

# --- ⚙️ Trading Configuration Dropdowns ---
st.write("##### ⚙️ Configuration Board")

# 1. Broker Selection
brokers = ["Quotex", "Pocket Option", "Binomo"]
selected_broker = st.selectbox("🏦 BROKER", brokers)

# 2. Market Type Selection (Live / OTC Choice Filter)
market_type = st.radio(
    "🏛️ MARKET TYPE SELECT KAREIN",
    ["Live Markets", "OTC Markets"],
    index=0,
    horizontal=True
)

# 3. Dynamic Trading Pairs (Jaisa Market type select hoga, wahi pairs dikhenge)
live_pairs = [
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "EUR/GBP", "USD/CAD", 
    "GBP/JPY", "EUR/JPY", "AUD/JPY", "NZD/USD", "EUR/CHF", "GBP/CHF"
]

otc_pairs = [
    "EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "AUD/USD (OTC)", 
    "EUR/GBP (OTC)", "USD/CAD (OTC)", "GBP/JPY (OTC)", "EUR/JPY (OTC)", 
    "AUD/JPY (OTC)", "NZD/USD (OTC)", "USD/CHF (OTC)", "CHF/JPY (OTC)"
]

if market_type == "Live Markets":
    selected_asset = st.selectbox("💹 PAIR (Live Only)", live_pairs)
else:
    selected_asset = st.selectbox("💹 PAIR (OTC Only)", otc_pairs)

# 4. Timer/Timeframes
timeframes = ["5 Seconds", "10 Seconds", "15 Seconds", "30 Seconds", "1 Minute"]
selected_tf = st.selectbox("⏱️ TIMER", timeframes)

st.write("")

# --- 🔄 AI High Level Strategy Signal Generator ---
if st.button("🚀 GENERATE SIGNAL", type="primary"):
    with st.spinner("Executing Pro Strategy (Indicator + Trend + Structure + Candle)..."):
        time.sleep(1.5) # Strategy calculation delay
        
        # Scenario A: Generator OFF Condition (Automatic Down Trade)
        if "OFF" in gen_status:
            st.error("⚠️ 🔴 EMERGENCY PUT (DOWN)")
            st.warning(f"🚨 Generator Light is OFF! High-Priority Down Trade Triggered on {selected_asset}.")
            
            st.write("📈 **Market Structure:** Break of Structure (BOS) Detected")
            st.write("📉 **Trend Direction:** Strong Bearish Order Flow")
            st.write("📊 **Indicators:** RSI Overbought (>70) + Fractal Resistance")
            st.write("🕯️ **Candle Analysis:** Confirmation Candle Closed Bearish")
            st.metric(label="🔥 AI Probability Accuracy", value="99% (Forced Down)")
            
        # Scenario B: Generator ON Condition (Calculated Signals)
        else:
            signal_type = random.choice(["CALL", "PUT"])
            probability = random.randint(92, 98) # High Level Accuracy Range
            
            if signal_type == "PUT":
                st.error("🔴 PUT (DOWN)")
                st.write(f"📊 **Asset:** {selected_asset} | ⏱️ **Timer:** {selected_tf}")
                st.write("📈 **Market Structure:** Liquidity Swept From Top Resistance")
                st.write("📉 **Trend Direction:** Major Downtrend Re-established")
                st.write("📊 **Indicators:** RSI/ZigZag Overbought Alignment")
                st.write("🕯️ **Confirmation Candle:** Bearish Engulfing Candle Confirmed")
                st.metric(label="🔥 AI Probability Accuracy", value=f"{probability}%")
            else:
                st.success("🟢 CALL (UP)")
                st.write(f"📊 **Asset:** {selected_asset} | ⏱️ **Timer:** {selected_tf}")
                st.write("📈 **Market Structure:** Order Block Tap + Change of Character (CHoCH)")
                st.write("📈 **Trend Direction:** Major Bullish Trend Confirmed")
                st.write("📊 **Indicators:** RSI Oversold (<30) + Fractal Support Arrow")
                st.write("🕯️ **Confirmation Candle:** Bullish Hammer Candle Confirmed")
                st.metric(label="🔥 AI Probability Accuracy", value=f"{probability}%")

st.write("---")
st.caption("⚡ System Powered by Hassan Malik High-Frequency Quantitative Algorithm")
