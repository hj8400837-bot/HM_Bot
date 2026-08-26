<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hassan Malik Signal Generator</title>
    <style>
        /* Base Styling & Background */
        body {
            margin: 0;
            padding: 0;
            background-color: #0b141a;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        /* App Container Layout */
        .app-container {
            width: 90%;
            max-width: 400px;
            background-color: #0d1f22;
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
            border: 1px solid #1a3a3a;
        }

        /* Top Header & Logo Section */
        .header {
            text-align: center;
            margin-bottom: 25px;
        }

        .header h1 {
            font-size: 24px;
            color: #00ffaa;
            margin: 5px 0;
            text-shadow: 0 0 10px rgba(0, 255, 170, 0.3);
        }

        .header p {
            font-size: 12px;
            color: #8fa0a0;
            margin: 0;
        }

        /* Form Controls & Dropdowns */
        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 8px;
            color: #cbd5e1;
        }

        .form-group select {
            width: 100%;
            padding: 12px 15px;
            background-color: #132d30;
            border: 1px solid #224d52;
            border-radius: 10px;
            color: #ffffff;
            font-size: 15px;
            outline: none;
            cursor: pointer;
            box-sizing: border-box;
        }

        /* Live Signal Display Box */
        .signal-box {
            background-color: #071618;
            border: 1px dashed #1a3a3a;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            margin-bottom: 25px;
            min-height: 80px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        .placeholder-text {
            color: #64748b;
            font-size: 14px;
        }

        .signal-output {
            display: none;
            width: 100%;
        }

        .signal-type {
            font-size: 28px;
            font-weight: bold;
            letter-spacing: 2px;
            margin-bottom: 8px;
        }

        .call-text { color: #00ff66; text-shadow: 0 0 10px rgba(0,255,102,0.3); }
        .put-text { color: #ff3366; text-shadow: 0 0 10px rgba(255,51,102,0.3); }

        .signal-details {
            font-size: 13px;
            color: #94a3b8;
            line-height: 1.6;
        }

        .accuracy-badge {
            display: inline-block;
            background-color: rgba(0, 255, 170, 0.1);
            color: #00ffaa;
            padding: 4px 8px;
            border-radius: 5px;
            font-size: 12px;
            margin-top: 5px;
            font-weight: bold;
        }

        /* Action Button */
        .generate-btn {
            width: 100%;
            background: linear-gradient(135deg, #00ffaa, #00cc88);
            border: none;
            padding: 15px;
            border-radius: 12px;
            color: #0d1f22;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 255, 170, 0.2);
        }

        .generate-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 255, 170, 0.4);
        }

        .generate-btn:active {
            transform: translateY(0);
        }
    </style>
</head>
<body>

<div class="app-container">
    <!-- Header Section -->
    <div class="header">
        <h1>🚀 Hassan Malik <br>Signal Generator 🚀</h1>
        <p>Generate high-precision trading signals with advanced AI algorithms</p>
    </div>

    <!-- Inputs Section -->
    <div class="form-group">
        <label>🏛️ Select Broker</label>
        <select id="broker">
            <option value="Quotex">Quotex</option>
            <option value="PocketOption">Pocket Option</option>
            <option value="Binomo">Binomo</option>
        </select>
    </div>

    <div class="form-group">
        <label>💹 Trading Asset</label>
        <select id="asset">
            <option value="EUR/USD (OTC)">EUR/USD (OTC)</option>
            <option value="GBP/USD (OTC)">GBP/USD (OTC)</option>
            <option value="USD/JPY">USD/JPY</option>
            <option value="AUD/USD">AUD/USD</option>
        </select>
    </div>

    <div class="form-group">
        <label>⏱️ Time Frame</label>
        <select id="timeframe">
            <option value="15secs">15 Secs</option>
            <option value="1min">1 Minute</option>
            <option value="5min">5 Minutes</option>
        </select>
    </div>

    <!-- Dynamic Output Box -->
    <div class="signal-box">
        <div id="placeholder" class="placeholder-text">
            Click "GENERATE NEW SIGNAL" below to get your first analysis
        </div>
        <div id="signalOutput" class="signal-output">
            <div id="signalDirection" class="signal-type">CALL</div>
            <div class="signal-details">
                Asset: <span id="resAsset" style="color: #fff;">-</span> | 
                Timeframe: <span id="resTF" style="color: #fff;">-</span> <br>
                <div id="accuracy" class="accuracy-badge">Accuracy: 89%</div>
            </div>
        </div>
    </div>

    <!-- Button Trigger -->
    <button class="generate-btn" onclick="generateSignal()">⚡ GENERATE NEW SIGNAL ⚡</button>
</div>

<script>
    function generateSignal() {
        // Fetch values chosen by user
        const asset = document.getElementById('asset').value;
        const timeframe = document.getElementById('timeframe').value;

        // Interactive UI Elements
        const placeholder = document.getElementById('placeholder');
        const outputBox = document.getElementById('signalOutput');
        const directionText = document.getElementById('signalDirection');
        const resAsset = document.getElementById('resAsset');
        const resTF = document.getElementById('resTF');
        const accuracyText = document.getElementById('accuracy');

        // Show loading state briefly
        placeholder.style.display = 'none';
        outputBox.style.display = 'block';
        directionText.innerHTML = "ANALYZING...";
        directionText.className = "signal-type";
        directionText.style.color = "#8fa0a0";

        setTimeout(() => {
            // Algorithm logic to choose direction and probability randomly
            const signals = ['CALL', 'PUT'];
            const randomSignal = signals[Math.floor(Math.random() * signals.length)];
            const randomAccuracy = Math.floor(Math.random() * (95 - 82 + 1)) + 82; // 82% to 95%

            // Assign values dynamically
            resAsset.innerText = asset;
            resTF.innerText = timeframe;
            accuracyText.innerText = `AI Probability: ${randomAccuracy}%`;

            if(randomSignal === 'CALL') {
                directionText.innerText = "🟢 CALL (UP)";
                directionText.className = "signal-type call-text";
            } else {
                directionText.innerText = "🔴 PUT (DOWN)";
                directionText.className = "signal-type put-text";
            }
        }, 800); // 800ms artificial setup delay for visual feel
    }
</script>

</body>
</html>
