from django.urls import path, include

from .views import(
    UserSolutionsDetailAPIView,
    UserSampleCreateAPIView,
)

app_name = 'apps.user_monitoring'

urlpatterns = [
    path("user-solutions/<slug:slug>/", UserSolutionsDetailAPIView.as_view(),
         name="user-solutions-detail-api"),
    
    path("data-collection/", UserSampleCreateAPIView.as_view(),
         name="data-collection-api"),

    # path("solution-objective/", SolutionObjectiveListAPIView.as_view(),
    #      name="solution-obj-list-api"),
    # path("solution-objective/<slug:slug>/",
    #      SolutionObjectiveDetailAPIView.as_view(), name="solution-obj-detail-api"),

    # path("solution/", SolutionListAPIView.as_view(), name="solution-list-api"),
    # path("solution/<slug:slug>/", SolutionDetailAPIView.as_view(), name="solution-detail-api"),

]
