import streamlit as st,pandas as pd
st.set_page_config(page_title="HASSAN MALIK AI BOT",page_icon="🤖")
st.markdown("""<style>
.stApp{background:radial-gradient(circle,#082b50,#00030a 60%);color:white}
.box{border:1px solid #168cff;border-radius:20px;padding:16px;margin:10px 0;background:#031126}
h1,h2{text-align:center}.blue{color:#09f}.stButton>button{width:100%;height:60px;border-radius:35px;background:linear-gradient(90deg,#09f,#62e);color:white;font-weight:900}
</style>""",unsafe_allow_html=True)

st.markdown('<div class="box"><h1>🤖 HASSAN MALIK<br><span class="blue">AI BOT</span></h1><h3 style="text-align:center">♛ PRO MAX</h3></div>',unsafe_allow_html=True)

market=st.selectbox("🌐 MARKET",["Live Market","OTC Markets"])
pairs=["EUR/USD","GBP/USD","USD/JPY","AUD/USD","USD/CAD","USD/CHF","EUR/JPY","EUR/GBP","GBP/JPY","AUD/JPY"]
pair=st.selectbox("🌎 PAIR",pairs)
timer=st.selectbox("⏱️ TIMER",["5 Seconds","10 Seconds","15 Seconds","30 Seconds","1 Minute","5 Minutes"])

def analysis():
    import yfinance as yf
    s=pair.replace("/","")+"=X"
    d=yf.download(s,period="5d",interval="5m",progress=False)
    if d.empty:return None
    c=d["Close"].astype(float)
    e9=c.ewm(span=9).mean().iloc[-1]
    e21=c.ewm(span=21).mean().iloc[-1]
    r=c.diff();g=r.clip(lower=0).rolling(14).mean();l=(-r.clip(upper=0)).rolling(14).mean()
    rsi=(100-100/(1+g/l)).iloc[-1]
    score=(e9>e21)+(rsi>55)+(c.iloc[-1]>c.iloc[-2])
    score-= (e9<e21)+(rsi<45)+(c.iloc[-1]<c.iloc[-2])
    return ("UP","🟢") if score>=2 else ("DOWN","🔴") if score<=-2 else ("WAIT","🟡")

if st.button("🚀 NEXT CANDLE SIGNAL"):
    if market=="OTC Markets":
        st.warning("🟡 OTC LIVE DATA NOT AVAILABLE — No Fake Signal")
    else:
        try:
            x=analysis()
            if x:
                st.markdown(f'<div class="box"><h1>{x[1]} NEXT CANDLE: {x[0]}</h1><center>{pair}<br>⏱️ {timer}<br><br>RSI + EMA + TREND ANALYSIS</center></div>',unsafe_allow_html=True)
            else:st.error("Live data unavailable")
        except:st.error("Live data unavailable")

try: st.code(st.context.url)
except: pass

st.caption("HASSAN MALIK AI BOT • Analysis Only • No automatic trade execution")
