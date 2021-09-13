from PIL import Image
from PIL import ImageFile
import os
ImageFile.LOAD_TRUNCATED_IMAGES = True
# Esta parte reestructura las imagenes usadas

image = Image.open(os.path.abspath('../bin/GUARDAR_ICON.png'))
_1 = image.resize((50, 50))
_1.save(os.path.abspath('../bin/GUARDAR_ICON.png'))

image = Image.open(os.path.abspath('../bin/Home.png'))
_1 = image.resize((70, 70))
_1.save(os.path.abspath('../bin/Home.png'))

image = Image.open(os.path.abspath('../bin/Home_click.png'))
_1 = image.resize((70, 70))
_1.save(os.path.abspath('../bin/Home_click.png'))

image = Image.open(os.path.abspath('../bin/Factura ordinaria.png'))
_1 = image.resize((600, 430))
_1.save(os.path.abspath('../bin/Factura ordinaria.png'))

image = Image.open(os.path.abspath('../bin/Factura resumen.png'))
_1 = image.resize((600, 430))
_1.save(os.path.abspath('../bin/Factura resumen.png'))

image = Image.open(os.path.abspath('../bin/Pagaré.png'))
_1 = image.resize((600, 430))
_1.save(os.path.abspath('../bin/Pagaré.png'))

image = Image.open(os.path.abspath('../bin/Less focus.png'))
_1 = image.resize((600, 430))
_1.save(os.path.abspath('../bin/Less focus.png'))

Productos_Pres = [os.path.abspath('../bin/Tubos pvc.png'),
                  os.path.abspath('../bin/Pacasmayo.png'),
                  os.path.abspath('../bin/Fierros.png')]

for _ in Productos_Pres:
    x = Image.open(_)
    _1 = x.resize((50, 50))
    _1.save(_)

image = Image.open(os.path.abspath('../bin/Buscar.png'))
_1 = image.resize((120, 120))
_1.save(os.path.abspath('../bin/Buscar.png'))

image = Image.open(os.path.abspath('../bin/Buscar_Click.png'))
_1 = image.resize((120, 120))
_1.save(os.path.abspath('../bin/Buscar_Click.png'))

image = Image.open(os.path.abspath('../bin/Agregar.png'))
_1 = image.resize((50, 50))
_1.save(os.path.abspath('../bin/Agregar.png'))

image = Image.open(os.path.abspath('../bin/Quitar.png'))
_1 = image.resize((50, 50))
_1.save(os.path.abspath('../bin/Quitar.png'))

image = Image.open(os.path.abspath('../bin/Agregar_Out.png'))
_1 = image.resize((50, 50))
_1.save(os.path.abspath('../bin/Agregar_Out.png'))

image = Image.open(os.path.abspath('../bin/Quitar_Out.png'))
_1 = image.resize((50, 50))
_1.save(os.path.abspath('../bin/Quitar_Out.png'))