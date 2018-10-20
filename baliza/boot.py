import network
import webrepl
print("\n----> INICIANDO webrepl\n")
webrepl.start()
print("\n----> INICIANDO AP\n")
ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
print("\n\t~~ BIENVENIDO A LA BALIZA ~~\n")
