from .models import Women, Category
from django.contrib.sitemaps import Sitemap


class PostSiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Women.published.all()
    
    def lastmod(self, obj):
        return obj.time_update
    

class CategorySiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Category.objects.all()