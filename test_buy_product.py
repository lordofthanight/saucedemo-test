from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_buy_product(browser, url):
    # заходим на сайт
    browser.get(url)

    # логинимся
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # добавляем товар в корзину (первый попавшийся)
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # идем в корзину
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # чекаут
    browser.find_element(By.ID, "checkout").click()

    # заполняем форму
    browser.find_element(By.ID, "first-name").send_keys("Ivan")
    browser.find_element(By.ID, "last-name").send_keys("Petrov")
    browser.find_element(By.ID, "postal-code").send_keys("123456")
    browser.find_element(By.ID, "continue").click()

    # заканчиваем покупку
    browser.find_element(By.ID, "finish").click()

    # проверяем что все ок
    wait = WebDriverWait(browser, 10)
    success_text = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert success_text.text == "Thank you for your order!"
