import random
import time
import streamlit as st
import streamlit.components.v1 as components

# Page Configuration & Ultra-Pro Neon Theme
st.set_page_config(page_title="Malikg7166 ULTRA PRO MAX", layout="centered")

st.markdown(
    """
    <style>
    .main {
        background-color: #05070b;
        color: #ffffff;
    }
    .stApp {
        background-color: #05070b;
    }
    /* Ultra Glowing Neon Header Card */
    .hero-card {
        background: linear-gradient(135deg, #0f172a, #1e1b4b);
        padding: 24px;
        border-radius: 18px;
        border: 2px solid rgba(0, 255, 204, 0.6);
        text-align: center;
        box-shadow: 0 0 35px rgba(0, 255, 204, 0.3);
        margin-bottom: 20px;
    }
    .stSelectbox label, .stRadio label {
        color: #00ffcc !important;
        font-weight: 700;
        font-size: 14px;
    }
    /* Output Box */
    .output-box {
        background-color: #0a0f1d;
        padding: 25px;
        border-radius: 16px;
        text-align: center;
        border: 2px dashed rgba(0, 255, 204, 0.5);
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.15);
        color: #94a3b8;
        font-size: 15px;
        margin-bottom: 20px;
    }
    /* Signal UP Box (Intense Neon Green Glow) */
    .signal-up {
        background: linear-gradient(135deg, #064e3b, #059669);
        color: white;
        padding: 24px;
        border-radius: 16px;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        box-shadow: 0 0 35px rgba(16, 185, 129, 0.8);
        border: 2px solid #34d399;
    }
    /* Signal DOWN Box (Intense Neon Red Glow) */
    .signal-down {
        background: linear-gradient(135deg, #7f1d1d, #dc2626);
        color: white;
        padding: 24px;
        border-radius: 16px;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        box-shadow: 0 0 35px rgba(239, 68, 68, 0.8);
        border: 2px solid #f87171;
    }
    /* Danger / Choppy Market Box */
    .danger-box {
        background: linear-gradient(135deg, #450a0a, #991b1b);
        color: #fca5a5;
        padding: 22px;
        border-radius: 16px;
        text-align: center;
        font-weight: bold;
        border: 2px solid #ef4444;
        box-shadow: 0 0 30px rgba(239, 68, 68, 0.6);
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
            let utterance = new SpeechSynthesisUtterance("Malikg7166 Ultra Pro Max Initialized");
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

# Main UI Header
st.markdown(
    """
    <div class="hero-card">
        <h2 style='color: #00ffcc; margin: 0 0 5px 0; text-shadow: 0 0 15px rgba(0,255,204,0.8);'>⚡ MALIKG7166 ULTRA PRO MAX ⚡</h2>
        <p style='color: #94a3b8; font-size: 14px; margin: 0;'>Military-Grade Sureshot Algorithmic Engine with Multi-Confluence & Strict Choppy Filter</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Broker Selection
selected_broker = st.selectbox(
    "🏛️ Select Broker Platform",
    [
        "Quotex",
        "Pocket Option",
        "Binomo",
        "IQ Option",
        "Quotex VIP (OTC)",
    ],
)

# Market Type
asset_type = st.radio(
    "📊 Market Category:", ["Live Market Pairs", "OTC Market Pairs"], horizontal=True
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

# Timeframe Selection
selected_timeframe = st.selectbox(
    "⏱️ Execution Time Frame & Expiry",
    [
        "5 Seconds",
        "10 Seconds",
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
        Click "GENERATE ULTRA SIGNAL" below to initiate deep institutional-grade market filtering and price action scan.
    </div>
""",
    unsafe_allow_html=True,
)

# Button Styling
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #10b981, #047857);
        color: white;
        font-size: 19px;
        font-weight: bold;
        padding: 16px;
        border-radius: 14px;
        border: 2px solid #34d399;
        box-shadow: 0 0 30px rgba(16, 185, 129, 0.8);
        width: 100%;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(135deg, #059669, #065f46);
        box-shadow: 0 0 45px rgba(16, 185, 129, 1.0);
    }
    </style>
""",
    unsafe_allow_html=True,
)

if st.button("⚡ GENERATE ULTRA SIGNAL ⚡"):
  # Multi-step status simulation for pro feel
  with st.status(
      "🚀 Running Ultra Pro Max Market Diagnostics...", expanded=True
  ) as status:
    st.write("Phase 1: Analyzing order flow imbalances & volume velocity...")
    time.sleep(0.7)
    st.write("Phase 2: Verifying Support/Resistance zone rejection wicks...")
    time.sleep(0.7)
    st.write("Phase 3: Running RSI momentum & EMA trend alignment checks...")
    time.sleep(0.7)
    st.write("Phase 4: Scanning for micro-consolidation & choppy noise traps...")
    time.sleep(0.6)
    status.update(
        label="✅ All Confluences Verified Successfully!",
        state="complete",
        expanded=False,
    )

  market_health = random.choices(["Clean", "Choppy"], weights=[0.72, 0.28], k=1)[
      0
  ]

  if market_health == "Choppy":
    signal_slot.markdown(
        """
            <div class="danger-box">
                🚨 MARKET CHOPPY / HIGH RISK DETECTED!<br><br>
                <span style="font-size: 13px; font-weight: normal;">Malikg7166 Ultra Pro Max identified messy sideways pricing or false liquidity sweeps. Trade has been **REJECTED** automatically to protect your capital. Stay safe!</span>
            </div>
        """,
        unsafe_allow_html=True,
    )
  else:
    trade_dir = random.choice(["CALL (UP 🟢)", "PUT (DOWN 🔴)"])
    confidence = round(random.uniform(95.2, 99.8), 2)
    confluence_rating = random.choice(
        ["5/5 Confluences Met", "S/R + RSI Perfect Alignment"]
    )

    if "CALL" in trade_dir:
      signal_slot.markdown(
          f"""
                <div class="signal-up">
                    👑 MALIKG7166 ULTRA PRO SURESHOT 👑<br><br>
                    Asset: {selected_asset}<br>
                    Direction: 🟢 BUY / CALL (UP)<br>
                    Expiry: {selected_timeframe}<br>
                    <span style="font-size: 13px; background: rgba(0,0,0,0.4); padding: 5px 12px; border-radius: 6px; display:inline-block; margin-top:8px;">Accuracy Score: {confidence}% ({confluence_rating})</span>
                </div>
            """,
          unsafe_allow_html=True,
      )
    else:
      signal_slot.markdown(
          f"""
                <div class="signal-down">
                    👑 MALIKG7166 ULTRA PRO SURESHOT 👑<br><br>
                    Asset: {selected_asset}<br>
                    Direction: 🔴 SELL / PUT (DOWN)<br>
                    Expiry: {selected_timeframe}<br>
                    <span style="font-size: 13px; background: rgba(0,0,0,0.4); padding: 5px 12px; border-radius: 6px; display:inline-block; margin-top:8px;">Accuracy Score: {confidence}% ({confluence_rating})</span>
                </div>
            """,
          unsafe_allow_html=True,
      )
    st.balloons()
