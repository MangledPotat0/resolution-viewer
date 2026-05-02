from dash import Dash
from connection import db_connect
from core.data_provider import DBDataProvider
from core.chart_service import ChartService
from core.layout_service import LayoutService
from dashboard.dashboard import Dashboard
from dashboard.callbacks import register_callbacks

app = Dash(__name__)

# Dependency Injection
data_provider = DBDataProvider(db_connect())
chart_service = ChartService(data_provider)
layout_service = LayoutService(data_provider)

dashboard = Dashboard(layout_service, chart_service)

# Set layout
app.layout = dashboard.layout()

# Register callbacks
register_callbacks(app, dashboard)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)

