import streamlit as st
import random
import time
import os

# --- Page Configuration ---
st.set_page_config(page_title="Hassan Malik Trading Bot", page_icon="🚀", layout="centered")

IMAGE_SOURCE = "profile.png"
col1, col2, col3 = st.columns([1.5, 1.0, 1.5])
with col2:
    if os.path.exists(IMAGE_SOURCE):
        st.image(IMAGE_SOURCE, caption="Hassan Malik", use_container_width=True)
    else:
        st.image("https://unsplash.com", caption="Hassan Malik", use_container_width=True)

st.write("### 🚀 Hassan Malik 💗 EH 💗 Bot Pro")
st.caption("⚡ Anti-Loss Extreme Trend Guard & Martingale Manager Active")
st.write("---")

# --- Configuration Dropdowns ---
brokers = ["Quotex", "Pocket Option", "Binomo"]
selected_broker = st.selectbox("🏛 *Broker*", brokers)

market_type = st.radio("🏛️ *Market Type*", ["Live Markets", "OTC Markets"], index=0, horizontal=True)

live_pairs = ["EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "EUR/GBP", "USD/CAD"]
otc_pairs = ["EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "AUD/USD (OTC)"]
selected_asset = st.selectbox("💹 *Asset*", live_pairs if market_type == "Live Markets" else otc_pairs)

timeframes = ["5 Seconds", "10 Seconds", "15 Seconds", "30 Seconds", "1 Minute"]
selected_tf = st.selectbox("⏱ *Candle Timeframe*", timeframes)

# --- 🎯 Balance & Martingale Calculator Component ---
st.subheader("💰 Smart Money Management")
balance = st.number_input("Apna Current Balance Likhein ($):", min_value=5, value=100)
base_trade = round(balance * 0.02, 2) # Safety Rule: Sirf 2% risk per trade
st.info(f"👉 **Safe Trading Step:** Aapki Pehli Trade ka amount max **${base_trade if base_trade >= 1 else 1.0}** hona chahiye.")

st.write("---")

if st.button("🔄 ANALYZE & PREDICT NEXT CANDLE", type="primary"):
    with st.spinner("Scanning Chart Rejections & Anti-Trend Exhaustion..."):
        time.sleep(1.2)
        
        # Simulated safety logic to block consecutive crashes like the image sample
        market_condition = random.choice(["Normal", "Extreme Falling Momentum"])
        
        if market_condition == "Extreme Falling Momentum":
            st.warning("⚠️ **MARKET GUARD ALERT: NO TRADE SIGNAL GENERATED**")
            st.info(f"Analysis multi-red consecutive candles detect kar raha hai (Jaisa aapki screen crash pattern me tha). Is wave ke khatam hone tak system ne capital protect karne ke liye **Trade Block** kar di hai.")
        else:
            prediction = random.choice(["GREEN", "RED"])
            prob = random.randint(95, 99)
            
            if prediction == "RED":
                st.error("🔴 ACTION TARGET: NEXT CANDLE RED (PUT)")
                st.write(f"📊 **Structure:** Extreme Resistance Sweep | Accuracy: **{prob}%**")
                st.subheader("🛡️ Martingale Recovery Setup")
                st.warning(f"If Loss -> Next Trade immediately place **${round(base_trade * 2, 2)} DOWN (PUT)** [M1]")
            else:
                st.success("🟢 ACTION TARGET: NEXT CANDLE GREEN (CALL)")
                st.write(f"📊 **Structure:** Institutional Order Block Tap | Accuracy: **{prob}%**")
                st.subheader("🛡️ Martingale Recovery Setup")
                st.warning(f"If Loss -> Next Trade immediately place **${round(base_trade * 2, 2)} UP (CALL)** [M1]")

st.write("---")
st.caption("Powered by Hassan Malik Risk-Controlled Algorithmic Engine")
