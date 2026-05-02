# -*- coding: utf-8 -*-
"""
dashboard/callbacks.py

Callback for updating the figures on the dashboard with user input
"""

# built-in module imports
from typing import Tuple

# 3rd party module imports
from dash import Dash, Input, Output
from plotly.graph_objects import Figure

# local module imports
from dashboard import Dashboard

def register_callbacks(app: Dash, dashboard: Dashboard):
    """
    Registers a callback function to respond when the input value on the
    activity-type-dropdown changes, and triggering the output (figures) to
    update, and then returning the updated figure objects to render.

    Args:
        app (dash.Dash): Dash application from dash library, which is the
            actual application that is serving contents.
        dashboard (Dashboard): Locally defined Dashboard object that holds the
            figure objects as its attributes.
    """
    @app.callback(
        Output("progress-bar", "figure"),
        Output("line-plot", "figure"),
        Output("cumulative-line-plot", "figure"),
        Input("activity-type-dropdown", "value"),
    )
    def update_charts(activity_type:str) -> tuple[Figure, Figure, Figure]:
        """
        When the activity type is selected, return the graphic objects.

        Args:
            activity_type (str): String name of the activity.
        Return:
            tuple[Figure, Figure, Figure]: Tuple of dashboard objects from the
            figure.
        """
        return (
            dashboard.progress_bar(activity_type),
            dashboard.lineplot(activity_type),
            dashboard.cumlineplot(activity_type)
        )

