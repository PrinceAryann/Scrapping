---

```markdown
# 📰 Hacker News Web Scraper

This Python script scrapes the [Hacker News](https://news.ycombinator.com/news) homepage to collect and store post titles, links, and their upvote scores in a CSV file, sorted by highest score.

## 🔧 Features

- Fetches titles, links, and points from Hacker News.
- Sorts posts by score (highest first).
- Outputs to a clean, structured CSV file.
- Built using `requests`, `BeautifulSoup`, and `csv`.
- Easy to customize path and format.

## 🛠️ Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`

You can install the requirements using:

```bash
pip install requests beautifulsoup4
```

## 📁 File Output

The output CSV file will contain:

| Title | Link | Points |
|-------|------|--------|
| Example Post | https://example.com | 123 |

> ⚠️ Change the `SAVE_PATH` in the script to your preferred directory.

## 🚀 Usage

Run the script:

```bash
python hn_scraper.py
```

> Make sure to update the `SAVE_PATH` in the script if needed.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 👨‍💻 Author

- **Prince Kumar Kuswaha**  
```

---
# Scrapping
