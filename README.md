# News Headlines Scraper

This project is a Python-based web scraper that fetches the latest news headlines from **The Hindu** and **Indian Express** websites and stores them in a `headlines.txt` file. It utilizes the `requests` and `BeautifulSoup` libraries for scraping and parsing the HTML content.


---
##  Features

- ✅ Scrapes `<h2>` headlines from two popular Indian news websites.
- ✅ Retrieves and logs the page title for each website.
- ✅ Limits the number of scraped headlines (default: 20 per source).
- ✅ Handles errors gracefully.
- ✅ Saves all scraped data to a `.txt` file (`headlines.txt`).
- ✅ Prints results in the console for immediate review.

---

##  How It Works

1. **Send HTTP Request**:
   - Uses `requests.get()` to fetch the HTML content of each news website.

2. **Parse HTML**:
   - Parses the HTML using `BeautifulSoup` with `'html.parser'`.

3. **Extract Data**:
   - Retrieves the `<title>` tag (page title).
   - Finds all `<h2>` tags and extracts their text content.

4. **Limit Results**:
   - Only the first 20 headlines are saved from each site (customizable).

5. **Output**:
   - Prints results to the console.
   - Saves results to a file named `headlines.txt` (in the same directory).

---

##  Technologies Used

| Technology     | Purpose                        |
|----------------|--------------------------------|
| Python         | Core programming language      |
| Requests       | For sending HTTP requests      |
| BeautifulSoup4 | For parsing and navigating HTML|
| datetime       | For timestamping the output    |

---

## how to run:
Step : Install Required Libraries
requests
beautifulsoup4

Step: Run the Script

python scraper.py


After running, check the console for live output and open headlines.txt to view saved results.
And if you want any other new paper headline so just enter the link in sources[].

---

## Disclaimer
This project is for educational purposes only. Make sure to review the terms of service and robots.txt of any site you scrape.

Do not overload or spam any server with multiple or frequent requests.

---

## Contact
For questions or feedback, feel free to open an issue or reach out via GitHub.

---

## Author
Github: @Krishna-S-27
