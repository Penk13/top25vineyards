from .models import Navbar, Footer, Sidebar, Script
from list.models import Post, Category, Billboard
from filters.models import WorldArea, GeoRegion, Country, WineRegion, Wine, Facility, Service, Rating


def base_variable(request):
    # Filter Vineyard
    world_area_filters = WorldArea.objects.all()
    geo_region_filters = GeoRegion.objects.all()
    country_filters = Country.objects.all()
    wine_region_filters = WineRegion.objects.all()
    wine_filters = Wine.objects.all()
    facility_filters = Facility.objects.all()
    service_filters = Service.objects.all()
    rating_filters = Rating.objects.all()

    # Base
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
    return {"world_area_filters": world_area_filters,
            "geo_region_filters": geo_region_filters,
            "country_filters": country_filters,
            "wine_region_filters": wine_region_filters,
            "wine_filters": wine_filters,
            "facility_filters": facility_filters,
            "service_filters": service_filters,
            "rating_filters": rating_filters,

            "header_script": header_script,
            "navbars": navbars,
            "default_sidebar": default_sidebar,
            "default_ad_manager": default_ad_manager,
            "travel_news": travel_news,
            "billboards": billboards,
            "footers1": footers1,
            "footers2": footers2,
            "footers3": footers3}
