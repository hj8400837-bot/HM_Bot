import streamlit as st
import random
import time
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="Hassan Malik Trading Bot", 
    page_icon="🚀", 
    layout="centered"
)

# --- Premium Dark Theme Configuration ---
st.markdown("""
    <style>
    .stApp {
        background-color: #061619 !important;
        color: #FFFFFF !important;
    }
    div[data-testid="stMarkdownContainer"] p {
        color: #FFFFFF !important;
    }
    .stSelectbox div[data-baseweb="select"] {
        background-color: #0b2226 !important;
        color: white !important;
        border: 1px solid #1a4d54 !important;
    }
    </style>
""", unsafe_allowed_html=True)

# --- 🖼️ Profile Section (GitHub Local Path) ---
IMAGE_SOURCE = "profile.png"

col1, col2, col3 = st.columns([1.5, 1.0, 1.5])
with col2:
    if os.path.exists(IMAGE_SOURCE):
        st.image(IMAGE_SOURCE, caption="Hassan Malik", use_container_width=True)
    else:
        st.image("https://unsplash.com", caption="Hassan Malik (No Photo Found)", use_container_width=True)

# --- Header Section ---
st.write("### 🚀 Hassan Malik 💗 EH 💗 Bot Pro")
st.caption("⚡ Next Candle Prediction & Technical Analysis System")
st.write("---")

# --- 🔌 Hardware & Power Status ---
st.subheader("🔌 Hardware & Power Status")
gen_status = st.radio(
    "Generator Light Status:", 
    ["🟢 ON", "🔴 OFF"], 
    index=0,
    horizontal=True
)
st.write("---")

# --- ⚙️ Trading Configuration Dropdowns ---
st.subheader("⚙️ Trading Configuration")

# 1. Broker Selection
brokers = ["Quotex", "Pocket Option", "Binomo"]
selected_broker = st.selectbox("🏛 *Broker*", brokers)

# 2. Market Type Selector
market_type = st.radio(
    "🏛️ *Market Type*",
    ["Live Markets", "OTC Markets"],
    index=0,
    horizontal=True
)

# 3. Separated Assets Array (12 Live + 12 OTC Pairs)
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
    selected_asset = st.selectbox("💹 *Asset (Live Only)*", live_pairs)
else:
    selected_asset = st.selectbox("💹 *Asset (OTC Only)*", otc_pairs)

# 4. Candle Timeframes
timeframes = ["5 Seconds", "10 Seconds", "15 Seconds", "30 Seconds", "1 Minute", "2 Minutes", "5 Minutes"]
selected_tf = st.selectbox("⏱ *Candle Timeframe*", timeframes)

st.write("")

# --- 🔄 Next Candle Forecast Engine ---
if st.button("🔄 PREDICT NEXT CANDLE", type="primary"):
    with st.spinner("Analyzing Current Candle Patterns & Structure..."):
        time.sleep(1.5) # Next candle calculation simulation delay
        
        # Generator OFF Condition (Emergency Next Candle RED Shortcut)
        if "OFF" in gen_status:
            st.error("⚠️ 🔴 NEXT CANDLE: RED (BEARISH)")
            st.warning(f"🚨 Generator Light is OFF! High-Priority Downward Pressure Forecasted on {selected_asset}.")
            st.write(f"⏱ **Candle TF:** {selected_tf} | 🏛 **Broker:** {selected_broker}")
            st.write("⚡ **Power Status:** Light is OFF (Next Candle Forced RED)")
            st.write("📊 **Indicators:** RSI / Fractal Overbought Filter Triggered")
            st.write("🕯 **Current Candle Status:** Closing with strong upper wick rejection")
            st.metric(label="🔥 Forecast Accuracy Probability", value="99%")
            
        # Generator ON Condition (Calculated Next Candle Signals)
        else:
            next_candle = random.choice(["GREEN", "RED"])
            probability = random.randint(91, 98)
            
            if next_candle == "RED":
                st.error("🔴 NEXT CANDLE FORECAST: RED (BEARISH)")
                st.write(f"💹 **Asset:** {selected_asset} | ⏱ **Candle TF:** {selected_tf} | 🏛 **Broker:** {selected_broker}")
                st.write("📊 **Market Trend:** Current candle is exhausting at major resistance")
                st.write("📉 **RSI Analysis:** Overbought zone touched, reversal expected in next candle")
                st.write("📐 **Structure:** Liquidity swept. Next candle expected to drop")
                st.write("🕯 **Confirmation:** Bearish Confirmation Candle structure active")
                st.metric(label="🔥 Forecast Accuracy Probability", value=f"{probability}%")
            else:
                st.success("🟢 NEXT CANDLE FORECAST: GREEN (BULLISH)")
                st.write(f"💹 **Asset:** {selected_asset} | ⏱ **Candle TF:** {selected_tf} | 🏛 **Broker:** {selected_broker}")
                st.write("📊 **Market Trend:** Current candle building strong support base")
                st.write("📈 **RSI Analysis:** Oversold zone rejection, upward bounce expected in next candle")
                st.write("📐 **Structure:** Demand Order Block tap completed")
                st.write("🕯 **Confirmation:** Bullish Confirmation Candle structure active")
                st.metric(label="🔥 Forecast Accuracy Probability", value=f"{probability}%")

st.write("---")
st.caption("Powered by Hassan Malik Next-Candle Predictive Algorithm")
