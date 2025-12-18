import logging
import traceback

import requests

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def get_request(url):
  try:
    res = requests.get(url)
    logging.info("The website returned : " + str(res.status_code))
    # The content of response is in in chunk, it can be iterated
    if res.raise_for_status() is None:
      for chunks in res.iter_content(1000):
        logging.info(" Current chunk : " + str(chunks))
    else:
      logging.critical("Error scenario")
  except requests.HTTPError as exception:
    logging.critical(str(exception.response))
  except Exception:
    logging.critical(
        " Unknown request : " + url + " trace : " + traceback.format_exc())


def demo():
  get_request("https://www.google.com")
  get_request("http://nonexistent.url")
  get_request("https://maps.google.com/111+richmond+st")


demo()
