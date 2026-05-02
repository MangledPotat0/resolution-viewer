from dash import Input, Output

def register_callbacks(app, dashboard):
    @app.callback(
        Output("progress-bar", "figure"),
        Output("line-plot", "figure"),
        Output("cumulative-line-plot", "figure"),
        Input("activity-type-dropdown", "value"),
    )
    def update_charts(activity_type):
        return (
            dashboard.progress_bar(activity_type),
            dashboard.lineplot(activity_type),
            dashboard.cumlineplot(activity_type)
        )

