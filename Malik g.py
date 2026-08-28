import streamlit as st

st.set_page_config(
    page_title="HASSAN MALIK AI BOT",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
.stApp{
 background:radial-gradient(circle at top,#082b50,#020611 48%,#00030a);
 color:white
}
.block-container{max-width:850px;padding:15px 12px 90px}

.box{
 border:1px solid #168cff;
 border-radius:22px;
 padding:18px;
 margin:12px 0;
 background:#031126;
 box-shadow:0 0 15px #006eff18
}

.title{text-align:center;font-size:32px;font-weight:900}
.blue{color:#08a8ff}
.pro{
 display:block;width:max-content;margin:8px auto;
 background:#f5c62d;color:#111;
 padding:7px 25px;border-radius:25px;font-weight:900
}

.status{
 display:flex;
 justify-content:space-around;
 text-align:center;
 font-size:14px
}
.green{color:#00e676;font-weight:900;font-size:19px}

.unlock{
 border:1px solid #e5b900;
 border-radius:25px;
 padding:14px;
 text-align:center;
 color:#ffd21c;
 font-size:20px;
 font-weight:900
}

.heading{text-align:center;font-size:30px;font-weight:900}
.heading span{color:#079cff}

.stButton>button{
 width:100%;
 height:62px;
 border:0;
 border-radius:35px;
 background:linear-gradient(90deg,#009cff,#6525e8);
 color:white;
 font-size:17px;
 font-weight:900
}

.stats{
 display:flex;
 justify-content:space-around;
 text-align:center;
 padding:15px 0
}

.stat b{font-size:20px}

.nav{
 display:flex;
 justify-content:space-around;
 text-align:center;
 color:#aeb4d0;
 font-size:13px
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown("""
<div class="box">
<div class="title">
🤖 HASSAN MALIK<br>
<span class="blue">AI BOT</span>
</div>
<div class="pro">♛ PRO MAX</div>
</div>
""", unsafe_allow_html=True)

# ---------------- STATUS ----------------

st.markdown("""
<div class="box status">
<div>🛡️ LICENSE STATUS<br>
<span class="green">ACTIVE ●</span></div>

<div>🧠 AI ENGINE STATUS<br>
<span class="green">ONLINE ●</span></div>

<div>👥 ACTIVE USERS<br>
<b>1M+</b></div>
</div>
""", unsafe_allow_html=True)

# ---------------- PRO ----------------

st.markdown("""
<div class="unlock">
♛ PRO MAX UNLOCKED ✅
</div>
""", unsafe_allow_html=True)

# ---------------- SIGNAL AREA ----------------

st.markdown("""
<div class="box">
<div class="heading">
GENERATE <span>SIGNALS</span>
</div>
<p style="text-align:center;color:#aeb4d0">
AI Analyzed High Accuracy Trading Signals
</p>
""", unsafe_allow_html=True)

broker = st.selectbox(
    "🔴 BROKER",
    ["Quotex", "Pocket Option", "Binomo", "Other"]
)

market = st.selectbox(
    "🌐 MARKET",
    ["OTC Markets", "Live Market"]
)

otc = [
    "USD/ARS (OTC)","EUR/USD (OTC)","GBP/USD (OTC)",
    "USD/JPY (OTC)","AUD/USD (OTC)","USD/CAD (OTC)",
    "USD/CHF (OTC)","EUR/GBP (OTC)","EUR/JPY (OTC)",
    "GBP/JPY (OTC)","NZD/USD (OTC)","AUD/JPY (OTC)",
    "EUR/AUD (OTC)","EUR/CAD (OTC)","BTC/USD (OTC)",
    "ETH/USD (OTC)","Gold (OTC)","Silver (OTC)","Oil (OTC)"
]

live = [
    "EUR/USD","USD/JPY","GBP/USD","AUD/USD",
    "USD/CAD","USD/CHF","EUR/JPY","EUR/GBP",
    "NZD/USD","AUD/NZD","EUR/AUD","EUR/CAD",
    "GBP/JPY","AUD/JPY"
]

pair = st.selectbox(
    "🌎 PAIR",
    otc if market == "OTC Markets" else live
)

timer = st.selectbox(
    "⏱️ TIMER",
    ["5 Seconds","10 Seconds","15 Seconds","30 Seconds",
     "1 Minute","2 Minutes","3 Minutes","5 Minutes"]
)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SIGNAL BUTTON ----------------

if st.button("🚀  NEXT CANDLE GENERATE SIGNAL"):

    st.session_state["generated"] = True

if st.session_state.get("generated", False):

    st.markdown("""
    <div class="box" style="text-align:center">
    <h2>⏳ ANALYZING MARKET...</h2>
    <p>Live candle data API required for real signal.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- STATS ----------------

st.markdown("""
<div class="box stats">

<div class="stat">
🎯<br>ACCURACY<br>
<b style="color:#00e676">89%</b>
</div>

<div class="stat">
📊<br>SIGNAL STR<br>
<b style="color:#168cff">STRONG</b>
</div>

<div class="stat">
⏱️<br>AVG TIME<br>
<b style="color:#c33cff">00:05</b>
</div>

<div class="stat">
〽️<br>TODAY<br>
<b style="color:#ffd21c">128</b>
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- APP LINK ----------------

try:
    url = st.context.url
except:
    url = ""

if url:
    st.markdown("### 🔗 BOT LINK")
    st.code(url)
else:
    st.info("Deploy hone ke baad yahan app ka link show hoga.")

# ---------------- NAVIGATION ----------------

st.markdown("""
<div class="box nav">
<div>🏠<br>Dashboard</div>
<div>◷<br>History</div>
<div>▥<br>Performance</div>
<div>🎧<br>Support</div>
<div>•••<br>More</div>
</div>
""", unsafe_allow_html=True)

st.caption(
    "HASSAN MALIK AI BOT • Analysis Only • No automatic trade execution"
)
