import dash_table

# tabla para limite liquido e Indice de plasticidad 

propiedades = [
    # Definición de las columnas de la tabla de propiedades
    {'name': 'Propiedad', 'id': 'Propiedad', 'editable': False},
    {'name': 'Valor', 'id': 'Valor', 'editable': True},
]

# Crear una lista de diccionarios para las propiedades
datos_propiedades = [
    {'Propiedad': 'Limite liquido (LL)', 'Valor': '10'},
    {'Propiedad': 'Indice de Plasticidad (IP)', 'Valor': '5'},
    # Agrega más propiedades y valores según tus necesidades
]
