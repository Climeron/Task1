# Шматок Алексей P3175

import codecs
import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

alpha = "alphabet"
symbols = \
    {
        'a':
            [
                "   A    ",
                "  A A   ",
                " A   A  ",
                "A     A ",
                "AAAAAAA ",
                "A     A ",
                "A     A "
            ],
        'b':
            [
                "BBBBBB  ",
                "B     B ",
                "B     B ",
                "BBBBBB  ",
                "B     B ",
                "B     B ",
                "BBBBBB  "
            ],
        'c':
            [
                " CCCCC  ",
                "C     C ",
                "C       ",
                "C       ",
                "C       ",
                "C     C ",
                " CCCCC  "
            ],
        'd':
            [
                "DDDDDD  ",
                "D     D ",
                "D     D ",
                "D     D ",
                "D     D ",
                "D     D ",
                "DDDDDD  "
            ],
        'e':
            [
                "EEEEEEE ",
                "E       ",
                "E       ",
                "EEEEEEE ",
                "E       ",
                "E       ",
                "EEEEEEE "
            ],
        'f':
            [
                "FFFFFFF ",
                "F       ",
                "F       ",
                "FFFF    ",
                "F       ",
                "F       ",
                "F       "
            ],
        'g':
            [
                " GGGGG  ",
                "G     G ",
                "G       ",
                "G       ",
                "G  GGGG ",
                "G     G ",
                " GGGGGG "
            ],
        'h':
            [
                "H     H ",
                "H     H ",
                "H     H ",
                "HHHHHHH ",
                "H     H ",
                "H     H ",
                "H     H "
            ],
        'i':
            [
                "IIIIIII ",
                "   I    ",
                "   I    ",
                "   I    ",
                "   I    ",
                "   I    ",
                "IIIIIII "
            ],
        'j':
            [
                "JJJJJJJ ",
                "      J ",
                "      J ",
                "      J ",
                "      J ",
                "J     J ",
                " JJJJJ  "
            ],
        'k':
            [
                "K    KK ",
                "K   K   ",
                "K  K    ",
                "KKK     ",
                "K  K    ",
                "K   K   ",
                "K    KK "
            ],
        'l':
            [
                "L       ",
                "L       ",
                "L       ",
                "L       ",
                "L       ",
                "L       ",
                "LLLLLLL "
            ],
        'm':
            [
                "M     M ",
                "MM   MM ",
                "M M M M ",
                "M  M  M ",
                "M     M ",
                "M     M ",
                "M     M "
            ],
        'n':
            [
                "N     N ",
                "NN    N ",
                "N N   N ",
                "N  N  N ",
                "N   N N ",
                "N    NN ",
                "N     N "
            ],
        'o':
            [
                " OOOOO  ",
                "O     O ",
                "O     O ",
                "O     O ",
                "O     O ",
                "O     O ",
                " OOOOO  "
            ],
        'p':
            [
                "PPPPPP  ",
                "P     P ",
                "P     P ",
                "PPPPPP  ",
                "P       ",
                "P       ",
                "P       "
            ],
        'q':
            [
                " QQQQQ  ",
                "Q     Q ",
                "Q     Q ",
                "Q     Q ",
                "Q   Q Q ",
                "Q    QQ ",
                " QQQQQQ "
            ],
        'r':
            [
                "RRRRRR  ",
                "R     R ",
                "R     R ",
                "RRRRRR  ",
                "R   R   ",
                "R    R  ",
                "R     R "
            ],
        's':
            [
                " SSSSS  ",
                "S     S ",
                "S       ",
                " SSSSS  ",
                "      S ",
                "S     S ",
                " SSSSS  "
            ],
        't':
            [
                "TTTTTTT ",
                "   T    ",
                "   T    ",
                "   T    ",
                "   T    ",
                "   T    ",
                "   T    "
            ],
        'u':
            [
                "U     U ",
                "U     U ",
                "U     U ",
                "U     U ",
                "U     U ",
                "U     U ",
                " UUUUU  "
            ],
        'v':
            [
                "V     V ",
                "V     V ",
                "V     V ",
                "V     V ",
                " V   V  ",
                "  V V   ",
                "   V    "
            ],
        'w':
            [
                "W     W ",
                "W     W ",
                "W     W ",
                "W  W  W ",
                "W W W W ",
                "WW   WW ",
                "W     W "
            ],
        'x':
            [
                "X     X ",
                " X   X  ",
                "  X X   ",
                "   X    ",
                "  X X   ",
                " X   X  ",
                "X     X "
            ],
        'y':
            [
                "Y     Y ",
                "Y     Y ",
                " Y   Y  ",
                "  Y Y   ",
                "   Y    ",
                "   Y    ",
                "   Y    "
            ],
        'z':
            [
                "ZZZZZZZ ",
                "     Z  ",
                "    Z   ",
                "   Z    ",
                "  Z     ",
                " Z      ",
                "ZZZZZZZ "
            ],
        ' ':
            [
                "      ",
                "      ",
                "      ",
                "      ",
                "      ",
                "      ",
                "      "
            ],
        '1':
            [
                "═",
                " ",
                " ",
                " ",
                " ",
                " ",
                "═"
            ],
        '2':
            [
                "══════",
                " ╔══╗ ",
                "═╝  ║ ",
                "════╝ ",
                " ╔════",
                " ╚════",
                "══════"
            ],
        '3':
            [
                "══════",
                " ╔══╗ ",
                "═╝╔═╝ ",
                "  ╚═╗ ",
                "═╗  ║ ",
                " ╚══╝ ",
                "══════"
            ],
        '4':
            [
                "═╗  ╔═",
                " ║  ║ ",
                " ╚══╝ ",
                "════╗ ",
                "    ║ ",
                "    ║ ",
                "    ╚═"
            ],
        '5':
            [
                "══════",
                " ╔════",
                " ╚════",
                "════╗ ",
                "═╗  ║ ",
                " ╚══╝ ",
                "══════"
            ],
        '6':
            [
                "══════",
                " ╔══╗ ",
                " ║  ╚═",
                " ╚════",
                " ╔══╗ ",
                " ╚══╝ ",
                "══════"
            ],
        '7':
            [
                "══════",
                "════╗ ",
                "    ║ ",
                "    ║ ",
                "    ║ ",
                "    ║ ",
                "    ╚═"
            ],
        '8':
            [
                "══════",
                " ╔══╗ ",
                " ╚══╝ ",
                "──────",
                " ╔══╗ ",
                " ╚══╝ ",
                "══════"
            ],
        '9':
            [
                "══════",
                " ╔══╗ ",
                " ╚══╝ ",
                "════╗ ",
                "═╗  ║ ",
                " ╚══╝ ",
                "══════"
            ],
        '0':
            [
                "══════",
                " ╔══╗ ",
                " ║  ║ ",
                " ║  ║ ",
                " ║  ║ ",
                " ╚══╝ ",
                "══════"
            ],
        '-':
            [
                "      ",
                "      ",
                "══════",
                "      ",
                "══════",
                "      ",
                "      "
            ],
        '+':
            [
                "      ",
                " ╔══╗ ",
                "═╝  ╚═",
                "      ",
                "═╗  ╔═",
                " ╚══╝ ",
                "      "
            ],
        '=':
            [
                "      ",
                "══════",
                "══════",
                "      ",
                "══════",
                "══════",
                "      "
            ]
    }
