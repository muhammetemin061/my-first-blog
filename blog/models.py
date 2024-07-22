##Bu satır, Django'nun ayarlarını (settings) içe aktarır. settings modülü, Django projenizin yapılandırma ayarlarını içerir. Bu ayarlar, veritabanı bağlantı bilgileri, şablon konfigürasyonları, statik dosyalar ve diğer yapılandırma parametrelerini içerir.

from django.conf import settings 
from django.db import models
from django.utils import timezone


class Post(models.Model):  #model djanbdonun veritabanı şemasını tanımlamak için kullanılır
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)#veritabanında karakter uzunlugunu tutma işine denir

    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)#veritabanı9nda bir alanın boş bırakılmasına izin vermek blanlk=true null degerine sahip olmasına izin vermek ise  null = true dir 

    def publish(self):
        self.published_date = timezone.now() #geçerli tarih ve saat bilgisini döndürür
        self.save()

    def __str__(self):
        return self.title