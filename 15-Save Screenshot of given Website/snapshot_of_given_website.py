import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# google驱动路径
path = r"D:\Python\chromedriver.exe"
script_name = sys.argv[0]
print(script_name)

options = Options()
options.add_argument('--headless')
driver = driver = webdriver.Chrome(executable_path=r"{}".format(path))
print(options)

try:
    url = input("请输入url:")
    driver.get(url)
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(page_width, page_height)
    driver.save_screenshot('screenshot.png')
    driver.quit()
    print("SUCCESS")
except IndexError:
    print('Usage: %s URL' % script_name)