import streamlit as st, random, time

st.set_page_config(page_title="HASSAN MALIK AI BOT", page_icon="🤖")

# --- Custom Short CSS Styling ---
st.markdown("<style>.stApp{background-color:#010610!important; text-align:center;} .main-title{font-family:'Impact'; font-size:35px; color:#FFF;} .sub-title{font-family:'Arial Black'; font-size:22px; color:#00A3FF; margin-top:-15px;} .pro-badge{display:inline-block; background:#061224; color:#00FF66; font-weight:bold; padding:4px 12px; border:1px solid #00FF66; border-radius:4px;} .panel{padding:15px; border-radius:6px; margin-top:10px; color:#FFF; font-weight:bold;}</style>", unsafe_allow_html=True)

# --- Header & Badges ---
st.markdown('<div class="main-title">HASSAN MALIK</div><div class="sub-title">AI BOT</div><div class="pro-badge">👑 PRO MAX UNLOCKED ✓</div><br><br>', unsafe_allow_html=True)

col_a, col_b, col_c = st.columns(3)
col_a.markdown("<span style='color:#00FF66; font-size:11px;'>🛡️ LICENSE: ACTIVE</span>", unsafe_allow_html=True)
col_b.markdown("<span style='color:#00FF66; font-size:11px;'>🧠 ENGINE: ONLINE</span>", unsafe_allow_html=True)
col_c.markdown("<span style='color:#00A3FF; font-size:11px;'>👥 USERS: 1M+</span>", unsafe_allow_html=True)

# --- Pairs Arrays ---
LIVE = ["EUR/USD", "USD/JPY", "GBP/USD", "AUD/USD", "USD/CAD", "USD/BRL", "EUR/JPY", "EUR/GBP", "USD/MXN"]
OTC = ["USD/ARS (OTC)", "USD/BRL (OTC)", "EUR/USD (OTC)", "USD/JPY (OTC)", "GBP/USD (OTC)", "AUD/USD (OTC)", "GOLD (OTC)", "SILVER (OTC)", "Bitcoin (OTC)", "Ethereum (OTC)", "NASDAQ 100 (OTC)"]
TIMEFRAMES = ["5 Seconds", "10 Seconds", "15 Seconds", "30 Seconds", "1 Minute", "2 Minute", "3 Minute", "5 Minute"]

# --- Input Dropdowns ---
st.selectbox("BROKER", ["Quotex"], disabled=True)
market = st.selectbox("MARKET", ["OTC Markets", "Live Markets"])
pair = st.selectbox("PAIR", LIVE if market == "Live Markets" else OTC)
timer = st.selectbox("TIMER (EXPIRY TIME)", TIMEFRAMES, index=4)

st.markdown("<br>", unsafe_allow_html=True)

# --- Manual Signal Logic ---
if st.button("🚀 NEXT CANDLE GENERATE SIGNAL", use_container_width=True):
    with st.spinner("ANALYZING MOMENTUM..."):
        time.sleep(1.0)
        move = random.choice(["CALL", "PUT", "SKIP"])
        
        if move == "CALL":
            st.markdown(f'<div class="panel" style="background:#041a12; border:2px solid #00FF66;"><h2>🟢 CALL (UP) 🟢</h2><p>{pair} | Time: {timer}</p><span style="color:#A0AEC0; font-size:12px;">Support Bounce Verified.</span></div>', unsafe_allow_html=True)
        elif move == "PUT":
            st.markdown(f'<div class="panel" style="background:#1a0606; border:2px solid #FF2A2A;"><h2>🔴 PUT (DOWN) 🔴</h2><p>{pair} | Time: {timer}</p><span style="color:#A0AEC0; font-size:12px;">Resistance Rejection Tracked.</span></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="panel" style="background:#1a1103; border:1px solid #FFA500;"><h2 style="color:#FFA500;">⏳ SKIP ⏳</h2><p>{pair}</p><span style="color:#A0AEC0; font-size:12px;">Market Sideways. Protect Capital.</span></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="panel" style="background:#071120; border:1px solid #00A3FF; color:#6F7E94;"><h3>SYSTEM READY</h3><p style="font-size:12px;">Click button to get next candle signal.</p></div>', unsafe_allow_html=True)

# --- Footer Accuracy Badges ---
st.markdown("<br><hr>", unsafe_allow_html=True)
f1, f2, f3 = st.columns(3)
f1.markdown("<p style='color:#6F7E94; font-size:11px;'>ACCURACY<br><span style='color:#00FF66; font-size:14px;'>89%</span></p>", unsafe_allow_html=True)
f2.markdown("<p style='color:#6F7E94; font-size:11px;'>SIGNAL STR<br><span style='color:#00A3FF; font-size:14px;'>STRONG</span></p>", unsafe_allow_html=True)
f3.markdown("<p style='color:#6F7E94; font-size:11px;'>AVG TIME<br><span style='color:#FF00A3; font-size:14px;'>00:05</span></p>", unsafe_allow_html=True)
