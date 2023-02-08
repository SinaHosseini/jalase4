import qrcode

img = qrcode.make(
    "sshosseinivaez@gmail.com | https://instagram.com/s.sina_hosseini.v")
img.save("MyFirstQR.png")
