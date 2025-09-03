# Tiny Tower Bot

A Python bot that automates **Tiny Tower** gameplay on an Android emulator.  
It focuses on the "friend visit + elevator trick" to generate coins indefinitely by detecting when the elevator has stopped and chaining visits.

---

## Features
- Automates the **friend visit loop** trick
- Detects elevator arrival by watching the **coin counter change**
- Finds and clicks buttons via image recognition
- Lightweight screenshot capture + region hashing
- Designed to run forever with minimal overhead

---

## Configuration

Edit `bot/config.py`:
- `COIN_COUNTER_REGION` → (x, y, width, height) of the coin counter area
- Button image paths (stored in `assets/`)
- Emulator connection method (ADB, PyAutoGUI, etc.)

---

## Dependencies
Core packages:
- `opencv-python` – image capture + region matching  
- `pytesseract` – (optional) OCR if needed  
- `numpy` – array ops  
- `pyautogui` or `adbutils` – sending clicks/taps  

See `requirements.txt` for pinned versions.

---

## Disclaimer
This bot is for **educational purposes only**.  
Automating Tiny Tower may violate the game’s Terms of Service. Use responsibly and at your own risk.

---
