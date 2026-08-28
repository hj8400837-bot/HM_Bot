from pathlib import Path
import zipfile

app = r'''
import streamlit as st
import pandas as pd
import numpy as np
import statistics
from dataclasses import dataclass
from datetime import datetime, timedelta

st.set_page_config(
    page_title="HASSAN MALIK AI BOT",
    page_icon="🤖",
    layout="centered"
)

# =========================
# DATA MODEL
# =========================

@dataclass
class Candle:
    timestamp: int
    open: float
    high: float
    low: float
    close: float


# =========================
# ANALYSIS ENGINE
# =========================

class HassanMalikAIBot:
    def __init__(self, candles):
        self.candles = candles

    def ema(self, values, period):
        if len(values) < period:
            return None
        alpha = 2 / (period + 1)
        value = float(np.mean(values[:period]))
        for price in values[period:]:
            value = alpha * price + (1 - alpha) * value
        return value

    def rsi(self, values, period=14):
        if len(values) <= period:
            return None

        delta = np.diff(values)
        gains = np.maximum(delta, 0)
        losses = np.maximum(-delta, 0)

        avg_gain = np.mean(gains[:period])
        avg_loss = np.mean(losses[:period])

        for i in range(period, len(delta)):
            avg_gain = ((avg_gain * (period - 1)) + gains[i]) / period
            avg_loss = ((avg_loss * (period - 1)) + losses[i]) / period

        if avg_loss == 0:
            return 100.0

        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))

    def macd(self):
        closes = np.array([c.close for c in self.candles], dtype=float)
        e12 = self.ema(closes, 12)
        e26 = self.ema(closes, 26)
        if e12 is None or e26 is None:
            return None
        return e12 - e26

    def bollinger(self, values, period=20):
        if len(values) < period:
            return None
        section = np.array(values[-period:], dtype=float)
        middle = float(np.mean(section))
        deviation = float(np.std(section, ddof=1))
        return (
            middle + 2 * deviation,
            middle,
            middle - 2 * deviation
        )

    def candle_pattern(self):
        if len(self.candles) < 3:
            return "NONE"

        a = self.candles[-2]
        b = self.candles[-1]

        body = abs(b.close - b.open)
        rng = b.high - b.low

        if (
            a.close < a.open and b.close > b.open
            and b.close >= a.open and b.open <= a.close
        ):
            return "BULLISH ENGULFING"

        if (
            a.close > a.open and b.close < b.open
            and b.open >= a.close and b.close <= a.open
        ):
            return "BEARISH ENGULFING"

        if rng > 0 and body <= rng * 0.10:
            return "DOJI"

        upper = b.high - max(b.open, b.close)
        lower = min(b.open, b.close) - b.low

        if rng > 0 and lower > body * 2 and upper < body:
            return "HAMMER"

        if rng > 0 and upper > body * 2 and lower < body:
            return "SHOOTING STAR"

        return "NONE"

    def trend(self):
        closes = np.array([c.close for c in self.candles], dtype=float)

        e9 = self.ema(closes, 9)
        e21 = self.ema(closes, 21)
        e50 = self.ema(closes, 50)

        if None in (e9, e21, e50):
            return "UNKNOWN"

        if e9 > e21 > e50:
            return "UP"

        if e9 < e21 < e50:
            return "DOWN"

        return "SIDEWAYS"

    def support_resistance(self):
        recent = self.candles[-30:]
        support = min(c.low for c in recent)
        resistance = max(c.high for c in recent)
        price = recent[-1].close
        return support, resistance, price

    def generate_signal(self):
        if len(self.candles) < 60:
            return {
                "signal": "NO TRADE",
                "strength": "LOW",
                "confidence": 0,
                "reason": "At least 60 candles are required."
            }

        closes = np.array([c.close for c in self.candles], dtype=float)

        trend = self.trend()
        rsi = self.rsi(closes)
        macd = self.macd()
        bb = self.bollinger(closes)
        pattern = self.candle_pattern()
        support, resistance, price = self.support_resistance()

        up = 0
        down = 0

        # Primary trend filter
        if trend == "UP":
            up += 4
        elif trend == "DOWN":
            down += 4

        # RSI
        if rsi is not None:
            if 52 <= rsi <= 68:
                up += 2
            elif 32 <= rsi <= 48:
                down += 2

        # MACD
        if macd is not None:
            if macd > 0:
                up += 1
            elif macd < 0:
                down += 1

        # Bollinger position
        if bb:
            upper, middle, lower = bb
            if price > middle:
                up += 1
            elif price < middle:
                down += 1

        # Candle pattern
        if pattern in ("BULLISH ENGULFING", "HAMMER"):
            up += 2
        elif pattern in ("BEARISH ENGULFING", "SHOOTING STAR"):
            down += 2

        # Avoid extreme entries
        width = max(resistance - support, 1e-12)
        position = (price - support) / width

        if position > 0.85:
            up -= 1
        if position < 0.15:
            down -= 1

        difference = abs(up - down)
        total = max(up + down, 1)

        if trend in ("SIDEWAYS", "UNKNOWN"):
            signal = "NO TRADE"
            strength = "LOW"
            reason = "Trend is not clear."
        elif difference < 3:
            signal = "NO TRADE"
            strength = "MEDIUM"
            reason = "Indicators are not sufficiently aligned."
        elif up > down and trend == "UP":
            signal = "UP"
            strength = "STRONG" if up >= 7 else "MEDIUM"
            reason = "Bullish confirmation agrees with the trend."
        elif down > up and trend == "DOWN":
            signal = "DOWN"
            strength = "STRONG" if down >= 7 else "MEDIUM"
            reason = "Bearish confirmation agrees with the trend."
        else:
            signal = "NO TRADE"
            strength = "LOW"
            reason = "Setup conflicts with the main trend."

        confidence = round(
            50 + min(45, (difference / total) * 45), 1
        )

        return {
            "signal": signal,
            "strength": strength,
            "confidence": confidence,
            "trend": trend,
            "rsi": None if rsi is None else round(float(rsi), 2),
            "macd": None if macd is None else round(float(macd), 6),
            "pattern": pattern,
            "support": round(float(support), 6),
            "resistance": round(float(resistance), 6),
            "price": round(float(price), 6),
            "up_score": up,
            "down_score": down,
            "reason": reason
        }


# =========================
# DEMO DATA
# =========================
# This is TEST data only. It is NOT a live Quotex feed.

def make_demo_candles(n=240, seed=17):
    rng = np.random.default_rng(seed)
    price = 1600.0
    candles = []

    for i in range(n):
        drift = 0.035 if (i // 45) % 2 == 0 else -0.025
        change = drift + rng.normal(0, 0.55)

        o = price
        c = max(0.01, price + change)
        h = max(o, c) + abs(rng.normal(0, 0.18))
        l = min(o, c) - abs(rng.normal(0, 0.18))

        candles.append(
            Candle(
                timestamp=int(
                    (datetime.now() - timedelta(minutes=n-i)).timestamp()
                ),
                open=float(o),
                high=float(h),
                low=float(l),
                close=float(c)
            )
        )
        price = c

    return candles


def dataframe_to_candles(df):
    cols = {str(c).lower().strip() for c in df.columns}
    required = {"open", "high", "low", "close"}

    if not required.issubset(cols):
        raise ValueError(
            "CSV must contain open, high, low and close columns."
        )

    rename = {c: str(c).lower().strip() for c in df.columns}
    df = df.rename(columns=rename)

    result = []

    for i, row in df.iterrows():
        result.append(
            Candle(
                timestamp=int(datetime.now().timestamp()) + int(i),
                open=float(row["open"]),
                high=float(row["high"]),
                low=float(row["low"]),
                close=float(row["close"])
            )
        )

    return result


# =========================
# PAIRS / TIMEFRAMES
# =========================

OTC_PAIRS = [
    "USD/ARS (OTC)",
    "EUR/USD (OTC)",
    "GBP/USD (OTC)",
    "USD/JPY (OTC)",
    "AUD/USD (OTC)",
    "USD/CAD (OTC)",
    "USD/CHF (OTC)",
    "EUR/GBP (OTC)",
    "EUR/JPY (OTC)",
    "GBP/JPY (OTC)"
]

LIVE_PAIRS = [
    "EUR/USD",
    "GBP/USD",
    "USD/JPY",
    "AUD/USD",
    "USD/CAD",
    "USD/CHF",
    "EUR/GBP",
    "EUR/JPY",
    "GBP/JPY",
    "NZD/USD"
]

TIMEFRAMES = [
    "5 Seconds",
    "10 Seconds",
    "30 Seconds",
    "50 Seconds",
    "1 Minute",
    "2 Minutes",
    "3 Minutes",
    "4 Minutes",
    "5 Minutes"
]


# =========================
# STYLING
# =========================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg,#04152f 0%,#071d42 55%,#020817 100%);
    color: white;
}
.block-container {
    max-width: 760px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}
.hero {
    border: 1px solid #087fff;
    border-radius: 26px;
    padding: 24px 18px;
    text-align: center;
    background: linear-gradient(145deg,#061a3d,#08112a);
    box-shadow: 0 0 28px rgba(0,130,255,.25);
    margin-bottom: 18px;
}
.hero h1 {
    margin: 0;
    font-size: 29px;
}
.hero p {
    margin: 8px 0 0;
    color: #52b8ff;
}
.card {
    border: 1px solid #155ca5;
    border-radius: 20px;
    padding: 16px;
    margin: 12px 0;
    background: rgba(2,13,35,.88);
}
.signal-box {
    border: 1px solid #19a9ff;
    border-radius: 24px;
    padding: 28px 15px;
    text-align: center;
    background: #061b3d;
    margin: 18px 0;
}
.signal-title {
    font-size: 14px;
    color: #8bcfff;
}
.signal-value {
    font-size: 42px;
    font-weight: 800;
    margin-top: 6px;
}
.small {
    color: #a9c6e8;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)


# =========================
# HEADER
# =========================

st.markdown("""
<div class="hero">
    <h1>🤖 HASSAN MALIK AI BOT</h1>
    <p>Multi-factor market analysis dashboard</p>
</div>
""", unsafe_allow_html=True)

st.warning(
    "DEMO MODE: This app uses generated/test candles unless you provide "
    "a real OHLC data source. It does not connect to Quotex automatically."
)

# =========================
# CONTROLS
# =========================

market = st.radio(
    "Market",
    ["OTC Markets", "Live Markets"],
    horizontal=True
)

pairs = OTC_PAIRS if market == "OTC Markets" else LIVE_PAIRS

pair = st.selectbox("Pair", pairs)

timeframe = st.selectbox(
    "Signal / Expiry Timeframe",
    TIMEFRAMES,
    index=4
)

analysis_window = st.selectbox(
    "Historical Analysis",
    ["30 Minutes", "1 Hour", "2 Hours"],
    index=1
)

uploaded = st.file_uploader(
    "Optional: upload OHLC CSV",
    type=["csv"],
    help="CSV columns required: open, high, low, close"
)

# =========================
# DATA
# =========================

try:
    if uploaded is not None:
        df = pd.read_csv(uploaded)
        candles = dataframe_to_candles(df)
        data_source = "Uploaded OHLC CSV"
    else:
        candles = make_demo_candles()
        data_source = "Demo/Test candles"
except Exception as exc:
    st.error(f"Data error: {exc}")
    st.stop()

# =========================
# GENERATE
# =========================

if st.button("🚀 GENERATE SIGNAL", use_container_width=True, type="primary"):

    bot = HassanMalikAIBot(candles)
    result = bot.generate_signal()

    st.session_state["last_result"] = result
    st.session_state["last_pair"] = pair
    st.session_state["last_timeframe"] = timeframe
    st.session_state["last_source"] = data_source

    if "history" not in st.session_state:
        st.session_state["history"] = []

    st.session_state["history"].insert(
        0,
        {
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Pair": pair,
            "Timeframe": timeframe,
            "Signal": result["signal"],
            "Strength": result["strength"],
            "Confidence": result["confidence"]
        }
    )

    st.session_state["history"] = st.session_state["history"][:50]


# =========================
# RESULT
# =========================

if "last_result" in st.session_state:

    result = st.session_state["last_result"]

    st.markdown(
        f"""
        <div class="signal-box">
            <div class="signal-title">
                {st.session_state["last_pair"]} •
                {st.session_state["last_timeframe"]}
            </div>
            <div class="signal-value">
                {result["signal"]}
            </div>
            <div class="small">
                Strength: {result["strength"]} |
                Confidence: {result["confidence"]}%
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Analysis")

    c1, c2 = st.columns(2)
    c1.metric("Trend", result.get("trend", "-"))
    c2.metric("RSI", result.get("rsi", "-"))

    c3, c4 = st.columns(2)
    c3.metric("Pattern", result.get("pattern", "-"))
    c4.metric("MACD", result.get("macd", "-"))

    st.markdown(
        f"""
        <div class="card">
        <b>Support:</b> {result.get("support", "-")}<br>
        <b>Resistance:</b> {result.get("resistance", "-")}<br>
        <b>Price:</b> {result.get("price", "-")}<br>
        <b>UP Score:</b> {result.get("up_score", "-")}<br>
        <b>DOWN Score:</b> {result.get("down_score", "-")}<br><br>
        <b>Decision:</b> {result.get("reason", "-")}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption(
        f"Data source: {st.session_state.get('last_source', '-')}. "
        "Signal is a probability-based analysis, not a guaranteed prediction."
    )

# =========================
# HISTORY
# =========================

st.markdown("### Signal History")

history = st.session_state.get("history", [])

if history:
    st.dataframe(
        pd.DataFrame(history),
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("No signals generated yet.")

st.markdown("### Important")
st.write(
    "The bot intentionally returns NO TRADE when the main trend is unclear "
    "or the indicators conflict. This is a risk-control rule, not a guarantee "
    "of profit."
)
'''

requirements = """streamlit>=1.35
pandas>=2.0
numpy>=1.24
"""

readme = """# HASSAN MALIK AI BOT

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Important

This version is a DEMO/TEST dashboard. It does not connect automatically to Quotex
and does not claim to predict the next candle with certainty.

For real market use, connect a lawful/reliable OHLC market-data source to the
`candles` input. Do not treat generated demo candles as live market data.

CSV upload columns:
`open, high, low, close`
"""

outdir = Path("/mnt/data/hassan_malik_ai_bot")
outdir.mkdir(exist_ok=True)

(outdir / "app.py").write_text(app, encoding="utf-8")
(outdir / "requirements.txt").write_text(requirements, encoding="utf-8")
(outdir / "README.txt").write_text(readme, encoding="utf-8")

zip_path = Path("/mnt/data/HASSAN_MALIK_AI_BOT.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    z.write(outdir / "app.py", "app.py")
    z.write(outdir / "requirements.txt", "requirements.txt")
    z.write(outdir / "README.txt", "README.txt")

print(f"Created: {zip_path}")
