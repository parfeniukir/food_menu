import qrcode

image = qrcode.make("https://github.com/parfeniukir/food_menu")
image.save("github_qr.png")
