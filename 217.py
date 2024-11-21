from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

d = webdriver.Chrome()
d.get("C:/Users/klitv/PycharmProjects/tip_calc/index.html")
# sleep(3)
# try:
#     alert = d.switch_to.alert
#     alert.accept()
#
# except NoAlertPresentException:
#     pass

d.find_element(by="id", value="billamt").send_keys("100")
select_element = d.find_element(by='id', value="serviceQual")
select = Select(select_element)
select.select_by_index(2)
d.find_element(by="id", value="peopleamt").send_keys("5")
sleep(2)
d.find_element(by="id", value="calculate").click()
sleep(2)
expected = "6.00"
actual = d.find_element(by="id", value="tip").text


# def my_test(values_to_check, expected):
#     is_visible = d.find_element(by="id", value="tip").is_displayed()
#     assert actual == expected
#     assert is_visible
#

if expected != actual:
    print("bad")

else:
    print("good")

# my_test(["100","5", "2"], "6.00")

sleep(100)