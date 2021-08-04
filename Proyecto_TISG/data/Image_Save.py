from PIL import Image

# Esta parte reestructura las imagenes usadas

image = Image.open("C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/GUARDAR_ICON.png")
new_image = image.resize((50, 50))
new_image.save("C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/GUARDAR_ICON.png")

image = Image.open('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home.png')
new_image = image.resize((70, 70))
new_image.save('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home.png')

image = Image.open('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home_click.png')
new_image = image.resize((70, 70))
new_image.save('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home_click.png')

image = Image.open('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Factura ordinaria.png')
new_image = image.resize((690, 430))
new_image.save('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Factura ordinaria.png')

image = Image.open('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Factura resumen.png')
new_image = image.resize((690, 430))
new_image.save('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Factura resumen.png')

image = Image.open('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Pagaré.png')
new_image = image.resize((690, 430))
new_image.save('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Pagaré.png')

image = Image.open('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Less focus.png')
new_image = image.resize((690, 430))
new_image.save('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Less focus.png')


