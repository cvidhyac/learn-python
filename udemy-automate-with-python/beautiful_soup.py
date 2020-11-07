import bs4
import requests

## Works only in specific sites that allows web scraping
def parse_with_bsoup(input_url):
  res = requests.get(input_url)
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text, "html.parser")
  html_elements = soup.select(
      "#edit-attributes-1 > div:nth-child(1) > label")
  print(html_elements[0].text.strip())


url = "https://nostarch.com/automatestuff2"
parse_with_bsoup(url)
