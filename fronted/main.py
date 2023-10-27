from dash import html, dcc
import dash_bootstrap_components as dbc

#import fronted
from fronted.navegador import navegador
from fronted.derecha.derecha import derecha
from fronted.izquierda.izquierda import izquierda

layout= dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(navegador, md=12, style={'background-color':'black'}),
                dbc.Col(izquierda, md=5,style={'background-color':'black'}),
                dbc.Col(derecha, md=7, style={'background-color':'black'}),

            ]
        )
    ]
)
