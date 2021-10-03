from .models import ContentPage, Navbar
from news.models import Post


def base_variable(request):
    navbars = Navbar.objects.all().order_by("order")
    travel_news = Post.objects.all()
    footer_count = ContentPage.objects.filter(types="FOOTER").count()
    footer_index = int(footer_count/2)
    footers1 = ContentPage.objects.filter(types="FOOTER")[:footer_index]
    footers2 = ContentPage.objects.filter(types="FOOTER")[footer_index:]
    return {"navbars": navbars,
            "travel_news": travel_news,
            "footers1": footers1,
            "footers2": footers2}
