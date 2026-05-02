import numpy as np
import pandas as pd
import plotly.express as px

class ChartService:
    def __init__(self, data_provider):
        self.data_provider = data_provider

    def progress_bar(self, activity_type):
        df, metadata = self.data_provider.get_activity(activity_type)
        if np.isnan(metadata["goal"]):
            print("nan")
            metadata["goal"] = 1
        progress = round(100*df["display_quantity"].sum()/metadata["goal"], 2)
        bar = pd.DataFrame(
                [{"progress (%)": progress,
                  "label": "filled",
                  "y":0},
                 {"progress (%)": 100-progress,
                  "label": "empty",
                  "y":0}]
        )
        cmap = {"filled": "#4CAF50", "empty": "#eee"}
        fig = px.bar(
            bar,
            x="progress (%)",
            y="y",
            color="label",
            orientation="h",
            range_x=[0,100],
            height=80,
            color_discrete_map=cmap,
            title=f"Progress for {activity_type}: {progress}%"
        )
        fig.update_traces(text=None, hoverinfo="skip")
        fig.update_layout(
            margin=dict(l=0,r=0,t=55,b=10),
            barmode="stack",
            showlegend=False,
            yaxis=dict(visible=False),
            plot_bgcolor="white",
            paper_bgcolor="white",
            title_x=0.5,
            hovermode=False
        )
        return fig

    def lineplot(self, activity_type):
        df, metadata = self.data_provider.get_activity(activity_type)
        new_name = f"Quantity ({metadata['uname']})"
        df.rename(columns={"display_quantity": new_name},
                  inplace=True)
        fig = px.line(
            df,
            x="timestamp",
            y=new_name,
            hover_name=new_name,
            title=f"Logs for {activity_type}"
        )
        fig.update_layout(
            margin=dict(l=0,r=0,t=55,b=10),
            plot_bgcolor="white",
            paper_bgcolor="white",
            title_x=0.5,
        )
        return fig

    def cumlineplot(self, activity_type):
        df, metadata = self.data_provider.get_activity(activity_type)
        df["display_quantity"] = df["display_quantity"].cumsum()
        new_name = f"Quantity ({metadata['uname']})"
        df.rename(columns={"display_quantity": new_name},
                  inplace=True)
        fig = px.line(
            df,
            x="timestamp",
            y=new_name,
            hover_name=new_name,
            title=f"Cumulative progress for {activity_type}"
        )
        fig.update_layout(
            margin=dict(l=0,r=0,t=55,b=10),
            plot_bgcolor="white",
            paper_bgcolor="white",
            title_x=0.5,
        )
        return fig

# EOF
