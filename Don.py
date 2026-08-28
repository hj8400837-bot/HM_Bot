from dataclasses import dataclass
from typing import List
import statistics


@dataclass
class Candle:
    timestamp: int
    open: float
    high: float
    low: float
    close: float


class HassanMalikAIBot:

    def __init__(self, candles: List[Candle]):
        self.candles = candles

    # ---------- BASIC INDICATORS ----------

    def ema(self, values, period):
        if len(values) < period:
            return None

        multiplier = 2 / (period + 1)
        value = sum(values[:period]) / period

        for price in values[period:]:
            value = (price - value) * multiplier + value

        return value

    def rsi(self, values, period=14):
        if len(values) <= period:
            return None

        gains = []
        losses = []

        for i in range(1, len(values)):
            change = values[i] - values[i - 1]
            gains.append(max(change, 0))
            losses.append(max(-change, 0))

        avg_gain = sum(gains[:period]) / period
        avg_loss = sum(losses[:period]) / period

        for i in range(period, len(gains)):
            avg_gain = ((avg_gain * (period - 1)) + gains[i]) / period
            avg_loss = ((avg_loss * (period - 1)) + losses[i]) / period

        if avg_loss == 0:
            return 100

        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))

    def bollinger(self, values, period=20):
        if len(values) < period:
            return None

        section = values[-period:]
        middle = sum(section) / period
        deviation = statistics.stdev(section)

        upper = middle + (2 * deviation)
        lower = middle - (2 * deviation)

        return upper, middle, lower

    # ---------- CANDLE PATTERNS ----------

    def candle_pattern(self):

        if len(self.candles) < 3:
            return "NONE"

        a = self.candles[-2]
        b = self.candles[-1]

        body_a = abs(a.close - a.open)
        body_b = abs(b.close - b.open)

        # Bullish engulfing
        if (
            a.close < a.open
            and b.close > b.open
            and b.close > a.open
            and b.open < a.close
        ):
            return "BULLISH_ENGULFING"

        # Bearish engulfing
        if (
            a.close > a.open
            and b.close < b.open
            and b.open > a.close
            and b.close < a.open
        ):
            return "BEARISH_ENGULFING"

        # Doji
        if body_b <= (b.high - b.low) * 0.10:
            return "DOJI"

        return "NONE"

    # ---------- TREND ----------

    def trend(self):

        closes = [c.close for c in self.candles]

        ema9 = self.ema(closes, 9)
        ema21 = self.ema(closes, 21)
        ema50 = self.ema(closes, 50)

        if None in (ema9, ema21, ema50):
            return "UNKNOWN"

        if ema9 > ema21 > ema50:
            return "UP"

        if ema9 < ema21 < ema50:
            return "DOWN"

        return "SIDEWAYS"

    # ---------- SUPPORT / RESISTANCE ----------

    def support_resistance(self):

        recent = self.candles[-30:]

        support = min(c.low for c in recent)
        resistance = max(c.high for c in recent)

        price = recent[-1].close

        return support, resistance, price

    # ---------- MAIN SIGNAL ----------

    def generate_signal(self):

        if len(self.candles) < 60:
            return {
                "signal": "NO TRADE",
                "strength": "LOW",
                "reason": "کم از کم 60 candles درکار ہیں"
            }

        closes = [c.close for c in self.candles]

        trend = self.trend()
        rsi = self.rsi(closes)
        bb = self.bollinger(closes)
        pattern = self.candle_pattern()

        support, resistance, price = self.support_resistance()

        score_up = 0
        score_down = 0

        # ---- TREND FILTER ----

        if trend == "UP":
            score_up += 3

        elif trend == "DOWN":
            score_down += 3

        # ---- RSI ----

        if rsi is not None:

            if 50 < rsi < 70:
                score_up += 2

            elif 30 < rsi < 50:
                score_down += 2

        # ---- BOLLINGER ----

        if bb:
            upper, middle, lower = bb

            if price > middle:
                score_up += 1

            elif price < middle:
                score_down += 1

        # ---- CANDLE PATTERN ----

        if pattern == "BULLISH_ENGULFING":
            score_up += 2

        elif pattern == "BEARISH_ENGULFING":
            score_down += 2

        # ---- FINAL DECISION ----

        difference = abs(score_up - score_down)

        # Trend conflict / weak setup
        if trend == "SIDEWAYS" or trend == "UNKNOWN":
            return {
                "signal": "NO TRADE",
                "strength": "LOW",
                "trend": trend,
                "rsi": round(rsi, 2) if rsi else None,
                "pattern": pattern
            }

        if difference < 3:
            return {
                "signal": "NO TRADE",
                "strength": "MEDIUM",
                "trend": trend,
                "rsi": round(rsi, 2) if rsi else None,
                "pattern": pattern
            }

        if score_up > score_down and trend == "UP":
            signal = "UP"
            score = score_up

        elif score_down > score_up and trend == "DOWN":
            signal = "DOWN"
            score = score_down

        else:
            return {
                "signal": "NO TRADE",
                "strength": "LOW",
                "reason": "Trend کے خلاف setup آیا"
            }

        if score >= 7:
            strength = "STRONG"
        elif score >= 5:
            strength = "MEDIUM"
        else:
            strength = "WEAK"

        return {
            "signal": signal,
            "strength": strength,
            "score": score,
            "trend": trend,
            "rsi": round(rsi, 2) if rsi else None,
            "pattern": pattern,
            "support": support,
            "resistance": resistance,
            "price": price
        }
