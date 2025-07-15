from dash.dependencies import Input, Output, State
import dash
from dash import html
from ui.dashboard import interface 
from dash import dcc
import requests
def main():

    app = interface()


    @app.callback(
        Output("chat-history", "children"),
        Output("chat-store", "data"),
        Output("query", "value"),
        [Input("submit", "n_clicks"), Input("query", "n_submit")],
        State("query", "value"),
        State("chat-store", "data"),
        prevent_initial_call=True
    )
    def update_chat(n_clicks, n_submit, query, chat_history):
        if not query:
            return dash.no_update, dash.no_update, ""

        try:
            response = requests.post(
                "http://127.0.0.1:8000/query",
                json={"query": query},
            )
            response.raise_for_status()
            answer = response.json().get("answer", "No answer received.")
        except Exception as e:
            answer = f"❌ Error: {str(e)}"

        chat_history.append({"role": "user", "text": query})
        chat_history.append({"role": "assistant", "text": answer})

        chat_bubbles = []
        for msg in chat_history:
            bubble_style = {
                "user": {
                    "backgroundColor": "#DCF8C6",
                    "marginLeft": "auto", "marginRight": "10px",
                },
                "assistant": {
                    "backgroundColor": "#E4E6EB",
                    "marginRight": "auto", "marginLeft": "10px",
                }
            }[msg["role"]]

            chat_bubbles.append(
                html.Div(
                    dcc.Markdown(msg["text"]),
                    style={
                        **bubble_style,
                        "padding": "10px",
                        "borderRadius": "10px",
                        "maxWidth": "70%",
                        "marginTop": "5px",
                        "whiteSpace": "pre-wrap",
                    }
                )
            )

        return chat_bubbles, chat_history, ""
        
    app.run(host="0.0.0.0", port=8050)
      
if __name__ == "__main__":
    main()
    
    
