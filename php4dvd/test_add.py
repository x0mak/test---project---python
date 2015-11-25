# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import app
import time
from model.user import User
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.by import By


def do_login(driver, user):
    driver.get("http://localhost:8080/php4dvd/")
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(user.username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(user.password)
    driver.find_element_by_name("submit").click()


def test_login(app):
    do_login(app.driver, User.Admin())


def test_add(app):
    do_login(app.driver, User.Admin())
    app.driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
    app.driver.find_element_by_name("name").clear()
    app.driver.find_element_by_name("name").send_keys("titaniccc")
    app.driver.find_element_by_name("year").clear()
    app.driver.find_element_by_name("year").send_keys("1995")
    app.driver.find_element_by_id("submit").click()


def test_remove(app):
    do_login(app.driver, User.Admin())
    app.driver.find_element(By.XPATH, '//*[.="titaniccc"]').click()
    app.driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
    app.driver.assertRegexpMatches(app.driver.close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")


def test_search(app):
    do_login(app.driver, User.Admin())
    app.driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
    app.driver.find_element_by_id("imdbsearch").clear()
    app.driver.find_element_by_id("imdbsearch").send_keys(u"Шар")
    app.driver.find_element_by_css_selector("input[type=\"submit\"]").click()
    app.driver.assertTrue(app.driver.is_element_present(By.LINK_TEXT, u"Шар"))

