from time import sleep
import network

def wifi_connect(ssid, key):
    sta_if = network.WLAN(network.WLAN.IF_STA)
    sta_if.active(False)
    for i in range(10):
        if not sta_if.isconnected() == True:
            sta_if.active(False)
            sta_if.active(True)
            sta_if.connect(ssid, key)
            print(f"Attempting[{i + 1}] to connect")
            sleep(10)            
        else:
            print(f"Connected to Wifi{sta_if.ipconfig('addr4')}")
            break