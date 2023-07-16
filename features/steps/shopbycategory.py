from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


CHOOSE_BODY = (By.CSS_SELECTOR,"nav.header__inline-menu li list-menu-item[data-title='Body'")
SHOP_CATEGORY = (By.CSS_SELECTOR,"nav.header__inline-menu li summary svg")
# SHOP_CATEGORY = (By.XPATH, "//summary[@class = 'header__menu-item header__menu-item--top list-menu__item focus-inset']//span[contains(text(),'Shop by Category')]")


#$$("form[name='signIn']")
#$$("input#ap_email")

@given('Open CureSkin Shopping page')
def open_cureskin(context):
    context.app.main_page.open_main_page()

@when('Click Shop by Category Menu')
def click_category(context ):
    # order_button=context.driver.find_element(*CLICK_CART)
    # context.driver.wait.until(EC.element_to_be_clickable(order_button))
    # order_button.click()
    print('about to click')
    # sleep(5)
    # print('after sleep to click')
    # myelement=context.app.main_page.find_element(*SHOP_CATEGORY)
    # print("element text:",myelement.text)
    # context.app.main_page.click(*SHOP_CATEGORY)
    # sleep(10)

    catlist=context.app.main_page.find_elements(*SHOP_CATEGORY)
    print("category list length:", len(catlist))
    for cat in catlist:
        print("category text",cat.text)
        if cat.text == 'SHOP BY CATEGORY':
            cat.click()


    if len(catlist) >2 :
        category=catlist[2]
        print("category text",category.text)
        category.click()
@when('Click Body Menu item')
def click_Body(context ):
    # order_button=context.driver.find_element(*CLICK_CART)
    # context.driver.wait.until(EC.element_to_be_clickable(order_button))
    # order_button.click()
    context.app.main_page.wait_for_element_click(*CHOOSE_BODY)


@then('Verify that {category} text is exists in URL')
def verify_amazon_empty_page_open(context,category):
    context.app.main_page.verify_url_contains_query(category)

