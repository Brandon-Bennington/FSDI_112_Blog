from django.views.generic import TemplateView
from posts.models import Post

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.all().order_by('-created_on')[:5]  # Adjust the number as needed
        return context

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'  # This points to pages/templates/about.html
