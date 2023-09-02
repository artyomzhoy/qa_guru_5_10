import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


# Шаги с декоратором @allure.step
def test_decorator_allure_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('81')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('')


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-button').click()
    s('#query-builder-test').send_keys(repo).press_enter()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открывает таб Issues')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step('Проверяем наличие Issue c номером {number}')
def should_see_issue_with_number(number):
    s(by.partial_text('#' + number)).should(be.visible)
