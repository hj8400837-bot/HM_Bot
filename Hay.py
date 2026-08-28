import streamlit as st,yfinance as yf,pandas as pd

st.set_page_config(page_title="HASSAN MALIK AI BOT",page_icon="🤖")

st.markdown("""<style>
.stApp{background:radial-gradient(circle,#082b50,#00030a 60%);color:white}
.box{border:1px solid #168cff;border-radius:20px;padding:15px;margin:10px 0;background:#031126}
h1,h2{text-align:center}.blue{color:#09f}
.stButton>button{width:100%;height:58px;border-radius:35px;
background:linear-gradient(90deg,#09f,#62e);color:white;font-weight:900}
</style>""",unsafe_allow_html=True)

st.markdown('<div class="box"><h1>🤖 HASSAN MALIK<br><span class="blue">AI BOT</span></h1><h3 style="text-align:center">♛ PRO MAX</h3></div>',unsafe_allow_html=True)

live=["EUR/USD","GBP/USD","USD/JPY","AUD/USD","USD/CAD","USD/CHF",
"EUR/JPY","EUR/GBP","GBP/JPY","AUD/JPY","NZD/USD","AUD/NZD",
"EUR/AUD","EUR/CAD","CAD/JPY","CHF/JPY","GBP/MXN","USD/MXN","USD/BRL"]

otc=["AUD/CAD OTC","AUD/CHF OTC","AUD/JPY OTC","AUD/NZD OTC","AUD/USD OTC",
"CAD/CHF OTC","CAD/JPY OTC","CHF/JPY OTC","EUR/AUD OTC","EUR/CAD OTC",
"EUR/CHF OTC","EUR/GBP OTC","EUR/JPY OTC","EUR/NZD OTC","EUR/USD OTC",
"GBP/AUD OTC","GBP/CAD OTC","GBP/CHF OTC","GBP/JPY OTC","GBP/NZD OTC",
"GBP/USD OTC","NZD/CAD OTC","NZD/CHF OTC","NZD/JPY OTC","NZD/USD OTC",
"USD/CAD OTC","USD/CHF OTC","USD/JPY OTC","USD/SGD OTC",
"Bitcoin OTC","Ethereum OTC","Litecoin OTC","Ripple OTC","Dogecoin OTC",
"Gold OTC","Silver OTC","Oil OTC","S&P 500 OTC","Nasdaq 100 OTC",
"Dow Jones 30 OTC","DAX 30 OTC"]

m=st.selectbox("🌐 MARKET",["Live Market","OTC Markets"])
p=st.selectbox("🌎 PAIR / ASSET",live if m=="Live Market" else otc)
t=st.selectbox("⏱️ TIMER",["5 Seconds","10 Seconds","15 Seconds","30 Seconds","1 Minute","5 Minutes"])

def ana():
    s=p.replace("/","")+"=X"
    d=yf.download(s,period="10d",interval="5m",progress=False)
    if d.empty:return None
    c=d["Close"].astype(float).squeeze()
    h=d["High"].astype(float).squeeze()
    l=d["Low"].astype(float).squeeze()

    e9=c.ewm(span=9).mean();e21=c.ewm(span=21).mean();e50=c.ewm(span=50).mean()
    x=c.diff();g=x.clip(lower=0).rolling(14).mean();z=(-x.clip(upper=0)).rolling(14).mean()
    rsi=100-100/(1+g/z)
    mac=c.ewm(span=12).mean()-c.ewm(span=26).mean()
    sg=mac.ewm(span=9).mean()
    mid=c.rolling(20).mean();sd=c.rolling(20).std()
    lo=l.rolling(14).min();hi=h.rolling(14).max()
    st=100*(c-lo)/(hi-lo)
    tr=pd.concat([h-l,(h-c.shift()).abs(),(l-c.shift()).abs()],axis=1).max(axis=1)
    adx=(tr.rolling(14).mean()/c*100).rolling(14).mean()

    q=0
    q+=2 if e9.iloc[-1]>e21.iloc[-1]>e50.iloc[-1] else -2 if e9.iloc[-1]<e21.iloc[-1]<e50.iloc[-1] else 0
    q+=1 if rsi.iloc[-1]>55 else -1 if rsi.iloc[-1]<45 else 0
    q+=1 if mac.iloc[-1]>sg.iloc[-1] else -1
    q+=1 if c.iloc[-1]>mid.iloc[-1] else -1
    q+=1 if st.iloc[-1]>55 else -1 if st.iloc[-1]<45 else 0

    if q>=5 and adx.iloc[-1]>.15:return "UP","🟢",min(95,70+q*4)
    if q<=-5 and adx.iloc[-1]>.15:return "DOWN","🔴",min(95,70+abs(q)*4)
    return "WAIT","🟡",50

if st.button("🚀 NEXT CANDLE SIGNAL"):
    if m=="OTC Markets":
        st.markdown(f'<div class="box"><h1>🟡 OTC DATA</h1><center>{p}<br><br>Real OTC feed unavailable<br>🚫 NO FAKE SIGNAL</center></div>',unsafe_allow_html=True)
    else:
        try:
            x=ana()
            if x:
                st.markdown(f'<div class="box"><h1>{x[1]} NEXT CANDLE: {x[0]}</h1><center>{p}<br>⏱️ {t}<br><br>🎯 CONFIDENCE: {x[2]}%<br><br>EMA • RSI • MACD • ADX • BB • STOCHASTIC</center></div>',unsafe_allow_html=True)
            else:st.error("Live data unavailable")
        except:st.error("Live data unavailable")

try:st.code(st.context.url)
except:pass

st.caption("HASSAN MALIK AI BOT • Analysis Only • No automatic trade execution")
