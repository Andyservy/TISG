from PIL import Image

image = Image.open("C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/GUARDAR_ICON.png")
new_image = image.resize((50, 50))
new_image.save("C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/GUARDAR_ICON.png")

image = Image.open('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home.png')
new_image = image.resize((70, 70))
new_image.save('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home.png')

image = Image.open('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home_click.png')
new_image = image.resize((70, 70))
new_image.save('C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home_click.png')
