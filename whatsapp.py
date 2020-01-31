from selenium import webdriver
driver=webdriver.Firefox(executable_path = '/home/tejas/Downloads/geckodriver')
driver.get('https://web.whatsapp.com/')

name=input("Enter the Name of User ")
msg=input("Enter Message")

count=int(input("How many times You want to send the same messsage to the user:"))

input("enter anything after scanning QR code")

user=driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()

msg_box=driver.find_element_by_class_name('_13mgZ')
#_3FeAD _1PRhq  (_13mgZ)  (wjdTm)
for i in range(count):
	msg_box.send_keys(msg)
	button=driver.find_element_by_class_name('_3M-N-')
	button.click()

#_3M-N-   hnQHL
# its working...dont touch it

'''
from selenium import webdriver

driver = webdriver.Firefox(executable_path = '/home/tejas/Downloads/geckodriver')
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_2S1VP')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()'''