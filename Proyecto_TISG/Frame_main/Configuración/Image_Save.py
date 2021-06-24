from PIL import Image

image = Image.open('../../data/GUARDAR_ICON.png')
new_image = image.resize((50, 50))
new_image.save('../../data/GUARDAR_ICON.png')

image = Image.open('../../data/Home.png')
new_image = image.resize((70, 70))
new_image.save('../../data/Home.png')

image = Image.open('../../data/Home_click.png')
new_image = image.resize((70, 70))
new_image.save('../../data/Home_click.png')
