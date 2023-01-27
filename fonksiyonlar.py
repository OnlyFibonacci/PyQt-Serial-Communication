from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem # Tasarladığımız arayüzün kullanılabilmesi için
import serial #serial kütüphanesi ile seri port haberleşmesi
import sys
import serial.tools.list_ports
from arayuz import*



ui = Ui_MainWindow()

#Seri portların listesini döndürür.
def seriPortListesi():
    ports = list(serial.tools.list_ports.comports())
    return ports




#!PARÇALAMA İŞLERİ
# Verilerin geliş tarzına göre 
def veriParcala(data):
    return str(data).split("'")[1][0:-4]

def verileriBol(data):
    return str(data).split("+")



def yesilYak():
    baglanti.write(b'yesil_led_on')
def yesilSondur():
    baglanti.write(b'yesil_led_off')







def maviYak():
    baglanti.write(b'mavi_led_on')
    
    

    
    
def maviSondur():
    baglanti.write(b'mavi_led_off')


def kirmiziYak():
    baglanti.write(b'kirmizi_led_on')
    

def kirmiziSondur():
    baglanti.write(b'kirmizi_led_off')


def hepsiniYak():
    yesilYak()
    maviYak()
    kirmiziYak()
    
    
def hepsiniSondur():
    maviSondur()
    yesilSondur()
    kirmiziSondur()



def yesilBTN():
    txt = ui.btn_yesilLedAc.text()
    if txt=="AÇ":
        yesilYak()
    else:
        yesilSondur()


def maviBTN():
    txt = ui.btn_maviLedAc.text()
    if txt=="AÇ":
        maviYak()
    else:
        maviSondur()

def kirmiziBTN():
    txt = ui.btn_kirmiziLedAc.text()
    if txt=="AÇ":
        kirmiziYak()
    else:
        kirmiziSondur()

#! ARAYÜZ FONKSİYONLARI
def taraButon(): #sürekli güncellendiği için aslında tarama butonuna gerek yok.
    portlariEkle()
    if ui.combo_portList.count() > 0:
        ui.btn_portBaglan.setEnabled(True)
        


def portListesiniTemizle():
    ui.combo_portList.clear()

def portlariEkle():
    portListesi = seriPortListesi()
    for port in portListesi:
        if ui.combo_portList.findText(port.name) == -1: #port eğer varsa eklemez.
            ui.combo_portList.addItem(port.name)



def seriBaglan():
    port = ui.combo_portList.currentText()
    baud = ui.combo_baudRateList.currentText()
    global baglanti
    baglanti = serial.Serial(port,baud)
    
    
def seriKapat():
    global baglanti
    try:
        baglanti.close()
    except:
        pass  


def ekranGuncelle():
    

    if len(seriPortListesi()) > 0:
        portlariEkle()
        ui.btn_portBaglan.setEnabled(True)
    else:
        ui.btn_portBaglan.setEnabled(False)
        seriKapat()
        portListesiniTemizle()
    
     
    try:
        global baglanti
        if baglanti.is_open : 
            ui.btn_portBaglan.setEnabled(False)
            ui.combo_portList.setEnabled(False)
            ui.combo_baudRateList.setEnabled(False)
            ui.btn_portBaglantiKes.setEnabled(True)
            ui.statusbar.showMessage("Bağlantı Var.")
            ui.groupBox_sicaklikVeNem.setEnabled(True)
            ui.groupBox_led.setEnabled(True)
            gelenVeri = verileriBol(veriParcala(baglanti.readline()))
            if ui.btn_kirmiziLedAc.text() == "AÇ":
                ui.btn_kirmiziLedAc.setStyleSheet("background-color: #2ecc71;\ncolor: rgb(255, 255, 255);") 
            else:
                ui.btn_kirmiziLedAc.setStyleSheet("background-color: #e74c3c;\ncolor: rgb(255, 255, 255);")
                
            if ui.btn_maviLedAc.text() == "AÇ":
                ui.btn_maviLedAc.setStyleSheet("background-color: #2ecc71;\ncolor: rgb(255, 255, 255);") 
            else:
                ui.btn_maviLedAc.setStyleSheet("background-color: #e74c3c;\ncolor: rgb(255, 255, 255);")
                
            if ui.btn_yesilLedAc.text() == "AÇ":
                ui.btn_yesilLedAc.setStyleSheet("background-color: #2ecc71;\ncolor: rgb(255, 255, 255);") 
            else:
                ui.btn_yesilLedAc.setStyleSheet("background-color: #e74c3c;\ncolor: rgb(255, 255, 255);")
            if len(gelenVeri) == 6:
                yesilLedDurum = gelenVeri[0]
                kirmiziLedDurum = gelenVeri[1]
                maviLedDurum = gelenVeri[2]
                potansVeri = gelenVeri[3]
                nem = int(float(gelenVeri[4]))
                sicaklik = int(float(gelenVeri[5]))
                if yesilLedDurum == '1':
                    ui.btn_yesilLedAc.setText("KAPA")
                else :
                    ui.btn_yesilLedAc.setText("AÇ")
                if kirmiziLedDurum == '1':
                    ui.btn_kirmiziLedAc.setText("KAPA")
                else:
                    ui.btn_kirmiziLedAc.setText("AÇ")
                if maviLedDurum == '1':
                    ui.btn_maviLedAc.setText("KAPA")
                else : 
                    ui.btn_maviLedAc.setText("AÇ")
                ui.lcdNumber.setProperty("value",potansVeri)
                ui.progressBar_sicaklik.setValue(sicaklik)
                ui.progressBar_nem.setValue(nem)
        else:
            ui.btn_portBaglan.setEnabled(True)
            ui.btn_portBaglantiKes.setEnabled(False)
            ui.combo_portList.setEnabled(True)
            ui.combo_baudRateList.setEnabled(True)
            ui.statusbar.showMessage("Bağlantı Yok.")
            ui.groupBox_sicaklikVeNem.setEnabled(False)
            ui.groupBox_led.setEnabled(False)
            ui.groupBox_2.setEnabled(False)
            ui.btn_kirmiziLedAc.setStyleSheet("")
            ui.btn_maviLedAc.setStyleSheet("")
            ui.btn_yesilLedAc.setStyleSheet("")
            
    except:
        pass
        
        

