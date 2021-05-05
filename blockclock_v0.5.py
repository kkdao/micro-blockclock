#mit funktion für schlanken code
#wlan automatisch auswählen

from m5stack import *
from m5ui import *
from uiflow import *
import urequests
import wifiCfg
import time 

console = M5TextBox(2, 228, "", lcd.FONT_DefaultSmall, 0xFFFFFF, rotate=0)
console2 = M5TextBox(2, 228, "", lcd.FONT_DefaultSmall, 0xFFFFFF, rotate=0)
console3 = M5TextBox(2, 200, "", lcd.FONT_DefaultSmall, 0xFFFFFF, rotate=0)
hintergrund = M5Img(0, 0, "res/block_v0.5.png", True)
version = M5TextBox(225, 228, "blockclock v0.5", lcd.FONT_DefaultSmall, 0xFFFFFF, rotate=0)

wlan_AP = 'insert WiFi SSID here'
wlan_PW = 'insert WiFi pwd here'

wifiCfg.doConnect(wlan_AP, wlan_PW)
if wifiCfg.wlan_sta.isconnected(): 
    console2.setText(wlan_AP)
    time.sleep(1)
    
    
else:  
    console.setText('wifi not connected')  
    time.sleep(0.1)  


zahl = ["res/0neu.png",
        "res/1neu.png",
        "res/2neu.png",
        "res/3neu.png",
        "res/4neu.png",
        "res/5neu.png",
        "res/6neu.png",
        "res/7neu.png",
        "res/8neu.png",
        "res/9neu.png",
]

zahl_leer = "res/none.png"

display_pos = {
           "x1": 24,
           "x2": 64,
           "x3": 104,
           "x4": 144,
           "x5": 184,
           "x6": 224,
           "x7": 264,
           "y": 75,                        
}

raw_data = None
liste =[]
blockcount_alt = "xxxxxxx"

while True:
  version.setText("blockclock v0.5")
  lcd.pixel(2, 236, 0xB40000) #send request
  try:
      req = urequests.request(method='GET', url='https://api.blockcypher.com/v1/btc/main', headers={'Content-Type':'text/html'})
      lcd.pixel(2, 236, 0xFF8001) #request succeeded 
      time.sleep(0.1)
      console.setText('')
      raw_data = req.text
  except:
      console.setText('failed')

  liste = raw_data.split()
  blockcount = liste[4]
  blockcount = blockcount.replace(",", "")

  #console3.setText(blockcount)
  #console2.setText(blockcount_alt)
  
  def get_blockcount(blockcount_index, display_PosX, display_PosY):
    global blockcount_alt
    global zaehler_alt 
    global zaehler 
    zaehler = 0
    
    while zaehler <= 10:
      if blockcount[blockcount_index] is not blockcount_alt[blockcount_index]:
        if int(blockcount[blockcount_index]) == zaehler:
            bild = M5Img(display_PosX, display_PosY, zahl_leer, True)
            time.sleep(0.1)
            bild = M5Img(display_PosX, display_PosY, zahl[zaehler], True)
            zaehler_alt = zaehler
            break
            
        else:
            zaehler += 1
      else:
        break
  
  
  get_blockcount(-1, display_pos["x7"], display_pos["y"])
  get_blockcount(-2, display_pos["x6"], display_pos["y"])
  get_blockcount(-3, display_pos["x5"], display_pos["y"])
  get_blockcount(-4, display_pos["x4"], display_pos["y"])
  get_blockcount(-5, display_pos["x3"], display_pos["y"])
  get_blockcount(-6, display_pos["x2"], display_pos["y"])
  
  if len(blockcount) > 6:
      get_blockcount(0, display_pos["x1"], display_pos["y"])

  blockcount_alt = blockcount
  #console2.setText(blockcount_alt)
  #console3.setText(blockcount)

  i = 0  
  while i < 20:
      lcd.pixel(105, 236, 0x00F000)
      time.sleep(0.5)
      lcd.pixel(105, 236, 0x000500)
      time.sleep(0.5)
      lcd.pixel(105, 236, 0x00F000)
      time.sleep(0.5)
      lcd.pixel(105, 236, 0x000500)
      time.sleep(0.5)
      lcd.pixel(105, 236, 0x00F000)
      time.sleep(0.5)
      lcd.pixel(105, 236, 0x000500)
      time.sleep(0.5)
      i = i + 1
