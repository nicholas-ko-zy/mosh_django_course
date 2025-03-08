from django.urls import path
# So we can reference our views function
from .import views

# Django will look for this variable urlpatterns, so don't change it.
# This is also called a URLConf or URLConfiguration
# Every app will have its own URLConf
urlpatterns = [
    # NOTE: Always end route with a forward slash.
    path(route='hello/', view=views.say_hello)
]
