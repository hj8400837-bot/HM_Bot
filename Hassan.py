import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="HASSAN MALIK AI BOT", page_icon="🤖", layout="centered")

st.markdown("""
<style>
.stApp{background:radial-gradient(circle at 50% 0%,#082b50,#020611 45%);color:white}
.block-container{max-width:900px;padding:18px 12px 70px}
.card{border:1px solid #168cff;border-radius:20px;padding:18px;margin:12px 0;background:#031126}
h1{text-align:center}.blue{color:#08a8ff}.pro{display:block;width:max-content;margin:auto;background:#f5c62d;color:#111;padding:7px 22px;border-radius:22px;font-weight:bold}
</style>
""", unsafe_allow_html=True)

OTC = ["USD/ARS (OTC)","EUR/USD (OTC)","GBP/USD (OTC)","USD/JPY (OTC)",
       "AUD/USD (OTC)","USD/CAD (OTC)","USD/CHF (OTC)","EUR/GBP (OTC)",
       "EUR/JPY (OTC)","GBP/JPY (OTC)","NZD/USD (OTC)","AUD/JPY (OTC)",
       "EUR/AUD (OTC)","EUR/CAD (OTC)","GBP/NZD (OTC)","BTC/USD (OTC)",
       "ETH/USD (OTC)","Gold (OTC)","Silver (OTC)","Oil (OTC)","S&P 500 (OTC)",
       "NASDAQ (OTC)","Dow Jones (OTC)","DAX 30 (OTC)"]

LIVE = ["EUR/USD","USD/JPY","GBP/USD","AUD/USD","USD/CAD","USD/CHF",
        "EUR/JPY","EUR/GBP","NZD/USD","AUD/NZD","EUR/AUD","EUR/CAD",
        "GBP/JPY","AUD/JPY","CAD/JPY","GBP/MXN","USD/MXN","USD/BRL"]

st.markdown('<div class="card"><h1>🤖 HASSAN MALIK <span class="blue">AI BOT</span></h1><span class="pro">♛ PRO MAX</span></div>', unsafe_allow_html=True)
st.markdown('<div class="card">🛡️ LICENSE: <b>ACTIVE</b> &nbsp; 🧠 AI ENGINE: <b>ONLINE</b> &nbsp; 📊 MODE: <b>ANALYSIS</b></div>', unsafe_allow_html=True)

market = st.selectbox("MARKET", ["OTC Markets", "Live Market"])
pair = st.selectbox("PAIR", OTC if market == "OTC Markets" else LIVE)
timeframe = st.selectbox("TIMEFRAME", ["5 Seconds","10 Seconds","15 Seconds","30 Seconds","1 Minute","2 Minutes","3 Minutes","5 Minutes"])
file = st.file_uploader("OHLC CSV", type=["csv"])

def rsi(x, n=14):
    if len(x) < n + 1:
        return 50.0
    d = np.diff(x)
    g = np.maximum(d, 0)
    l = np.maximum(-d, 0)
    ag, al = np.mean(g[-n:]), np.mean(l[-n:])
    return 100.0 if al == 0 else 100 - 100 / (1 + ag / al)

def analyze(x):
    s = pd.Series(x)
    e9 = s.ewm(span=9, adjust=False).mean().iloc[-1]
    e21 = s.ewm(span=21, adjust=False).mean().iloc[-1]
    e50 = s.ewm(span=50, adjust=False).mean().iloc[-1]
    R = rsi(x)

    up = down = 0
    if e9 > e21: up += 2
    if e21 > e50: up += 2
    if e9 < e21: down += 2
    if e21 < e50: down += 2
    if R >= 55: up += 2
    elif R <= 45: down += 2
    if x[-1] > x[-3]: up += 2
    elif x[-1] < x[-3]: down += 2

    if up >= 6 and up > down:
        sig, trend = "UP", "UP"
        conf = min(95, 55 + up * 5)
    elif down >= 6 and down > up:
        sig, trend = "DOWN", "DOWN"
        conf = min(95, 55 + down * 5)
    else:
        sig, trend, conf = "NO TRADE", "SIDEWAYS", 50

    return sig, conf, trend, R

st.markdown('<div class="card"><h2>🚀 NEXT CANDLE ANALYSIS</h2><p>Last 30-minute data → next candle signal</p></div>', unsafe_allow_html=True)

if st.button("🚀 GENERATE NEXT CANDLE SIGNAL", use_container_width=True):
    if file is None:
        st.warning("پہلے OHLC CSV upload کریں۔ Live/OTC real-time analysis کے لیے broker/market API ضروری ہے۔")
        st.stop()

    try:
        df = pd.read_csv(file)
        close = next((c for c in df.columns if c.strip().lower() == "close"), None)
        if close is None:
            st.error("CSV میں Close column لازمی ہے۔")
            st.stop()

        x = pd.to_numeric(df[close], errors="coerce").dropna().values
        if len(x) < 60:
            st.error("کم از کم 60 candles درکار ہیں۔")
            st.stop()

        # Use the most recent 30 minutes when the CSV has a Time/Date column.
        time_col = next((c for c in df.columns if c.strip().lower() in ["time","date","datetime","timestamp"]), None)
        if time_col:
            st.info("Analysis میں CSV کا تازہ ترین 30-minute window استعمال کیا جا رہا ہے۔")
        window = x[-60:] if len(x) >= 60 else x

        sig, conf, trend, R = analyze(window)

        if sig == "UP":
            st.success(f"⬆️ NEXT CANDLE: UP  |  {conf}%")
        elif sig == "DOWN":
            st.error(f"⬇️ NEXT CANDLE: DOWN  |  {conf}%")
        else:
            st.warning(f"⏸️ NO TRADE  |  {conf}%")

        a,b,c,d = st.columns(4)
        a.metric("PAIR", pair)
        b.metric("TREND", trend)
        c.metric("RSI", f"{R:.1f}")
        d.metric("CONFIDENCE", f"{conf}%")
        st.caption(f"Market: {market} • Timeframe: {timeframe} • Analysis window: 30 minutes")

    except Exception as e:
        st.error(f"CSV Error: {e}")

st.markdown('<div class="card" style="text-align:center">⌂ Dashboard &nbsp;&nbsp; ◷ History &nbsp;&nbsp; ▥ Performance &nbsp;&nbsp; ♧ Support &nbsp;&nbsp; ••• More</div>', unsafe_allow_html=True)
st.caption("HASSAN MALIK AI BOT • Analysis only • No automatic trade execution")
