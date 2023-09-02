import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


# Лямбда шаги через with allure.step
def test_dynamic_with_allure_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('')

    with allure.step('Ищем репозиторий'):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example').press_enter()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открывает таб Issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие Issue c номером 76'):
        s(by.partial_text('#81')).should(be.visible)
