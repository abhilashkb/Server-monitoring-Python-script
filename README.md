# Server Monitor Script

This Python script monitors servers from ansible hosts file by pinging them or checking if their 80 port is open. If a server is found to be down or up, an alert is sent to Telegram.

## Requirements

- Python 3.x
- `python-telegram-bot` library (`pip install python-telegram-bot`)

## Usage

1. Clone the repository:

```
git clone https://github.com/abhilashkb/Server-monitoring-script-uisng-python.git
```

2. Install the `python-telegram-bot` library:

```
pip install python-telegram-bot
```

3. Update the `config.py` file with your Telegram Bot Token and Chat ID:

```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID_HERE"
```

4. Update the `servers.txt` file with the servers you want to monitor. Each server should be on a separate line.

5. Run the script:

```
python server_monitor.py
```

The script will run continuously and check the servers every minute. If a server is found to be down or up, an alert will be sent to Telegram.
