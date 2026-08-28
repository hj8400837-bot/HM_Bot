import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="HASSAN MALIK AI BOT",page_icon="🤖")

st.markdown("""<style>
.stApp{background:radial-gradient(circle,#082b50,#00030a 60%);color:white}
.box{border:1px solid #168cff;border-radius:20px;padding:15px;background:#031126}
h1{text-align:center}.blue{color:#09f}
.stButton>button{width:100%;height:55px;border-radius:30px;
background:linear-gradient(90deg,#09f,#62e);color:white;font-weight:900}
</style>""",unsafe_allow_html=True)

st.markdown('<div class="box"><h1>🤖 HASSAN MALIK<br><span class="blue">AI BOT</span></h1><center>♛ PRO MAX</center></div>',unsafe_allow_html=True)

L=["EUR/USD","GBP/USD","USD/JPY","AUD/USD","USD/CAD","USD/CHF","EUR/JPY","EUR/GBP","GBP/JPY","AUD/JPY","NZD/USD","AUD/NZD","EUR/AUD","EUR/CAD","CAD/JPY","CHF/JPY"]
O=["AUD/CAD OTC","AUD/CHF OTC","AUD/JPY OTC","AUD/NZD OTC","AUD/USD OTC","CAD/CHF OTC","CAD/JPY OTC","CHF/JPY OTC","EUR/AUD OTC","EUR/CAD OTC","EUR/CHF OTC","EUR/GBP OTC","EUR/JPY OTC","EUR/NZD OTC","EUR/USD OTC","GBP/AUD OTC","GBP/CAD OTC","GBP/CHF OTC","GBP/JPY OTC","GBP/NZD OTC","GBP/USD OTC","NZD/CAD OTC","NZD/CHF OTC","NZD/JPY OTC","NZD/USD OTC","USD/CAD OTC","USD/CHF OTC","USD/JPY OTC","Bitcoin OTC","Ethereum OTC","Gold OTC","Silver OTC","Oil OTC","S&P 500 OTC","Nasdaq 100 OTC","Dow Jones 30 OTC","DAX 30 OTC"]

m=st.selectbox("🌐 MARKET",["Live Market","OTC Markets"])
p=st.selectbox("🌎 PAIR / ASSET",L if m=="Live Market" else O)
t=st.selectbox("⏱️ TIMER",["5 Seconds","10 Seconds","15 Seconds","30 Seconds","1 Minute","5 Minutes"])

def ana():
    d=yf.download(p.replace("/","")+"=X",period="10d",interval="5m",progress=False)
    if d.empty:return
    c=d["Close"].astype(float).squeeze()
    e9=c.ewm(span=9).mean();e21=c.ewm(span=21).mean();e50=c.ewm(span=50).mean()
    x=c.diff();g=x.clip(lower=0).rolling(14).mean();l=(-x.clip(upper=0)).rolling(14).mean()
    r=100-100/(1+g/l)
    mac=c.ewm(span=12).mean()-c.ewm(span=26).mean()
    sg=mac.ewm(span=9).mean();mid=c.rolling(20).mean()
    q=0
    q+=2 if e9.iloc[-1]>e21.iloc[-1]>e50.iloc[-1] else -2 if e9.iloc[-1]<e21.iloc[-1]<e50.iloc[-1] else 0
    q+=1 if r.iloc[-1]>55 else -1 if r.iloc[-1]<45 else 0
    q+=1 if mac.iloc[-1]>sg.iloc[-1] else -1
    q+=1 if c.iloc[-1]>mid.iloc[-1] else -1
    return ("UP","🟢",min(95,70+q*4)) if q>=4 else ("DOWN","🔴",min(95,70+abs(q)*4)) if q<=-4 else ("WAIT","🟡",50)

if st.button("🚀 NEXT CANDLE SIGNAL"):
    if m=="OTC Markets":
        st.markdown(f'<div class="box"><h1>🟡 OTC</h1><center>{p}<br><br>⚠️ Real OTC feed unavailable<br>🚫 NO FAKE SIGNAL<br>⏱️ {t}</center></div>',unsafe_allow_html=True)
    else:
        try:
            x=ana()
            if x:
                st.markdown(f'<div class="box"><h1>{x[1]} NEXT CANDLE: {x[0]}</h1><center>{p}<br>⏱️ {t}<br><br>🎯 {x[2]}% CONFIDENCE<br><br>EMA • RSI • MACD • BOLLINGER</center></div>',unsafe_allow_html=True)
            else:st.error("Live data unavailable")
        except:st.error("Live data unavailable")

st.caption("HASSAN MALIK AI BOT • Analysis Only")
