import pandas as pd
import requests

# --- CONFIGURATION ---
# Yahan apne Telegram ki details daalein
TELEGRAM_TOKEN = ""8967104171:AAGcP1hQOf1NkFyZZKFD_IYSb17pQm2_Vds
CHAT_ID = ""7937795393

MARKET_TYPE = "OTC"  # "OTC" ya "LIVE"
BASE_AMOUNT = 10
MAX_MARTINGALE = 2

class Bot7166:
    def __init__(self):
        self.step = 0

    def send_telegram(self, message):
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        try:
            requests.get(url)
        except:
            pass

    def run_logic(self, df, pair, tf):
        # 1. Market Stability Check (Volatility Filter)
        atr = (df['high'] - df['low']).rolling(window=14).mean().iloc[-1]
        volatility = df['high'].iloc[-1] - df['low'].iloc[-1]
        if volatility > (atr * 2.0):
            return "WAIT", 0, "High Volatility"

        # 2. Support/Resistance Calculation
        support = df['low'].rolling(window=20).min().iloc[-1]
        resistance = df['high'].rolling(window=20).max().iloc[-1]
        curr = df['close'].iloc[-1]
        
        # 3. Patterns
        is_hammer = (df['close'].iloc[-1] > df['open'].iloc[-1])
        is_shooting_star = (df['open'].iloc[-1] > df['close'].iloc[-1])

        # 4. Strategy
        signal = "NONE"
        reason = ""
        
        if MARKET_TYPE == "OTC":
            if curr <= (support * 1.001) and is_hammer:
                signal = "BUY"
                reason = "OTC_Support_Bounce"
            elif curr >= (resistance * 0.999) and is_shooting_star:
                signal = "SELL"
                reason = "OTC_Resist_Bounce"
        
        elif MARKET_TYPE == "LIVE":
            if curr > resistance:
                signal = "BUY"
                reason = "LIVE_Breakout"
            elif curr < support:
                signal = "SELL"
                reason = "LIVE_Breakout"

        # 5. Telegram Alert
        if signal != "NONE":
            amount = BASE_AMOUNT * (2.2 ** self.step)
            msg = f"🚀 7166 BOT SIGNAL\nPair: {pair}\nTF: {tf}\nAction: {signal}\nAmount: ${amount:.2f}\nReason: {reason}"
            self.send_telegram(msg)
            return signal, amount, reason

        return "NONE", 0, "No Signal"

# --- MAIN LOOP ---
bot = Bot7166()
# Yahan aap apna data loop chalayein aur 'bot.run_logic(df, pair, tf)' call karein
