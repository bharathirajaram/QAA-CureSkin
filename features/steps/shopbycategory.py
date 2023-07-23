from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


CHOOSE_BODY = (By.CSS_SELECTOR,"nav.header__inline-menu li list-menu-item[data-title='Body'")
# SHOP_CATEGORY = (By.CSS_SELECTOR,"nav.header__inline-menu li summary svg")
SHOP_CATEGORY = (By.XPATH, "//span[text()='Shop by Category' and (@class='label')]")

POP_UP_CLOSE_BTN = (By.XPATH, "//button[@class='popup-close']")
# SHOP_CATEGORY = (By.XPATH, "//summary[@class = 'header__menu-item header__menu-item--top list-menu__item focus-inset']//span[contains(text(),'Shop by Category')]")


#$$("form[name='signIn']")
#$$("input#ap_email")

@given('Open CureSkin Shopping page')
def open_cureskin(context):
    context.app.main_page.open_main_page()

@when('Click Shop by Category Menu')
def click_category(context ):
    # sleep(2)
    #close popup window
    context.app.main_page.wait_for_element_click(*POP_UP_CLOSE_BTN)
    # click Shop by Category
    # sleep(10)
    context.app.main_page.wait_for_element_click(*SHOP_CATEGORY)

@when('Click Body Menu item')
def click_Body(context ):
    #Click Body menu item
    context.app.main_page.wait_for_element_click(*CHOOSE_BODY)


@then('Verify that {category} text is exists in URL')
def verify_selected_category_exists(context,category):
    #Verify the URL contains that category name
    context.app.main_page.verify_url_contains_query(category)

