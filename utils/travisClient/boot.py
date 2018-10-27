"""
import network
import webrepl
print("\n----> INICIANDO webrepl\n")
webrepl.start()
print("\n----> INICIANDO AP\n")
ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
print("\n\t~~ BIENVENIDO A LA BALIZA ~~\n")
"""
# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
import network
import webrepl
import time


webrepl.start()
ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
ap_if.config(essid='ESP32', authmode=network.AUTH_WPA_WPA2_PSK, password='micropython')
"""
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
for i in range(10):
    sta_if.connect('CyberGames', '')
    if(sta_if.isconnected()):
        break
    time.sleep(1)

print("Conectado a CyberGames ", sta_if.isconnected())

for i in range(10):
    sta_if.connect('AP', 'Passw0rd')
    if(sta_if.isconnected()):
        break
    time.sleep(1)

print("Conectado a AP ", sta_if.isconnected())
"""
