import dash,os
import dash_bootstrap_components as dbc
from database import *
from layout import mainLayout

external_stylesheets = [dbc.themes.MORPH]
external_scripts = ['https://cdn.plot.ly/plotly-locale-nl-latest.js']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,external_scripts=external_scripts, url_base_pathname='/dash/')

database = 'gebruikers.db'

if not os.path.isfile(database):
    # import deploy functions
    from deploy import *
    createDB(database)


app.layout = mainLayout(database) 

if __name__ == "__main__":
    app.run_server()
    
    