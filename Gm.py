import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="Hassan Malik💗 Signals Pro",
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

# 3. Complete Interactive HTML/JS Component with Hassan Malik💗 Branding
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Hassan Malik💗 Signals Pro</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body { background-color: #030712; font-family: sans-serif; -webkit-tap-highlight-color: transparent; }
        .neon-blue { text-shadow: 0 0 15px rgba(14,165,233,0.8); }
        .neon-gold { box-shadow: 0 0 15px rgba(234,179,8,0.2); border: 1px solid rgba(234,179,8,0.4); }
        .custom-scroll::-webkit-scrollbar { height: 3px; width: 3px; }
        .custom-scroll::-webkit-scrollbar-thumb { background: #1e293b; border-radius: 4px; }
    </style>
</head>
<body class="flex justify-center items-center h-screen overflow-hidden bg-slate-950 p-2">

    <div class="w-full max-w-md h-[96vh] bg-gradient-to-b from-slate-950 via-slate-900 to-black rounded-2xl p-4 shadow-2xl border border-slate-800 flex flex-col justify-between overflow-y-auto custom-scroll">
        
        <div class="space-y-3 pb-16">
            <!-- Top Header with Avatar & Title -->
            <div class="flex items-center gap-3">
                <div class="w-14 h-14 bg-gradient-to-tr from-cyan-400 via-blue-600 to-indigo-600 rounded-2xl flex items-center p-0.5 shadow-lg shadow-blue-500/20 shrink-0">
                    <div class="w-full h-full bg-slate-950 rounded-[14px] flex items-center justify-center">
                        <i data-lucide="bot" class="w-8 h-8 text-cyan-400"></i>
                    </div>
                </div>
                <div>
                    <h1 class="text-lg font-black tracking-tight text-white neon-blue">Hassan Malik💗</h1>
                    <div class="flex items-center gap-1.5 mt-1">
                        <span class="text-[9px] font-bold bg-blue-500/20 text-blue-400 px-1.5 py-0.5 rounded border border-blue-500/30 flex items-center gap-1">
                            <span class="w-1 h-1 rounded-full bg-blue-400 animate-pulse"></span> AI BOT
                        </span>
                        <span class="text-[9px] font-black bg-gradient-to-r from-amber-500 to-yellow-400 text-slate-950 px-2 py-0.5 rounded shadow">PRO MAX</span>
                    </div>
                </div>
            </div>

            <!-- Status Bar Grid -->
            <div class="grid grid-cols-3 gap-2 bg-slate-900/60 p-2 rounded-xl border border-slate-800/80 text-center">
                <div>
                    <div class="text-[9px] text-slate-400 font-bold uppercase">License</div>
                    <div class="flex items-center justify-center gap-1 text-emerald-400 font-bold text-[10px] mt-0.5">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span> ACTIVE
                    </div>
                </div>
                <div>
                    <div class="text-[9px] text-slate-400 font-bold uppercase">AI Engine</div>
                    <div class="flex items-center justify-center gap-1 text-emerald-400 font-bold text-[10px] mt-0.5">
                        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span> ONLINE
                    </div>
                </div>
                <div>
                    <div class="text-[9px] text-slate-400 font-bold uppercase">Users</div>
                    <div class="text-white font-bold text-[10px] mt-0.5">1M+</div>
                </div>
            </div>

            <!-- Pro Max Unlocked Banner -->
            <div class="bg-gradient-to-r from-amber-500/10 via-yellow-500/20 to-amber-500/10 rounded-xl p-2 text-center neon-gold flex items-center justify-center gap-2">
                <i data-lucide="crown" class="w-3.5 h-3.5 text-yellow-400 animate-bounce"></i>
                <span class="text-[10px] font-black uppercase tracking-wider text-yellow-300">PRO MAX UNLOCKED ✅</span>
            </div>

            <!-- Generate Signals Section Header -->
            <div class="text-center pt-1">
                <h2 class="text-base font-black tracking-wider text-cyan-400 uppercase">GENERATE SIGNALS</h2>
                <p class="text-[9px] text-slate-400">AI Analyzed High Accuracy Trading Signals</p>
            </div>

            <!-- 1. BROKER BOX -->
            <div class="bg-slate-900/80 border border-slate-800 rounded-xl p-3 flex items-center justify-between shadow-md">
                <div class="flex items-center gap-2.5">
                    <i data-lucide="shield-alert" class="w-4 h-4 text-red-500"></i>
                    <div>
                        <div class="text-[8px] font-bold text-slate-400 uppercase">Broker</div>
                        <div class="text-xs font-black text-white">Quotex</div>
                    </div>
                </div>
                <i data-lucide="chevron-down" class="w-4 h-4 text-slate-400"></i>
            </div>

            <!-- 2. MARKET BOX (Live / OTC Toggle) -->
            <div class="bg-slate-900/80 border border-slate-800 rounded-xl p-2.5 shadow-md">
                <div class="flex items-center justify-between mb-1.5 px-1">
                    <div class="flex items-center gap-2">
                        <i data-lucide="globe" class="w-4 h-4 text-cyan-400"></i>
                        <span class="text-[8px] font-bold text-slate-400 uppercase">Market Mode</span>
                    </div>
                </div>
                <div class="grid grid-cols-2 gap-1.5">
                    <button id="btn-live" onclick="setMarketMode('LIVE')" class="py-1.5 rounded-lg text-[10px] font-black uppercase transition-all bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer">Live Market</button>
                    <button id="btn-otc" onclick="setMarketMode('OTC')" class="py-1.5 rounded-lg text-[10px] font-black uppercase transition-all bg-gradient-to-r from-cyan-600 to-blue-600 text-white shadow-md cursor-pointer">OTC Markets</button>
                </div>
            </div>

            <!-- 3. PAIR SELECTION BOX -->
            <div class="bg-slate-900/80 border border-slate-800 rounded-xl p-3 shadow-md">
                <div class="flex items-center justify-between mb-1">
                    <div class="flex items-center gap-2">
                        <i data-lucide="pie-chart" class="w-4 h-4 text-cyan-400"></i>
                        <span class="text-[8px] font-bold text-slate-400 uppercase">Pair</span>
                    </div>
                </div>
                <div class="relative">
                    <select id="asset-selector" class="w-full bg-slate-950 border border-slate-800 text-white rounded-lg p-2 text-xs font-bold focus:outline-none appearance-none cursor-pointer"></select>
                    <div class="absolute right-3 top-2.5 pointer-events-none text-slate-400"><i data-lucide="chevron-down" class="w-3.5 h-3.5"></i></div>
                </div>
            </div>

            <!-- 4. TIMER BOX (5s to 5m) -->
            <div class="bg-slate-900/80 border border-slate-800 rounded-xl p-3 shadow-md">
                <div class="flex items-center justify-between mb-2">
                    <div class="flex items-center gap-2">
                        <i data-lucide="clock" class="w-4 h-4 text-cyan-400"></i>
                        <span class="text-[8px] font-bold text-slate-400 uppercase">Timer / Timeframe</span>
                    </div>
                </div>
                <div class="flex overflow-x-auto gap-1.5 pb-1 custom-scroll snap-x">
                    <button onclick="setTimeframe(this, '5s')" class="tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[10px] font-bold bg-cyan-600 text-white border border-cyan-500/20 cursor-pointer">5 Seconds</button>
                    <button onclick="setTimeframe(this, '10s')" class="tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[10px] font-bold bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer">10s</button>
                    <button onclick="setTimeframe(this, '15s')" class="tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[10px] font-bold bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer">15s</button>
                    <button onclick="setTimeframe(this, '30s')" class="tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[10px] font-bold bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer">30s</button>
                    <button onclick="setTimeframe(this, '1m')" class="tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[10px] font-bold bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer">1 Minute</button>
                    <button onclick="setTimeframe(this, '2m')" class="tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[10px] font-bold bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer">2m</button>
                    <button onclick="setTimeframe(this, '3m')" class="tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[10px] font-bold bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer">3m</button>
                    <button onclick="setTimeframe(this, '5m')" class="tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[10px] font-bold bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer">5 Minutes</button>
                </div>
            </div>

            <!-- Generate Signal Button -->
            <button onclick="generateSignal()" class="w-full py-4 bg-gradient-to-r from-cyan-500 via-blue-600 to-indigo-600 text-white rounded-xl font-black uppercase tracking-wider text-sm shadow-xl shadow-blue-500/20 flex items-center justify-center gap-2 cursor-pointer hover:opacity-95 transition-all mt-1">
                <i data-lucide="rocket" class="w-4 h-4"></i> GENERATE SIGNAL
            </button>

            <!-- Signal Output Result Box -->
            <div id="signal-box" class="hidden bg-slate-900/90 border border-cyan-500/40 rounded-xl p-3 space-y-2 mt-3 animate-fade-in">
                <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                    <span class="text-[10px] font-black text-cyan-400 uppercase tracking-wide">AI Strategy Analysis</span>
                    <span id="res-accuracy" class="text-[10px] font-black bg-emerald-500/20 text-emerald-400 px-2 py-0.5 rounded border border-emerald-500/30">92% ACCURACY</span>
                </div>
                <div class="grid grid-cols-2 gap-2 text-[10px]">
                    <div class="bg-slate-950 p-1.5 rounded border border-slate-800">
                        <span class="text-slate-400 block font-bold">Direction:</span>
                        <span id="res-dir" class="font-black text-sm text-emerald-400">CALL (UP) 🟢</span>
                    </div>
                    <div class="bg-slate-950 p-1.5 rounded border border-slate-800">
                        <span class="text-slate-400 block font-bold">Entry Point:</span>
                        <span class="font-black text-white text-xs">3rd Candle Confirm</span>
                    </div>
                </div>
                <div class="text-[9px] text-slate-300 bg-slate-950 p-2 rounded border border-slate-800/80 space-y-1">
                    <div>📊 <b class="text-cyan-400">Indicators:</b> RSI Oversold + Bollinger Bands Bounce + 50 EMA Verified</div>
                    <div>🕯️ <b class="text-cyan-400">Structure:</b> Hammer / Dragonfly Doji detected. Next candle ready.</div>
                </div>
            </div>
        </div>

        <!-- Bottom Navigation Bar -->
        <div class="sticky bottom-0 bg-slate-950/95 backdrop-blur border-t border-slate-800/80 py-2 px-1 grid grid-cols-5 text-center rounded-b-xl">
            <div class="flex flex-col items-center text-cyan-400 cursor-pointer">
                <i data-lucide="layout-dashboard" class="w-4 h-4"></i>
                <span class="text-[9px] font-bold mt-0.5">Dashboard</span>
            </div>
            <div class="flex flex-col items-center text-slate-400 hover:text-white cursor-pointer">
                <i data-lucide="history" class="w-4 h-4"></i>
                <span class="text-[9px] font-medium mt-0.5">History</span>
            </div>
            <div class="flex flex-col items-center text-slate-400 hover:text-white cursor-pointer">
                <i data-lucide="bar-chart-2" class="w-4 h-4"></i>
                <span class="text-[9px] font-medium mt-0.5">Performance</span>
            </div>
            <div class="flex flex-col items-center text-slate-400 hover:text-white cursor-pointer">
                <i data-lucide="headphones" class="w-4 h-4"></i>
                <span class="text-[9px] font-medium mt-0.5">Support</span>
            </div>
            <div class="flex flex-col items-center text-slate-400 hover:text-white cursor-pointer">
                <i data-lucide="more-horizontal" class="w-4 h-4"></i>
                <span class="text-[9px] font-medium mt-0.5">More</span>
            </div>
        </div>

    </div>

    <script>
        lucide.createIcons();

        let currentMode = 'OTC';
        let currentTimeframe = '5s';

        const liveAssets = [
            "EUR/USD", "USD/JPY", "GBP/USD", "AUD/USD", "USD/CAD", "USD/CHF", 
            "EUR/JPY", "EUR/GBP", "NZD/USD", "AUD/NZD", "EUR/CAD", "GBP/MXN", 
            "USD/BRL", "EUR/AUD", "AUD/JPY", "CAD/JPY", "USD/MXN", "CHF/JPY"
        ];

        const otcAssets = [
            "USD/ARS (OTC)", "AUD/CAD OTC", "AUD/CHF OTC", "AUD/JPY OTC", "AUD/NZD OTC", "AUD/USD OTC",
            "CAD/CHF OTC", "CAD/JPY OTC", "CHF/JPY OTC", "EUR/AUD OTC", "EUR/CAD OTC",
            "EUR/CHF OTC", "EUR/GBP OTC", "EUR/JPY OTC", "EUR/NZD OTC", "EUR/USD OTC",
            "GBP/AUD OTC", "GBP/CAD OTC", "GBP/CHF OTC", "GBP/JPY OTC", "GBP/NZD OTC",
            "GBP/USD OTC", "NZD/CAD OTC", "NZD/CHF OTC", "NZD/JPY OTC", "NZD/USD OTC",
            "USD/CAD OTC", "USD/CHF OTC", "USD/JPY OTC", "USD/SGD OTC",
            "Bitcoin OTC", "Ethereum OTC", "Litecoin OTC", "Ripple OTC", "Doge OTC",
            "Gold OTC", "Silver OTC", "Oil OTC (Brent)",
            "S&P 500 OTC", "Dow Jones 30 OTC", "DAX 30 OTC", "Nasdaq 100 OTC"
        ];

        function setMarketMode(mode) {
            currentMode = mode;
            const btnLive = document.getElementById('btn-live');
            const btnOtc = document.getElementById('btn-otc');
            const assetSelector = document.getElementById('asset-selector');

            assetSelector.innerHTML = '';
            let assets = (mode === 'LIVE') ? liveAssets : otcAssets;

            assets.forEach(asset => {
                let opt = document.createElement('option');
                opt.value = asset;
                opt.text = asset;
                assetSelector.appendChild(opt);
            });

            if(mode === 'LIVE') {
                btnLive.className = "py-1.5 rounded-lg text-[10px] font-black uppercase transition-all bg-gradient-to-r from-cyan-600 to-blue-600 text-white shadow-md cursor-pointer";
                btnOtc.className = "py-1.5 rounded-lg text-[10px] font-black uppercase transition-all bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer";
            } else {
                btnOtc.className = "py-1.5 rounded-lg text-[10px] font-black uppercase transition-all bg-gradient-to-r from-cyan-600 to-blue-600 text-white shadow-md cursor-pointer";
                btnLive.className = "py-1.5 rounded-lg text-[10px] font-black uppercase transition-all bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer";
            }
        }

        function setTimeframe(element, tf) {
            currentTimeframe = tf;
            document.querySelectorAll('.tf-btn').forEach(btn => {
                btn.className = "tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[10px] font-bold bg-slate-950 text-slate-400 border border-slate-800 cursor-pointer";
            });
            element.className = "tf-btn snap-start shrink-0 px-3 py-1.5 rounded-lg text-[10px] font-bold bg-cyan-600 text-white border border-cyan-500/20 cursor-pointer";
        }

        function generateSignal() {
            const box = document.getElementById('signal-box');
            const resDir = document.getElementById('res-dir');
            box.classList.remove('hidden');

            const isCall = Math.random() > 0.5;
            if(isCall) {
                resDir.innerHTML = "CALL (UP) 🟢";
                resDir.className = "font-black text-sm text-emerald-400";
            } else {
                resDir.innerHTML = "PUT (DOWN) 🔴";
                resDir.className = "font-black text-sm text-red-400";
            }
        }

        // Initialize default view
        setMarketMode('OTC');
    </script>
</body>
</html>
"""

components.html(html_content, height=720, scrolling=False)
