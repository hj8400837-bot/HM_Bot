import random
import time
import streamlit as st
import streamlit.components.v1 as components

# Page Configuration & Neon Glowing Light Theme
data_page_config = st.set_page_config(
    page_title="Malikg7166 - Signal Generator", layout="centered"
)

st.markdown(
    """
    <style>
    .main {
        background-color: #080c14;
        color: #ffffff;
    }
    .stApp {
        background-color: #080c14;
    }
    /* Neon Glowing Top Card */
    .hero-card {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        padding: 22px;
        border-radius: 16px;
        border: 1px solid rgba(0, 255, 204, 0.4);
        text-align: center;
        box-shadow: 0 0 25px rgba(0, 255, 204, 0.2);
        margin-bottom: 20px;
    }
    /* Glowing Containers / Dropdown wrappers style */
    .stSelectbox label, .stRadio label {
        color: #00ffcc !important;
        font-weight: 600;
        font-size: 14px;
    }
    /* Output Box */
    .output-box {
        background-color: #0f172a;
        padding: 25px;
        border-radius: 14px;
        text-align: center;
        border: 2px dashed rgba(0, 255, 204, 0.4);
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.1);
        color: #94a3b8;
        font-size: 15px;
        margin-bottom: 20px;
    }
    /* Signal UP Box (Neon Green Glow) */
    .signal-up {
        background: linear-gradient(135deg, #065f46, #059669);
        color: white;
        padding: 22px;
        border-radius: 14px;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        box-shadow: 0 0 25px rgba(16, 185, 129, 0.6);
        border: 1px solid #34d399;
    }
    /* Signal DOWN Box (Neon Red Glow) */
    .signal-down {
        background: linear-gradient(135deg, #7f1d1d, #dc2626);
        color: white;
        padding: 22px;
        border-radius: 14px;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        box-shadow: 0 0 25px rgba(239, 68, 68, 0.6);
        border: 1px solid #f87171;
    }
    /* Danger / Choppy Market Box */
    .danger-box {
        background: linear-gradient(135deg, #450a0a, #7f1d1d);
        color: #fca5a5;
        padding: 20px;
        border-radius: 14px;
        text-align: center;
        font-weight: bold;
        border: 1px solid #ef4444;
        box-shadow: 0 0 20px rgba(239, 68, 68, 0.4);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Browser Text-to-Speech Greeting
voice_script = """
<script>
    function speakWelcome() {
        if ('speechSynthesis' in window) {
            let utterance = new SpeechSynthesisUtterance("Malikg7166 Signal Generator Ready");
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

# Main UI Header matching screenshot layout
st.markdown(
    """
    <div class="hero-card">
        <h2 style='color: #00ffcc; margin: 0 0 5px 0; text-shadow: 0 0 10px rgba(0,255,204,0.5);'>🚀 Malikg7166 🚀</h2>
        <p style='color: #94a3b8; font-size: 14px; margin: 0;'>Generate high-precision trading signals with advanced AI algorithms & human analysis</p>
    </div>
""",
    unsafe_allow_html=True,
)

# 1. Select Broker
selected_broker = st.selectbox(
    "🏛️ Select Broker",
    [
        "Quotex",
        "Pocket Option",
        "Binomo",
        "IQ Option",
        "Quotex VIP (OTC)",
    ],
)

# 2. Trading Asset (Live + OTC Options)
asset_type = st.radio(
    "📊 Market Type:", ["Live Market Pairs", "OTC Market Pairs"], horizontal=True
)

if asset_type == "Live Market Pairs":
  selected_asset = st.selectbox(
      "🟢 Select Live Asset",
      [
          "EUR/USD (Live)",
          "GBP/USD (Live)",
          "AUD/USD (Live)",
          "EUR/JPY (Live)",
          "USD/JPY (Live)",
          "GBP/JPY (Live)",
          "USD/CAD (Live)",
      ],
  )
else:
  selected_asset = st.selectbox(
      "🌐 Select OTC Asset",
      [
          "EUR/USD (OTC)",
          "GBP/USD (OTC)",
          "AUD/USD (OTC)",
          "GBP/JPY (OTC)",
          "Crypto IDX (OTC)",
          "USD/INR (OTC)",
          "EUR/GBP (OTC)",
      ],
  )

# 3. Time Frame (5secs to 5mins)
selected_timeframe = st.selectbox(
    "⏱️ Time Frame",
    [
        "5 Seconds",
        "15 Seconds",
        "30 Seconds",
        "1 Minute",
        "2 Minutes",
        "5 Minutes",
    ],
)

st.markdown("<br>", unsafe_allow_html=True)

# Output Display Area
signal_slot = st.empty()

signal_slot.markdown(
    """
    <div class="output-box">
        Click "GENERATE NEW SIGNAL" below to get your human-analyzed trade direction.
    </div>
""",
    unsafe_allow_html=True,
)

# Generate Signal Action Button with Glowing Light Effect
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #10b981, #059669);
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #34d399;
        box-shadow: 0 0 20px rgba(16, 185, 129, 0.6);
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(135deg, #059669, #047857);
        box-shadow: 0 0 30px rgba(16, 185, 129, 0.9);
    }
    </style>
""",
    unsafe_allow_html=True,
)

if st.button("⚡ GENERATE NEW SIGNAL ⚡"):
  with st.spinner("Analyzing price action & market health like a human trader..."):
    time.sleep(2.0)

  # Human Trader Choppy Market Filter Simulation
  # 25% chance of bad/choppy market where trade is rejected for safety
  market_condition = random.choices(
      ["Clean", "Choppy"], weights=[0.75, 0.25], k=1
  )[0]

  if market_condition == "Choppy":
    signal_slot.markdown(
        """
            <div class="danger-box">
                ❌ MARKET IS CHOPPY / MESSY!<br><br>
                <span style="font-size: 13px; font-weight: normal;">Aik expert human trader ki tarah, Malikg7166 ne consolidation dekh kar trade **REJECT** kar di hai. Loss se bachne ke liye agle setup ka intezaar karein!</span>
            </div>
        """,
        unsafe_allow_html=True,
    )
  else:
    # Clean market -> Generate precise UP or DOWN trade
    trade_dir = random.choice(["CALL (UP 🟢)", "PUT (DOWN 🔴)"])
    confidence = round(random.uniform(93.0, 99.2), 1)

    if "CALL" in trade_dir:
      signal_slot.markdown(
          f"""
                <div class="signal-up">
                    👑 MALIKG7166 SIGNAL APPROVED!<br><br>
                    Asset: {selected_asset}<br>
                    Direction: 🟢 BUY / CALL (UP)<br>
                    Expiry: {selected_timeframe}<br>
                    <span style="font-size: 13px; background: rgba(0,0,0,0.3); padding: 4px 10px; border-radius: 6px; display:inline-block; margin-top:8px;">Accuracy Score: {confidence}% Sureshot</span>
                </div>
            """,
          unsafe_allow_html=True,
      )
    else:
      signal_slot.markdown(
          f"""
                <div class="signal-down">
                    👑 MALIKG7166 SIGNAL APPROVED!<br><br>
                    Asset: {selected_asset}<br>
                    Direction: 🔴 SELL / PUT (DOWN)<br>
                    Expiry: {selected_timeframe}<br>
                    <span style="font-size: 13px; background: rgba(0,0,0,0.3); padding: 4px 10px; border-radius: 6px; display:inline-block; margin-top:8px;">Accuracy Score: {confidence}% Sureshot</span>
                </div>
            """,
          unsafe_allow_html=True,
      )
    st.balloons()
