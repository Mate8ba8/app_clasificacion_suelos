import dash_bootstrap_components as dbc
from dash import  dash_table, dcc, html
from backend.granulometria import*
from backend.estilos import*
from backend.imagenes import*
from backend.Tablas import*
from backend.cartaplasticidad import*
import dash_core_components as dcc





izquierda = dbc.Container(
    [
        html.Hr(),


        # titulo

        dbc.Row(
            [
                dbc.Col(
                    html.H1("Tabla de Tamizado Agregados Finos y Gruesos", style=titulo_estilo),
                    width=20, # Ancho de la columna del título
                    align='center'  # Alinea el contenido verticalmente en el centro
                ),
            ], 
        ),


        # descripción 


        dbc.Row(
            [
                dbc.Col(
                    html.Div("El tamizado de agregados, tanto gruesos como finos, es un proceso esencial en la industria de la construcción y la ingeniería civil. El objetivo principal del tamizado es separar partículas de diferentes tamaños para obtener agregados con una granulometría adecuada para su uso en concreto, asfalto u otros productos de construcción. Aquí te presento una tabla donde puedes registrar la cantidad de material retenido en cada tamiz que registarste en el laboratorio: Por favor registra en la columna roja el los valores correspondientes",
                    style=estilo_borde_descripcion),
                    width=20,
                    style={'padding': '10px'}
                ),
           ],
        ),

        html.Hr(), 
        html.Hr(), 
        # Tabla de tamizado
        
        
        dbc.Row(
            [

                dbc.Col(
                    dash_table.DataTable(
                        id='tabla_granulometria',
                        columns=[
                            {'name': 'Malla', 'id': 'Malla','editable': False},
                            {'name': 'Abertura', 'id': 'Abertura','editable': False},
                            {'name': 'Retenido', 'id': 'Retenido', 'editable': True},
                            {'name': 'Retenido_acum', 'id': 'Retenido_acum', 'editable': False},
                            {'name': 'Pasa', 'id': 'Pasa', 'editable': False},
                            {'name': 'Por_Pasa', 'id': 'Por_Pasa', 'editable': False}
                         ],
                        
                        data=granulometria.to_dict('records'),
                        style_table={**tabla_estilo, **estilo_borde_tabla},
                        style_data_conditional=estilo_columna_retenido,  # Estilo para la columna 'Retenido'
                        style_cell={'width': ancho_fijo}  # Establecer ancho fijo para todas las celdas

                    ),
                ),
            ],
         ),

        


        html.Hr(), 
        html.Hr(), 

        # Limite de plasticidad



        html.Hr(),

        html.Div(
            [
                html.H2('Limite Plastico'),

                html.Hr(),

                html.Div([
                html.Label('Limite líquido:   '),
                dcc.Input(
                    id='Limite_liquido_input',
                    type='number',
                    value=55,
                ),
                html.Div(id='Limite_liquido_output')
                ]),


                html.Div([
                dcc.Slider(
                    id='Limite_liquido',
                    min=0,
                    max=100,
                    value=55,
                    step=1,
                    marks={i: str(i) for i in range(0, 101, 10)}
                ),
                html.Div(id='Limite_liquido_output')
                ]),


                html.Hr(),

                html.Div([
                html.Label('Índice de plasticidad  :'),
                dcc.Input(
                    id='Indice_plasticidad_input',
                    type='number',
                    value=20,
                ),
                html.Div(id='Indice_plasticidad_output')
                ]),


                html.Div([
                dcc.Slider(
                    id='Indice_plasticidad',
                    min=0,
                    max=60,
                    value=20,
                    step=1,
                    marks={i: str(i) for i in range(0, 61, 10)}
                ),
                html.Div(id='Indice_plasticidad_output')
                ]),

                
                html.Div(id='salidaCartaPlasticidad')

            ],

        ),


        html.Hr(), 
        html.Hr(), 

    ],
    style={'background-color':'white'},
    fluid=True
)
