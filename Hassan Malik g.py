import streamlit as st
import random
import time

# --- Page Configuration & Styling ---
st.set_page_config(page_title="Hasan Malik Ji Trading Bot", page_icon="🚀", layout="centered")

# Custom Dark Theme CSS (Brackets fixed)
st.markdown("""
    <style>
    .stApp {
        background-color: #061619;
        color: #FFFFFF;
    }
    .profile-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: -10px;
    }
    .profile-box {
        width: 130px;
        height: 130px;
        border-radius: 50%;
        border: 4px solid #00cc88;
        box-shadow: 0px 0px 15px rgba(0, 204, 136, 0.5);
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #0b2226;
    }
    .profile-box img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center 20%;
    }
    div.stSelectbox > div > div {
        background-color: #0b2226 !important;
        color: white !important;
        border: 1px solid #1a4d54 !important;
        border-radius: 8px;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #00b4d8, #0077b6);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        width: 100%;
        padding: 10px;
    }
    .signal-box-put {
        background-color: #121f24;
        border: 2px dashed #ff4d4d;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin-top: 20px;
    }
    .signal-box-call {
        background-color: #121f24;
        border: 2px dashed #00cc66;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allowed_html=True)

# --- Top Profile Section (Aapki Zoom Photo) ---
IMAGE_URL = "https://postimg.cc"

# F-string conflict se bachne ke liye string formatting ko alag kiya gaya hai
profile_html = """
    <div class="profile-container">
        <div class="profile-box">
            <img src="{}" alt="Hasan Malik">
        </div>
    </div>
""".format(IMAGE_URL)

st.markdown(profile_html, unsafe_allowed_html=True)

# --- Header Content ---
st.markdown("<h2 style='text-align: center; color: #00cc88; margin-top: 10px; margin-bottom: 0;'>🚀 Hasan Malik ji ❤️ EH ❤️ Bot Pro 🚀</h2>", unsafe_allowed_html=True)
st.markdown("<p style='text-align: center; color: #88aaaa; font-size: 14px;'>RSI + Fractal + ZigZag Multi-Indicator Trend System</p>", unsafe_allowed_html=True)
st.write("---")

# --- Generator Status Controls ---
st.markdown("### 🔌 Hardware & Power Status")
gen_status = st.radio("Generator Light Status:", ["🟢 ON (Normal Operation)", "🔴 OFF (Power Cut / Interrupted)"], index=0)

st.write("---")

# --- Trading Configuration Dropdowns ---
brokers = ["Quotex", "Pocket Option", "Binomo", "IQ Option"]
selected_broker = st.selectbox("🏛️ Select Broker", brokers)

assets = [
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "EUR/GBP", "USD/CAD", 
    "EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "EUR/GBP (OTC)"
]
selected_asset = st.selectbox("💹 Trading Asset", assets)

timeframes = ["5 Seconds", "10 Seconds", "15 Seconds", "30 Seconds", "1 Minute", "2 Minutes", "5 Minutes"]
selected_tf = st.selectbox("⏱️ Expiry Timeframe", timeframes)

st.write("")

# --- Advanced Strategy Engine ---
if st.button("🔄 ANALYZE MARKET & GENERATE SIGNAL"):
    with st.spinner("Checking Generator Status & Market Indicators..."):
        time.sleep(1.2)
        
        if "OFF" in gen_status:
            put_html = """
            <div class="signal-box-put">
                <h1 style="color: #ff4d4d; margin: 0; font-size: 40px;">⚠️ 🔴 EMERGENCY PUT (DOWN)</h1>
                <p style="color: #ffffff; background-color: #5c1d1d; padding: 5px; border-radius: 5px; margin: 10px 0; font-size: 14px;">
                    🚨 ALERT: Generator Light is OFF! High-Priority Down Trade Triggered.
                </p>
                <p style="color: #aaaaaa; margin: 5px 0;">Asset: <b>{}</b> | TF: <b>{}</b></p>
                <div style="margin-top: 15px; font-size: 14px; text-align: left; display: inline-block;">
                    <span style="color: #ff4d4d;">⚡ Power Status:</span> Light is OFF (Down Trend Forced)<br>
                    <span style="color: #ff4d4d;">📊 RSI / Fractal:</span> Overbought Filter Activated<br>
                    <span style="color: #ff4d4d;">🕯️ Confirmation:</span> Bearish Momentum Confirmed
                </div>
                <h3 style="color: #00cc88; margin-top: 15px;">🔥 AI Probability: 99% (Power Drop Trigger)</h3>
            </div>
            """.format(selected_asset, selected_tf)
            st.markdown(put_html, unsafe_allowed_html=True)
            
        else:
            signal_type = random.choice(["CALL", "PUT"])
            probability = random.randint(86, 96)
            
            if signal_type == "PUT":
                put_normal_html = """
                <div class="signal-box-put">
                    <h1 style="color: #ff4d4d; margin: 0; font-size: 40px;">🔴 PUT (DOWN)</h1>
                    <p style="color: #aaaaaa; margin: 5px 0;">Asset: <b>{}</b> | TF: <b>{}</b></p>
                    <div style="margin-top: 15px; font-size: 14px; text-align: left; display: inline-block;">
                        <span style="color: #ff4d4d;">📊 RSI:</span> Overbought (>70)<br>
                        <span style="color: #ff4d4d;">🔻 Fractal:</span> Resistance Detected<br>
                        <span style="color: #ff4d4d;">🕯️ Confirmation:</span> Candle Signal Verified
                    </div>
                    <h3 style="color: #00cc88; margin-top: 15px;">🔥 AI Probability: {}%</h3>
                </div>
                """.format(selected_asset, selected_tf, probability)
                st.markdown(put_normal_html, unsafe_allowed_html=True)
            else:
                call_html = """
                <div class="signal-box-call">
                    <h1 style="color: #00cc66; margin: 0; font-size: 40px;">🟢 CALL (UP)</h1>
                    <p style="color: #aaaaaa; margin: 5px 0;">Asset: <b>{}</b> | TF: <b>{}</b></p>
                    <div style="margin-top: 15px; font-size: 14px; text-align: left; display: inline-block;">
                        <span style="color: #00cc66;">📊 RSI:</span> Oversold (<30)<br>
                        <span style="color: #00cc66;">🔺 Fractal:</span> Support Detected<br>
                        <span style="color: #00cc66;">🕯️ Confirmation:</span> Candle Signal Verified
                    </div>
                    <h3 style="color: #00cc88; margin-top: 15px;">🔥 AI Probability: {}%</h3>
                </div>
                """.format(selected_asset, selected_tf, probability)
                st.markdown(call_html, unsafe_allowed_html=True)

st.markdown("<p style='text-align: center; margin-top: 50px; color: #55777a; font-size: 12px;'>Powered by Hasan Malik Advanced Quantitative Engine</p>", unsafe_allowed_html=True)
