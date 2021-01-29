from django.urls import path, include

from .views import(
    MonitoringCategoryListAPIView,
    MonitoringCategoryDetailAPIView,

    SolutionObjectiveListAPIView,
    SolutionObjectiveDetailAPIView,

    SolutionListAPIView,
    SolutionDetailAPIView,
)

app_name = 'apps.monitoring_solutions'

urlpatterns = [
    path("monitoring-category/", MonitoringCategoryListAPIView.as_view(),
         name="monitoring-cat-list-api"),
    path("monitoring-category/<slug:slug>/", MonitoringCategoryDetailAPIView.as_view(),
         name="monitoring-cat-detail-api"),

    path("solution-objective/", SolutionObjectiveListAPIView.as_view(),
         name="solution-obj-list-api"),
    path("solution-objective/<slug:slug>/",
         SolutionObjectiveDetailAPIView.as_view(), name="solution-obj-detail-api"),

    path("solution/", SolutionListAPIView.as_view(), name="solution-list-api"),
    path("solution/<slug:slug>/", SolutionDetailAPIView.as_view(), name="solution-detail-api"),

]
