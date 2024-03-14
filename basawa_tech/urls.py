from django.urls import path
from .views import *

urlpatterns = [
    path('show_template/', home_page),
    path('showform/1/1/3by1-first/', form_page1),
    path('showform/1/1/3by1-second/', form_page2),
    path('showform/1/1/3by1-third/', form_page3),
    path('showform/1/1/3by1-fourth/', form_page4),
    path('showform/1/1/3by1-fifth/', form_page5),
    path('showform/1/1/3by1-sixth/', form_page6),

    # Add similar paths for other routes
    path('showpdf/1/1/first/', show_pdf1),
    path('showpdf/1/1/second/', show_pdf2),
    path('showpdf/1/1/third/', show_pdf3),
    path('showpdf/1/1/fourth/', show_pdf4),
    path('showpdf/1/1/fifth/', show_pdf5),
    path('showpdf/1/1/sixth/', show_pdf6),
]
