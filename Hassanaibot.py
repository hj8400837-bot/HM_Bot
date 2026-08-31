import streamlit as st,pandas as pd,yfinance as yf

st.set_page_config(page_title="HASSAN MALIK AI BOT",page_icon="🤖",layout="wide")

# 🔐 PASSWORDS
OWNER="Hassan7166"
USERS=["HM-AX7K-29P4","HM-BQ8L-51RX","HM-CN4T-73WD","HM-DP6Y-18KF","HM-EZ9M-42QV"]

if "ok" not in st.session_state: st.session_state.ok=False
if not st.session_state.ok:
    st.title("🔐 HASSAN MALIK AI BOT")
    p=st.text_input("Password",type="password")
    if st.button("ENTER"):
        if p==OWNER or p in USERS:
            st.session_state.ok=True
            st.rerun()
        else: st.error("Wrong password")
    st.stop()

st.markdown("""
<style>
.stApp{background:radial-gradient(circle,#09294f,#020611 55%,#000);color:white}
.box{background:#061120;border:1px solid #0875ff;border-radius:18px;padding:16px;margin:8px 0}
.sig{text-align:center;font-size:60px;font-weight:900}
</style>
""",unsafe_allow_html=True)

st.markdown("""
<div class="box">
<h1 style="text-align:center">🤖 HASSAN MALIK AI BOT</h1>
<h2 style="text-align:center">👑 QUOTEX BINARY TRADING</h2>
<p style="text-align:center">NEXT CANDLE • TREND • RSI • MACD • EMA • CANDLE PATTERN</p>
</div>
""",unsafe_allow_html=True)

# LIVE
LIVE={
"EUR/USD":"EURUSD=X","GBP/USD":"GBPUSD=X","USD/JPY":"JPY=X",
"AUD/USD":"AUDUSD=X","USD/CAD":"CAD=X","USD/CHF":"CHF=X",
"EUR/JPY":"EURJPY=X","EUR/GBP":"EURGBP=X","NZD/USD":"NZDUSD=X",
"GBP/JPY":"GBPJPY=X","AUD/JPY":"AUDJPY=X","USD/SGD":"SGD=X"
}

# OTC
OTC=[
"EUR/USD OTC","GBP/USD OTC","USD/JPY OTC","AUD/USD OTC",
"EUR/JPY OTC","GBP/JPY OTC","USD/CAD OTC","USD/CHF OTC",
"BTC/USD OTC","ETH/USD OTC","GOLD OTC","SILVER OTC",
"S&P 500 OTC","NASDAQ 100 OTC","DOW JONES 30 OTC"
]

market=st.radio("🌐 MARKET",["🟢 LIVE","🟣 OTC"],horizontal=True)

if market=="🟢 LIVE":
    pair=st.selectbox("💱 LIVE PAIR",list(LIVE))
else:
    pair=st.selectbox("💱 OTC PAIR",OTC)

time=st.selectbox(
    "⏱️ TIME",
    ["5 Seconds","10 Seconds","15 Seconds","30 Seconds",
     "1 Minute","2 Minutes","5 Minutes"]
)

def RSI(x,n=14):
    d=x.diff()
    g=d.clip(lower=0).rolling(n).mean()
    l=(-d.clip(upper=0)).rolling(n).mean()
    return 100-100/(1+g/(l+1e-9))

def signal(df):
    c=df.Close
    e9=c.ewm(span=9).mean()
    e21=c.ewm(span=21).mean()
    e50=c.ewm(span=50).mean()
    r=float(RSI(c).iloc[-1])
    mac=c.ewm(span=12).mean()-c.ewm(span=26).mean()

    s=0
    s+=2 if e9.iloc[-1]>e21.iloc[-1] else -2
    s+=2 if e21.iloc[-1]>e50.iloc[-1] else -2
    s+=1 if r>50 else -1
    s+=1 if mac.iloc[-1]>0 else -1

    a=df.iloc[-1];p=df.iloc[-2]
    body=abs(a.Close-a.Open)
    rng=max(a.High-a.Low,1e-9)
    lo=min(a.Open,a.Close)-a.Low
    up=a.High-max(a.Open,a.Close)
    pat="Normal"

    if body/rng<.12: pat="Doji"
    elif lo>body*2 and up<body:
        pat="Hammer";s+=2
    elif up>body*2 and lo<body:
        pat="Shooting Star";s-=2
    elif a.Close>a.Open and p.Close<p.Open and a.Close>=p.Open and a.Open<=p.Close:
        pat="Bullish Engulfing";s+=2
    elif a.Close<a.Open and p.Close>p.Open and a.Open>=p.Close and a.Close<=p.Open:
        pat="Bearish Engulfing";s-=2

    sig="UP" if s>=3 else "DOWN" if s<=-3 else "NO SIGNAL"
    conf=min(95,55+abs(s)*6)
    return sig,conf,r,pat

if st.button("🚀 GENERATE NEXT CANDLE",use_container_width=True):

    if market=="🟣 OTC":
        st.warning(
            "OTC selected. Genuine Quotex OTC candles require "
            "an authorized OTC data feed. Fake data is not used."
        )

    else:
        try:
            df=yf.download(
                LIVE[pair],
                period="5d",
                interval="1m",
                progress=False,
                auto_adjust=False
            )

            if isinstance(df.columns,pd.MultiIndex):
                df.columns=df.columns.get_level_values(0)

            df=df.dropna()

            if len(df)<60:
                st.error("Not enough live market data.")
            else:
                s,cf,r,pat=signal(df)
                icon="⬆️" if s=="UP" else "⬇️" if s=="DOWN" else "⏸️"

                st.markdown(
                    f'<div class="box"><div class="sig">{s} {icon}</div>'
                    f'<h2 style="text-align:center">NEXT CANDLE • {cf}%</h2></div>',
                    unsafe_allow_html=True
                )

                a,b,c=st.columns(3)
                a.metric("RSI",f"{r:.1f}")
                b.metric("CANDLE",pat)
                c.metric("CONFIDENCE",f"{cf}%")

        except Exception:
            st.error("Live market data unavailable.")

st.markdown(
'<div class="box"><b>🧠 AI STRATEGIES:</b> '
'Trend • Structure • RSI • MACD • EMA • Candlestick</div>',
unsafe_allow_html=True
)

st.caption(
"⚠️ Analytical estimates only. No guaranteed accuracy or profit. "
"This bot does not automatically place trades."
)
