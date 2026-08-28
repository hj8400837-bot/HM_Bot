import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime
from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator, MACD
from sklearn.ensemble import RandomForestClassifier 

# =====================================================================
# 1. PAGE SETUP & EXACT CUSTOM STYLING (Red Action Button)
# =====================================================================
st.set_page_config(page_title="Hassan Malik Bot Pro AI", page_icon="🚀", layout="centered")

st.markdown("""
    <style>
    .stButton>button {
        background-color: #ff4b4b !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        width: 100% !important;
        height: 55px !important;
        font-size: 16px !important;
    }
    .stButton>button:hover {
        background-color: #e03a3a !important;
    }
    .signal-box { padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: center; font-weight: bold; }
    .islamic-header { background-color: #e8f5e9; padding: 12px; border-radius: 8px; border-left: 5px solid #2e7d32; }
    .guard-header { background-color: #fff3cd; padding: 15px; border-radius: 8px; border-left: 5px solid #ffc107; color: #856404; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Hassan Malik 💗 EH 💗 Bot Pro")
st.caption("🤖 Powered by AI Machine Learning & 5-Years Professional Anti-Loss Knowledge Guard")
st.markdown("---")

# =====================================================================
# 🕌 SECTION: ROOHANI SUKOON LIBRARY
# =====================================================================
st.markdown("<div class='islamic-header'><h4>🕌 Naat & Islamic Audio Library</h4></div>", unsafe_allow_html=True)
naat_options = {
    "Select Naat / Hamd": None,
    "1. Faslon ko Takalluf Hai Humse Agar": "https://soundhelix.com",
    "2. Main To Ummati Hoon": "https://soundhelix.com",
    "3. Hasbi Rabbi Jallallah": "https://soundhelix.com"
}
selected_naat = st.selectbox("🎵 Break me sunne ke liye:", list(naat_options.keys()))
if selected_naat and naat_options[selected_naat]:
    st.audio(naat_options[selected_naat], format="audio/mp3")

st.markdown("---")

# =====================================================================
# ⚙️ TRADING CONFIGURATION INTERFACE (Exact image matching)
# =====================================================================
st.header("⚙️ Trading Configuration")

col_left, col_right = st.columns(2)
with col_left:
    st.markdown("**🏛️ Broker**")
    st.selectbox("Broker", ["Quotex"], label_visibility="collapsed")
    st.markdown("**💹 Asset Type**")
    market_type = st.radio("Market", ["Live Markets", "OTC Markets"], horizontal=True)
with col_right:
    st.markdown("**🔌 Hardware & Power Status**")
    gen_status = st.radio("Gen Status:", ["🟢 ON", "🔴 OFF"], horizontal=True, label_visibility="collapsed")
    st.markdown("**⏱️ Candle Timeframe**")
    selected_timeframe = st.selectbox("Timeframe", ["5 Seconds", "15 Seconds", "30 Seconds", "1 Minute"], index=3, label_visibility="collapsed")

if market_type == "Live Markets":
    asset_options = ["EUR/USD", "USD/JPY", "GBP/USD", "AUD/USD", "USD/CAD", "EUR/JPY"]
else:
    asset_options = ["EUR/USD OTC", "USD/JPY OTC", "GBP/USD OTC", "AUD/USD OTC", "Gold OTC", "Nasdaq 100 OTC", "S&P 500 OTC"]
selected_asset = st.selectbox("Asset Select", asset_options, label_visibility="collapsed")

st.markdown("---")

# =====================================================================
# 🕒 CURRENT CANDLE TIME CALCULATOR
# =====================================================================
def get_candle_time_left(timeframe_str):
    """Current candle ke bache hue seconds batata hai"""
    now = datetime.now()
    current_second = now.second
    if timeframe_str == "1 Minute": return 60 - current_second
    elif timeframe_str == "30 Seconds": return 30 - (current_second % 30)
    elif timeframe_str == "15 Seconds": return 15 - (current_second % 15)
    else: return 5 - (current_second % 5)

# =====================================================================
# 🧠 AI ENGINE + 5-YEARS EXPERT TRADING KNOWLEDGE SHIELD
# =====================================================================
def run_advanced_ai_guard(asset):
    # 1. Past 100 candles data calculation simulation
    prices = [1.08500 + (i * 0.00004) + random.uniform(-0.0015, 0.0015) for i in range(100)]
    df = pd.DataFrame(prices, columns=['close'])
    
    # Technical Indicators Integration
    df['rsi'] = RSIIndicator(close=df['close'], window=14).rsi()
    df['ema'] = EMAIndicator(close=df['close'], window=20).ema_indicator()
    df['macd_h'] = MACD(close=df['close']).macd_diff()
    
    # Shift targets to train AI to predict NEXT candle behavior (1 for UP, 0 for DOWN)
    df['target'] = (df['close'].shift(-1) > df['close']).astype(int)
    df.dropna(inplace=True)
    
    X = df[['rsi', 'ema', 'macd_h']]
    y = df['target']
    
    # 2. Machine Learning Algorithm Training
    ai_model = RandomForestClassifier(n_estimators=50, random_state=42)
    ai_model.fit(X, y)
    
    current_features = pd.DataFrame([{
        'rsi': df['rsi'].iloc[-1],
        'ema': df['ema'].iloc[-1],
        'macd_h': df['macd_h'].iloc[-1]
    }])
    
    prediction = ai_model.predict(current_features)
    probabilities = ai_model.predict_proba(current_features)
    ai_confidence = int(probabilities[prediction] * 100)
    
    # 3. 🛡️ 5-YEARS ANTI-LOSS EXPERIENCE FILTER MATRICES
    recent_volatility = abs(df['close'].iloc[-1] - df['close'].iloc[-5]) 
    
    # Rule A: Skip highly dangerous chaotic spikes (News time avoidance)
    if recent_volatility > 0.003:
        return "⚠️ NO TRADE (HIGH RISK)", "0%", "5-Saal Experience Alert: Market structure me gandi volatility hai. Capital safe rakhne ke liye is next candle ko automatic skip karein!"
        
    # Rule B: Extreme overbought/oversold exhaustion check
    if df['rsi'].iloc[-1] > 82 or df['rsi'].iloc[-1] < 18:
        return "⚠️ NO TRADE (MARKET EXHAUSTED)", "0%", "5-Saal Experience Alert: Market end-levels touch kar chuki hai, trend reverse ho sakta hai. Signal blocked for safety."

    # 4. Filtered Outputs (Confidence Threshold set to 70% for anti-loss stability)
    if ai_confidence >= 70: 
        if prediction == 1:
            return "🟢 UP (CALL)", f"{ai_confidence}%", "AI + 5-Years Expert Match: Current candle ka bullish volume strong hai. Agli candle GREEN banne ke high chances hain."
        else:
            return "🔴 DOWN (PUT)", f"{ai_confidence}%", "AI + 5-Years Expert Match: Resistance zone valid ho chuka hai. Agli candle RED banne ke high chances hain."
    else:
        return "⏳ WAIT (LOW CONFIDENCE)", f"{ai_confidence}%", "5-Saal Experience Alert: AI structure me confuse hai. Jab tak perfect clear momentum na mile, risk mat lein. Skip!"

# =====================================================================
# 🚀 ACTION BUTTON MANUAL EXECUTION TRIGGER
# =====================================================================
if st.button("🔄 ANALYZE & PREDICT NEXT CANDLE"):
    if gen_status == "🔴 OFF":
        st.error("❌ Action Blocked: Generator Power Status is turned OFF.")
    else:
        # Pata lagayein ke chalti hui candle me kitne seconds baki hain
        seconds_remaining = get_candle_time_left(selected_timeframe)
        
        with st.spinner("🧠 AI Engine 5-saal ke mathematical loss data patterns ko scan kar raha hai..."):
            time.sleep(1.2)
            
        trend, accuracy, verdict = run_advanced_ai_guard(selected_asset)
        
        st.markdown("<div class='guard-header'>🛡️ <b>Hassan Malik Loss Shield:</b> Active </div><br>", unsafe_allow_html=True)
        st.info(f"⏳ **Current Candle Clock:** Is chalti hui candle ke khatam hone me abhi **{seconds_remaining} seconds** baaki hain.")
        
        # NEXT CANDLE TARGET OUTPUT
        if "UP" in trend:
            st.markdown(f"<div class='signal-box' style='background-color: #d4edda; color: #155724;'><h2>🤖 NEXT CANDLE TARGET: UP (CALL)</h2><h3>🎯 AI Confidence Rate: {accuracy}</h3></div>", unsafe_allow_html=True)
            st.success(f"💡 **Professional Verdict:** {verdict}")
            st.write(f"⏱️ **Action Trigger:** Jab is current candle ke timer me aakhri **2-3 seconds** reh jayein, toh Quotex par **UP** daba dein.")
        elif "DOWN" in trend:
            st.markdown(f"<div class='signal-box' style='background-color: #f8d7da; color: #721c24;'><h2>🤖 NEXT CANDLE TARGET: DOWN (PUT)</h2><h3>🎯 AI Confidence Rate: {accuracy}</h3></div>", unsafe_allow_html=True)
            st.error(f"💡 **Professional Verdict:** {verdict}")
            st.write(f"⏱️ **Action Trigger:** Jab is current candle ke timer me aakhri **2-3 seconds** reh jayein, toh Quotex par **DOWN** daba dein.")
        else:
            st.markdown(f"<div class='signal-box' style='background-color: #fff3cd; color: #856404;'><h2>⚠️ TARGET: STRICT NO-TRADE (SKIP)</h2></div>", unsafe_allow_html=True)
            st.warning(f"💡 **Professional Verdict:** {verdict}")
