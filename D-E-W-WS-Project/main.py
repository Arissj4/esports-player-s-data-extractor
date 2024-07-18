from Lib import libs


class ExampleApp(libs.QtWidgets.QMainWindow, libs.design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.game = ""
        self.game_link = "dota2"

        self.comboBox.currentIndexChanged.connect(self.select_game)

        self.search_but.clicked.connect(self.search)

    def select_game(self):
        self.game = ""

        index_game = self.comboBox.currentIndex()
        li_game = ["dota2", "leagueoflegends", "rainbowsix", "counterstrike", "valorant", "pubg",
                   "overwatch", "apexlegends", "rocketleague"]

        self.game_link = li_game[index_game]

    def search(self):
        word_search = str(self.lineEdit.text())
        error = 0

        if word_search == "":
            Message_box = libs.QMessageBox()
            Message_box.setIcon(libs.QMessageBox.Information)
            Message_box.setText("Serach box is empty")
            Message_box.setInformativeText("Please enter the name of the player you want")
            Message_box.setWindowTitle("Player Name")
            Message_box.setStandardButtons(libs.QMessageBox.Ok)
            x = Message_box.exec_()


        else:
            try:
                sup, driver = libs.drivers.chrome(word_search, self.game_link)
            except:
                error = 1
                # try:
                #     sup, driver = libs.drivers.fire(word_search, self.game_link)
                # except:
                #     try:
                #         sup, driver = libs.drivers.chrome(word_search, self.game_link)
                #     except:
                #         error = 1

            if error == 0:
                try:

                    res = sup.find_all("div", {"class": "infobox-cell-2"})

                    el = driver.find_element_by_partial_link_text("Results")
                    driver.execute_script("arguments[0].click()", el)

                    elm_page = []
                    for item in range(0, len(res)):
                        elm_page.append(str(res[item].text))

                    self.lbl_w_name.setText(libs.find.find_name(elm_page))

                    self.lbl_w_birth.setText(libs.find.birth(elm_page))

                    self.lbl_w_country.setText(libs.find.Country(elm_page))

                    self.lbl_w_status.setText(libs.find.status(elm_page))

                    self.lbl_w_team.setText(libs.find.team(elm_page))

                    self.lbl_w_role.setText(libs.find.role(elm_page))

                    self.lbl_w_money.setText(libs.find.earn(elm_page))

                    self.lbl_w_hero.setText(libs.find.hero(sup, self.game_link))

                    self.lbl_w_id.setText(libs.find.id(elm_page))

                    self.listWidget.clear()
                    self.listWidget.addItems(libs.find.achiv(driver))

                    driver.close()

                except:

                    Message_box = libs.QMessageBox()
                    Message_box.setIcon(libs.QMessageBox.Information)
                    Message_box.setText("Player name or Game isn't correct")
                    Message_box.setInformativeText("Couldn't Find the Player you are looking for in this Game")
                    Message_box.setWindowTitle("Wrong Name/Game")
                    Message_box.setStandardButtons(libs.QMessageBox.Ok)
                    x = Message_box.exec_()

            else:
                Message_box = libs.QMessageBox()
                Message_box.setIcon(libs.QMessageBox.Information)
                Message_box.setText("Download Webdriver")
                Message_box.setInformativeText("Couldn't Find WebDriver.Please Download WebDriver for Google Chrome")
                Message_box.setWindowTitle("WebDriver")
                Message_box.setStandardButtons(libs.QMessageBox.Ok)
                x = Message_box.exec_()


if __name__ == '__main__':
    app = libs.QtWidgets.QApplication(libs.sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()
