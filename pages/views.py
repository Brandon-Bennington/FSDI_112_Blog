from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'  # This points to pages/templates/home.html

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'  # This points to pages/templates/about.html
