import qrcode

img = qrcode.make(tracking_id)
img.save("qr.png")