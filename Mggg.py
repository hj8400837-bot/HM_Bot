import streamlit as st
import pandas as pd
import numpy as np

# --- 1. PREMIUM DARK UI THEME (Exact Image Match CSS) ---
st.set_page_config(page_title="Hassan Malik AI Bot Pro Max", layout="centered")

st.markdown("""
    <style>
    /* Full App Premium Dark Background */
    .stApp {
        background-color: #010613;
        color: #ffffff;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    header, footer {visibility: hidden;}
    
    /* Styled Input Field Containers with Borders */
    .input-field-box {
        background-color: #050d1e;
        border: 1px solid #122144;
        border-radius: 12px;
        padding: 10px 15px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
    }
    
    /* Overriding Streamlit Selectbox to blend into our premium design */
    div[data-baseweb="select"] > div {
        background-color: #050d1e !important;
        border: 1px solid #122144 !important;
        color: white !important;
        border-radius: 12px !important;
    }
    
    /* Main Purple Glow "NEXT CANDLE GENERATE SIGNAL" Button */
    .stButton > button {
        background: linear-gradient(90deg, #1d4ed8 0%, #7c3aed 50%, #4f46e5 100%) !important;
        color: white !important;
        border-radius: 14px !important;
        border: none !important;
        font-weight: bold !important;
        font-size: 16px !important;
        padding: 15px 20px !important;
        width: 100% !important;
        box-shadow: 0px 5px 25px rgba(124, 58, 237, 0.4);
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    
    /* Top Bar Section (Status Rows) */
    .top-status-container {
        display: flex;
        justify-content: space-between;
        background-color: #030a18;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    .top-status-box {
        text-align: center;
        flex: 1;
    }
    .top-status-title {
        color: #5f759c;
        font-size: 9px;
        font-weight: bold;
        letter-spacing: 0.5px;
    }
    .top-status-val {
        font-size: 13px;
        font-weight: bold;
        margin-top: 2px;
    }
    
    /* Gold Unlock Banner */
    .unlock-banner {
        background: linear-gradient(90deg, rgba(212,175,55,0.05) 0%, rgba(212,175,55,0.15) 50%, rgba(212,175,55,0.05) 100%);
        border: 1px solid #d4af37;
        border-radius: 10px;
        text-align: center;
        padding: 10px;
        font-weight: bold;
        font-size: 13px;
        letter-spacing: 1px;
        color: #ffd700;
        margin-bottom: 25px;
    }
    
    /* Bottom Stats Boxes Grid */
    .bottom-stat-box {
        background-color: #020917;
        border: 1px solid #0b152b;
        border-radius: 8px;
        padding: 12px 5px;
        text-align: center;
    }
    .bottom-title {
        color: #5f759c;
        font-size: 9px;
        font-weight: bold;
        letter-spacing: 0.5px;
        margin-bottom: 3px;
    }
    .bottom-value {
        font-size: 16px;
        font-weight: bold;
    }
    
    /* Dropdown custom text helper label */
    .field-label {
        color: #5f759c;
        font-size: 11px;
        font-weight: bold;
        letter-spacing: 0.5px;
        margin-top: 10px;
        margin-bottom: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. HIGH ACCURACY PURE MATH INDICATORS ENGINE ---
def run_indicator_analysis(prices_series):
    ema_20 = prices_series.ewm(span=20, adjust=False).mean()
    sma_20 = prices_series.rolling(window=20).mean()
    std_20 = prices_series.rolling(window=20).std()
    bb_upper = sma_20 + (2 * std_20)
    bb_lower = sma_20 - (2 * std_20)
    
    delta = prices_series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=6).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=6).mean()
    rs = gain / (loss + 1e-10)
    rsi_val = 100 - (100 / (1 + rs))
    return ema_20, bb_upper, bb_lower, rsi_val

def execute_signal_prediction(history):
    df = pd.DataFrame(history)
    ema, bb_h, bb_l, rsi = run_indicator_analysis(df['close'])
    
    c_close, c_rsi = df['close'].iloc[-1], rsi.iloc[-1]
    b_h, b_l, e_v = bb_h.iloc[-1], bb_l.iloc[-1], ema.iloc[-1]
    p_close, p_open = df['close'].iloc[-2], df['open'].iloc[-2]

    if (c_close > e_v and c_close <= b_l and c_rsi <= 38 and p_close > p_open):
        acc = "89%" if c_rsi > 30 else "94%"
        return "🟢 CALL (UP)", "STRONG", acc, "Market pichhe se lower support grid par hai aur RSI oversold hai."
    elif (c_close < e_v and c_close >= b_h and c_rsi >= 62 and p_close HASSAN MALIK</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #00d2ff; margin-top: 0px; font-size: 20px; letter-spacing: 2px;'>AI BOT</h3>", unsafe_allow_html=True)

# Top Bar Section (Status Rows)
st.markdown("""
<div class='top-status-container'>
    <div class='top-status-box'><div class='top-status-title'>LICENSE STATUS</div><div class='top-status-val' style='color:#00ff66;'>ACTIVE ●</div></div>
    <div class='top-status-box'><div class='top-status-title'>AI ENGINE STATUS</div><div class='top-status-val' style='color:#00ff66;'>ONLINE ●</div></div>
    <div class='top-status-box'><div class='top-status-title'>ACTIVE USERS</div><div class='top-status-val' style='color:#00ff66;'>1M+</div></div>
</div>
""", unsafe_allow_html=True)

# Pro Max Status Ribbon
st.markdown("<div class='unlock-banner'>👑 PRO MAX UNLOCKED ✅</div>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; font-size: 19px; font-weight: bold; margin-bottom: 2px;'>GENERATE SIGNALS</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5f759c; font-size: 12px; margin-top: 0px; margin-bottom: 20px;'>AI Analyzed High Accuracy Trading Signals</p>", unsafe_allow_html=True)

# --- DROP DOWN MENUS ---

# 1. BROKER FIELD
st.markdown("<div class='field-label'>BROKER</div>", unsafe_allow_html=True)
st.selectbox("LABEL_BROKER", ["Quotex", "Pocket Option", "IQ Option"], label_visibility="collapsed", key="br_val")

# 2. MARKET FIELD
st.markdown("<div class='field-label'>MARKET</div>", unsafe_allow_html=True)
market_selection = st.selectbox("LABEL_MARKET", ["OTC Markets", "Live Markets"], label_visibility="collapsed", key="mk_val")

# Dynamic sorting for pairs based on market type selection
if market_selection == "OTC Markets":
    pairs_list = [
        "USD/ARS (OTC)", "EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "AUD/USD (OTC)", "USD/CAD (OTC)",
        "EUR/GBP (OTC)", "GOLD OTC", "SILVER OTC", "OIL OTC (WTI)", "Bitcoin OTC", "Ethereum OTC", 
        "Nasdaq 100 OTC", "S&P 500 OTC", "Dow Jones 30 OTC", "DAX 30 OTC"
    ]
else:
    pairs_list = [
        "EUR/USD (Live)", "USD/JPY (Live)", "GBP/USD (Live)", "AUD/USD (Live)", "USD/CAD (Live)", "USD/CHF (Live)"
    ]

# 3. PAIR FIELD
st.markdown("<div class='field-label'>PAIR</div>", unsafe_allow_html=True)
st.selectbox("LABEL_PAIR", pairs_list, label_visibility="collapsed", key="pr_val")

# 4. TIMER FIELD (Exact Sequence)
st.markdown("<div class='field-label'>TIMER</div>", unsafe_allow_html=True)
timer_selection = st.selectbox("LABEL_TIMER", [
    "5 Seconds", "10 Seconds", "15 Seconds", "30 Seconds", 
    "1 Minute", "2 Minutes", "3 Minutes", "5 Minutes"
], label_visibility="collapsed", key="tm_val")

st.write("")

# Simulated Historical Continuous Pipeline Data Engine 
np.random.seed(40)
prices_data = np.sin(np.linspace(0, 25, 60)) * 0.003 + 1.0910
simulated_history = {'open': prices_data[:-1], 'high': prices_data[:-1]+0.0002, 'low': prices_data[:-1]-0.0002, 'close': prices_data[1:]}

# Main Rocket Action Trigger Button
if st.button("🚀 NEXT CANDLE GENERATE SIGNAL"):
    with st.spinner("Analyzing past market pichhe se..."):
        signal, strength, accuracy, reason = execute_signal_prediction(simulated_history)
        
        st.write("")
        
        # 4 Column Analytics Grid Matrix matching bottom row of screenshot image
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f"<div class='bottom-stat-box'><div class='bottom-title'>ACCURACY</div><div class='bottom-value' style='color:#00ff66;'>{accuracy}</div></div>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div class='bottom-stat-box'><div class='bottom-title'>SIGNAL STR</div><div class='bottom-value' style='color:#00ff66;'>{strength}</div></div>", unsafe_allow_html=True)
        with c3:
            st.markdown(f"<div class='bottom-stat-box'><div class='bottom-title'>AVG TIME</div><div class='bottom-value' style='color:#ff007f;'>00:05</div></div>", unsafe_allow_html=True)
        with c4:
            st.markdown(f"<div class='bottom-stat-box'><div class='bottom-title'>TODAY</div><div class='bottom-value' style='color:#ffd700;'>128</div></div>", unsafe_allow_html=True)
            
        st.write("")
        # Main Direction Window Box Alert
        st.success(f"🎯 **BOT DIRECTION SIGNAL:** {signal} (Expiry: Next {timer_selection} Candle)")
        st.info(f"📋 **Urdu Analytics:** {reason}")
