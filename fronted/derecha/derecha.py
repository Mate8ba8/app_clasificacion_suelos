
from dash import dcc, html
from backend.granulometria import*
from backend.estilos import*
from backend.imagenes import*
from backend.Tablas import*
from backend.cartaplasticidad import*
import dash_bootstrap_components as dbc











derecha = dbc.Container(
    [
            dbc.Row(
            [
                 dbc.Col(
                    dcc.Graph(id='granulometria-plot'),
                    style={'margin-top': '20px', 'max-width': '100%'},
                ),
            ], 

            ),

            html.Hr(), 

            dbc.Row(
            [
                 html.Div(id='salidaCartaPlasticidad', style={'width': '55%', 'height': '55%'}),
                 
            ], 


        ),

        html.Hr(), 
        
    ]
)
