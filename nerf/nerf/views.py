
from django.views.generic import TemplateView
from crawl.crawl_profile import download_images
from crawl.config import *

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        
        # input에 크롤링하고 싶은 유저의 아이디를 입력
        download_images('yellow_for_me')
        return {}