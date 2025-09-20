# UBTUIT Curriculum Bot 📚

A Telegram bot for UBTUIT (University of Business Technology Information Technology) students to access their weekly class schedules easily.

## 🚀 Features

- 📅 **Weekly Schedule Access**: Get your class schedule for any day of the week
- 🔐 **Secure Login**: Uses your student ID and password for authentication
- 💾 **Data Caching**: Stores schedule data locally for faster access
- 🔄 **Schedule Updates**: Refresh your schedule data when needed
- 👨‍💻 **Support**: Direct contact with developers and consultation services
- 🇺🇿 **Uzbek Language**: Full support for Uzbek language interface

## 🛠️ Technology Stack

- **Python 3.10**: Core programming language
- **aiogram**: Telegram Bot API framework
- **Selenium**: Web scraping for university website
- **SQLite**: Local database for data storage
- **ChromeDriver**: Browser automation

## 📋 Prerequisites

- Python 3.10 or higher
- Google Chrome browser
- ChromeDriver (included in repository)
- Telegram Bot Token from [@BotFather](https://t.me/botfather)

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/My-name-is-Jamshidbek/ubtuit_curricullum.git
   cd ubtuit_curricullum
   ```

2. **Install dependencies:**
   ```bash
   pip install pipenv
   pipenv install
   ```
   
   Or using pip directly:
   ```bash
   pip install aiogram xlsxwriter selenium openpyxl pandas python-dotenv cryptography
   ```

3. **Configure environment variables:**
   
   Create or update the `.env` file with your bot credentials:
   ```env
   TOKEN=your_telegram_bot_token_here
   ADMIN_ID=your_telegram_user_id
   KEY=JAMshidbek
   ```

4. **Make ChromeDriver executable (Linux/Mac):**
   ```bash
   chmod +x chromedriver
   ```

## 🚀 Usage

1. **Start the bot:**
   ```bash
   python main.py
   ```

2. **Interact with the bot on Telegram:**
   - Start a conversation with your bot
   - Enter your student ID (username)
   - Enter your student password
   - Select the day of the week to view your schedule

## 🤖 Bot Commands & Flow

### Initial Setup
1. **Student ID**: Enter your university student ID
2. **Password**: Enter your student portal password
3. **Day Selection**: Choose which day's schedule to view

### Available Options
- **📅 Weekdays**: Dushanba, Seshanba, Chorshanba, Payshanba, Juma, Shanba
- **🔄 Yangilash**: Refresh your schedule data
- **🏠 Boshiga qaytish**: Return to main menu
- **👨‍💻 Dasturchi**: Contact developer
- **👨🏻‍💻 Konsultatsiya**: Get consultation

## 📁 Project Structure

```
ubtuit_curricullum/
├── app.py              # Main bot handlers and logic
├── database.py         # Database operations and web scraping
├── config.py           # Configuration management
├── loader.py           # Bot and dispatcher initialization
├── main.py             # Application entry point
├── buttons.py          # Telegram keyboard layouts
├── states.py           # FSM states for conversation flow
├── chromedriver        # Chrome WebDriver executable
├── users.db            # SQLite database (auto-generated)
├── .env                # Environment variables
├── Pipfile             # Python dependencies
└── README.md           # This file
```

## 💾 Database Schema

### Users Table
- `telegram_id`: User's Telegram ID (Primary Key)
- `student_id`: University student ID
- `student_password`: Encrypted student password
- `student_about`: Additional user information

### Users Table (Schedule Data)
- `telegram_id`: User's Telegram ID (Primary Key)
- `student_id`: University student ID
- `student_password`: Student password
- `yuklangan_sana`: Last update date
- `dushanba` through `shanba`: Daily schedules

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `TOKEN` | Telegram Bot Token from BotFather | ✅ |
| `ADMIN_ID` | Admin Telegram User ID | ✅ |
| `KEY` | Encryption key for data security | ✅ |

### Bot Settings

The bot includes several configurable settings in `config.py`:
- `ERRORS_SEND`: Enable/disable error reporting
- `ADMIN_USER`: Admin contact link
- `WEB_SAYT`: Developer website/GitHub

## 🛡️ Security Features

- Password encryption for stored credentials
- Secure session management
- Input validation and sanitization
- Error handling for invalid credentials

## 📞 Support & Contact

- **Developer**: [Jamshidbek Ollanazarov](https://t.me/mal_un)
- **Admin Support**: [t.me/mal_un](https://t.me/mal_un)
- **GitHub**: [My-name-is-Jamshidbek](https://github.com/My-name-is-Jamshidbek)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is created for educational purposes and is intended for UBTUIT students.

## ⚠️ Disclaimer

This bot is an unofficial tool created to help UBTUIT students access their schedules more easily. It is not affiliated with the university administration. Please use your own credentials responsibly.

## 🔄 Version History

- **v1.0**: Initial release with basic schedule fetching functionality
- **Current**: Enhanced error handling and user experience improvements

---

**Made with ❤️ for UBTUIT students by [Jamshidbek Ollanazarov](https://github.com/My-name-is-Jamshidbek)**