import network
import webrepl
import time

webrepl.start()
ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
ap_if.config(essid='ESP32', authmode=network.AUTH_WPA_WPA2_PSK, password='micropython')