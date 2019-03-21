# whatsapp post using python by Mahesh Sawant.

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print("scan the Qr code")

name = input("Enter the name of user or group : ")
msg = input("Enter your message : ")
count = int(input("How many times you wants to send the same message : "))

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_1Plpp')

for i in range (count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
