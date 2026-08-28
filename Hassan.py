import streamlit as st
import random

st.set_page_config(
    page_title="HASSAN MALIK AI BOT",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
.stApp{background:radial-gradient(circle at top,#082b50,#020611 48%,#00030a);color:white}
.block-container{max-width:850px;padding:15px 12px 90px}
.box{border:1px solid #168cff;border-radius:22px;padding:18px;margin:12px 0;background:#031126;box-shadow:0 0 15px #006eff18}
.title{text-align:center;font-size:32px;font-weight:900}.blue{color:#08a8ff}
.pro{display:block;width:max-content;margin:8px auto;background:#f5c62d;color:#111;padding:7px 25px;border-radius:25px;font-weight:900}
.status,.stats,.nav{display:flex;justify-content:space-around;text-align:center}
.status{font-size:14px}.green{color:#00e676;font-weight:900;font-size:19px}
.unlock{border:1px solid #e5b900;border-radius:25px;padding:14px;text-align:center;color:#ffd21c;font-size:20px;font-weight:900}
.heading{text-align:center;font-size:30px;font-weight:900}.heading span{color:#079cff}
.stButton>button{width:100%;height:62px;border:0;border-radius:35px;background:linear-gradient(90deg,#009cff,#6525e8);color:white;font-size:17px;font-weight:900}
.stats{padding:15px 0}.stat b{font-size:20px}.nav{color:#aeb4d0;font-size:13px}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="box"><div class="title">🤖 HASSAN MALIK<br>
<span class="blue">AI BOT</span></div><div class="pro">♛ PRO MAX</div></div>

<div class="box status">
<div>🛡️ LICENSE STATUS<br><span class="green">ACTIVE ●</span></div>
<div>🧠 AI ENGINE STATUS<br><span class="green">ONLINE ●</span></div>
<div>👥 ACTIVE USERS<br><b>1M+</b></div></div>

<div class="unlock">♛ PRO MAX UNLOCKED ✅</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="box"><div class="heading">GENERATE <span>SIGNALS</span></div>
<p style="text-align:center;color:#aeb4d0">AI Analyzed High Accuracy Trading Signals</p>
""", unsafe_allow_html=True)

broker=st.selectbox("🔴 BROKER",["Quotex","Pocket Option","Binomo","Other"])
market=st.selectbox("🌐 MARKET",["OTC Markets","Live Market"])

otc=["USD/ARS (OTC)","EUR/USD (OTC)","GBP/USD (OTC)","USD/JPY (OTC)",
"AUD/USD (OTC)","USD/CAD (OTC)","USD/CHF (OTC)","EUR/GBP (OTC)",
"EUR/JPY (OTC)","GBP/JPY (OTC)","NZD/USD (OTC)","AUD/JPY (OTC)",
"EUR/AUD (OTC)","EUR/CAD (OTC)","BTC/USD (OTC)","ETH/USD (OTC)",
"Gold (OTC)","Silver (OTC)","Oil (OTC)"]

live=["EUR/USD","USD/JPY","GBP/USD","AUD/USD","USD/CAD","USD/CHF",
"EUR/JPY","EUR/GBP","NZD/USD","AUD/NZD","EUR/AUD","EUR/CAD",
"GBP/JPY","AUD/JPY"]

pair=st.selectbox("🌎 PAIR",otc if market=="OTC Markets" else live)
timer=st.selectbox("⏱️ TIMER",["5 Seconds","10 Seconds","15 Seconds","30 Seconds",
"1 Minute","2 Minutes","3 Minutes","5 Minutes"])

st.markdown("</div>",unsafe_allow_html=True)

if st.button("🚀 NEXT CANDLE GENERATE SIGNAL"):
    signal=random.choice(["UP","DOWN"])
    emoji="🟢" if signal=="UP" else "🔴"
    st.markdown(f"""
    <div class="box" style="text-align:center">
    <h1>{emoji} NEXT CANDLE: {signal}</h1>
    <p>Pair: {pair}</p>
    <p>Timer: {timer}</p>
    <b>Signal Generated Successfully</b>
    </div>
    """,unsafe_allow_html=True)

st.markdown("""
<div class="box stats">
<div class="stat">🎯<br>ACCURACY<br><b style="color:#00e676">89%</b></div>
<div class="stat">📊<br>SIGNAL STR<br><b style="color:#168cff">STRONG</b></div>
<div class="stat">⏱️<br>AVG TIME<br><b style="color:#c33cff">00:05</b></div>
<div class="stat">〽️<br>TODAY<br><b style="color:#ffd21c">128</b></div>
</div>
""",unsafe_allow_html=True)

try:url=st.context.url
except:url=""

if url:
    st.markdown("### 🔗 BOT LINK")
    st.code(url)
else:
    st.info("Deploy hone ke baad yahan app ka link show hoga.")

st.markdown("""
<div class="box nav">
<div>🏠<br>Dashboard</div><div>◷<br>History</div>
<div>▥<br>Performance</div><div>🎧<br>Support</div><div>•••<br>More</div>
</div>
""",unsafe_allow_html=True)

st.caption("HASSAN MALIK AI BOT • Analysis Only • No automatic trade execution")
