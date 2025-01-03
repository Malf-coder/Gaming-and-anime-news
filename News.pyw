import sys
import UInews
import requests as req
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

ParsedGamesNews = []

urlGame = "https://stopgame.ru/news" 

headersGame = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                  "/100.0.4896.160 YaBrowser/22.5.2.615 Yowser/2.5 Safari/537.36"
}

pageGame = req.get(urlGame, headers=headersGame)

soupGame = BeautifulSoup(pageGame.text, "html.parser")

name1 = soupGame.find_all("div", {"class": "caption caption-bold"}) # не работает!!!!!!!!!!!!!!
for item in name1:
    ParsedGamesNews.append(item.text.replace('\n', '').replace('\nB', ''))

ParsedAnimeNews = []

urlAnime = "https://kg-portal.ru/news/anime/"

headersAnime = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                  "/100.0.4896.160 YaBrowser/22.5.2.615 Yowser/2.5 Safari/537.36"
}

pageAnime = req.get(urlAnime, headers=headersAnime)

soupAnime = BeautifulSoup(pageAnime.text, "html.parser")

name1 = soupAnime.find_all("a", {"class": "news_card_link"})
for item in name1:
    ParsedAnimeNews.append(item.text.replace('\n', '').replace('\nB', ''))


class ExampleAppWin(QMainWindow, UInews.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.y = 20
        self.Posts = []
        self.GamesNewsPars2 = ParsedGamesNews
        self.GamesAnimePars2 = ParsedAnimeNews
        self.Enablbutton = True
        font = QFont()
        font.setPointSize(13)
        for i in range(7):
            self.label_3 = QLabel(self.centralwidget)
            self.label_3.setGeometry(QRect(180, -150, 501, 61))
            self.label_3.setStyleSheet("background-color: rgba(238, 238, 238, 140);")
            self.label_3.setFont(font)

            self.Posts.append(self.label_3)

        self.NewsButton.clicked.connect(self.GameNews)
        self.AnimeButton.clicked.connect(self.AnimeNews)
        self.parsedGameNews()

    def parsedGameNews(self):

        nomerSz = 59
        srez = 59
        self.stepText = 0

        for i in self.GamesNewsPars2:

            if self.stepText == 7:
                break

            if i == " ":
                print("None")
                continue

            if len(i) <= nomerSz:
                self.Posts[self.stepText].setText(i)
                continue

            i2 = i[0:srez]

            if i[srez] == " ":
                if len(i[srez + 1:]) > nomerSz:
                    print(len(i[srez + 1:]))
                    srez2 = nomerSz * 2
                    while i[srez2] != " ":
                        srez2 -= 1
                    self.Posts[self.stepText].setText(f"{i2}\n{i[srez + 1:srez2]}\n{i[srez2 + 1:]}")
                else:

                    self.Posts[self.stepText].setText(f"{i[0:srez]}\n{i[srez + 1:]}")

            if i[srez] != " ":
                while i[srez] != " ":
                    srez -= 1
                    i2 = i[0:srez]
                if len(i[nomerSz + 1:]) > nomerSz:

                    srez2 = nomerSz * 2
                    while i[srez2] != " ":
                        srez2 -= 1
                    self.Posts[self.stepText].setText(f"{i2}\n{i[srez + 1:srez2]}\n{i[srez2 + 1:]}")
                else:
                    self.Posts[self.stepText].setText(f"{i[0:srez]}\n{i[srez + 1:]}")

            srez = 59
            self.stepText += 1

        self.stepText = 0
        self.AnimationPosts()

    def parsedAnimeNews(self):
        nomerSz = 55
        srez = 55
        self.stepText = 0

        for i in self.GamesAnimePars2:

            if self.stepText == 7:
                break

            if i == " ":
                print("None")
                continue

            if len(i) <= nomerSz:
                self.Posts[self.stepText].setText(i)
                continue

            i2 = i[0:srez]

            if i[srez] == " ":
                if len(i[srez + 1:]) > nomerSz:
                    print(len(i[srez + 1:]))
                    srez2 = nomerSz * 2
                    while i[srez2] != " ":
                        srez2 -= 1
                    self.Posts[self.stepText].setText(f"{i2}\n{i[srez + 1:srez2]}\n{i[srez2 + 1:]}")
                else:

                    self.Posts[self.stepText].setText(f"{i[0:srez]}\n{i[srez + 1:]}")

            if i[srez] != " ":
                while i[srez] != " ":
                    srez -= 1
                    i2 = i[0:srez]
                if len(i[nomerSz + 1:]) > nomerSz:

                    srez2 = nomerSz * 2
                    while i[srez2] != " ":
                        srez2 -= 1
                    self.Posts[self.stepText].setText(f"{i2}\n{i[srez + 1:srez2]}\n{i[srez2 + 1:]}")
                else:
                    self.Posts[self.stepText].setText(f"{i[0:srez]}\n{i[srez + 1:]}")

            srez = 55
            self.stepText += 1

        self.stepText = 0
        self.AnimationPosts()

    def GameNews(self):

        self.NewsButton.setStyleSheet("QPushButton#NewsButton {\n"
                                      "  font-weight: 700;\n"
                                      "  color:#00ADB5 ;\n"
                                      "  text-decoration: none;\n"
                                      "  border-radius: 3px;\n"
                                      "  border-width: 3px;\n"
                                      "  box-shadow: 0 -3px rgb(53,167,110) inset;\n"
                                      "  transition: 0.2s;\n"
                                      "  border-style: outset;\n"
                                      "  border-radius: 20px;\n"
                                      "  border-color:#00ADB5;\n"
                                      "} \n"
                                      "QPushButton#NewsButton:hover { border-color: rgb(0, 145, 150);\n"
                                      "                                                     color: rgb(0, 145, 150);\n"
                                      "}\n"
                                      "\n"
                                      "")

        self.AnimeButton.setStyleSheet("QPushButton#AnimeButton {\n"
                                       "  font-weight: 700;\n"
                                       "  color:#222831 ;\n"
                                       "  text-decoration: none;\n"
                                       "  border-radius: 3px;\n"
                                       "  border-width: 3px;\n"
                                       "  box-shadow: 0 -3px rgb(53,167,110) inset;\n"
                                       "  transition: 0.2s;\n"
                                       "  border-style: outset;\n"
                                       "  border-radius: 20px;\n"
                                       "  border-color:#222831;\n"
                                       "} \n"
                                       "QPushButton#AnimeButton:hover { border-color:rgb(20, 24, 30);\n"
                                       "                                                    color:rgb(20, 24, 30);\n"
                                       "}")

        if not self.Enablbutton:
            self.Enablbutton = True
            self.ExitAnimationPosts()

    def AnimeNews(self):

        self.AnimeButton.setStyleSheet("QPushButton#AnimeButton {\n"
                                       "  font-weight: 700;\n"
                                       "  color:#00ADB5 ;\n"
                                       "  text-decoration: none;\n"
                                       "  border-radius: 3px;\n"
                                       "  border-width: 3px;\n"
                                       "  box-shadow: 0 -3px rgb(53,167,110) inset;\n"
                                       "  transition: 0.2s;\n"
                                       "  border-style: outset;\n"
                                       "  border-radius: 20px;\n"
                                       "  border-color:#00ADB5;\n"
                                       "} \n"
                                       "QPushButton#AnimeButton:hover { border-color:rgb(0, 145, 150);\n"
                                       "                                                    color:rgb(0, 145, 150);\n"
                                       "}")

        self.NewsButton.setStyleSheet("QPushButton#NewsButton {\n"
                                      "  font-weight: 700;\n"
                                      "  color:#222831 ;\n"
                                      "  text-decoration: none;\n"
                                      "  border-radius: 3px;\n"
                                      "  border-width: 3px;\n"
                                      "  box-shadow: 0 -3px rgb(53,167,110) inset;\n"
                                      "  transition: 0.2s;\n"
                                      "  border-style: outset;\n"
                                      "  border-radius: 20px;\n"
                                      "  border-color:#222831;\n"
                                      "} \n"
                                      "QPushButton#NewsButton:hover { border-color: rgb(20, 24, 30);\n"
                                      "                                                     color: rgb(20, 24, 30);\n"
                                      "}\n"
                                      "\n"
                                      "")

        if self.Enablbutton:
            self.Enablbutton = False
            self.ExitAnimationPosts()

    def setTextBlox(self):
        if self.Enablbutton:
            self.parsedGameNews()
        if not self.Enablbutton:
            self.parsedAnimeNews()

    def ExitAnimationPosts(self):
        self.AlertAnim1 = QPropertyAnimation(self.Posts[0], b"pos")
        self.AlertAnim1.setEasingCurve(QEasingCurve.OutCubic)
        self.AlertAnim1.setEndValue(QPoint(180, 700))
        self.AlertAnim1.setDuration(3900)
        self.AlertAnim1.start()

        self.AlertAnim2 = QPropertyAnimation(self.Posts[1], b"pos")
        self.AlertAnim2.setEasingCurve(QEasingCurve.OutCubic)
        self.AlertAnim2.setEndValue(QPoint(180, 700))
        self.AlertAnim2.setDuration(3400)
        self.AlertAnim2.start()

        self.AlertAnim3 = QPropertyAnimation(self.Posts[2], b"pos")
        self.AlertAnim3.setEasingCurve(QEasingCurve.OutCubic)
        self.AlertAnim3.setEndValue(QPoint(180, 700))
        self.AlertAnim3.setDuration(2900)
        self.AlertAnim3.start()

        self.AlertAnim4 = QPropertyAnimation(self.Posts[3], b"pos")
        self.AlertAnim4.setEasingCurve(QEasingCurve.OutCubic)
        self.AlertAnim4.setEndValue(QPoint(180, 700))
        self.AlertAnim4.setDuration(2400)
        self.AlertAnim4.start()

        self.AlertAnim5 = QPropertyAnimation(self.Posts[4], b"pos")
        self.AlertAnim5.setEasingCurve(QEasingCurve.OutCubic)
        self.AlertAnim5.setEndValue(QPoint(180, 700))
        self.AlertAnim5.setDuration(1900)
        self.AlertAnim5.start()

        self.AlertAnim6 = QPropertyAnimation(self.Posts[5], b"pos")
        self.AlertAnim6.setEasingCurve(QEasingCurve.OutCubic)
        self.AlertAnim6.setEndValue(QPoint(180, 700))
        self.AlertAnim6.setDuration(1400)
        self.AlertAnim6.start()

        self.AlertAnim7 = QPropertyAnimation(self.Posts[6], b"pos")
        self.AlertAnim7.setEasingCurve(QEasingCurve.OutCubic)
        self.AlertAnim7.setEndValue(QPoint(180, 700))
        self.AlertAnim7.setDuration(1000)
        self.AlertAnim7.start()
        QTimer.singleShot(1900, self.setTextBlox)

    def AnimationPosts(self):

        self.AlertAnim1 = QPropertyAnimation(self.Posts[0], b"pos")
        self.AlertAnim1.setEasingCurve(QEasingCurve.OutCubic)
        self.AlertAnim1.setStartValue(QPoint(180, -150))
        self.AlertAnim1.setEndValue(QPoint(180, self.y))
        self.AlertAnim1.setDuration(1000)
        self.AlertAnim1.start()
        self.y += 80
        self.AlertAnim2 = QPropertyAnimation(self.Posts[1], b"pos")
        self.AlertAnim2.setEasingCurve(QEasingCurve.OutCubic)
        self.AlertAnim2.setStartValue(QPoint(180, -150))
        self.AlertAnim2.setEndValue(QPoint(180, self.y))
        self.AlertAnim2.setDuration(1400)
        self.AlertAnim2.start()
        self.y += 80
        self.AlertAnim3 = QPropertyAnimation(self.Posts[2], b"pos")
        self.AlertAnim3.setEasingCurve(QEasingCurve.OutCubic)
        self.AlertAnim3.setStartValue(QPoint(180, -150))
        self.AlertAnim3.setEndValue(QPoint(180, self.y))
        self.AlertAnim3.setDuration(1900)
        self.AlertAnim3.start()
        self.y += 80
        self.AlertAnim4 = QPropertyAnimation(self.Posts[3], b"pos")
        self.AlertAnim4.setEasingCurve(QEasingCurve.OutCubic)
        self.AlertAnim4.setStartValue(QPoint(180, -150))
        self.AlertAnim4.setEndValue(QPoint(180, self.y))
        self.AlertAnim4.setDuration(2400)
        self.AlertAnim4.start()
        self.y += 80
        self.AlertAnim5 = QPropertyAnimation(self.Posts[4], b"pos")
        self.AlertAnim5.setEasingCurve(QEasingCurve.OutCubic)
        self.AlertAnim5.setStartValue(QPoint(180, -150))
        self.AlertAnim5.setEndValue(QPoint(180, self.y))
        self.AlertAnim5.setDuration(2900)
        self.AlertAnim5.start()
        self.y += 80
        self.AlertAnim6 = QPropertyAnimation(self.Posts[5], b"pos")
        self.AlertAnim6.setEasingCurve(QEasingCurve.OutCubic)
        self.AlertAnim6.setStartValue(QPoint(180, -150))
        self.AlertAnim6.setEndValue(QPoint(180, self.y))
        self.AlertAnim6.setDuration(3400)
        self.AlertAnim6.start()
        self.y += 80
        self.AlertAnim7 = QPropertyAnimation(self.Posts[6], b"pos")
        self.AlertAnim7.setEasingCurve(QEasingCurve.OutCubic)
        self.AlertAnim7.setStartValue(QPoint(180, -150))
        self.AlertAnim7.setEndValue(QPoint(180, self.y))
        self.AlertAnim7.setDuration(3900)
        self.AlertAnim7.start()
        self.y = 20


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExampleAppWin()
    window.show()
    app.exec_()
