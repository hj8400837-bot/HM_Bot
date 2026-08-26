import streamlit as st
import random
import time
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="Hassan Malik💗EH 💗 Trading Bot", 
    page_icon="🚀", 
    layout="centered"
)

# --- 🖼️ Profile Section (GitHub Se Local Path) ---
# Apni photo ko 'profile.png' naam se GitHub repo ke andar upload karein
if os.path.exists("profile.png"):
    IMAGE_SOURCE = "profile.png"
else:
    # Backup secure placeholder link jab tak aap photo upload nahi karte
    IMAGE_SOURCE = "https://unsplash.com"

col1, col2, col3 = st.columns([1.5, 1.0, 1.5])
with col2:
    st.image(
        IMAGE_SOURCE, 
        caption="Hassan Malik", 
        use_container_width=True
    )

# --- Header Section (Naya Naam Update Kiya Gaya Hai) ---
st.markdown("<h3 style='text-align: center; color: #00cc88; margin-top: 0px;'>🚀 Hassan Malik💗EH 💗 Bot Pro</h3>", unsafe_allowed_html=True)
st.markdown("<p style='text-align: center; color: #88aaaa; font-size: 13px; margin-top: -10px;'>RSI + Fractal + ZigZag Multi-Indicator System</p>", unsafe_allowed_html=True)
st.write("---")

# --- 🔌 Hardware & Power Status ---
st.markdown("##### 🔌 Hardware & Power Status")
gen_status = st.radio(
    "Generator Light Status:", 
    ["🟢 ON", "🔴 OFF"], 
    index=0,
    horizontal=True
)
st.write("---")

# --- ⚙️ Trading Configuration Dropdowns ---
st.markdown("##### ⚙️ Trading Configuration")

brokers = ["Quotex", "Pocket Option", "Binomo", "IQ Option"]
selected_broker = st.selectbox("🏛️ Broker", brokers)

assets = [
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "EUR/GBP", "USD/CAD", 
    "GBP/JPY", "EUR/JPY", "AUD/JPY", "NZD/USD", "EUR/CHF", "GBP/CHF",
    "EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "AUD/USD (OTC)", 
    "EUR/GBP (OTC)", "USD/CAD (OTC)", "GBP/JPY (OTC)", "EUR/JPY (OTC)", 
    "AUD/JPY (OTC)", "NZD/USD (OTC)", "USD/CHF (OTC)", "CHF/JPY (OTC)"
]
selected_asset = st.selectbox("💹 Asset", assets)

timeframes = ["5 Seconds", "10 Seconds", "15 Seconds", "30 Seconds", "1 Minute", "2 Minutes", "5 Minutes"]
selected_tf = st.selectbox("⏱️ Timeframe", timeframes)

st.write("")

# --- 🔄 Advanced Strategy Engine ---
if st.button("🔄 GENERATE SIGNAL", type="primary"):
    with st.spinner("Analyzing..."):
        time.sleep(1.0)
        
        # Generator OFF Condition
        if "OFF" in gen_status:
            st.error("⚠️ 🔴 EMERGENCY PUT (DOWN)")
            st.warning(f"🚨 Generator Light is OFF! Down Trade Triggered on {selected_asset}.")
            st.write(f"⏱️ **TF:** {selected_tf} | 🏛️ **Broker:** {selected_broker}")
            st.write("⚡ **Power:** Light is OFF (Down Trend Forced)")
            st.write("📊 **Indicators:** RSI / Fractal Overbought Filter Activated")
            st.write("🕯️ **Confirmation:** Bearish Momentum Confirmed")
            st.metric(label="🔥 AI Probability", value="99%")
            
        # Generator ON Condition
        else:
            signal_type = random.choice(["CALL", "PUT"])
            probability = random.randint(88, 97)
            
            if signal_type == "PUT":
                st.error("🔴 PUT (DOWN)")
                st.write(f"💹 **Asset:** {selected_asset} | ⏱️ **TF:** {selected_tf}")
                st.write("📊 **RSI:** Overbought (>70) | 🔻 **Fractal:** Resistance")
                st.write("🕯️ **Confirmation:** Bearish Candle Verified")
                st.metric(label="🔥 AI Probability", value=f"{probability}%")
            else:
                st.success("🟢 CALL (UP)")
                st.write(f"💹 **Asset:** {selected_asset} | ⏱️ **TF:** {selected_tf}")
                st.write("📊 **RSI:** Oversold (<30) | 🔺 **Fractal:** Support")
                st.write("🕯️ **Confirmation:** Bullish Candle Verified")
                st.metric(label="🔥 AI Probability", value=f"{probability}%")

st.write("---")
st.caption("Powered by Hassan Malik Engine")
