from PIL import Image

# Esta parte reestructura las imagenes usadas

image = Image.open("C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/GUARDAR_ICON.png")
_1 = image.resize((50, 50))
_1.save("C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/GUARDAR_ICON.png")

image = Image.open('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home.png')
_1 = image.resize((70, 70))
_1.save('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home.png')

image = Image.open('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home_click.png')
_1 = image.resize((70, 70))
_1.save('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home_click.png')

image = Image.open('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Factura ordinaria.png')
_1 = image.resize((690, 430))
_1.save('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Factura ordinaria.png')

image = Image.open('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Factura resumen.png')
_1 = image.resize((690, 430))
_1.save('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Factura resumen.png')

image = Image.open('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Pagaré.png')
_1 = image.resize((690, 430))
_1.save('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Pagaré.png')

image = Image.open('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Less focus.png')
_1 = image.resize((690, 430))
_1.save('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Less focus.png')

Productos_Pres = ['C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Tubos pvc.png',
                  'C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Pacasmayo.png',
                  'C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Fierros.png']

for _ in Productos_Pres:
    x = Image.open(_)
    _1 = x.resize((50, 50))
    _1.save(_)