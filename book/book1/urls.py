from django.urls import path
from .views import add_book,netflix_home,home_view,programming_view,academic_view,portfolio_view,contact,grade,table,add_user,view_books

# http://127.0.0.1:8000/emp/add_emp

urlpatterns = [
    path('a', add_book),
    path('netflix/', netflix_home),
    path('home/', home_view),
    path('programming/', programming_view),
    path('academic/', academic_view),
    path('portfolio/', portfolio_view),
    path('contact/',contact),
    path('grade/<int:marks>',grade),
    path('table/', table),
    path('userform/',add_user),
    path('view_books/',view_books),
]