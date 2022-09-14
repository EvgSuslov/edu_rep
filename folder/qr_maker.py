from art import text2art as art
import qrcode
import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

print(art('qr resolver'))
img = qrcode.make(input('here is your url: '))
type(img)
path = (os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
img.save(os.path.join(path, input('here is your image name:') + '.png'))

input('press any key to continue')
