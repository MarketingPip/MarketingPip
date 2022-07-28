from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import chromedriver_autoinstaller
import os
import json
import sys
import time









PythonScriptPath = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
print(PythonScriptPath)
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1920, 1024))
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path



chrome_options = webdriver.ChromeOptions()
options = [
   "--start-maximized",
   #"--window-size=1000,1000",
    "--ignore-certificate-errors",
    "--hide-scrollbars",
    "--user-agent=[Mozilla/5.0 (Linux; Android 5.1; PULP Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.119 Mobile Safari/537.36]"
]
for option in options:
    chrome_options.add_argument(option)


    
driver = webdriver.Chrome(options = chrome_options)


input_variable = "html/quote.html,html/movies.html"


input_variable2 = "demo"
input_variable3 = "File"
input_variable4 = "MarketingPip"



FileNames = input_variable







if input_variable3 == "URL":
    Files = FileNames.split(',')
    ReplaceText = "https://"
    Type="https://"
    Type2 = ""
    Type2 = Type2.replace(" ", "")
    Sleep = 10



else:

    Files = FileNames.split('.')
    ReplaceText = ".html"
    Type = f"file:///home/runner/work/{input_variable4}/{input_variable4}/"
    Type2 = ".html"
    Sleep = 5
    
    



if input_variable2 == "":
    FilePath = ""
else:
    FilePath = "./" + input_variable2 + "/"



FileNames = FileNames.split(',')
File_Names_List = []


for i in Files:
    File_Names_List.append(i)






File_Names_List.pop()
driver = webdriver.Chrome()
for s in File_Names_List:
    ScreenshotPath = FilePath
    FilePath = s.replace(ReplaceText, "")
    FileName = FilePath.replace(",", "")
    Name = FileName
    ScreenshotName = Name
    Link =  Type + Name + Type2
    if input_variable3 == "":
        index(Link)
    else:
        pass
    ScreenshotPath = ScreenshotPath + ScreenshotName
    ScreenshotPath = ScreenshotPath.replace("/", "-") 
    try:
        ScreenshotPath = ScreenshotPath.split('.com', 1)[0] + '.png'
        #driver.get('/home/runner/work/ProxyScraper-PY/ProxyScraper-PY/index.html')
        #driver.get("https://marketingpipeline.github.io/Markdown-Tag")
        driver.get(Link)
        driver.execute_script("document.querySelector('html').style.overflow = 'hidden';")
        time.sleep(Sleep)
        el = driver.find_element_by_tag_name('body')
        el = driver.save_screenshot(ScreenshotPath)
        print("Screenshot captured")
        print(Link)
        print(ScreenshotPath)
    except IOError as e:
        print(e)

driver.close()
