import sys
from PyQt5.QtCore import QUrl, QSize
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QAction, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.setIcon(QtGui.QIcon("back.jpg"))
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.setIcon(QtGui.QIcon('fw.jpg'))
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.setIcon(QtGui.QIcon('reload.png'))
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)


    def navigate_to_url(self):
        text_in_url_bar = self.url_bar.text()
        redirect_url = None
        if not text_in_url_bar:
            redirect_url = "http://google.com"
        if text_in_url_bar.startswith("https://") or text_in_url_bar.startswith("http://"):
            redirect_url = text_in_url_bar
        else:
            if text_in_url_bar == 'about:blank':
                redirect_url = "http://www.google.com"
            else:
                redirect_url = f"http://www.google.com/search?q={text_in_url_bar}"
        self.browser.setUrl(QUrl(redirect_url))

    def update_url(self, q):
        current_url = q.toString()
        self.url_bar.setText(current_url)



app = QApplication(sys.argv)
#create new application object
QApplication.setApplicationName('Parseltongue Browser')
#set application name as parseltongue browser
window = MainWindow()
#create main window for the application which a subclass of Qt main window
app_icon = QtGui.QIcon()
app_icon.addFile('logo.png', QSize(256,256))
app.setWindowIcon(app_icon)
# Add logo for the brower ans set icon
app.exec_()
# Run the app
