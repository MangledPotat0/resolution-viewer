class Dashboard:
    def __init__(self, layout_service, chart_service):
        self.layout_service = layout_service
        self.chart_service = chart_service

    def layout(self):
        return self.layout_service.build()

    def progress_bar(self, activity_type):
        return self.chart_service.progress_bar(activity_type)

    def lineplot(self, activity_type):
        return self.chart_service.lineplot(activity_type)

    def cumlineplot(self, activity_type):
        return self.chart_service.cumlineplot(activity_type)

