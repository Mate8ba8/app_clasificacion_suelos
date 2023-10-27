from dash import Dash, dcc, html, Input, Output, callback, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from backend.granulometria import*
from backend.estilos import*
from backend.imagenes import*
from backend.Tablas import*
from backend.cartaplasticidad import cartaPlasticidad 
import dash_core_components as dcc




#import fronted
from fronted.main import*

#import backend
from backend.cartaplasticidad import cartaPlasticidad


# creador de app

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

# Importar Diseño

app.layout = layout



@app.callback(
    Output('tabla_granulometria', 'data'),
    [Input('tabla_granulometria', 'data'),
     Input('tabla_granulometria', 'columns')]
)

def update_granulometria_table(rows, columns):
    granulometria = pd.DataFrame(rows)
    granulometria["Retenido"] = granulometria["Retenido"].astype("int") 
    granulometria["Retenido_acum"]= granulometria["Retenido"].cumsum() #se crea una columna para retenido acummulado y se aplica cumsum a la columna retenido para hallar su acumulado
    granulometria["Pasa"]= granulometria["Retenido"].sum()-granulometria["Retenido_acum"] #Se crea la columna Pasa y se realiza la resta del total de la muestra menos el retenido acumulado en cada fila
    granulometria["Por_Pasa"]= round(granulometria["Pasa"]*100/granulometria["Retenido"].sum(),2) #Se crea la columna % pasa y se realiza la operació entre la columna pasa por 100 dividido en el total de la muetra
      
    # Convertir las columnas numéricas a str para evitar el error
    granulometria["Retenido"] = granulometria["Retenido"].astype(str)
    granulometria["Retenido_acum"] = granulometria["Retenido_acum"].astype(str)
    granulometria["Pasa"] = granulometria["Pasa"].astype(str)
    granulometria["Por_Pasa"] = granulometria["Por_Pasa"].astype(str)
         
    return granulometria.to_dict('records')

@app.callback(
    Output('granulometria-plot', 'figure'),
    [Input('tabla_granulometria', 'data')]
)

def update_granulometria_plot(rows):
    granulometria = pd.DataFrame(rows)
    
    trace = go.Scatter(
        x=granulometria['Abertura'][0:11],
        y=granulometria['Por_Pasa'][0:11],
        mode='lines',
        line=dict(color='black', width=2, shape='spline'),  # Usar 'spline' para suavizar la curva
        name='Curva Granulométrica'
    )
    
    layout = go.Layout(
        title='CURVA GRANULOMETRICA DE LOS AGREGADOS',
        xaxis=dict(
            title='Tamiz (mm)',
            type='log',
            autorange=True,
            range=[granulometria['Abertura'][0], granulometria['Abertura'][1]]
        ),

        yaxis=dict(
            title='Porcentaje Pasa Acumulado %',
            range=[0, 105],
            tickvals=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],

        ),

        margin=dict(l=60, r=60, t=60, b=60),
        paper_bgcolor='lightgray',
        plot_bgcolor='white'
    )

    return {'data': [trace], 'layout': layout}



#calculamos la carta de plasticidad
@app.callback(
    Output('salidaCartaPlasticidad', 'children'),
    Input('Limite_liquido', 'value'),
    Input('Indice_plasticidad', 'value')
)

def cartaPlasticidadDash(Limite_liquido, Indice_plasticidad):
    #retrasar la página un segundo
    # time.sleep(1)
    encoded_image, messages = cartaPlasticidad(Limite_liquido, Indice_plasticidad)

    image_element = html.Img(src="data:image/png;base64,{}".format(encoded_image))
    messages_element = html.Label(messages)

    return html.Div([image_element, messages_element])



@app.callback(
    Output('Limite_liquido_output', 'children'),
    Output('Indice_plasticidad_output', 'children'),
    Input('Limite_liquido', 'value'),
    Input('Indice_plasticidad', 'value')
)
def update_output(limite_liquido_value, indice_plasticidad_value):
    return f'Limite líquido seleccionado: {limite_liquido_value}', f'Índice de plasticidad seleccionado: {indice_plasticidad_value}'

@app.callback(
    Output('Limite_liquido', 'value'),
    Input('Limite_liquido_input', 'value')
)
def update_limite_liquido_slider(value):
    return value

@app.callback(
    Output('Indice_plasticidad', 'value'),
    Input('Indice_plasticidad_input', 'value')
)
def update_indice_plasticidad_slider(value):
    return value



# Iniciar la aplicación Dash
if __name__ == '__main__':
    app.run_server(debug=True)

