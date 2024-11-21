from selenium import webdriver
from time import sleep

d = webdriver.Chrome()
d.get("C:/Users/klitv/Downloads/tip_calc/tip_calc/index.html")
d.find_element(by="id", value="billamt").send_keys("100")
d.find_element(by="xpath", value='//*[@id="serviceQual"]/option[3]')
d.find_element(by="id", value="peopleamt").send_keys("5")
d.find_element(by="id", value="musicamt").send_keys("2")
d.find_element(by="id", value="calculate").click()
sleep(2)
expected = "6.00"
actual = d.find_element(by="id", value="tip").text


def my_test(values_to_check, expected):
    is_visible = d.find_element(by="id", value="tip").is_displayed()
    assert actual == expected
    assert is_visible

#if i pass a list of value to a function like this:["100","5", "2"] , and in the function itself the argument is "values_to_check" and not a list how can i use the values from the list?
# if expected != actual:
#     print("bad")
#
# else:
#     print("good")

my_test(["100","5", "2"], "6.00")

sleep(100)