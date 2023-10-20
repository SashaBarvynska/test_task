from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from task import views


urlpatterns = [
    path('teams/', views.team_list),
    path('teams/<int:team_id>/', views.team_detail),
    path('people/', views.people_list),
    path('people/<int:person_id>/', views.people_detail),
    path('teams/<int:team_id>/people/', views.team_people_list),
    path('teams/<int:team_id>/people/<int:person_id>/', views.team_people),
]

urlpatterns = format_suffix_patterns(urlpatterns)
