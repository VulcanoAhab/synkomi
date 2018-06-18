from pySteer.api import Config
from pySteer.routes import Augur
from pyBrows import seleniumPhantom, seleniumChrome

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--configuration", "-c")
    args=parser.parse_args()

    #preset Config
    Config.registerDrivers(
        selenium_phantom_vanilla=seleniumPhantom.Vanilla,
        selenium_phantom_chrome=seleniumPhantom.Chrome,
        selenium_chrome=seleniumChrome.Headless
    )

    #load Config
    Config.setFile(args.configuration)
    CONF=Config()

    #create browser
    browser=CONF.getDriver() #need to implement drivers args

    #get target page
    if CONF.request["method"] != "GET":
        raise Exception("[-] Only GET method working for now")
    print("[+] GET: {}".format(CONF.request["url"]))
    browser.get(CONF.request["url"])

    #start interaction
    Augur.setBrowser(browser)
    Augur.process(CONF)

    #close browser
    browser.close()
