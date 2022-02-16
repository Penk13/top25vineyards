from .models import Navbar, Footer, Sidebar
from news.models import Post, Category, Billboard


def base_variable(request):
    navbars = Navbar.objects.all().order_by("order")
    default_sidebar = Sidebar.objects.get(id=1).sidebar
    default_ad_manager = Sidebar.objects.get(id=1).ad_manager
    category = Category.objects.get(slug="global-travel-news")
    travel_news = Post.objects.filter(category=category).order_by("-id")
    billboards = Billboard.objects.filter(display=True)
    footer = Footer.objects.all().order_by("order")
    footer_index = int(footer.count()/2)
    footers1 = footer[:footer_index]
    footers2 = footer[footer_index:]
    return {"navbars": navbars,
            "default_sidebar": default_sidebar,
            "default_ad_manager": default_ad_manager,
            "travel_news": travel_news,
            "billboards": billboards,
            "footers1": footers1,
            "footers2": footers2}
