import pandas as pd
import plotly.express as px

import core.activity_queries as aq
import core.unit_queries as uq

class DBDataProvider:
    def __init__(self, conn):
        self.conn = conn
        self.activity_types = pd.DataFrame(aq.get_all_activity_types(conn))
        self.units = uq.get_all_units(self.conn)
        self.units = {u["name"]: u["id"] for u in self.units}

    def get_activity(self, activity_type, uname=None):
        if activity_type == "All":
            pass
        else:
            return self._get_activity(activity_type, uname=uname)

    def _get_all_activities(self):
        return pd.DataFrame(aq.get_all_activities(self.conn))

    def _get_activity(self, activity_type, uname=None):
        cond = self.activity_types["name"] == activity_type
        if uname is None:
            ug = self.activity_types.loc[cond, "unit_group_id"].iloc[0]
            ug = uq.get_unit_group(self.conn, int(ug))
            uname = ug["canonical_unit_name"]
            unit = ug["canonical_unit_id"]
        else:
            unit = self.units[uname]
        activity_type = int(self.activity_types.loc[cond, "id"].iloc[0])
        result = pd.DataFrame(
                aq.get_activity_logs_for_type(self.conn, unit, activity_type)
        )

        metadata = {
            "goal": self.activity_types.loc[cond, "goal_quantity"].iloc[0],
            "uname": uname
        }
        return result, metadata
