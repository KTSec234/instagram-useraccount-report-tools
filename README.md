# 🔥 Instagram Report Tool 🔥

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-green.svg" alt="Platform">
  <img src="https://img.shields.io/badge/Status-Active-success.svg" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-red.svg" alt="License">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/yourusername/instagram-report-tool/main/banner.png" alt="Instagram Report Tool Banner">
</p>

## 📋 Description

**Instagram Report Tool** is an advanced automated tool designed to help users report spam, bot, and fake Instagram accounts efficiently. The tool utilizes Instagram's official reporting system to submit multiple reports automatically, helping to clean up the platform from unwanted content.

### ✨ Key Features

- 🚀 **Fast & Efficient**: Multi-threaded reporting system
- 🎯 **Targeted Reporting**: Report specific usernames/accounts
- 🌐 **Proxy Support**: Optional proxy usage for enhanced anonymity
- 🎨 **Beautiful UI**: Colored terminal interface with ASCII art banner
- 📊 **Real-time Progress**: Live reporting status updates
- 🔄 **Auto Email Generation**: Generates random emails for each report
- 🛡️ **Safe & Legal**: Uses Instagram's official reporting endpoints

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection

### Step-by-Step Installation

1. **Clone or Download the Repository**
   ```bash
   git clone https://github.com/yourusername/instagram-report-tool.git
   cd instagram-report-tool
   ```

2. **Create Virtual Environment (Recommended)**
   ```bash
   python -m venv env
   ```

3. **Activate Virtual Environment**
   - **Windows:**
     ```bash
     env\Scripts\activate.bat
     ```
   - **Linux/macOS:**
     ```bash
     source env/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install requests user-agent cfonts colorama
   ```

5. **Verify Installation**
   ```bash
   python -c "import requests, user_agent, cfonts, colorama; print('✅ All dependencies installed successfully!')"
   ```

## 📖 Usage

### Basic Usage

1. **Run the Tool**
   ```bash
   python Instagramreport.py
   ```

2. **Follow the Prompts**
   - Enter the target username
   - Enter the account name
   - Choose proxy option (Y/N)

### With Proxy Support

If you choose to use proxies:

1. Select proxy protocol (socks4/socks5)
2. Provide proxy file path (one proxy per line)
3. The tool will rotate through proxies automatically

### Example Output

```
============================================================

     ██╗ ███╗   ██╗ ███████╗ ████████╗  █████╗   ██████╗  ██████╗   █████╗
     ██║ ████╗  ██║ ██╔════╝ ╚══██╔══╝ ██╔══██╗ ██╔════╝  ██╔══██╗ ██╔══██╗
     ██║ ██╔██╗ ██║ ███████╗    ██║    ███████║ ██║  ███╗ ██████╔╝ ███████║
     ██║ ██║╚██╗██║ ╚════██║    ██║    ██╔══██║ ██║   ██║ ██╔══██╗ ██╔══██║
     ██║ ██║ ╚████║ ███████║    ██║    ██║  ██║ ╚██████╔╝ ██║  ██║ ██║  ██║
     ╚═╝ ╚═╝  ╚═══╝ ╚══════╝    ╚═╝    ╚═╝  ╚═╝  ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═╝

                                  ███╗   ███╗
                                  ████╗ ████║
                                  ██╔████╔██║
                                  ██║╚██╔╝██║
                                  ██║ ╚═╝ ██║
                                  ╚═╝     ╚═╝




    ___   ___   ___    ___    ___   _____       _____    ___     ___    _
   | _ \ | __| | _ \  / _ \  | _ \ |_   _|     |_   _|  / _ \   / _ \  | |
   |   / | _|  |  _/ | (_) | |   /   | |         | |   | (_) | | (_) | | |__
   |_|_\ |___| |_|    \___/  |_|_\   |_|         |_|    \___/   \___/  |____|


============================================================
🔥 Advanced Instagram Account Reporting Tool 🔥
📱 Report spam/bots/fake accounts automatically 📱
⚡ Fast & Efficient | Multi-threaded ⚡
👨‍💻 Created by: KUNAL 👨‍💻
============================================================

[?] Enter the target username : spam_account_123
[?] Enter the account name : Spam Account
[?] Do you want to use a proxy? Maybe the speed will slow down [Y/N] : N

=======================================
Username : spam_account_123
Name : Spam Account
Time : 14:30:25
=======================================

[!] Report number : 1  Sent ! spam_account_123
[!] Report number : 2  Sent ! spam_account_123
[!] Report number : 3  Sent ! spam_account_123
...
```

## 📋 Requirements

### Dependencies

- `requests` - HTTP library for API calls
- `user-agent` - Random user agent generation
- `cfonts` - ASCII art text rendering
- `colorama` - Cross-platform colored terminal text

### System Requirements

- **OS**: Windows 10+, Linux, macOS
- **RAM**: Minimum 2GB
- **Storage**: 50MB free space
- **Network**: Stable internet connection

## 🔧 Configuration

### Proxy Setup

Create a text file with proxies (one per line):

```
socks4://127.0.0.1:1080
socks5://127.0.0.1:1081
http://proxy.example.com:8080
```

### Customization

You can modify the following in the script:

- **Colors**: Change color schemes in the color variables
- **Headers**: Update user agents and request headers
- **Delay**: Add delays between requests to avoid rate limiting
- **Threads**: Adjust threading for performance

## ⚠️ Disclaimer

**This tool is for educational purposes only. Use responsibly and in accordance with Instagram's Terms of Service.**

- Only report accounts that genuinely violate Instagram's community guidelines
- Do not use for harassment or spam
- Respect rate limits to avoid account suspension
- The creator is not responsible for misuse

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
git clone https://github.com/yourusername/instagram-report-tool.git
cd instagram-report-tool
python -m venv env
env\Scripts\activate  # Windows
pip install -r requirements.txt
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Creator:** KUNAL

- **Telegram:** [@GtCvQ_NswDxmZDVl](https://t.me/+GtCvQ_NswDxmZDVl)
- **GitHub:** [yourusername](https://github.com/KTSec234)

## 🙏 Acknowledgments

- Thanks to the Python community
- Inspired by various open-source reporting tools
- ASCII art generated using cfonts library

---

<p align="center">
  <strong>Made with ❤️ by KUNAL</strong>
</p>

<p align="center">
  <img src="https://forthebadge.com/images/badges/built-with-love.svg" alt="Built with Love">
  <img src="https://forthebadge.com/images/badges/made-with-python.svg" alt="Made with Python">
</p>