connections = \
    {
        '1':
            [
                "╔",
                "║",
                "║",
                "║",
                "║",
                "║",
                "╚"
            ],
        '2':
            [
                "╗ ",
                "║ ",
                "║ ",
                "║ ",
                "║ ",
                "║ ",
                "╝ "
            ],
        '3':
            [
                "╔",
                "║",
                "╚",
                "╔",
                "║",
                "║",
                "╚"
            ],
        '4':
            [
                "╗ ",
                "║ ",
                "║ ",
                "║ ",
                "╝ ",
                "╗ ",
                "╝ "
            ],
        '5':
            [
                "╔",
                "║",
                "╚",
                " ",
                "╔",
                "║",
                "╚"
            ],
        '6':
            [
                "╔",
                "║",
                "║",
                "╚",
                " ",
                " ",
                " "
            ],
        '7':
            [
                "╔",
                "║",
                "║",
                "╚",
                "╔",
                "║",
                "╚"
            ],
        '8':
            [
                "╗ ",
                "╝ ",
                "╗ ",
                "║ ",
                "║ ",
                "║ ",
                "╝ "
            ],
        '9':
            [
                "╗ ",
                "║ ",
                "╝ ",
                "╗ ",
                "║ ",
                "║ ",
                "╝ "
            ],
        '10':
            [
                "╔",
                "╚",
                " ",
                " ",
                " ",
                " ",
                " "
            ],
        '11':
            [
                "╔",
                "║",
                "║",
                "╠",
                "║",
                "║",
                "╚"
            ],
        '12':
            [
                "╗ ",
                "║ ",
                "║ ",
                "╣ ",
                "║ ",
                "║ ",
                "╝ "
            ],
        '13':
            [
                " ",
                " ",
                "╔",
                "║",
                "╚",
                " ",
                " "
            ],
        '14':
            [
                "  ",
                "  ",
                "╗ ",
                "║ ",
                "╝ ",
                "  ",
                "  "
            ],
        '15':
            [
                " ",
                "╔",
                "╚",
                " ",
                "╔",
                "╚",
                " "
            ],
        '16':
            [
                "  ",
                "╗ ",
                "╝ ",
                "  ",
                "╗ ",
                "╝ ",
                "  "
            ],
        '17':
            [
                "╦",
                "║",
                "║",
                "║",
                "║",
                "║",
                "╩"
            ],
        '18':
            [
                "╦",
                "║",
                "╠",
                "╠",
                "║",
                "║",
                "╩"
            ],
        '19':
            [
                "╦",
                "║",
                "╠",
                "║",
                "╠",
                "║",
                "╩"
            ],
        '20':
            [
                "╦",
                "║",
                "║",
                "╠",
                "║",
                "║",
                "╝"
            ],
        '21':
            [
                "╦",
                "║",
                "║",
                "╠",
                "╠",
                "║",
                "╩"
            ],
        '22':
            [
                "╦",
                "╠",
                "║",
                "║",
                "║",
                "║",
                "╝"
            ],
        '23':
            [
                "╦",
                "║",
                "║",
                "╠",
                "║",
                "║",
                "╩"
            ],
        '24':
            [
                "╗",
                "║",
                "╠",
                "║",
                "╠",
                "║",
                "╝"
            ],
        '25':
            [
                "╗",
                "╠",
                "╠",
                "║",
                "╠",
                "╠",
                "╝"
            ],
        '26':
            [
                "╦",
                "║",
                "║",
                "║",
                "╣",
                "╣",
                "╩"
            ],
        '27':
            [
                "╦",
                "║",
                "╠",
                "╠",
                "╣",
                "╣",
                "╩"
            ],
        '28':
            [
                "╦",
                "║",
                "╠",
                "║",
                "╬",
                "╣",
                "╩"
            ],
        '29':
            [
                "╦",
                "║",
                "║",
                "╠",
                "╝",
                "╗",
                "╝"
            ],
        '30':
            [
                "╦",
                "║",
                "║",
                "╠",
                "╬",
                "╣",
                "╩"
            ],
        '31':
            [
                "╦",
                "╠",
                "║",
                "║",
                "╝",
                "╗",
                "╝"
            ],
        '32':
            [
                "╦",
                "║",
                "║",
                "╠",
                "╣",
                "╣",
                "╩"
            ],
        '33':
            [
                "╗",
                "║",
                "╠",
                "║",
                "╩",
                "╗",
                "╝"
            ],
        '34':
            [
                "╗",
                "╠",
                "╠",
                "║",
                "╬",
                "╬",
                "╝"
            ],
        '35':
            [
                "╦",
                "╣",
                "╣",
                "║",
                "║",
                "║",
                "╩"
            ],
        '36':
            [
                "╦",
                "╣",
                "╬",
                "╠",
                "║",
                "║",
                "╩"
            ],
        '37':
            [
                "╦",
                "╣",
                "╬",
                "║",
                "╠",
                "║",
                "╩"
            ],
        '38':
            [
                "╦",
                "╣",
                "╣",
                "╠",
                "║",
                "║",
                "╝"
            ],
        '39':
            [
                "╦",
                "╣",
                "╣",
                "╠",
                "╠",
                "║",
                "╩"
            ],
        '40':
            [
                "╦",
                "╩",
                "╗",
                "║",
                "║",
                "║",
                "╝"
            ],
        '41':
            [
                "╦",
                "╣",
                "╣",
                "╠",
                "║",
                "║",
                "╩"
            ],
        '42':
            [
                "╗",
                "╝",
                "╦",
                "║",
                "╠",
                "║",
                "╝"
            ],
        '43':
            [
                "╗",
                "╬",
                "╬",
                "║",
                "╠",
                "╠",
                "╝"
            ],
        '44':
            [
                "╦",
                "║",
                "╣",
                "╣",
                "║",
                "║",
                "╩"
            ],
        '45':
            [
                "╦",
                "║",
                "╩",
                "╦",
                "║",
                "║",
                "╩"
            ],
        '46':
            [
                "╦",
                "║",
                "╩",
                "╗",
                "╠",
                "║",
                "╩"
            ],
        '47':
            [
                "╦",
                "║",
                "╣",
                "╬",
                "║",
                "║",
                "╝"
            ],
        '48':
            [
                "╦",
                "║",
                "╣",
                "╬",
                "╠",
                "║",
                "╩"
            ],
        '49':
            [
                "╦",
                "╠",
                "╝",
                "╗",
                "║",
                "║",
                "╝"
            ],
        '50':
            [
                "╦",
                "║",
                "╣",
                "╬",
                "║",
                "║",
                "╩"
            ],
        '51':
            [
                "╗",
                "║",
                "╬",
                "╣",
                "╠",
                "║",
                "╝"
            ],
        '52':
            [
                "╗",
                "╠",
                "╩",
                "╗",
                "╠",
                "╠",
                "╝"
            ],
        '53':
            [
                "╦",
                "║",
                "║",
                "╣",
                "║",
                "║",
                "╩"
            ],
        '54':
            [
                "╦",
                "║",
                "╠",
                "╬",
                "║",
                "║",
                "╩"
            ],
        '55':
            [
                "╦",
                "║",
                "╠",
                "╣",
                "╠",
                "║",
                "╩"
            ],
        '56':
            [
                "╦",
                "║",
                "║",
                "╬",
                "║",
                "║",
                "╝"
            ],
        '57':
            [
                "╦",
                "║",
                "║",
                "╬",
                "╠",
                "║",
                "╩"
            ],
        '58':
            [
                "╦",
                "╠",
                "║",
                "╣",
                "║",
                "║",
                "╝"
            ],
        '59':
            [
                "╦",
                "║",
                "║",
                "╬",
                "║",
                "║",
                "╩"
            ],
        '60':
            [
                "╗",
                "║",
                "╠",
                "╣",
                "╠",
                "║",
                "╝"
            ],
        '61':
            [
                "╗",
                "╠",
                "╠",
                "╣",
                "╠",
                "╠",
                "╝"
            ],
        '62':
            [
                "╔",
                "║",
                "╣",
                "║",
                "╣",
                "║",
                "╚"
            ],
        '63':
            [
                "╔",
                "║",
                "╬",
                "╠",
                "╣",
                "║",
                "╚"
            ],
        '64':
            [
                "╔",
                "║",
                "╬",
                "║",
                "╬",
                "║",
                "╚"
            ],
        '65':
            [
                "╔",
                "║",
                "╣",
                "╠",
                "╝",
                " ",
                " "
            ],
        '66':
            [
                "╔",
                "║",
                "╣",
                "╠",
                "╬",
                "║",
                "╚"
            ],
        '67':
            [
                "╔",
                "╚",
                "╗",
                "║",
                "╝",
                " ",
                " "
            ],
        '68':
            [
                "╔",
                "║",
                "╣",
                "╠",
                "╣",
                "║",
                "╚"
            ],
        '69':
            [
                " ",
                " ",
                "╦",
                "║",
                "╩",
                " ",
                " "
            ],
        '70':
            [
                " ",
                "╔",
                "╬",
                "║",
                "╬",
                "╚",
                " "
            ],
        '71':
            [
                "╔",
                "╣",
                "╣",
                "║",
                "╣",
                "╣",
                "╚"
            ],
        '72':
            [
                "╔",
                "╣",
                "╩",
                "╔",
                "╣",
                "╣",
                "╚"
            ],
        '73':
            [
                "╔",
                "╣",
                "╩",
                " ",
                "╦",
                "╣",
                "╚"
            ],
        '74':
            [
                "╔",
                "╣",
                "╣",
                "╚",
                "╗",
                "╝",
                " "
            ],
        '75':
            [
                "╔",
                "╣",
                "╣",
                "╚",
                "╦",
                "╣",
                "╚"
            ],
        '76':
            [
                "╔",
                "╬",
                "╝",
                " ",
                "╗",
                "╝",
                " "
            ],
        '77':
            [
                "╔",
                "╣",
                "╣",
                "╠",
                "╣",
                "╣",
                "╚"
            ],
        '78':
            [
                " ",
                "╗",
                "╬",
                "║",
                "╬",
                "╝",
                " "
            ],
        '79':
            [
                " ",
                "╦",
                "╩",
                " ",
                "╦",
                "╩",
                " "
            ]
    }


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.move(100, 500)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowTitle('Transformation of symbols')
        self.setFixedSize(1300, 300)

        self.inputBox = QtWidgets.QLineEdit(self)
        self.inputBox.move(20, 20)
        self.inputBox.resize(970, 30)

        self.outputBox = QtWidgets.QTextEdit(self)
        self.outputBox.move(20, 60)
        self.outputBox.resize(1260, 230)
        self.outputBox.setFont(QtGui.QFont("Courier", 9))

        self.transformButton = QtWidgets.QPushButton('Transformation', self)
        self.transformButton.setGeometry(1000, 20, 100, 30)
        self.transformButton.clicked.connect(self.transformClicked)

        self.saveButton = QtWidgets.QPushButton('Save', self)
        self.saveButton.setGeometry(1180, 20, 100, 30)
        self.saveButton.clicked.connect(self.saveClicked)

        self.show()

    def transformClicked(self):
        inputText = self.inputBox.text().lower()
        self.outputText = ""
        self.outputBox.setText("")
        try:
            for j in range(7):
                n = '-1'  # n - предыдущий символ ('-1' -- буква, '0-9,-,+,=' -- знаки)
                k = 0  # k - номер символа
                for i in inputText:
                    k += 1
                    if n == '-1':
                        if i == '0' or i == '1' or i == '6':
                            self.outputText += connections['1'][j]
                        elif i == '2':
                            self.outputText += connections['3'][j]
                        elif i == '3':
                            self.outputText += connections['5'][j]
                        elif i == '4':
                            self.outputText += connections['6'][j]
                        elif i == '5' or i == '9':
                            self.outputText += connections['7'][j]
                        elif i == '7':
                            self.outputText += connections['10'][j]
                        elif i == '8':
                            self.outputText += connections['11'][j]
                        elif i == '-' or i == '+':
                            self.outputText += connections['13'][j]
                        elif i == '=':
                            self.outputText += connections['15'][j]
                    if n == '0' or n == '1' or n == '3' or n == '4' or n == '7' or n == '9':
                        if i == '0' or i == '1' or i == '6':
                            self.outputText += connections['17'][j]
                        elif i == '2':
                            self.outputText += connections['18'][j]
                        elif i == '3':
                            self.outputText += connections['19'][j]
                        elif i == '4':
                            self.outputText += connections['20'][j]
                        elif i == '5' or i == '9':
                            self.outputText += connections['21'][j]
                        elif i == '7':
                            self.outputText += connections['22'][j]
                        elif i == '8':
                            self.outputText += connections['23'][j]
                        elif i == '-' or i == '+':
                            self.outputText += connections['24'][j]
                        elif i == '=':
                            self.outputText += connections['25'][j]
                    if n == '2':
                        if i == '0' or i == '1' or i == '6':
                            self.outputText += connections['26'][j]
                        elif i == '2':
                            self.outputText += connections['27'][j]
                        elif i == '3':
                            self.outputText += connections['28'][j]
                        elif i == '4':
                            self.outputText += connections['29'][j]
                        elif i == '5' or i == '9':
                            self.outputText += connections['30'][j]
                        elif i == '7':
                            self.outputText += connections['31'][j]
                        elif i == '8':
                            self.outputText += connections['32'][j]
                        elif i == '-' or i == '+':
                            self.outputText += connections['33'][j]
                        elif i == '=':
                            self.outputText += connections['34'][j]
                    if n == '5':
                        if i == '0' or i == '1' or i == '6':
                            self.outputText += connections['35'][j]
                        elif i == '2':
                            self.outputText += connections['36'][j]
                        elif i == '3':
                            self.outputText += connections['37'][j]
                        elif i == '4':
                            self.outputText += connections['38'][j]
                        elif i == '5' or i == '9':
                            self.outputText += connections['39'][j]
                        elif i == '7':
                            self.outputText += connections['40'][j]
                        elif i == '8':
                            self.outputText += connections['41'][j]
                        elif i == '-' or i == '+':
                            self.outputText += connections['42'][j]
                        elif i == '=':
                            self.outputText += connections['43'][j]
                    if n == '6':
                        if i == '0' or i == '1' or i == '6':
                            self.outputText += connections['44'][j]
                        elif i == '2':
                            self.outputText += connections['45'][j]
                        elif i == '3':
                            self.outputText += connections['46'][j]
                        elif i == '4':
                            self.outputText += connections['47'][j]
                        elif i == '5' or i == '9':
                            self.outputText += connections['48'][j]
                        elif i == '7':
                            self.outputText += connections['49'][j]
                        elif i == '8':
                            self.outputText += connections['50'][j]
                        elif i == '-' or i == '+':
                            self.outputText += connections['51'][j]
                        elif i == '=':
                            self.outputText += connections['52'][j]
                    if n == '8':
                        if i == '0' or i == '1' or i == '6':
                            self.outputText += connections['53'][j]
                        elif i == '2':
                            self.outputText += connections['54'][j]
                        elif i == '3':
                            self.outputText += connections['55'][j]
                        elif i == '4':
                            self.outputText += connections['56'][j]
                        elif i == '5' or i == '9':
                            self.outputText += connections['57'][j]
                        elif i == '7':
                            self.outputText += connections['58'][j]
                        elif i == '8':
                            self.outputText += connections['59'][j]
                        elif i == '-' or i == '+':
                            self.outputText += connections['60'][j]
                        elif i == '=':
                            self.outputText += connections['61'][j]
                    if n == '-' or n == '+':
                        if i == '0' or i == '1' or i == '6':
                            self.outputText += connections['62'][j]
                        elif i == '2':
                            self.outputText += connections['63'][j]
                        elif i == '3':
                            self.outputText += connections['64'][j]
                        elif i == '4':
                            self.outputText += connections['65'][j]
                        elif i == '5' or i == '9':
                            self.outputText += connections['66'][j]
                        elif i == '7':
                            self.outputText += connections['67'][j]
                        elif i == '8':
                            self.outputText += connections['68'][j]
                        elif i == '-' or i == '+':
                            self.outputText += connections['69'][j]
                        elif i == '=':
                            self.outputText += connections['70'][j]
                    if n == '=':
                        if i == '0' or i == '1' or i == '6':
                            self.outputText += connections['71'][j]
                        elif i == '2':
                            self.outputText += connections['72'][j]
                        elif i == '3':
                            self.outputText += connections['73'][j]
                        elif i == '4':
                            self.outputText += connections['74'][j]
                        elif i == '5' or i == '9':
                            self.outputText += connections['75'][j]
                        elif i == '7':
                            self.outputText += connections['76'][j]
                        elif i == '8':
                            self.outputText += connections['77'][j]
                        elif i == '-' or i == '+':
                            self.outputText += connections['78'][j]
                        elif i == '=':
                            self.outputText += connections['79'][j]
                    if n == '0' or n == '1' or n == '3' or n == '4' or n == '7' or n == '9':
                        if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6':
                            if i != '7' and i != '8' and i != '9' and i != '-' and i != '+' and i != '=':
                                self.outputText += connections['2'][j]
                    if n == '2':
                        if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6':
                            if i != '7' and i != '8' and i != '9' and i != '-' and i != '+' and i != '=':
                                self.outputText += connections['4'][j]
                    if n == '5':
                        if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6':
                            if i != '7' and i != '8' and i != '9' and i != '-' and i != '+' and i != '=':
                                self.outputText += connections['8'][j]
                    if n == '6':
                        if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6':
                            if i != '7' and i != '8' and i != '9' and i != '-' and i != '+' and i != '=':
                                self.outputText += connections['9'][j]
                    if n == '8':
                        if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6':
                            if i != '7' and i != '8' and i != '9' and i != '-' and i != '+' and i != '=':
                                self.outputText += connections['12'][j]
                    if n == '-' or n == '+':
                        if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6':
                            if i != '7' and i != '8' and i != '9' and i != '-' and i != '+' and i != '=':
                                self.outputText += connections['14'][j]
                    if n == '=':
                        if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6':
                            if i != '7' and i != '8' and i != '9' and i != '-' and i != '+' and i != '=':
                                self.outputText += connections['16'][j]
                    n = i
                    self.outputText += symbols[i][j]
                    if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6':
                        if i != '7' and i != '8' and i != '9' and i != '-' and i != '+' and i != '=':
                            n = '-1'
                    if k == len(inputText):
                        if i == '0' or i == '1' or i == '3' or i == '4' or i == '7' or i == '9':
                            self.outputText += connections['2'][j]
                        elif i == '2':
                            self.outputText += connections['4'][j]
                        elif i == '5':
                            self.outputText += connections['8'][j]
                        elif i == '6':
                            self.outputText += connections['9'][j]
                        elif i == '8':
                            self.outputText += connections['12'][j]
                        elif i == '-' or i == '+':
                            self.outputText += connections['14'][j]
                        elif i == '=':
                            self.outputText += connections['16'][j]
                self.outputText += '\n'
        except LookupError:
            buttonReply = QtWidgets.QMessageBox.question(self, 'Message', "Wrong Symbol",
                                                         QtWidgets.QMessageBox.Ok)
        except TypeError:
            buttonReply = QtWidgets.QMessageBox.question(self, 'Message', "Type Error",
                                                         QtWidgets.QMessageBox.Ok)
        self.outputBox.setText(self.outputText)

    def saveClicked(self):
        f = codecs.open('TransformSymbols.txt', 'w', 'utf8')
        f.write(self.outputText)
        f.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
