# Personal Projects

Collection of personal automation and utility scripts.

## Projects

### hl3.py - WhatsApp Automated Message Sender

A Python script that automatically sends scheduled messages to a WhatsApp group using Selenium WebDriver.

#### Features

- Automated WhatsApp Web interaction
- Scheduled daily message sending
- Persistent Chrome profile for session management
- Configurable group name, message, and send time

#### Requirements

```bash
pip install selenium webdriver-manager
```

#### Configuration

Edit the following variables in `hl3.py`:

```python
GROUP_NAME = "Your Group Name"
MESSAGE = "Your message here"
SEND_TIME = "HH:MM"  # 24-hour format
```

#### Usage

1. Run the script:
   ```bash
   python hl3.py
   ```

2. Scan the QR code when prompted (first time only)

3. The script will automatically send the message at the specified time every day

#### Notes

- Chrome browser must be installed
- WhatsApp Web must be accessible
- The script uses a persistent Chrome profile to maintain login session
- Messages are sent only once per day (resets at midnight)

## License

Personal use only.

