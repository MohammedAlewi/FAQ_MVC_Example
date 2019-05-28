from django.urls import path
from . import views

urlpatterns=[
    # require no privileged
    path('',views.addQuestionPage,name="add_Question"),


    # require privileged and FAQ related
    path('add_question_page/',views.addQuestionPage,name="add_Question"),
    path('add_question/',views.addQestion,name="add_qtn"),
    path('more/<int:qt_id>/',views.detailOnQestion,name="FAQ"),
]
