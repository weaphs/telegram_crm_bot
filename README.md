# 💧 Water Delivery CRM Telegram Bot

A Telegram bot for managing water delivery orders. Built with Aiogram 3, Google Sheets (gspread), and FSM. The bot allows users to register, place water delivery orders, track order status, manage addresses, and support the service with Telegram Stars.

---

## 🚀 Features

✅ User registration with full name, phone, and address
✅ Automatic address suggestion for returning users
✅ Multi-step order workflow with FSM
✅ Track user orders
✅ Support the service via Telegram Stars (donations)
✅ Blacklist middleware for blocking specific users
✅ Async architecture (Aiogram 3)
✅ Google Sheets integration for storage
✅ Modular project structure
✅ Environment configuration via .env

---

## 🧩 Project Structure
```
tg_crm_bot/
│
├── bot/
│   ├── handlers/       # Message & callback handlers 
│   ├── keyboards/      # Inline & reply keyboards
│   ├── fsm/            # FSM states for sign-up and orders
│   ├── middlewares/    # Middleware (e.g., BlackListMiddleware)
│   ├── g_services/     # Google Sheets service wrapper
│   ├── bot.py          # Bot and Dispatcher initialization
│   └── __init__.py
│
├── settings/
│   ├── settings.py     # Environment variables & configuration
│   └── __init__.py
│
├── main.py             # Entry point (starts polling)
├── requirements.txt    # Project dependencies
├── .env                # Environment variables (ignored by git)
└── README.md

```
---
## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/weaphs/telegram_crm_bot.git
cd tg_water_delivery_bot
```
### 2️⃣ Create and activate a virtual environment
```
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```
### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```
### 🗄️ Google Sheets Setup

Create a Google Service Account and download the JSON credentials file.

Share your Google Sheet with the Service Account email (read/write).

Create the following worksheets:

Clients – stores user info (user_id, full_name, phone, address)

Order_list – stores orders (user_id, name, address, water_amount, date_time)

Blocked_users – optional, for blacklisted users

### 🔑 Environment Configuration

Create a .env file in the root directory:

```
BOT_TOKEN=<your_telegram_bot_token>
GOOGLE_CREDENTIALS_PATH=<path_to_google_credentials.json>
GOOGLE_SHEET_NAME=<your_google_sheet_name>
GOOGLE_WORKSHEET_CLIENTS=Clients
GOOGLE_WORKSHEET_ORDERS=Order_list
GOOGLE_WORKSHEET_BLOCKED=Blocked_users

```

### ▶️ Run the Bot

```
python main.py

```

## Created by WEAPHS



