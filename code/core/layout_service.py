from dash import html, dcc

class LayoutService:
    def __init__(self, data_provider):
        self.data_provider = data_provider

    def build(self):
        df = self.data_provider.activity_types

        return html.Div(
            className="layout-container",
            children=[
                self._sidebar(df),
                self._main_content()
            ]
        )

    def _sidebar(self, df):
        return html.Div(
            className="sidebar",
            children=[
                html.H2("Filters"),

                html.Label("Select Activity to View"),
                dcc.Dropdown(
                    id="activity-type-dropdown",
                    #options=[{"label": "All", "value": "All"}] +
                    options=[{"label": c, "value": c}
                             for c in df["name"].unique()],
                    value="walking",
                    clearable=False
                ),

                html.Br(),

            ],
        )

    def _main_content(self):
        return html.Div(
            className="main-content",
            children=[
                html.H1("New Years Resolution Progress Dashboard"),
                html.Div(
                    style={"display": "flex", "gap": "10px", "flexWrap": "wrap"},
                    children=[
                        dcc.Graph(id="progress-bar", style={"flex": 1})
                    ]
                ),
                html.Div(
                    style={"display": "flex", "gap": "10px", "flexWrap": "wrap"},
                    children=[
                        dcc.Graph(id="line-plot", style={"flex": "1 1 400px"}),
                        dcc.Graph(id="cumulative-line-plot",
                                  style={"flex": "1 1 400px"}),
                    ],
                ),
            ],
        )

