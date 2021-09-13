# #cuando poner fetchone soloe scoje el primero, pero aune sta el lista, eso generara error si no corrijes en ComercialBilling
from Proyecto_TISG import connection
import os

cursor = connection().cursor()

Icon_Home = [os.path.abspath('Home.png'),
             os.path.abspath('Home_click.png')]
Color = "#212F3C"

Preview_Billing = [os.path.abspath('Factura ordinaria.png'),
                   os.path.abspath('Factura resumen.png'),
                   os.path.abspath('Pagaré.png'),
                   os.path.abspath('Less focus.png')]

Productos_Pres = [os.path.abspath('Tubos pvc.png'),
                  os.path.abspath('Pacasmayo.png'),
                  os.path.abspath('Fierros.png')]

Buscador = [os.path.abspath('Buscar.png'),
            os.path.abspath('Buscar_Click.png')]

Agregar = [os.path.abspath('Agregar.png'), os.path.abspath('Agregar_Out.png')]

Quitar = [os.path.abspath('Quitar.png'), os.path.abspath('Quitar_Out.png')]

list_DatosEmpresa = ['RazonSocial', 'DireccionMatriz', 'RUC', 'Resumen', 'IGV', 'TipoEmpresa', 'Telefono']

TiposEmpresa = ['SA', 'SAC', 'SRL', 'EIRL', 'SAA', '']

ResponsableCompraVenta = ['Empresa', 'Individuo']
TipoDePago = ['Cheque', 'Transferencia', 'Contado']
Comprobante = ['Boleta de venta', 'Factura']
Serie = ['F-', 'B-', 'R-']

cursor.execute("SELECT * FROM dataempresa")
Consult_DataEmpresa = cursor.fetchall()
Consult_DataEmpresa = Consult_DataEmpresa[0]

cursor.execute("SELECT COUNT(*) FROM factura_ordinaria")
Conteo_FacturaOrdinaria = cursor.fetchone()
Conteo_FacturaOrdinaria = Conteo_FacturaOrdinaria[0]

cursor.execute("SELECT COUNT(*) FROM factura")
Conteo_Factura = cursor.fetchone()
Conteo_Factura = Conteo_Factura[0]

cursor.execute("SELECT COUNT(*) FROM factura WHERE Concepto='Venta'")
Conteo_FacturaVenta = cursor.fetchone()
Conteo_FacturaVenta = Conteo_FacturaVenta[0]

cursor.execute("SELECT COUNT(*) FROM factura WHERE Concepto='Compra'")
Conteo_FacturaCompra = cursor.fetchone()
Conteo_FacturaCompra = Conteo_FacturaCompra[0]

cursor.execute("SELECT IGV FROM dataempresa")
IGV = cursor.fetchone()
IGV = IGV[0]

cursor.execute("SELECT * FROM factura")
Conteo_Recapitulativa = cursor.fetchall()
Conteo_Recapitulativa = len([x[1] for x in Conteo_Recapitulativa if x[1][0] == 'R'])

