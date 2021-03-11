from selenium import webdriver
from config import dubizzle_username, dubizzle_password


def run():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://dubai.dubizzle.com/')
    login_button = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[1]/div[2]/div[1]/div/div[2]/button[3]')
    login_button.click()

    login_by_email = driver.find_element_by_xpath('//*[@id="popup_login_link"]')
    login_by_email.click()

    username = driver.find_element_by_xpath('//*[@id="popup_email"]')
    username.clear()
    username.send_keys(dubizzle_username)

    password = driver.find_element_by_xpath('//*[@id="popup_password"]')
    password.clear()
    password.send_keys(dubizzle_password)

    login_btn = driver.find_element_by_xpath('//*[@id="popup_login_btn"]')
    login_btn.click()

    driver.get_cookie()
    driver.close()


if __name__ == '__main__':
    run()