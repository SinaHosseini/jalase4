import qrcode

information = []
name = input("enter ur name: ")
information.append(name)
phone_number = input("enter ur phone number: ")
information.append(phone_number)

image = qrcode.make(information)
image.save("user_information_QR.png")
