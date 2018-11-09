from network import WLAN, AP_IF, AUTH_WPA_WPA2_PSK
from webrepl import start

start()
ap_if = WLAN(AP_IF)
ap_if.active(True)
ap_if.config(essid='ESP32', authmode=AUTH_WPA_WPA2_PSK, password='micropython')