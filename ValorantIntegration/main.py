from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


def get_driver(browser="edge"):
    if browser.lower() == "edge":
        options = webdriver.EdgeOptions()
        service = webdriver.EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
    elif browser.lower() == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError("Unsupported browser. Choose from 'edge' or 'safari'.")
    return driver


def scrape_tracker_gg(url, browser="edge"):
    driver = get_driver(browser)
    driver.get(url)
    wait = WebDriverWait(driver, 10)  # Explicit wait for elements to load

    data = {}
    try:
        # Scrape Rank
        try:
            rank_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".valorant-rank-icon + span")))
            data["Rank"] = rank_element.text.strip()
        except:
            data["Rank"] = "N/A"

        # Scrape ACS (Average Combat Score)
        try:
            acs_element = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(), 'Combat Score')]/following-sibling::div")))
            data["ACS"] = acs_element.text.strip()
        except:
            data["ACS"] = "N/A"

        # Scrape K/D Ratio
        try:
            kd_element = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(), 'K/D Ratio')]/following-sibling::div")))
            data["K/D"] = kd_element.text.strip()
        except:
            data["K/D"] = "N/A"

        # Scrape Win Percentage
        try:
            win_percent_element = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Win %')]/following-sibling::div")))
            data["Win Percentage"] = win_percent_element.text.strip()
        except:
            data["Win Percentage"] = "N/A"

        # Scrape Headshot Percentage
        try:
            hs_percent_element = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(), 'Headshot %')]/following-sibling::div")))
            data["Headshot Percentage"] = hs_percent_element.text.strip()
        except:
            data["Headshot Percentage"] = "N/A"

        return data

    except Exception as e:
        print(f"Error during scraping: {e}")
        return None

    finally:
        driver.quit()


if __name__ == "__main__":
    # Replace with your Tracker.gg profile URL
    url = "https://tracker.gg/valorant/profile/riot/vauv%2010k-izzy/overview"

    print("Scraping data from Tracker.gg...")
    stats = scrape_tracker_gg(url, browser="edge")

    if stats:
        print("\nScraped Stats:")
        for key, value in stats.items():
            print(f"{key}: {value}")
    else:
        print("Failed to scrape data.")