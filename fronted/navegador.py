from dash import html
import dash_bootstrap_components as dbc

#importar componentes del navegador
from backend.estilos import*
from backend.imagenes import*


navegador = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(src=url_de_la_imagen, style={'width': ancho_imagen}),
                    width=4,  # Ancho de la columna de la imagen (más grande)
                ),
                dbc.Col(
                    html.H1("CLASIFICACIÓN DE SUELOS", style={'color': 'black'}),
                    width=6,  # Ancho de la columna del título
                    style={'display': 'flex', 'align-items': 'center'},  # Centra verticalmente el título
                ),

            
            ]
        )
    ],
    style={'background-color': 'lightgray'}
)