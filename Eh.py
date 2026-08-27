import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="Hassan Malik Bot Pro",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Strict framework mask to remove native Streamlit gaps
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0px !important; margin: 0px !important;}
        iframe {border: none !important; width: 100% !important; height: 100vh !important;}
    </style>
""", unsafe_allow_html=True)

# 3. Clean and Complete HTML/JS Component Layout
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Hassan Malik Bot Pro</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body { background-color: #030712; font-family: sans-serif; -webkit-tap-highlight-color: transparent; }
        .neon-blue { text-shadow: 0 0 15px rgba(14,165,233,0.8); }
        .neon-gold { box-shadow: 0 0 15px rgba(234,179,8,0.2); border: 1px solid rgba(234,179,8,0.4); }
        .custom-scroll::-webkit-scrollbar { height: 3px; }
        .custom-scroll::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 4px; }
    </style>
</head>
<body class="flex justify-center items-center h-screen overflow-hidden bg-slate-950 p-2">

    <div class="w-full max-w-md h-[96vh] bg-gradient-to-b from-slate-950 via-slate-900 to-black rounded-2xl p-4 shadow-2xl border border-slate-800 flex flex-col justify-between overflow-hidden">
        
        <div class="space-y-2.5">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                    <div class="w-11 h-11 bg-gradient-to-tr from-cyan-400 via-blue-600 to-indigo-600 rounded-xl flex items-center p-0.5 shadow-lg shadow-blue-500/20">
                        <div class="w-full h-full bg-slate-950 rounded-[10px] flex items-center justify-center">
                            <i data-lucide="bot" class="w-6 h-6 text-cyan-400"></i>
                        </div>
                    </div>
                    <div>
                        <h1 class="text-xl font-black tracking-tight text-white neon-blue">Hassan Malik Bot</h1>
                        <div class="flex items-center gap-1.5 mt-0.5">
                            <span class="text-[9px] font-bold bg-blue-500/20 text-blue-400 px-1.5 py-0.5 rounded border border-blue-500/30 flex items-center gap-1">
                                <span class="w-1 h-1 rounded-full bg-blue-400 animate-pulse"></span> AI BOT
                            </span>
                            <span class="text-[9px] font-black bg-gradient-to-r from-amber-500 to-yellow-400 text-slate-950 px-2 py-0.5 rounded shadow">PRO MAX</span>
                        </div>
                    </div>
                </div>
                
                <div class="text-right bg-slate-900/60 p-2 rounded-xl border border-slate-800/80">
                    <div class="flex items-center justify-end gap-1.5 text-emerald-400 font-bold text-[10px]">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span> ONLINE
                    </div>
                    <div class="text-[9px] text-gray-400 mt-0.5 font-medium">Active Users: 1M+</div>
                </div>
            </div>

            <div class="bg-gradient-to-r from-amber-500/10 via-yellow-500/20 to-amber-500/10 rounded-xl p-2 text-center neon-gold flex items-center justify-center gap-2">
                <i data-lucide="crown" class="w-3.5 h-3.5 text-yellow-400 animate-bounce"></i>
                <span class="text-[10px] font-black uppercase tracking-wider text-yellow-300">85% - 90% WIN RATE ACCURACY LOCKED</span>
            </div>

            <div>
                <label class="block text-[9px] font-bold text-slate-400 uppercase transition-all mb-1 flex items-center gap-1">
                    <i data-lucide="globe" class="w-3 h-3 text-cyan-400"></i> Select Market Mode
                </label>
                <div class="grid grid-cols-2 gap-1.5 bg-slate-950 p-1 rounded-xl border border-slate-800">               
                    <button id="btn-live" onclick="setMarket('LIVE')" class="py-1.5 rounded-lg text-[10px] font-black uppercase transition-all flex items-center justify-center gap-1 text-slate-400 hover:text-white cursor-pointer">Live Market</button>
                    <button id="btn-otc" onclick="setMarket('OTC')" class="py-1.5 rounded-lg text-[10px] font-black uppercase transition-all flex items-center justify-center gap-1 bg-gradient-to-r from-cyan-600 to-blue-600 text-white shadow-lg cursor-pointer">OTC Market</button>
                </div>
            </div>

            <div>
                <label class="block text-[9px] font-bold text-slate-400 uppercase transition-all mb-1 flex items-center gap-1">
                    <i data-lucide="layers" class="w-3 h-3 text-cyan-400"></i> Asset Selection Matrix
                </label>
                <div class="relative">
                    <select id="asset-selector" onchange="clearSignalBox()" class="w-full bg-slate-950 border border-slate-800 text-white rounded-xl p-2 text-xs font-bold focus:outline-none appearance-none cursor-pointer"></select>
                    <div class="absolute right-3 top-2.5 pointer-events-none text-slate-400"><i data-lucide="chevron-down" class="w-3.5 h-3.5"></i></div>
                </div>
            </div>

            <div>
                <label class="block text-[9px] font-bold text-slate-400 uppercase transition-all mb-1 flex items-center gap-1">
                    <i data-lucide="clock" class="w-3 h-3 text-cyan-400"></i> Chart Timeframe (Candle Period)
                </label>
                <div class="flex overflow-x-auto gap-1 pb-1 custom-scroll snap-x">
                    <button onclick="setTimeframe(this,'5s','5 Seconds')" class="tf-btn snap-start shrink-0 px-2.5 py-1 rounded-lg text-[10px] font-bold bg-cyan-600 text-white border border-cyan-500/20 cursor-pointer">5s</button>
                    <button onclick="setTimeframe(this,'15s','15 Seconds')" class="tf-btn snap-start shrink-0 px-2.5 py-1 rounded-lg text-[10px] font-bold bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer">15s</button>
                    <button onclick="setTimeframe(this,'30s','30 Seconds')" class="tf-btn snap-start shrink-0 px-2.5 py-1 rounded-lg text-[10px] font-bold bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer">30s</button>
                    <button onclick="setTimeframe(this,'1m','1 Minute')" class="tf-btn snap-start shrink-0 px-2.5 py-1 rounded-lg text-[10px] font-bold bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer">1m</button>
                    <button onclick="setTimeframe(this,'2m','2 Minutes')" class="tf-btn snap-start shrink-0 px-2.5 py-1 rounded-lg text-[10px] font-bold bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer">2m</button>
                    <button onclick="setTimeframe(this,'3m','3 Minutes')" class="tf-btn snap-start shrink-0 px-2.5 py-1 rounded-lg text-[10px] font-bold bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer">3m</button>
                    <button onclick="setTimeframe(this,'5m','5 Minutes')" class="tf-btn snap-start shrink-0 px-2.5 py-1 rounded-lg text-[10px] font-bold bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer">5m</button>
                </div>
            </div>
        </div>

    </div>
    <script>
        lucide.createIcons();
        function setMarket(m) { console.log(m); }
        function setTimeframe(el, t, label) { console.log(t); }
        function clearSignalBox() {}
    </script>
</body>
</html>
"""

# Render component cleanly without base64 truncation issues
components.html(html_content, height=650, scrolling=False)
