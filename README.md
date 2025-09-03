# 🏢 Tiny Tower Bot

A Python bot that automates **Tiny Tower** gameplay on an Android emulator.  
It focuses on the "friend visit + elevator trick" to generate coins indefinitely by detecting when the elevator has stopped and chaining visits.

---

## ✨ Features
- 🚀 Automates the **friend visit loop** trick
- 🪙 Detects elevator arrival by watching the **coin counter change**
- 🖱️ Finds and clicks buttons via image recognition
- 📸 Lightweight screenshot capture + region hashing
- ⚡ Designed to run forever with minimal overhead

---

## 📂 Project Structure
```
tiny-tower-bot/
│
├── main.py                 # Entry point (runs the loop)
│
├── bot/                    # Bot logic
│   ├── loop.py             # Main loop logic
│   ├── elevator.py         # Elevator stop detection
│   ├── actions.py          # Button clicking, navigation
│   └── config.py           # Regions of interest, constants
│
├── automation/             # Generic automation helpers
│   ├── screenshot.py       # Capture emulator screen
│   ├── input.py            # Send clicks/taps to emulator
│   └── detection.py        # Region hashing + image matching
│
├── assets/                 # Reference images (buttons, icons)
│
├── requirements.txt        # Python dependencies
└── README.md               # Documentation
```

---

## ⚙️ Installation

1. **Clone repo**
   ```bash
   git clone https://github.com/yourname/tiny-tower-bot.git
   cd tiny-tower-bot
   ```

2. **Create venv (recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux / Mac
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up emulator**
   - Launch your preferred emulator (BlueStacks, LDPlayer, etc.)
   - Ensure **ADB** is enabled and reachable
   - Update `config.py` with your emulator resolution + coin counter region

---

## ▶️ Usage

Run the bot:
```bash
python main.py
```

What happens:
1. Bot waits until the **elevator coins change** (meaning elevator arrived).
2. Bot **switches friends** before the slot closes.
3. Repeats indefinitely.

---

## 🔧 Configuration

Edit `bot/config.py`:
- `COIN_COUNTER_REGION` → (x, y, width, height) of the coin counter area
- Button image paths (stored in `assets/`)
- Emulator connection method (ADB, PyAutoGUI, etc.)

---

## 📦 Dependencies
Core packages:
- `opencv-python` – image capture + region matching  
- `pytesseract` – (optional) OCR if needed  
- `numpy` – array ops  
- `pyautogui` or `adbutils` – sending clicks/taps  

See `requirements.txt` for pinned versions.

---

## ⚠️ Disclaimer
This bot is for **educational purposes only**.  
Automating Tiny Tower may violate the game’s Terms of Service. Use responsibly and at your own risk.

---
