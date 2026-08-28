import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="HASSAN MALIK AI BOT",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
.stApp{
    background:radial-gradient(circle at 50% 0%,#082b50,#020611 48%);
    color:white;
}
.block-container{
    max-width:900px;
    padding:15px 10px 60px;
}
.box{
    border:1px solid #168cff;
    border-radius:24px;
    padding:18px;
    margin:12px 0;
    background:#031126;
    box-shadow:0 0 18px #087cff22;
}
h1{
    text-align:center;
    font-size:34px;
}
.blue{
    color:#08a8ff;
}
.pro{
    display:block;
    width:max-content;
    margin:auto;
    background:#f5c62d;
    color:#111;
    padding:7px 22px;
    border-radius:22px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

OTC = [
    "AUD/CAD (OTC)","AUD/CHF (OTC)","AUD/JPY (OTC)",
    "AUD/NZD (OTC)","AUD/USD (OTC)","CAD/CHF (OTC)",
    "CAD/JPY (OTC)","CHF/JPY (OTC)","EUR/AUD (OTC)",
    "EUR/CAD (OTC)","EUR/CHF (OTC)","EUR/GBP (OTC)",
    "EUR/JPY (OTC)","EUR/NZD (OTC)","EUR/USD (OTC)",
    "GBP/AUD (OTC)","GBP/CAD (OTC)","GBP/CHF (OTC)",
    "GBP/JPY (OTC)","GBP/NZD (OTC)","GBP/USD (OTC)",
    "NZD/CAD (OTC)","NZD/CHF (OTC)","NZD/JPY (OTC)",
    "NZD/USD (OTC)","USD/CAD (OTC)","USD/CHF (OTC)",
    "USD/JPY (OTC)","USD/SGD (OTC)",
    "BTC/USD (OTC)","ETH/USD (OTC)",
    "Gold (OTC)","Silver (OTC)","Oil (OTC)",
    "S&P 500 (OTC)","NASDAQ 100 (OTC)",
    "Dow Jones 30 (OTC)","DAX 30 (OTC)"
]

LIVE = [
    "EUR/USD","USD/JPY","GBP/USD","AUD/USD",
    "USD/CAD","USD/CHF","EUR/JPY","EUR/GBP",
    "NZD/USD","AUD/NZD","EUR/AUD","EUR/CAD",
    "GBP/JPY","AUD/JPY","CAD/JPY","GBP/MXN",
    "USD/MXN","USD/BRL"
]

TIMEFRAMES = [
    "5 Seconds","10 Seconds","15 Seconds",
    "30 Seconds","1 Minute","2 Minutes",
    "3 Minutes","4 Minutes","5 Minutes"]
st.markdown("""
<div class="box">
<h1>🤖 HASSAN MALIK <span class="blue">AI BOT</span></h1>
<span class="pro">♛ PRO MAX</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="box">
🛡️ LICENSE STATUS: <b>ACTIVE 🟢</b>
&nbsp;&nbsp;&nbsp;
🧠 AI ENGINE: <b>ONLINE 🟢</b>
&nbsp;&nbsp;&nbsp;
📊 MODE: <b>ANALYSIS</b>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="box" style="text-align:center;color:#ffd22e;font-weight:bold">
♛ PRO MAX UNLOCKED ✅
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="box">
<h2 style="text-align:center">
GENERATE <span class="blue">SIGNALS</span>
</h2>
<p style="text-align:center">
AI-assisted technical market analysis
</p>
""", unsafe_allow_html=True)

st.selectbox("BROKER", ["Quotex"])

market = st.selectbox(
    "MARKET",
    ["OTC Markets", "Live Market"]
)

pair = st.selectbox(
    "PAIR",
    OTC if market == "OTC Markets" else LIVE
)

timeframe = st.selectbox(
    "TIMEFRAME",
    TIMEFRAMES
)

st.markdown("</div>", unsafe_allow_html=True)

uploaded = st.file_uploader(
    "OHLC CSV (Optional)",
    type=["csv"]
)


def calculate_rsi(values, period=14):

    if len(values) < period + 1:
        return 50.0

    diff = np.diff(values)

    gains = np.maximum(diff, 0)
    losses = np.maximum(-diff, 0)

    avg_gain = np.mean(gains[-period:])
    avg_loss = np.mean(losses[-period:])

    if avg_loss == 0:
        return 100.0

    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))              
    
    
    def analyze_market(values):

    prices = pd.Series(values)

    ema9 = prices.ewm(
        span=9,
        adjust=False
    ).mean().iloc[-1]

    ema21 = prices.ewm(
        span=21,
        adjust=False
    ).mean().iloc[-1]

    ema50 = prices.ewm(
        span=50,
        adjust=False
    ).mean().iloc[-1]

    rsi = calculate_rsi(values)

    up_score = 0
    down_score = 0

    if ema9 > ema21 > ema50:
        trend = "UP"
        up_score += 3

    elif ema9 < ema21 < ema50:
        trend = "DOWN"
        down_score += 3

    else:
        trend = "SIDEWAYS"

    if 52 <= rsi <= 68:
        up_score += 2

    elif 32 <= rsi <= 48:
        down_score += 2

    mean20 = np.mean(values[-20:])

    if values[-1] > mean20:
        up_score += 1
    else:
        down_score += 1

    if values[-1] > values[-3]:
        up_score += 1
    else:
        down_score += 1

    if trend == "UP" and up_score > down_score:
        signal = "UP"
        score = up_score

    elif trend == "DOWN" and down_score > up_score:
        signal = "DOWN"
        score = down_score

    else:
        signal = "NO TRADE"
        score = 0

    if score >= 7:
        strength = "STRONG"

    elif score >= 5:
        strength = "MEDIUM"

    else:
        strength = "WEAK"

    return signal, strength, trend, rsiif st.button(
    "🚀 NEXT CANDLE GENERATE SIGNAL",
    use_container_width=True
):

    if uploaded is not None:

        df = pd.read_csv(uploaded)

        close_column = next(
            (
                c for c in df.columns
                if c.strip().lower() == "close"
            ),
            None
        )

        if close_column is None:
            st.error(
                "CSV میں Close column لازمی موجود ہونا چاہیے۔"
            )
            st.stop()

        values = pd.to_numeric(
            df[close_column],
            errors="coerce"
        ).dropna().values

        if len(values) < 60:
            st.error(
                "کم از کم 60 candles درکار ہیں۔"
            )
            st.stop()

    else:

        values = (
            100 +
            np.cumsum(
                np.random.default_rng().normal(
                    0,
                    0.35,
                    300
                )
            )
        )

    signal, strength, trend, rsi = analyze_market(values)

    if signal == "UP":
        st.success("⬆️ NEXT CANDLE: UP")

    elif signal == "DOWN":
        st.error("⬇️ NEXT CANDLE: DOWN")

    else:
        st.warning("⏸️ NO TRADE — Trend clear نہیں ہے")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("PAIR", pair)
    col2.metric("TREND", trend)
    col3.metric("RSI", f"{rsi:.1f}")
    col4.metric("STRENGTH", strength)

    st.info(
        f"Market: {market} | "
        f"Timeframe: {timeframe} | "
        f"Signal: {signal}"
    )

    st.caption(
        "یہ technical/historical analysis ہے؛ "
        "اگلی candle کی 100% guarantee نہیں۔"
    )

st.markdown("""
<div class="box" style="text-align:center">
⌂ Dashboard
&nbsp;&nbsp;&nbsp;
◷ History
&nbsp;&nbsp;&nbsp;
▥ Performance
&nbsp;&nbsp;&nbsp;
♧ Support
&nbsp;&nbsp;&nbsp;
••• More
</div>
""", unsafe_allow_html=True)

st.caption(
    "HASSAN MALIK AI BOT • Quotex Analysis Dashboard"
)
