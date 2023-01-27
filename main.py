
from fonksiyonlar import*



#########ARAYÜZÜ BAŞLAT
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui.setupUi(MainWindow)
MainWindow.show()






ui.btn_portBaglan.clicked.connect(seriBaglan)
ui.btn_portBaglantiKes.clicked.connect(seriKapat)

ui.btn_yesilLedAc.clicked.connect(yesilBTN)
ui.btn_kirmiziLedAc.clicked.connect(kirmiziBTN)
ui.btn_maviLedAc.clicked.connect(maviBTN)





#! TIMER
portKontrol = QtCore.QTimer()
portKontrol.start()
portKontrol.timeout.connect(ekranGuncelle)









# İŞLETİM SİSTEMİNE ÇIKIŞ
sys.exit(app.exec_())