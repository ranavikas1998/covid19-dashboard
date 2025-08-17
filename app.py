# -------------------------------
# Importing Libraries
# -------------------------------
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# -------------------------------
# Load CSV Data
# -------------------------------
df_age = pd.read_csv("AgeGroupDetails.csv")  # Age-wise data
df_state = pd.read_csv("covid_19_india.csv")  # State-wise data
df_individual = pd.read_csv("IndividualDetails.csv")  # Individual details

# -------------------------------
# Data Preprocessing
# -------------------------------
# Total numbers
total_cases = len(df_individual)
recovered_cases = len(df_individual[df_individual["current_status"] == "Recovered"])
death_cases = len(df_individual[df_individual["current_status"] == "Deceased"])
active_cases = total_cases - recovered_cases - death_cases

# -------------------------------
# Initialize Dash App
# -------------------------------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # for deployment (Heroku, etc.)

# -------------------------------
# Layout Design
# -------------------------------
app.layout = dbc.Container([

    # Title
    dbc.Row([
        dbc.Col(html.H1("Corona Virus - India's Perspective",
                        style={"textAlign": "center", "color": "white"}), width=12)
    ], style={"backgroundColor": "#2C3E50", "padding": "10px"}),

    # Counter Cards
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Total Cases", style={"color": "white"}),
                html.H2(total_cases, style={"color": "white"})
            ])
        ], style={"backgroundColor": "red", "textAlign": "center"}), width=3),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Active", style={"color": "white"}),
                html.H2(active_cases, style={"color": "white"})
            ])
        ], style={"backgroundColor": "dodgerblue", "textAlign": "center"}), width=3),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Recovered", style={"color": "white"}),
                html.H2(recovered_cases, style={"color": "white"})
            ])
        ], style={"backgroundColor": "gold", "textAlign": "center"}), width=3),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Deaths", style={"color": "white"}),
                html.H2(death_cases, style={"color": "white"})
            ])
        ], style={"backgroundColor": "green", "textAlign": "center"}), width=3),
    ], style={"marginTop": "20px"}),

    # Graphs Row
    dbc.Row([
        # Day by Day Analysis
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Day by Day Analysis"),
                dcc.Graph(
                    figure=px.line(df_state, x="Date", y="Confirmed", title="Day by Day Growth")
                )
            ])
        ]), width=6),

        # Age Distribution Pie
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Age Distribution"),
                dcc.Graph(
                    figure=px.pie(df_age, values="TotalCases", names="AgeGroup",
                                  title="Age Distribution of Cases")
                )
            ])
        ]), width=6),
    ], style={"marginTop": "20px"}),

    # State-wise Distribution with Dropdown
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("State Total Count"),
                dcc.Dropdown(
                    id="status-picker",
                    options=[
                        {"label": "Hospitalized", "value": "Hospitalized"},
                        {"label": "Recovered", "value": "Recovered"},
                        {"label": "Deceased", "value": "Deceased"},
                    ],
                    value="Hospitalized",  # Default selection
                    clearable=False
                ),
                dcc.Graph(id="state-graph")
            ])
        ]), width=12)
    ], style={"marginTop": "20px"}),

], fluid=True)


# -------------------------------
# Callback Function for State Graph
# -------------------------------
@app.callback(
    Output("state-graph", "figure"),
    Input("status-picker", "value")
)
def update_bar_chart(selected_status):
    """ Updates the bar chart based on dropdown selection """
    df_filtered = df_individual[df_individual["current_status"] == selected_status]
    state_count = df_filtered["detected_state"].value_counts().reset_index()
    state_count.columns = ["State", "Count"]

    fig = px.bar(state_count, x="State", y="Count", title=f"State wise {selected_status} Count")
    fig.update_layout(xaxis_tickangle=-45)
    return fig


# -------------------------------
# Run App
# -------------------------------
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8080, debug=True)

