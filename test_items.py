import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
  browser.get(link)

  # Пауза для визуальной проверки текста кнопки рецензентами (критерий 2)
  time.sleep(30)

  # Ищем кнопку добавления в корзину
  add_to_basket_buttons = browser.find_elements(
      By.CSS_SELECTOR, "button.btn-add-to-basket"
  )

  # Проверяем, что кнопка найдена на странице
  assert (
      len(add_to_basket_buttons) > 0
  ), "Button 'Add to basket' was not found on the page!"