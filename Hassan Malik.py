import streamlit as st
import streamlit.components.v1 as components

# Page config to hide Streamlit default paddings and make it truly mobile full screen
st.set_page_config(
    page_title="Sun Malik Board Pro",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Injecting CSS to hide Streamlit header, footer and margins
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding-top: 0rem; padding-bottom: 0rem; padding-left: 0rem; padding-right: 0rem;}
        iframe {border: none !important;}
    </style>
""", unsafe_allow_html=True)

# Main HTML + CSS + JS Single Confluence Engine Code Block
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Sun Malik Board Pro</title>
    <script src="https://jsdelivr.net"></script>
    <script src="https://unpkg.com"></script>
    <style>
        body {
            background-color: #020617;
            font-family: system-ui, -apple-system, sans-serif;
            -webkit-tap-highlight-color: transparent;
        }
        .neon-text-blue { text-shadow: 0 0 12px rgba(14, 165, 233, 0.7); }
        .neon-border-gold {
            box-shadow: 0 0 15px rgba(234, 179, 8, 0.15);
            border: 1px solid rgba(234, 179, 8, 0.35);
        }
        .custom-scrollbar::-webkit-scrollbar { height: 3px; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #334155; border-radius: 4px; }
    </style>
</head>
<body class="flex justify-center items-center h-screen overflow-hidden bg-slate-950 p-2">

    <div class="w-full max-w-md h-[96vh] bg-gradient-to-b from-slate-950 via-slate-900 to-black rounded-2xl p-3.5 shadow-2xl border border-slate-800 flex flex-col justify-between overflow-hidden">
        
        <div class="space-y-2.5">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-2.5">
                    <div class="w-10 h-10 bg-gradient-to-tr from-sky-400 to-blue-600 rounded-xl flex items-center justify-center p-0.5 shadow-lg shadow-blue-500/10">
                        <div class="w-full h-full bg-slate-950 rounded-[9px] flex items-center justify-center">
                            <i data-lucide="cpu" class="w-6 h-6 text-sky-400 animate-pulse"></i>
                        </div>
                    </div>
                    <div>
                        <h1 class="text-lg font-black tracking-tight text-white neon-text-blue">Sun Malik Board Pro</h1>
                        <div class="flex items-center gap-1 mt-0.5">
                            <span class="text-[9px] font-bold bg-sky-500/10 text-sky-400 px-1 py-0.5 rounded border border-sky-500/20 flex items-center gap-1">
                                <span class="w-1 h-1 rounded-full bg-sky-400 animate-pulse"></span> CONFLUENCE ENGINE
                            </span>
                            <span class="text-[9px] font-black bg-gradient-to-r from-amber-500 to-yellow-400 text-slate-950 px-1.5 py-0.5 rounded shadow">PRO MAX</span>
                        </div>
                    </div>
                </div>
                
                <div class="text-right bg-slate-900/80 px-2 py-1 rounded-lg border border-slate-800">
                    <div class="flex items-center justify-end gap-1 text-[10px] text-emerald-400 font-bold">
                        <span class="w-1 h-1 rounded-full bg-emerald-500 animate-ping"></span> LIVE SCANNING
                    </div>
                    <div class="text-[9px] text-slate-400 font-medium tracking-wide">Hasan Malik Pro v5.0</div>
                </div>
            </div>

            <div class="bg-gradient-to-r from-amber-500/5 via-yellow-500/15 to-amber-500/5 rounded-xl p-2 text-center neon-border-gold flex items-center justify-center gap-2">
                <i data-lucide="shield-check" class="w-3.5 h-3.5 text-yellow-400"></i>
                <span class="text-[10px] font-black uppercase tracking-wider text-yellow-300">STRUCTURE & CONFIRMATION ACTIVATED</span>
            </div>

            <div>
                <label class="block text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1 flex items-center gap-1">
                    <i data-lucide="globe" class="w-3 h-3 text-sky-400"></i> Select Trading Stream
                </label>
                <div class="grid grid-cols-2 gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">
                    <button id="btn-live" onclick="setMarket('LIVE')" class="py-2 rounded-lg text-[11px] font-black uppercase transition-all flex items-center justify-center gap-1.5 text-slate-400 hover:text-white cursor-pointer">
                        <i data-lucide="activity" class="w-3.5 h-3.5"></i> Live Pairs
                    </button>
                    <button id="btn-otc" onclick="setMarket('OTC')" class="py-2 rounded-lg text-[11px] font-black uppercase transition-all flex items-center justify-center gap-1.5 bg-gradient-to-r from-sky-600 to-blue-600 text-white shadow-lg cursor-pointer">
                        <i data-lucide="shuffle" class="w-3.5 h-3.5"></i> OTC Pairs
                    </button>
                </div>
            </div>

            <div>
                <label class="block text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1 flex items-center gap-1">
                    <i data-lucide="layers" class="w-3 h-3 text-sky-400"></i> Asset Selection (9-10 Setup Matrix)
                </label>
                <div class="relative">
                    <select id="asset-selector" onchange="clearSignalBox()" class="w-full bg-slate-950 border border-slate-800 text-white rounded-xl p-2.5 text-xs font-bold focus:outline-none focus:border-sky-500 appearance-none cursor-pointer">
                    </select>
                    <div class="absolute right-3 top-3 pointer-events-none text-slate-400">
                        <i data-lucide="chevron-down" class="w-3.5 h-3.5"></i>
                    </div>
                </div>
            </div>

            <div>
                <label class="block text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1 flex items-center gap-1">
                    <i data-lucide="clock" class="w-3 h-3 text-sky-400"></i> Analysis Timeframe
                </label>
                <div class="flex overflow-x-auto gap-1 pb-1 custom-scrollbar snap-x">
                    <button onclick="setTimeframe(this, '5s')" class="tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[11px] font-bold bg-sky-600 text-white border border-sky-500/20 cursor-pointer">5s</button>
                    <button onclick="setTimeframe(this, '10s')" class="tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[11px] font-bold bg-slate-950 text-slate-400 border border-slate-800 hover:text-white cursor-pointer">10s</button>
                    <button onclick="setTimeframe(this, '15s')" class="tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[11px] font-bold bg-slate-950 text-slate-400 border border-slate-800 hover:text-white cursor-pointer">15s</button>
                    <button onclick="setTimeframe(this, '30s')" class="tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[11px] font-bold bg-slate-950 text-slate-400 border border-slate-800 hover:text-white cursor-pointer">30s</button>
                    <button onclick="setTimeframe(this, '1m')" class="tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[11px] font-bold bg-slate-950 text-slate-400 border border-slate-800 hover:text-white cursor-pointer">1m</button>
                    <button onclick="setTimeframe(this, '2m')" class="tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[11px] font-bold bg-slate-950 text-slate-400 border border-slate-800 hover:text-white cursor-pointer">2m</button>
                    <button onclick="setTimeframe(this, '5m')" class="tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[11px] font-bold bg-slate-950 text-slate-400 border border-slate-800 hover:text-white cursor-pointer">5m</button>
                </div>
            </div>
        </div>

        <div class="flex-1 flex items-center justify-center my-2 min-h-[140px]">
            <div id="signal-box" class="w-full p-3.5 rounded-xl border border-dashed border-slate-800 text-center bg-slate-950/20">
                <i data-lucide="eye" class="w-6 h-6 text-slate-600 mx-auto mb-1 animate-bounce"></i>
                <div class="text-[11px] text-slate-400 font-black uppercase tracking-wider">Ready to Check Matrix</div>
                <div class="text-[10px] text-slate-500 mt-1 max-w-[280px] mx-auto">Will analyze Structural Trend, Pattern Match, and Confirmation Candle for the NEXT trade.</div>
            </div>
        </div>

        <div class="space-y-2.5">
            <button id="generate-btn" onclick="processHighAccuracySignal()" class="w-full bg-gradient-to-r from-sky-500 via-blue-600 to-indigo-600 text-white font-black uppercase text-xs tracking-widest py-3.5 rounded-xl shadow-xl shadow-blue-500/5 hover:brightness-105 active:scale-[0.99] transition-all cursor-pointer flex items-center justify-center gap-2">
                <i data-lucide="activity" class="w-3.5 h-3.5 text-yellow-300"></i> Scan Market Strategy
            </button>

            <div class="bg-slate-950/80 p-2.5 rounded-xl border border-slate-900 grid grid-cols-3 gap-1 text-center text-[10px]">
                <div>
                    <span class="block text-slate-500 font-semibold">Candle Matrix</span>
                    <span class="block font-bold text-sky-400 mt-0.5 truncate">Price Action HFX</span>
                </div>
                <div class="border-x border-slate-800">
