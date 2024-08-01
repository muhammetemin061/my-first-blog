from django.contrib import admin
from .models import Post
#super user modeli oluşturmamız lazım superuserin herşeye erişimi vardır
#Admin sayfasında modelimizi görünür kılabilmek için, modeli admin.site.register(Post) ile kaydetmemiz gerekiyor.
#venv etkinleştirmek için yürütme politikasını değiştir ardından myvenv\Scripts\activate bun kodu cmd ye yaz dogru  dizine dikkat et
#  

admin.site.register(Post)

