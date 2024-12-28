from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.safari.service import Service
from selenium.webdriver.safari.options import Options
import time

def scrape_blitz_gg(url):
    # Set up Safari WebDriver (headless mode)
    options = Options()
    options.headless = True  # Run in headless mode (no GUI)

    # Initialize Safari WebDriver
    driver = webdriver.Safari(options=options)

    try:
        # Open the Blitz.gg profile URL
        driver.get(url)
        time.sleep(5)  # Wait for the page to fully load (adjust the sleep time as needed)

        # Initialize an empty dictionary to store data
        data = {}

        # Scrape Rank (use CSS selectors or XPath based on your inspection)
        try:
            rank_element = driver.find_element(By.CSS_SELECTOR, '#main-content > div.⚡ce9f0725 > div.⚡980b7e11.inner-wrapper-col > div > div > div:nth-child(3) > div > div.⚡acd7108.flex.column.gap-sp-4.sidebar > section:nth-child(1) > div > div > div.⚡3284af55 > div.⚡f5047f69 > div > div > p')
            data["Rank"] = rank_element.text.strip() if rank_element else 'N/A'
        except:
            data["Rank"] = 'N/A'

        # Scrape ACS (Average Combat Score)
        try:
            acs_element = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div[3]/div/div/div[2]/div/div[1]/section[1]/div/div/div[3]/div[4]/p[2]')
            data["ACS"] = acs_element.text.strip() if acs_element else 'N/A'
        except:
            data["ACS"] = 'N/A'

        # Scrape K/D Ratio
        try:
            kda_element = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div[3]/div/div/div[2]/div/div[1]/section[1]/div/div/div[3]/div[1]/p[2]')
            data["K/D"] = kda_element.text.strip() if kda_element else 'N/A'
        except:
            data["K/D"] = 'N/A'

        # Scrape Win Percentage
        try:
            win_percent_element = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div[3]/div/div/div[2]/div/div[2]/section[1]/div/div[1]/div[1]/div[2]/h4')
            data["Win Percentage"] = win_percent_element.text.strip() if win_percent_element else 'N/A'
        except:
            data["Win Percentage"] = 'N/A'

        # Scrape Headshot Percentage
        try:
            hs_percent_element = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div[3]/div/div/div[2]/div/div[1]/section[1]/div/div/div[3]/div[3]/p[2]')
            data["Headshot Percentage"] = hs_percent_element.text.strip() if hs_percent_element else 'N/A'
        except:
            data["Headshot Percentage"] = 'N/A'

        return data

    except Exception as e:
        print(f"Error during scraping: {e}")
        return None

    finally:
        driver.quit()  # Always close the browser when done

if __name__ == "__main__":
    # Replace with your Blitz.gg profile URL
    url = "https://blitz.gg/valorant/profile/vauv%2010k-izzy"

    print("Scraping data from Blitz.gg...")
    stats = scrape_blitz_gg(url)

    if stats:
        print("\nScraped Stats:")
        for key, value in stats.items():
            print(f"{key}: {value}")
    else:
        print("Failed to scrape data.")
