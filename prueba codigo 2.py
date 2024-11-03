try:
    import machine
    import time

    # Configuración del LED
    led = machine.Pin(2, machine.Pin.OUT)

    while True:
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)

except Exception as e:
    print("Error al ejecutar el nuevo código:", e)
    machine.reset()  # Reinicia si hay un error
