from playwright.sync_api import Playwright, sync_playwright, expect
import re
import os
import multiprocessing
import pandas as pd
from time import sleep, perf_counter

url = 'https://www.saucedemo.com/'

def run(playwright: Playwright) -> None:
    # Browser [Chrome, Firefox, WebKit]
    # browser = playwright.firefox.lanch(headless=False)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    sleep(2)

    # Browsing the website

    # Login
    # page.reload()
    page.locator('//div//input[@placeholder="Username"]').fill('visual_user')
    sleep(0.2)
    page.locator('//div//input[@placeholder="Password"]').fill('secret_sauce')
    sleep(0.2)
    page.locator('//input[@type="submit"]').click()
    sleep(2)

    if page.locator('//div[contains(@class,"error-mess")]//h3').is_visible():
        print("Error loggin in to system. Please chcek your credentials...")
    
    # Input Actions : Buy 2 T-Shirts
    sleep(0.5)
    # T-Shirt - 1
    t1 = page.locator('((//div[@class="inventory_item"])[3]//div)[4]').inner_text()
    print(t1)
    sleep(0.2)
    page.locator('(//div[@class="inventory_item"])[3]//button').click()
    sleep(1)
    # T-Shirt - 2
    t2 = page.locator('((//div[@class="inventory_item"])[6]//div)[4]').inner_text()
    print(t2)
    sleep(0.2)
    page.locator('(//div[@class="inventory_item"])[6]//button').click()
    sleep(1)
    # Moving to Cart
    page.locator('//div//a[@class="shopping_cart_link"]').click()
    sleep(0.2)
    # Checkout
    page.locator('//button[@id="checkout"]').click()
    sleep(1)

    # Address Information
    page.locator('//div//input[@placeholder="First Name"]').fill('visual')
    sleep(0.2)
    page.locator('//div//input[@placeholder="Last Name"]').fill('user')
    sleep(0.2)
    page.locator('//div//input[@placeholder="Zip/Postal Code"]').fill('1011')
    sleep(0.2)
    page.locator('//div//input[@id="continue"]').click()
    sleep(1)
    page.locator('//button[@id="finish"]').click()
    sleep(2)

    context.close()
    browser.close()


def fn_run():
    # information('function f')
    with sync_playwright() as playwright:
        run(playwright)

if __name__ == "__main__":
    start = perf_counter()
    fn_run()
    end = perf_counter()
    print(f'\n---------------\n Finished in {round(end-start, 2)} second(s)')
