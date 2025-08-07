import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_headlines(url, site_name, max_headlines=20):
    headlines = []
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return [f"Failed to retrieve data from {site_name} (Status Code: {response.status_code})"]
        soup = BeautifulSoup(response.content, 'html.parser')
        if soup.title:
            page_title = soup.title.string.strip()
            headlines.append(f"{site_name} - Page Title: {page_title}")
        else:
            headlines.append(f"{site_name} - Page Title: Not found")

        h2_tags = soup.find_all('h2')
        if not h2_tags:
            headlines.append(f"No <h2> tags found on {site_name}")
        else:
            for i, h2 in enumerate(h2_tags, start=1):
                text = h2.get_text(strip=True)
                if text:
                    headlines.append(f"{i}. {text}")
                if i >= max_headlines:
                    break
    except Exception as e:
        headlines.append(f"Error fetching data from {site_name}: {e}")
    
    return headlines
sources = [
    ("https://www.thehindu.com/", "The Hindu"),
    ("https://indianexpress.com/todays-paper/", "Indian Express")
]
all_headlines = [f"News Headlines — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"]

for url, name in sources:
    all_headlines.append(f"\n--- Headlines from {name} ---\n")
    headlines = fetch_headlines(url, name)
    all_headlines.extend(headlines)

print("\n".join(all_headlines))
filename = "headlines.txt"
with open(filename, "w", encoding="utf-8") as file:
    for line in all_headlines:
        file.write(line + "\n")

print(f"\nAll headlines saved to: {filename}")
