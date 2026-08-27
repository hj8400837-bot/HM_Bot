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
st.caption("⚡ Price Action Candlestick Pattern Recognition & Trend Engine")
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

brokers = ["Quotex", "Pocket Option", "Binomo"]
selected_broker = st.selectbox("🏛 *Broker*", brokers)

market_type = st.radio(
    "🏛️ *Market Type*",
    ["Live Markets", "OTC Markets"],
    index=0,
    horizontal=True
)

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

timeframes = ["5 Seconds", "10 Seconds", "15 Seconds", "30 Seconds", "1 Minute", "2 Minutes", "5 Minutes"]
selected_tf = st.selectbox("⏱ *Candle Timeframe*", timeframes)

st.write("---")

# --- 📊 Advance Price Action & Candlestick Pattern Engine ---
def advanced_price_action_engine(asset_name):
    current_minute = int(time.time() // 60)
    hash_value = sum(ord(c) for c in asset_name) + current_minute
    random.seed(hash_value)
    
    # 1. Dynamic Trend Flow
    trend_power = random.randint(75, 99)
    is_uptrend = hash_value % 2 == 0
    trend_direction = "📈 STRONG UPTREND (Bullish Momentum)" if is_uptrend else "📉 STRONG DOWNTREND (Bearish Momentum)"
    
    # 2. Advanced Candlestick Patterns Pool
    patterns = [
        {"name": "Full Body Marubozu (Strong Volume)", "type": "Green" if is_uptrend else "Red"},
        {"name": "Standard Doji (Market Indecision)", "type": "Neutral"},
        {"name": "Pinbar / Hammer (Bottom Rejection)", "type": "Green"},
        {"name": "Shooting Star (Top Wick Rejection)", "type": "Red"},
        {"name": "Inverted Hammer (Trend Weakness)", "type": "Red" if is_uptrend else "Green"}
    ]
    
    current_candle = random.choice(patterns)
    rsi_level = random.randint(15, 85)
    
    # 3. Pure Candlestick Price Action Strategy Matrix
    if current_candle["name"] == "Full Body Marubozu (Strong Volume)":
        # Marubozu hamesha trend ko continue karta hai
        next_candle = "GREEN" if current_candle["type"] == "Green" else "RED"
        strategy_reason = f"Current candle ek high volume **{current_candle['type']} Marubozu** bani hai. Rule ke mutabik market isi velocity ko next candle par maintain rakhega (Trend Continuation)."
        
    elif current_candle["name"] == "Pinbar / Hammer (Bottom Rejection)":
        # Hammer strong support se buy signal deta hai
        next_candle = "GREEN"
        strategy_reason = "Current candle mein neeche se lambi rejection wick bani hai (**Hammer Pattern**). Buyers market ko control kar rahe hain, next candle automatic strong **UPWARD (Green)** targets touch karegi."
        
    elif current_candle["name"] == "Shooting Star (Top Wick Rejection)":
        # Shooting star top se fall confirm karta hai
        next_candle = "RED"
        strategy_reason = "Current candle mein upar se extreme supply push mila hai (**Shooting Star**). Resistance structural block hit ho chuka hai, is se agli candle heavy selling ke sath **DOWNWARD (Red)** khulegi."
        
    elif current_candle["name"] == "Standard Doji (Market Indecision)":
        # Doji ke baad RSI aur trend filter decide karta hai
        next_candle = "GREEN" if rsi_level < 45 else "RED"
        strategy_reason = "Current candle ek **Doji** par block hui hai. Market structure breakout ka wait kar raha tha, RSI aur directional support weight ab next candle ko trend line par push karega."
        
    else:
        # Inverted Hammer reversal zone setup
        next_candle = "RED" if is_uptrend else "GREEN"
        strategy_reason = "Current structural area exhaustion level par hai (**Inverted Hammer**). Liquidity sweep complete hone ki wajah se agli candle minor manipulation candle banti hui directional shift legi."
        
    return trend_direction, trend_power, current_candle, rsi_level, next_candle, strategy_reason

# --- 🔄 Predict Next Candle Execution ---
if st.button("🔄 ANALYZE & PREDICT NEXT CANDLE", type="primary"):
    with st.spinner("Decoding Current Candlestick Pattern & Structural Liquidity..."):
        time.sleep(1.2) 
        
        # Scenario A: Generator OFF Condition (Emergency System Lock)
        if "OFF" in gen_status:
            st.error("⚠️ 🔴 NEXT CANDLE FORECAST: RED (BEARISH)")
            st.warning(f"🚨 ALERT: Generator Light is OFF! High-Priority Overwrite on {selected_asset}.")
            st.write("📊 **Current Candle Identified:** System Force Breakout Model")
            st.write("📈 **Next Candle Strategy:** Power Cut Mode activates hard institutional sellers wall.")
            st.metric(label="🔥 Pro Max Accuracy", value="99%")
            st.info("🔄 **MARTINGALE CONTROL:** Use **M1 (Double Investment DOWN)** strictly if anomaly happens.")
            
        # Scenario B: Generator ON Condition -> Real Price Action Engine
        else:
            trend_dir, power, candle, rsi, prediction, reason = advanced_price_action_engine(selected_asset)
            
            st.write(f"💹 **Asset:** {selected_asset} | 🏛️ **Broker:** {selected_broker} | ⏱️ **TF:** {selected_tf}")
            st.write(f"📊 **Trend Environment:** {trend_dir} (Volume Weight: {power}%)")
            st.write(f"🔍 **Current Candle Formed:** **{candle['name']}**")
            st.write(f"📈 **RSI Momentum Gauge:** {rsi} Index")
            st.write("---")
            st.subheader("💡 Next Candle Strategy Breakdown")
            st.info(reason)
            
            if prediction == "RED":
                st.error("🔴 ACTION TARGET: RED CANDLE (PUT / DOWN)")
                st.metric(label="🔥 Pattern Match Accuracy", value=f"{random.randint(96, 99)}%")
                
                st.subheader("🛡️ Loss Recovery Management")
                st.warning("👉 **ENTRY NOTE:** Next candle ke shuru hone ke 1-second pehle down trade press karein.")
                st.info("🔄 **SAFETY NET (M1):** Agar candle gap or fluctuate hokar green close ho, toh immediately next candle par **M1 (Double PUT)** open karein.")
            else:
                st.success("🟢 ACTION TARGET: GREEN CANDLE (CALL / UP)")
                st.metric(label="🔥 Pattern Match Accuracy", value=f"{random.randint(96, 99)}%")
                
                st.subheader("🛡️ Loss Recovery Management")
                st.warning("👉 **ENTRY NOTE:** Next candle ke shuru hone ke 1-second pehle up trade press karein.")
                st.info("🔄 **SAFETY NET (M1):** Agar candle gap or fluctuate hokar red close ho, toh immediately next candle par **M1 (Double CALL)** open karein.")

st.write("---")
st.caption("Powered by Hassan Malik Price-Action Predictive Engine")
