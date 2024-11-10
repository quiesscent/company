from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/',views.about,name="about"),
    path('blogdetails/',views.blog_details,name='blogdetails'),
    path('blog/',views.blog,name="blog"),
    path('contact/',views.contact,name="contact"),
    path('portfoliodetails/',views.portfolio_details,name="portfoliodetails"),
    path('portfolio/',views.portfolio,name="portfolio"),
    path('pricing/',views.pricing,name="pricing"),
    path('servicedetails/',views.service_details,name="servicedetails"),
    path('services/',views.services,name="services"),
    path('team/',views.team,name="team"),
    path('testimonials/',views.testimonials,name="testimonials")
]