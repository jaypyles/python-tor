import argparse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tld import get_tld


def scrape_tor_site(url: str):
    """
    An example of how to use Selenium to use a Tor SOCKS Proxy
    and gather the title of a webpage.
    """
    options = webdriver.ChromeOptions()
    proxy = "localhost:9050"
    options.add_argument("--proxy-server=socks5://" + proxy)
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    timeout = 5

    try:
        title = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, ".//html"))
        )
        print("Page Title:", title.get_attribute("innerHTML"))
    except Exception as e:
        print("An error occurred:", e)

    driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get page title using Selenium")
    parser.add_argument("url", type=str, help="URL of the page")
    args = parser.parse_args()
    if get_tld(args.url, fix_protocol=True) == "onion":
        scrape_tor_site(args.url)
    else:
        print("Not a Tor site.")
