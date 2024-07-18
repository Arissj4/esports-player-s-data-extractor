from Lib import libs


def chrome(ws, game):
    c_option = libs.Options()
    c_option.headless = True

    try:
        driver = libs.webdriver.Chrome(options=c_option)
        driver.get("https://liquipedia.net/" + game + "/Main_Page")

        element = driver.find_element_by_id("searchInput")
        element.clear()
        element.send_keys(ws)
        element.send_keys(libs.Keys.ENTER)

        sup = libs.BeautifulSoup(driver.page_source, "html.parser")

        return sup, driver

    except:

        sup, driver = 0, 0


# def fire(ws, game):
#     f_options = libs.Options()
#     f_options.add_argument('-headless')
#     try:
#         driver = libs.webdriver.Firefox()
#         driver.get("https://liquipedia.net/" + game + "/Main_Page")
#
#         element = driver.find_element_by_id("searchInput")
#         element.clear()
#         element.send_keys(ws)
#         element.send_keys(libs.Keys.ENTER)
#
#         sup = libs.BeautifulSoup(driver.page_source, "html.parser")
#
#         return sup, driver
#
#     except:
#
#         sup, driver = 1,1
#         return sup,driver
#
#
# def edge(ws, game):
#     try:
#         driver = libs.webdriver.Edge()
#         driver.get("https://liquipedia.net/" + game + "/Main_Page")
#
#         element = driver.find_element_by_id("searchInput")
#         element.clear()
#         element.send_keys(ws)
#         element.send_keys(libs.Keys.ENTER)
#
#         sup = libs.BeautifulSoup(driver.page_source, "html.parser")
#
#         return sup, driver
#
#     except:
#
#         sup, driver = 2, 2
#         return sup, driver