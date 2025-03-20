# 🍪 Cookie Clicker Automation Bot

An automation bot for the Cookie Clicker game, built with Python and Selenium. It automates clicks and optimizes performance, collecting data for analysis.  

## 🚀 Features
- Automatic cookie clicking  
- Upgrading purchases based on efficiency  
- Performance data collection and visualization  

## 🛠 Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/JoaoVitorWS/cookie_cliker_bot.git
   ```
2. Navigate to the project folder:
   ```bash
   cd cookie_cliker_bot
   ```
3. Install dependencies:
   ```bash
   pip install selenium pandas matplotlib
   ```
4. Run the bot:
   ```bash
   python cookie_cliker.py
   ```

## 📊 Visualize Performance
The bot generates performance data in a CSV file (`cookie_performance.csv`), where each run's performance is logged under columns based on the time between buys (e.g., "5 minutes"). The data can be visualized using `graph.py`:
```bash
  python graph.py
```

## 📁 Folder Structure
```
cookie_cliker_bot/
│
├── cookie_cliker.py          # Main bot script
├── graph.py                  # Performance visualization script
├── cookie_performance.csv    # Performance data (gitignored)
├── README.md                 # Project documentation
└── .gitignore                # Files to exclude from version control
```

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

## 📝 License
This project is licensed under the MIT License.
