import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsTextItem
from PyQt5.QtCore import QRectF
from pypinyin import pinyin, Style

class PinyinViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Pinyin nad Znakami Chińskimi')

        # Scena dla grafiki
        self.scene = QGraphicsScene()

        # Widok dla sceny
        self.view = QGraphicsView(self.scene, self)
        self.setCentralWidget(self.view)

        # Przykładowy tekst
        self.displayText("走了个仕途 没走通", "ce4 shi4")

    def displayText(self, chineseText, pinyinText):
        x, y = 0, 0
        for char, py in zip(chineseText, pinyinText.split()):
            # Tworzenie elementu tekstowego dla pinyin
            pinyinItem = QGraphicsTextItem(py)
            pinyinItem.setPos(x, y - 20)  # Dostosuj pozycję
            self.scene.addItem(pinyinItem)

            # Tworzenie elementu tekstowego dla chińskiego znaku
            chineseItem = QGraphicsTextItem(char)
            chineseItem.setPos(x, y)
            self.scene.addItem(chineseItem)

            # Aktualizacja pozycji dla następnego znaku
            x += chineseItem.boundingRect().width()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PinyinViewer()
    ex.show()
    sys.exit(app.exec_())
