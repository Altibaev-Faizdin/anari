import qrcode

url = "https://anari.onrender.com"

img = qrcode.make(url)
img.save("site_qr.png")

print("QR код создан!")