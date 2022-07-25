import base64, time


while True:

    with open('input.txt', 'r', encoding="utf-8") as f:
        mes = f.read()
        if mes:
            mes = mes.encode('ascii')
            encoded = base64.b64encode(mes)
            encoded = encoded.decode("utf-8")
            with open('output.txt', 'w', encoding="utf-8") as f2:
                f2.write(encoded)

    time.sleep(3)

            