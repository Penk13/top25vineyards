from .models import ContentPage, Navbar, Sidebar
from news.models import Post, Category


def base_variable(request):
    navbars = Navbar.objects.all().order_by("order")
    default_sidebar = Sidebar.objects.get(id=1).sidebar
    default_ad_manager = Sidebar.objects.get(id=1).ad_manager
    category = Category.objects.get(slug="global-travel-news")
    travel_news = Post.objects.filter(category=category).order_by("-id")
    footer_count = ContentPage.objects.filter(types="FOOTER").count()
    footer_index = int(footer_count/2)
    footers1 = ContentPage.objects.filter(types="FOOTER")[:footer_index]
    footers2 = ContentPage.objects.filter(types="FOOTER")[footer_index:]
    return {"navbars": navbars,
            "default_sidebar": default_sidebar,
            "default_ad_manager": default_ad_manager,
            "travel_news": travel_news,
            "footers1": footers1,
            "footers2": footers2}
