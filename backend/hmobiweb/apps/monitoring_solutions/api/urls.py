from django.urls import path

from .views import(
    MonitoringCategoryListAPIView,
    SolutionObjectiveListAPIView,
)

app_name='apps.monitoring_solutions'


urlpatterns = [
    path("monitoring-category/", MonitoringCategoryListAPIView.as_view(), name="monitoring-cat-list-api"),
    path("solution-objective/", SolutionObjectiveListAPIView.as_view(), name="solution-obj-list-api"),
    # path("logout/", LogoutAPIView.as_view(), name="logout" ),
    # path("user-info/<uuid:alias>", PatientDetailAPIView.as_view(), name="user-info"),
]