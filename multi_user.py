# Whatsapp post using python by Mahesh Sawant

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print("Scan the QR code")

another_user = True
another_msg = True
use_again = True
all_names = []

while use_again == True:

    while another_user == True:
        name = input("Enter the name of user or group : ")
        all_names.append(name)
        y_n = int(input("Do you wants to add another user(1 for yes/0 for no) : "))
        if y_n == 1:
            another_user = True
        else:
            another_user = False

    while another_msg == True:
        msg = input("Enter your message : ")
        for name in all_names:
            try:
                user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
                user.click()

                msg_box = driver.find_element_by_class_name('_1Plpp')

                msg_box.send_keys(msg)
                button = driver.find_element_by_class_name('_35EW6')
                button.click()

            except NoSuchElementException as exception:
                print(name,"is not found in your friends or groups")

        y_n = int(input("Do you wants to send another message(1 for yes/0 for no) : "))
        if y_n == 1:
            another_msg = True
        else:
            another_msg = False

    y_n = int(input("Do you wants to use this again(1 for yes/0 for no) : "))
    if y_n == 1:
        use_again = True
        another_user = True
        another_msg = True
        all_names.clear()
    else:
        use_again = False
        print("Thank you, for using the program.")
