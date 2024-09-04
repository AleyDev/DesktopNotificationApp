# Plyer kütüphanesinden notification modülünü içe aktarıyorum
from plyer import notification

def bildirim_gonder(baslik, mesaj):
    """
    Masaüstü bildirimini göndermek için bir fonksiyon tanımlıyorum.

    Parametreler:
    baslik (str): Bildirimin başlığı.
    mesaj (str): Bildirimin içeriği.
    """
    # notification.notify() fonksiyonu ile bildirim gönderiyorum
    notification.notify(
        title=baslik,       # Bildirimin başlığını belirtiyorum
        message=mesaj,      # Bildirimin içeriğini belirtiyorum
        app_name="Bildirim Uygulaması",  # Bildirimi gönderen uygulamanın adını belirtiyorum
        timeout=10          # Bildirimin ekranda kalma süresi (saniye)
    )

# Kullanıcıdan bildirim başlığını girmesini istiyorum
baslik = input("Bildirim başlığını girin: ")

# Kullanıcıdan bildirim mesajını girmesini istiyorum
mesaj = input("Bildirim mesajını girin: ")


# Bildirim gönderme fonksiyonunu çağırıyorum
bildirim_gonder(baslik, mesaj)
