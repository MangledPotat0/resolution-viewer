# -*- coding: utf-8 -*-
"""
dashboard.py
"""

# 3rd-party module imports
from plotly.graph_objects import Figure

# local module imports
from core.chart_service import ChartService
from core.layout_service import LayoutService

class Dashboard:
    def __init__(
            self,
            layout_service: LayoutService,
            chart_service: ChartService
        ):
        """
        Dashboard object that holds all the relevant parts under one namespace.

        Args:
            layout_service (LayoutService): For defining the structure of the
                dashboard.
            chart_service (ChartService): For defining the types of charts to
                render on the dashboard.

        Attrs:
            ibid.
        """
        self.layout_service = layout_service
        self.chart_service = chart_service

    def layout(self):
        """
        Builds the layout. See core/layout_service.
        """
        return self.layout_service.build()

    def progress_bar(self, activity_type: str) -> Figure:
        """
        Render a progress bar for given activity type.

        Args:
            activity_type (str): Name of activity to plot.

        Returns:
            plotly.graphicObjects.Figure: Figure containing a progress bar.
        """
        return self.chart_service.progress_bar(activity_type)

    def lineplot(self, activity_type: str) -> Figure:
        """
        Render a lineplot for given activity type.

        Args:
            activity_type (str): Name of activity to plot.

        Returns:
            plotly.graphicObjects.Figure: Figure containing a line plot.
        """
        return self.chart_service.lineplot(activity_type)

    def cumlineplot(self, activity_type: str) -> Figure:
        """
        Render a cumulative plot of progress for given activity type.

        Args:
            activity_type (str): Name of activity to plot.

        Returns:
            plotly.graphicObjects.Figure: Figure containing a cumulative plot.
        """
        return self.chart_service.cumlineplot(activity_type)

