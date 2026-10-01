import requests

from bs4 import BeautifulSoup

if __name__ == "__main__":

    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

    page = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    page.raise_for_status()

    soup = BeautifulSoup(page.content, "html.parser")
    a_tag_list = [a_tag for a_tag in soup.find_all("a")]
    a_tag_with_href = [
        a_tag for a_tag in a_tag_list if a_tag.get("href", "").startswith("/wiki/")
    ]
    link_tags = {
        a_tag.get_text(): a_tag["href"]
        for a_tag in a_tag_with_href
    }

    print(link_tags)