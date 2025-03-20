from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import os.path
import time
import pandas as pd

def cookie_clicker(time_between_buys=15, duration=5):            # Duration in minutes
    """Automates Cookie Clicker and saves the performance in a sorted CSV."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://orteil.dashnet.org/cookieclicker/")
    time.sleep(3)

    # Select Language
    driver.find_element(By.ID, value="langSelect-PT-BR").click()
    time.sleep(3)

    cookie = driver.find_element(By.ID, value="bigCookie")
    start_time = time.time()

    # Time in minutes
    timeout = start_time + 60 * duration


    # Clicking loop
    while time.time() <= timeout:
        cookie.click()

        if time.time() - start_time > time_between_buys:  # Time between
            buy_upgrades(driver)
            buy_products(driver)
            start_time = time.time()

    cookies_per_second = get_cookies_per_second(driver)
    save_data(duration, time_between_buys, cookies_per_second)

    print(f"cookeis per second: {cookies_per_second}")

    driver.quit()


def buy_products(driver):
    """Buys available upgrades."""
    products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    for product in products[::-1]:
        try:
            product.click()
            time.sleep(0.1)
        except StaleElementReferenceException:
            continue


def buy_upgrades(driver):
    """Buys available products in reverse order (higher priority)."""
    upgrades = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")
    for upgrade in upgrades:
        try:
            upgrade.click()
            time.sleep(0.1)
        except StaleElementReferenceException:
            continue


def get_cookies_per_second(driver):
    """Returns the current cookies per second"""
    try:
        cookies_per_second = WebDriverWait(driver, 15).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="cookiesPerSecond"]'))
        )
        return cookies_per_second.text.split()[2]  # Formats the cookies per second
    except StaleElementReferenceException:
        cookies_per_second = WebDriverWait(driver, 15).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="cookiesPerSecond"]'))
        )
        return cookies_per_second.text.split()[2]  # Formats the cookies per second


def save_data(duration, time_between_buys, cookies_per_second):
    """Saves the data in a sorted CSV file based on time between buys."""

    file_exists = os.path.exists("cookie_performance.csv")
    duration_column_name = f"{duration} minutes"

    if not file_exists:
        # If the file doesn't exist, create it with the necessary columns
        df = pd.DataFrame({
            "Time Between Buys": [time_between_buys],
            duration_column_name: [cookies_per_second]
        })

    else:
        # Load existing data
        df = pd.read_csv('cookie_performance.csv')

        # Ensure the duration column exists
        if duration_column_name not in df.columns:
            df[duration_column_name] = pd.NA  # Add the column if it doesn't exist

        # Check if Time Between Buys already exists
        if time_between_buys in df["Time Between Buys"].values:
            # Update the existing row for the given Time Between Buys
            df.loc[df["Time Between Buys"] == time_between_buys, duration_column_name] = float(cookies_per_second)
        else:
            # Append a new row with the new data
            new_row = pd.DataFrame({
                "Time Between Buys": [time_between_buys],
                duration_column_name: [cookies_per_second]
            })
            df = pd.concat([df, new_row], ignore_index=True)

    # Sort the Time Between Buys
    df = df.sort_values(by="Time Between Buys", ascending=True)

    # Sort the minutes in ascending order
    column_order = ["Time Between Buys"] + sorted([col for col in df.columns if "minutes" in col], key=lambda x: int(x.split()[0]))
    df = df[column_order]

    print(df)

    # Save the updated DataFrame back to CSV
    df.to_csv('cookie_performance.csv', index=False)

if __name__ == "__main__":
    # Single run
    cookie_clicker(time_between_buys=5, duration=5)

    # # Changing time between buys
    # for i in range(1, 10):
    #     cookie_clicker(time_between_buys=i, duration=2)
    #
    # # Changing the duration
    # for i in range(1, 10):
    #     cookie_clicker(time_between_buys=i, duration=2)