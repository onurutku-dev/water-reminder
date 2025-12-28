"""
iOS bildirim yönetimi
"""
import platform

# iOS native sınıflarını yükle
try:
    from rubicon.objc import ObjCClass
    RUBICON_AVAILABLE = True
except ImportError:
    RUBICON_AVAILABLE = False

# iOS native sınıflarını yükle
if RUBICON_AVAILABLE and (platform.system() == 'Darwin' or hasattr(platform, 'ios')):
    try:
        # UNUserNotificationCenter ve ilgili sınıfları
        UNUserNotificationCenter = ObjCClass('UNUserNotificationCenter')
        UNMutableNotificationContent = ObjCClass('UNMutableNotificationContent')
        UNTimeIntervalNotificationTrigger = ObjCClass('UNTimeIntervalNotificationTrigger')
        UNNotificationRequest = ObjCClass('UNNotificationRequest')
    except Exception:
        # Simülatör veya test ortamında olabilir
        UNUserNotificationCenter = None
        UNMutableNotificationContent = None
        UNTimeIntervalNotificationTrigger = None
        UNNotificationRequest = None
else:
    UNUserNotificationCenter = None
    UNMutableNotificationContent = None
    UNTimeIntervalNotificationTrigger = None
    UNNotificationRequest = None


class NotificationManager:
    """iOS local notification yönetimi"""
    
    def __init__(self):
        self.notification_center = None
        self.is_running = False
        self.is_paused = False
        self._initialize_notification_center()
    
    def _initialize_notification_center(self):
        """iOS notification center'ı başlat"""
        try:
            if UNUserNotificationCenter:
                self.notification_center = UNUserNotificationCenter.currentNotificationCenter()
                # İzin iste
                self._request_permission()
        except Exception as e:
            print(f"Notification center başlatılamadı: {e}")
    
    def _request_permission(self):
        """Bildirim izni iste"""
        if not self.notification_center:
            return
        
        try:
            # UNAuthorizationOptions: alert=1, sound=2, badge=4
            options = 1 | 2 | 4
            
            def completion_handler(granted, error):
                if granted:
                    print("Bildirim izni verildi")
                else:
                    print("Bildirim izni reddedildi")
            
            self.notification_center.requestAuthorizationWithOptions_completionHandler_(
                options, completion_handler
            )
        except Exception as e:
            print(f"İzin istenemedi: {e}")
    
    def start_notifications(self):
        """Bildirimleri başlat (her 2 saatte bir)"""
        if self.is_paused:
            # Okul modu açık, sadece durumu güncelle
            return
        
        if self.is_running:
            # Zaten çalışıyor
            return
        
        if not self.notification_center:
            print("Notification center mevcut değil")
            return
        
        try:
            # Önceki bildirimleri temizle
            self.stop_notifications()
            
            # Yeni bildirim içeriği
            content = UNMutableNotificationContent.alloc().init()
            content.title = "Su İçme Hatırlatıcısı"
            content.body = "Creatine alıyorsun, su içmeyi unutma 💧"
            content.sound = "default"
            content.badge = 1
            
            # Her 2 saatte bir tekrarla (7200 saniye)
            trigger = UNTimeIntervalNotificationTrigger.triggerWithTimeInterval_repeats_(
                7200.0, True
            )
            
            # Bildirim isteği
            request = UNNotificationRequest.requestWithIdentifier_content_trigger_(
                "creatine_water_reminder",
                content,
                trigger
            )
            
            # Bildirimi ekle
            self.notification_center.addNotificationRequest_withCompletionHandler_(
                request, None
            )
            
            self.is_running = True
            print("Bildirimler başlatıldı (her 2 saatte bir)")
            
        except Exception as e:
            print(f"Bildirim başlatılamadı: {e}")
    
    def stop_notifications(self):
        """Bildirimleri durdur"""
        if not self.notification_center:
            return
        
        try:
            # Bekleyen bildirimleri iptal et
            pending_ids = ["creatine_water_reminder"]
            self.notification_center.removePendingNotificationRequestsWithIdentifiers_(
                pending_ids
            )
            
            # Delivered bildirimleri de temizle
            self.notification_center.removeDeliveredNotificationsWithIdentifiers_(
                pending_ids
            )
            
            self.is_running = False
            print("Bildirimler durduruldu")
            
        except Exception as e:
            print(f"Bildirimler durdurulamadı: {e}")
    
    def pause_notifications(self):
        """Bildirimleri geçici olarak durdur (okul modu)"""
        if self.is_running:
            self.stop_notifications()
        self.is_paused = True
    
    def resume_notifications(self):
        """Bildirimleri devam ettir (okul modu kapandı)"""
        self.is_paused = False
        if not self.is_running:
            self.start_notifications()

