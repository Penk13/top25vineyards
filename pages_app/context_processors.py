from .models import Navbar, Footer, Sidebar, Script
from list.models import Post, Category, Billboard


def base_variable(request):
    header_script = Script.objects.get(name="HEADER SCRIPT")
    navbars = Navbar.objects.all().order_by("order")
    default_sidebar = Sidebar.objects.get(id=1).sidebar
    default_ad_manager = Sidebar.objects.get(id=1).ad_manager
    category = Category.objects.get(slug="global-travel-news")
    travel_news = Post.objects.filter(category=category).order_by("-id")
    billboards = Billboard.objects.filter(display=True)
    footer = Footer.objects.all().order_by("order")
    remainder = int(footer.count() % 3)
    item_per_col = int(footer.count()/3)
    idx1 = item_per_col + remainder
    idx2 = idx1 + item_per_col
    footers1 = footer[:idx1]
    footers2 = footer[idx1:idx2]
    footers3 = footer[idx2:]
    return {"header_script": header_script,
            "navbars": navbars,
            "default_sidebar": default_sidebar,
            "default_ad_manager": default_ad_manager,
            "travel_news": travel_news,
            "billboards": billboards,
            "footers1": footers1,
            "footers2": footers2,
            "footers3": footers3}
