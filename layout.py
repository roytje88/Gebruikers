from database import tableToDf
import dash_core_components as dcc
import dash_html_components as html
import os
import pandas as pd
from dash import dash_table

def appTab(label, dbFile):
    return dcc.Tab(
        label = label,
        children = [
            html.Div(
                dash_table.DataTable(
                    id = label+'Tab',
                    columns = [{'name': i, 'id': i} for i in tableToDf('applicaties',dbFile).keys() if i != 'id'],
                    data = pd.DataFrame.from_dict(tableToDf('applicaties',dbFile)).to_dict('records')
                )
            )
        ]
        )


def mainLayout(dbFile):
    layout = html.Div(
        children = [
            html.Div(
                children = [
                html.H1('Header')    
                ]
            ),
            html.Div(
                children = [
                    dcc.Tabs(
                        children = [
                            dcc.Tab(
                                label = 'Personen',
                                children = [
                                    html.Div(
                                        dash_table.DataTable(
                                            id='test',
                                            columns = [{'name': i, 'id': i} for i in tableToDf('personen',dbFile).keys() if i != 'id'],
                                            data = pd.DataFrame.from_dict(tableToDf('personen',dbFile)).to_dict('records')
                                        )
                                    )
                                ]
                            ),
                            appTab('Suites4SociaalDomein',dbFile),
                            appTab('WIZportaal',dbFile)
                            
                        ]
                    ),
                ]
            )
        ]
    )
    
    
    # layout =  dash_table.DataTable(
    #     id='test',
    #     columns = [{'name': i, 'id': i} for i in tableToDf('personen',dbFile).keys() if i != 'id'],
    #     data = pd.DataFrame.from_dict(tableToDf('personen',dbFile)).to_dict('records')
    # )

    return layout