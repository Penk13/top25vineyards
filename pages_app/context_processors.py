from .models import ContentPage, Navbar
from news.models import Post, Category


def base_variable(request):
    navbars = Navbar.objects.all().order_by("order")
    category = Category.objects.get(slug="global-travel-news")
    travel_news = Post.objects.filter(category=category).order_by("-id")
    footer_count = ContentPage.objects.filter(types="FOOTER").count()
    footer_index = int(footer_count/2)
    footers1 = ContentPage.objects.filter(types="FOOTER")[:footer_index]
    footers2 = ContentPage.objects.filter(types="FOOTER")[footer_index:]
    return {"navbars": navbars,
            "travel_news": travel_news,
            "footers1": footers1,
            "footers2": footers2}
