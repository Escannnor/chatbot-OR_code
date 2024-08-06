import pyqrcode
import os

name = 'Escanor'
k = pyqrcode.create(name)
k.png('test.png', scale= 10)
os.system('test.png')

