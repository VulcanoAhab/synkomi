from pySteer.api import Config
from pyBrows import phantomSelenium, seleniumChrome

#preset Config
Config.registerDrivers(
    selenium_phantom=phantomSelenium,
    selenium_chrome=seleniumChrome.Headless
)

#load Config
Config.setFile("sample.yaml")
CONF=Config()

#create browser
browser=CONF.getDriver() #need to implement drivers args

#get target page
if CONF.request["method"] != "GET":
    raise Exception("[-] Only GET method working for now")
browser.get(CONF.request["url"])
