# Web Scraping Mini Projects

This repository contains small beginner-friendly projects using `requests` and `BeautifulSoup` to teach students the basics of web scraping.

## 📌 Project 1: Poki Game Title Scraper

**Objective:** Scrape game titles from [poki.com](https://poki.com/) and detect new games added over time.

### Features:

- Collects all visible game-related text from Poki’s homepage.
- Compares scraped data with previously saved data to identify new games.
- Stores results in `games.txt`.

### Files:

- `main.py`: Handles fetching, parsing, and saving game data.
- `games.txt`: Stores scraped game titles.

## 📌 Project 2: Wikipedia Article Scraper

**Objective:** Scrape Wikipedia articles and store their content for later use or analysis.

### Features:

- Reads a list of Wikipedia URLs from urls.txt.
- Extracts the article's title and main body text.
- Saves the cleaned content to articles.txt.

### Files:

- `main.py`: Fetches and parses article content from Wikipedia.
- `urls.txt`: A list of Wikipedia article links.

## 🎯 Why These Projects?

Many students love to open up Inspect Element and pretend they're "hacking Google"—so we channeled that curiosity into something real. These projects give students a taste of real-world web scraping, showing how the tools behind Inspect can be used programmatically to gather and analyze data.
