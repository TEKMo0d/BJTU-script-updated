from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 10)
URL_MIS = 'https://mis.bjtu.edu.cn/home/'
URL_JWC = 'http://jwc.bjtu.edu.cn'

USER_ID = ''
PASSWORD = ''
delta = 0.9

def search(user_id, password):
    driver.get(URL_MIS)
    try:
        name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#id_loginname')))
        password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#id_password')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form1 > div > div > button')))
        name.send_keys(user_id)
        password_field.send_keys(password)
        submit.click()
        return True
    except TimeoutException:
        return False

def tap_into_jiaowu():
    driver.maximize_window()
    shaung_xue_wei = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'CSS_SELECTOR_HERE')))
    shaung_xue_wei.click()

def solve():
    elem = driver.find_element_by_xpath(
        '//*[@id="wrap"]/div[2]/div[2]/div/div[2]/div/div/table/tbody/tr[2]/td[1]/div/div/h5/a')
    elem.click()

    handles = driver.window_handles
    driver.switch_to.window(handles[1])

    time.sleep(3)

    try:
        elem = driver.find_element_by_css_selector('#sidebar > div > div.nav-wrap > ul > li:nth-child(4) > a > span')
        elem.click()
    except:
        elem = driver.find_element_by_xpath('//*[@id="menu-toggler"]')
        print(elem.id)
        elem.click()
        print('End')

    driver.find_element_by_xpath('//*[@id="sidebar2"]/div[1]/div[1]/div/ul/li[1]/ul/li[2]/a').click()
def duoXuan(i):

    driver.find_element_by_xpath(f'//*[@id="current"]/table/tbody/tr[{i+2}]/td[1]/label').click()
    return True

def XuanKe():
    driver.find_element_by_xpath('//*[@id="sidebar2"]/div[1]/div[1]/div/ul/li[2]/ul/li[1]/a').click()
    flag = False
    try_cnt = 1
    i = 0
    while not flag:
        try:
            flag = duoXuan(i)
        except Exception as e:
            print(i)
            print(e)
            if i == 3:
                i = 0
            i += 1
            driver.refresh()
            try_cnt += 1
            time.sleep(delta)

    driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
    driver.find_element_by_xpath('//*[@id="select-submit-btn"]').click()
    print("OK!")
    print("You have try " + str(try_cnt) + " times.")

def main():
    if search(USER_ID, PASSWORD):
        tap_into_jiaowu()
        solve()
        XuanKe()
    else:
        print("Login failed, please check your credentials or network.")

if __name__ == '__main__':
    main()