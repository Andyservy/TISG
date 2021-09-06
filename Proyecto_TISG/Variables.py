from Proyecto_TISG.data.SERVIRDOR.DATABASE import connection

cursor = connection().cursor()
Icon_Home = ['C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home.png',
             'C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Home_click.png']
Color = "#212F3C"

Preview_Billing = ['C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Factura ordinaria.png',
                   'C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Factura resumen.png',
                   'C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Pagaré.png',
                   'C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Less focus.png']

Productos_Pres = ['C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Tubos pvc.png',
                  'C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Pacasmayo.png',
                  'C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Fierros.png']

Buscador = ['C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Buscar.png',
            'C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Buscar_Click.png']

Agregar = ['C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Agregar.png', 'C:/Users/USUARIO/Desktop/TISG'
                                                                           '/Proyecto_TISG/data/Agregar_Out.png']

Quitar = ['C:/Users/USUARIO/Desktop/TISG/Proyecto_TISG/data/Quitar.png', 'C:/Users/USUARIO/Desktop/TISG'
                                                                          '/Proyecto_TISG/data/Quitar_Out.png']

list_DatosEmpresa = ['RazonSocial', 'DireccionMatriz', 'RUC', 'Resumen', 'IGV', 'TipoEmpresa', 'Telefono']

TiposEmpresa = ['SA', 'SAC', 'SRL', 'EIRL', 'SAA', '']

ResponsableCompraVenta = ['Empresa', 'Individuo']
TipoDePago = ['Cheque', 'Transferencia', 'Contado']
Comprobante = ['Boleta de venta', 'Factura']
Serie = ['F-', 'B-', 'R-']

cursor.execute("SELECT * FROM DataEmpresa")
Consult_DataEmpresa = cursor.fetchone()

cursor.execute("SELECT COUNT(*) FROM factura_ordinaria")
Conteo_FacturaOrdinaria = cursor.fetchone()

cursor.execute("SELECT COUNT(*) FROM factura")
Conteo_Factura = cursor.fetchone()

cursor.execute("SELECT COUNT(*) FROM productos_compra")
Filas_Productos = cursor.fetchone()
