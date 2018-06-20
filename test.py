from pyzbar.pyzbar import decode
from PIL import Image

data = decode(Image.open("images/photos/file_3.jpg"))
# data = decode(Image.open("images/image4.jpg"))
print(data)
if data:
    # штрихкод в переменной data имеет тип bytes, поэтому конвертируем в str
    barcode = data[0][0].decode("utf-8")
    print(barcode)
    print(type(barcode))
else:
    barcode = 'Barcode not found'
    print('Barcode not found')