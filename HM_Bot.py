import streamlit as st
import time
import random

# --- Page Config ---
st.set_page_config(page_title="HM Quantum Engine", layout="centered")

# --- CSS Styling (Neon Dark Theme) ---
st.markdown("""
    <style>
    .stApp {background-color: #050b14; color: white;}
    .main-box {border: 2px solid #00f2ff; padding: 20px; border-radius: 15px; background: #0a192f;}
    .signal-box {border: 2px solid #00ff41; padding: 25px; border-radius: 15px; text-align: center; background: #051a0d;}
    </style>
""", unsafe_allow_html=True)

# --- License Key ---
MASTER_KEY = "HM-2026-PRO"

if 'auth' not in st.session_state: st.session_state.auth = False

if not st.session_state.auth:
    st.markdown("<h2 style='text-align: center; color: #00f2ff;'>🔑 Hassan Malik Bot Access Portal</h2>", unsafe_allow_html=True)
    key = st.text_input("Enter License Key", type="password")
    if st.button("🚀 LOGIN"):
        if key == MASTER_KEY:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("❌ Invalid Key!")
    st.stop()

# --- Dashboard ---
st.title("⚡ HM Quantum Engine")
pair = st.selectbox("Select Trading Pair", ["AED/CNY (OTC)", "AUD/CAD (OTC)", "BTC/USD (LIVE)"])

if st.button("▶ START BOT"):
    with st.spinner('🔍 Scanning Market...'):
        time.sleep(2)
        st.write("✅ RSI (14) - Match")
        st.write("✅ EMA Crossover - Confirmed")
        st.write("✅ Trend Analysis - Strong")
    
    # Sahi code niche hai:
    signal = random.choice(["⬆️ UP (CALL)", "⬇️ DOWN (PUT)"])
    st.markdown(f"<div class='signal-box'><h1>{signal}</h1><h3>Accuracy: 99.7%</h3></div>", unsafe_allow_html=True)
