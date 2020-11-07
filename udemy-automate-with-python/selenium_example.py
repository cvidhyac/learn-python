# brew cask install chromedriver
# Finding CSS Selector : Use Chrome developer tools -> Inspect -> Copy -> Selector

from selenium import webdriver


# Closes as soon as program exits
def open_browser(url):
  browser = webdriver.Chrome()
  browser.get(url)
  browser.refresh()
  browser.back()
  browser.forward()
  browser.quit()


## Read the content of the webpages
def read_content(url):
  browser = webdriver.Chrome()
  browser.get(url)
  elems = browser.find_element_by_css_selector(
      "body > div.main > div:nth-child(1) > p:nth-child(8)")
  print(elems.text)
  browser.quit()


def print_entire_webpage(url):
  browser = webdriver.Chrome()
  browser.get(url)
  elems = browser.find_element_by_css_selector('html')
  print(elems.text)
  browser.quit()


web_url = "https://nostarch.com/automatestuff2"
open_browser(web_url)
another_url = "https://automatetheboringstuff.com/"
read_content(another_url)
print_entire_webpage(another_url)
