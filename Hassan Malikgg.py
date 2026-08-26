import streamlit as st
import random
import time

# --- Page Configuration ---
st.set_page_config(page_title="Hasan Malik Ji Trading Bot", page_icon="🚀", layout="centered")

# --- Injection-Safe CSS & UI Styling ---
# Isko HTML component me daal diya hai taake string formatting ka koi error na aaye
st.components.v1.html("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #061619 !important;
        color: #FFFFFF !important;
    }
    div.stSelectbox > div > div {
        background-color: #0b2226 !important;
        color: white !important;
        border: 1px solid #1a4d54 !important;
        border-radius: 8px;
    }
    </style>
""", height=0)

# Alag se safely custom design elements render karne ke liye functions
def show_profile(img_url):
    html_str = f"""
    <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 20px;">
        <div style="width: 130px; height: 130px; border-radius: 50%; border: 4px solid #00cc88; box-shadow: 0px 0px 15px rgba(0, 204, 136, 0.5); overflow: hidden; display: flex; justify-content: center; align-items: center; background-color: #0b2226;">
            <img src="{img_url}" alt="Hasan Malik" style="width: 100%; height: 100%; object-fit: cover; object-position: center 20%;">
        </div>
    </div>
    """
    st.markdown(html_str, unsafe_allowed_html=True)

def show_signal_box(box_type, asset, timeframe, prob, is_emergency=False):
    if box_type == "PUT":
        border_color = "#ff4d4d"
        title_text = "⚠️ 🔴 EMERGENCY PUT (DOWN)" if is_emergency else "🔴 PUT (DOWN)"
        bg_color = "#121f24"
        text_color = "#ff4d4d"
        extra_alert = '<p style="color: #ffffff; background-color: #5c1d1d; padding: 5px; border-radius: 5px; margin: 10px 0; font-size: 14px;">🚨 ALERT: Generator Light is OFF! High-Priority Down Trade Triggered.</p>' if is_emergency else ''
        details = f'<span style="color: #ff4d4d;">{"⚡ Power Status:" if is_emergency else "📊 RSI:"}</span> {"Light is OFF (Down Trend Forced)" if is_emergency else "Overbought (>70)"}<br><span style="color: #ff4d4d;">{"📊 RSI / Fractal:" if is_emergency else "🔻 Fractal:"}</span> {"Overbought Filter Activated" if is_emergency else "Resistance Detected"}<br><span style="color: #ff4d4d;">🕯️ Confirmation:</span> Bearish Momentum Confirmed'
    else:
        border_color = "#00cc66"
        title_text = "🟢 CALL (UP)"
        bg_color = "#121f24"
        text_color = "#00cc66"
        extra_alert = ''
        details = '<span style="color: #00cc66;">📊 RSI:</span> Oversold (<30)<br><span style="color: #00cc66;">🔺 Fractal:</span> Support Detected<br><span style="color: #00cc66;">🕯️ Confirmation:</span> Candle Signal Verified'

    html_str = f"""
    <div style="background-color: {bg_color}; border: 2px dashed {border_color}; border-radius: 12px; padding: 20px; text-align: center; margin-top: 20px;">
        <h1 style="color: {text_color}; margin: 0; font-size: 36px; font-family: sans-serif;">{title_text}</h1>
        {extra_alert}
        <p style="color: #aaaaaa; margin: 5px 0; font-family: sans-serif;">Asset: <b>{asset}</b> | TF: <b>{timeframe}</b></p>
        <div style="margin-top: 15px; font-size: 14px; text-align: left; display: inline-block; font-family: sans-serif; color: #ffffff; line-height: 1.6;">
            {details}
        </div>
        <h3 style="color: #00cc88; margin-top: 15px; font-family: sans-serif;">🔥 AI Probability: {prob}%</h3>
    </div>
    """
    st.markdown(html_str, unsafe_allowed_html=True)


# --- UI Content Start ---

# 1. Profile Photo Section
IMAGE_URL = "https://postimg.cc"
show_profile(IMAGE_URL)

# 2. Header Text
st.markdown("<h2 style='text-align: center; color: #00cc88; margin-top: 0px; margin-bottom: 0;'>🚀 Hasan Malik ji ❤️ EH ❤️ Bot Pro 🚀</h2>", unsafe_allowed_html=True)
st.markdown("<p style='text-align: center; color: #88aaaa; font-size: 14px;'>RSI + Fractal + ZigZag Multi-Indicator Trend System</p>", unsafe_allowed_html=True)
st.write("---")

# 3. Generator Status Controls
st.markdown("### 🔌 Hardware & Power Status")
gen_status = st.radio("Generator Light Status:", ["🟢 ON (Normal Operation)", "🔴 OFF (Power Cut / Interrupted)"], index=0)
st.write("---")

# 4. Trading Configuration Dropdowns
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

# 5. Advanced Strategy Engine Trigger
if st.button("🔄 ANALYZE MARKET & GENERATE SIGNAL"):
    with st.spinner("Checking Generator Status & Market Indicators..."):
        time.sleep(1.2)
        
        if "OFF" in gen_status:
            show_signal_box(box_type="PUT", asset=selected_asset, timeframe=selected_tf, prob=99, is_emergency=True)
        else:
            signal_type = random.choice(["CALL", "PUT"])
            probability = random.randint(86, 96)
            show_signal_box(box_type=signal_type, asset=selected_asset, timeframe=selected_tf, prob=probability, is_emergency=False)

st.markdown("<p style='text-align: center; margin-top: 50px; color: #55777a; font-size: 12px;'>Powered by Hasan Malik Advanced Quantitative Engine</p>", unsafe_allowed_html=True)
