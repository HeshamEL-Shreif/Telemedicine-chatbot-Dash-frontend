from dash import dcc, html, Dash
import dash_bootstrap_components as dbc



def interface():
    app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.title = "TeleMedicine Question Answering System"


    header = html.H1(["TeleMedicine Chatbot"], style={"textAlign": "center",
                                                            "color": "white",
                                                            "fontSize": 35,
                                                            "backgroundColor": "#AAC0D7",
                                                            "padding": "45px",
                                                            "text-shadow": "2px 2px 2px #000000",
                                                            "font-family": "serif"})


    card = dbc.Card([
        dbc.CardBody([
            html.Div(
                id="chat-history",
                style={
                    "height": "650px",
                    "overflowY": "auto",
                    "padding": "10px",
                    "backgroundColor": "#f4f4f4",
                    "borderRadius": "10px"
                }
            )
        ]),
        dbc.CardFooter([
            dbc.InputGroup([
                dbc.Input(id="query", placeholder="Type your message...", type="text",  n_submit=0,),
                dbc.Button("Send", id="submit", color="#AAC0D7", n_clicks=0),
            ], style={"width": "100%"})
        ])
    ], style={"margin": "10px", "height": "100%"})


    app.layout = html.Div(children=[
        dbc.Row([header]),
        dbc.Row([card])
        
    ])

    app.layout.children.extend([
        dcc.Store(id="chat-store", data=[]), dcc.Store(id="pending-files", data=[]),
    ])
    
    return app
