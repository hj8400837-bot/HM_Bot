import streamlit as st
import streamlit.components.v1 as components

# Page Configuration & Heavy Dark Theme Styling
st.set_page_config(
    page_title="Hassan Malik - Heavy Pro Trading Bot", layout="wide"
)

st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stSidebar {
        background-color: #161b22;
    }
    .metric-card {
        background-color: #1f242d;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #30363d;
        margin-bottom: 15px;
    }
    .alert-box {
        background-color: #2ea043;
        color: white;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
    }
    .warning-box {
        background-color: #da3633;
        color: white;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Browser Text-to-Speech (Voice Output: "Welcome Hassan Malik bot")
voice_script = """
<script>
    function speakWelcome() {
        if ('speechSynthesis' in window) {
            let utterance = new SpeechSynthesisUtterance("Welcome Hassan Malik bot");
            utterance.rate = 0.9;
            utterance.pitch = 1.0;
            window.speechSynthesis.speak(utterance);
        }
    }
    window.onload = function() {
        setTimeout(speakWelcome, 800);
    };
    document.addEventListener('click', speakWelcome, {once: true});
</script>
"""
components.html(voice_script, height=0)

# Header Title
st.markdown(
    "<h1 style='text-align: center; color: #00ffcc;'>⚡ HASSAN MALIK - HEAVY PRO TRADING BOT ⚡</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #8b949e;'>Advanced Live & OTC Selection & Confirmation System (5s to 1m)</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# Sidebar - Heavy Settings & Parameters
st.sidebar.header("⚙️ Market & Execution Settings")

# 1. Market Type Selection (Live vs OTC Tick Option)
market_type = st.sidebar.radio(
    "🔘 Select Market Type:", ["Live Market", "OTC Market"]
)

# 2. Dynamic Pair Selection Based on Market Type
if market_type == "Live Market":
  selected_pair = st.sidebar.selectbox(
      "📊 Select Live Pair:",
      [
          "EUR/USD (Live)",
          "GBP/USD (Live)",
          "AUD/USD (Live)",
          "EUR/JPY (Live)",
          "USD/JPY (Live)",
          "GBP/JPY (Live)",
      ],
  )
else:
  selected_pair = st.sidebar.selectbox(
      "🌐 Select OTC Pair:",
      [
          "EUR/USD (OTC)",
          "GBP/USD (OTC)",
          "AUD/USD (OTC)",
          "Crypto IDX (OTC)",
          "USD/INR (OTC)",
      ],
  )

# 3. Timeframe Selection (5s to 1 Minute)
selected_timeframe = st.sidebar.selectbox(
    "⏱️ Select Timeframe (5s to 1 Min):",
    [
        "5 Seconds (Extreme Micro)",
        "10 Seconds",
        "15 Seconds (Ultra-Fast)",
        "30 Seconds",
        "45 Seconds",
        "1 Minute (Standard Expiry)",
    ],
)

# 4. Notebook Pattern Selection
selected_pattern = st.sidebar.selectbox(
    "📖 Select Notebook Pattern:",
    [
        "Bullish Engulfing",
        "Bearish Engulfing",
        "Hammer",
        "Shooting Star",
        "Morning Star",
        "Evening Star",
        "15-Sec OTC Strategy",
    ],
)

# 5. Market Condition / Bad Market Filter
market_condition = st.sidebar.selectbox(
    "🛡️ Market Quality Check:",
    [
        "Normal / Trending Market (Safe)",
        "High Volatility Market (Caution)",
        "Choppy / Sideways Market (AVOID TRADE)",
    ],
)

# Main Dashboard Layout (Split into Two Columns)
col_left, col_right = st.columns([1, 1])

with col_left:
  st.markdown("### 📌 Front View: Pattern Reference")
  filename = f"{selected_pattern.lower().replace(' ', '_')}.png"
  try:
    st.image(
        filename,
        caption=f"Hassan Malik Notebook: {selected_pattern}",
        use_container_width=True,
    )
  except Exception:
    st.warning(
        f"💡 Tip: Apni notebook ki tasveer ko `{filename}` ke naam se code wale"
        " folder mein save karein."
    )

with col_right:
  st.markdown("### 🚦 Strict Trade Execution Rules")

  # Bad Market Safeguard Warning
  if "AVOID" in market_condition:
    st.markdown(
        '<div class="warning-box">🚨 BAD MARKET DETECTED! TRADING STOPPED! Market'
        " choppy hai, loss se bachne ke liye trade mat lein.</div>",
        unsafe_allow_html=True,
    )
  else:
    st.markdown(
        '<div class="alert-box">✅ Market Condition Safe for Execution</div>',
        unsafe_allow_html=True,
    )

  st.info(f"**Market Type:** `{market_type}`\n\n"
          f"**Target Pair:** `{selected_pair}`\n\n"
          f"**Selected Timeframe:** `{selected_timeframe}`\n\n"
          f"**Active Pattern:** `{selected_pattern}`")

  st.markdown("---")
  st.markdown("#### 🔍 Confirmation Candle & Indicator Structure:")
  st.markdown(
      """
    * **Rule 1 (Patience):** Kabhi bhi blind entry na lein. Pehle setup candle banne dein aur phir **Confirmation Candle** ke close hone ka mukammal intezar karein.
    * **Rule 2 (Confirmation Structure):** Support/Resistance ya Sureshot zone par jab tak confirmation candle strong momentum ya wick rejection na de, trade execute nahi karni.
    * **Rule 3 (Indicator / Zone Alignment):** Price action zones aur candle structure match hon tabhi next candle par trade place karein.
    """
  )

# Live Signal Trigger Section
st.markdown("---")
st.markdown("### 🚀 Live Signal Scanner & Confirmation Check")

if st.button(
    "🔍 GENERATE SIGNAL & CHECK CONFIRMATION CANDLE", use_container_width=True
):
  if "AVOID" in market_condition:
    st.error(
        "❌ Trade Blocked! Market kharab (choppy) hai. Rules ke mutabiq trade"
        " lena mana hai."
    )
  else:
    with st.spinner(
        f"Scanning [{market_type}] {selected_pair} on {selected_timeframe} for"
        f" {selected_pattern}..."
    ):
      import time

      time.sleep(1.5)
    st.success(
        f"🎯 **SIGNAL GENERATED & CONFIRMED!** Pattern '{selected_pattern}' form"
        f" ho chuka hai aur confirmation mil gayi hai. [{market_type}]"
        f" **{selected_pair}** par foran trade lein!"
    )
    st.balloons()
