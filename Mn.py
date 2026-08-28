def rsi(x, n=14):
    if len(x) < n + 1:
        return 50
    d = np.diff(x)
    g = np.maximum(d, 0)
    l = np.maximum(-d, 0)
    ag, al = np.mean(g[-n:]), np.mean(l[-n:])
    return 100 if al == 0 else 100 - 100 / (1 + ag / al)


def analyze(x):
    s = pd.Series(x)
    e9 = s.ewm(span=9, adjust=False).mean().iloc[-1]
    e21 = s.ewm(span=21, adjust=False).mean().iloc[-1]
    e50 = s.ewm(span=50, adjust=False).mean().iloc[-1]
    R = rsi(x)

    score = 0
    if e9 > e21 > e50:
        trend = "UP"
        score += 4
    elif e9 < e21 < e50:
        trend = "DOWN"
        score += 4
    else:
        trend = "SIDEWAYS"

    if R >= 55:
        score += 2
    elif R <= 45:
        score += 2

    if x[-1] > x[-3]:
        score += 2
    else:
        score += 2

    if trend == "UP" and R >= 50:
        sig = "UP"
    elif trend == "DOWN" and R < 50:
        sig = "DOWN"
    else:
        sig = "NO TRADE"

   file = st.file_uploader(
    "Historical OHLC CSV",
    type="csv"
)

def analyze(x):
    s = pd.Series(x)
    e9 = s.ewm(span=9, adjust=False).mean().iloc[-1]
    e21 = s.ewm(span=21, adjust=False).mean().iloc[-1]
    e50 = s.ewm(span=50, adjust=False).mean().iloc[-1]

    if e9 > e21 > e50:
        trend = "UP"
        signal = "UP"
    elif e9 < e21 < e50:
        trend = "DOWN"
        signal = "DOWN"
    else:
        trend = "SIDEWAYS"
        signal = "NO TRADE"

    return signal, trend


if st.button("🚀 NEXT CANDLE", use_container_width=True):

    if file is None:
        st.warning("پہلے OHLC CSV upload کریں۔")
        st.stop()

    df = pd.read_csv(file)

    close = next(
        (c for c in df.columns if c.strip().lower() == "close"),
        None
    )

    if close is None:
        st.error("CSV میں Close column لازمی ہے۔")
        st.stop()

    x = pd.to_numeric(
        df[close], errors="coerce"
    ).dropna().values

    if len(x) < 60:
        st.error("کم از کم 60 candles درکار ہیں۔")
        st.stop()

    signal, trend = analyze(x)

    if signal == "UP":
        st.success("⬆️ NEXT CANDLE: UP")
    elif signal == "DOWN":
        st.error("⬇️ NEXT CANDLE: DOWN")
    else:
        st.warning("⏸️ NO TRADE")

    st.metric("PAIR", pair)
    st.metric("TREND", trend) conf = min(95, 50 + score * 5)
    return sig, conf, trend, R


if st.button("🚀 NEXT CANDLE", use_container_width=True):

    if file:
        df = pd.read_csv(file)
        c = next(
            (z for z in df.columns if z.strip().lower() == "close"),
            None
        )

        if c is None:
            st.error("CSV میں Close column لازمی ہے۔")
            st.stop()

        x = pd.to_numeric(
            df[c], errors="coerce"
        ).dropna().values

        if len(x) < 60:
            st.error("کم از کم 60 candles درکار ہیں۔")
            st.stop()

    else:
        st.warning("Live data کے لیے OHLC data/API ضروری ہے۔")
        st.stop()

    sig, conf, trend, R = analyze(x)

    if sig == "UP":
        st.success(f"⬆️ NEXT CANDLE: UP | {conf}%")
    elif sig == "DOWN":
        st.error(f"⬇️ NEXT CANDLE: DOWN | {conf}%")
    else:
        st.warning(f"⏸️ NO TRADE | {conf}%")

    a, b, c, d = st.columns(4)
    a.metric("PAIR", pair)
    b.metric("TREND", trend)
    c.metric("RSI", f"{R:.1f}")
    d.metric("CONFIDENCE", f"{conf}%")
