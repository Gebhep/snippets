from time import sleep
import network

def wifi_hotspot(ssid, key):
    ap_if = network.WLAN(network.WLAN.IF_AP)
    ap_if.active(False)
    sleep(1)
    
    ap_if.active(True)
    ap_if.config(essid=ssid, password=key, authmode=network.AUTH_WPA_WPA2_PSK)
    
    for i in range(10):
        if ap_if.active():
            print(f"Hotspot active: {ssid}")
            print(f"IP Address: {ap_if.ifconfig()[0]}")
            print(f"Clients can connect using password: {key}")
            break
        else:
            print(f"Attempting[{i + 1}] to activate hotspot")
            sleep(2)
    else:
        print("Failed to activate hotspot")