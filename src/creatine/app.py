"""
Creatine Water Reminder - Ana uygulama dosyası
"""
# #region agent log
import json, time, traceback, os
def _debug_log(location, message, hypothesis_id, data=None):
    try:
        if hasattr(os, 'environ') and 'HOME' in os.environ:
            log_path = os.path.join(os.environ['HOME'], 'Documents', 'debug.log')
        else:
            try:
                log_path = os.path.join(os.path.expanduser('~'), 'Documents', 'debug.log')
            except:
                log_path = 'debug.log'  # Fallback to current directory
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":hypothesis_id,"location":location,"message":message,"data":data or {},"timestamp":int(time.time()*1000)})+"\n")
    except Exception as e:
        print(f"DEBUG LOG ERROR: {e}")
        import traceback
        print(traceback.format_exc())
try:
    _debug_log("app.py:8", "Module import start", "A")
except: pass
# #endregion
import toga
# #region agent log
try:
    _debug_log("app.py:12", "toga imported", "A")
except: pass
# #endregion
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from datetime import datetime

# #region agent log
try:
    _debug_log("app.py:18", "Before storage import", "A")
except: pass
# #endregion
try:
    from .storage import Storage
    # #region agent log
    try:
        _debug_log("app.py:22", "Storage imported", "A")
    except: pass
    # #endregion
except Exception as e:
    # #region agent log
    try:
        _debug_log("app.py:26", "Storage import failed", "A", {"error":str(e),"traceback":traceback.format_exc()})
    except: pass
    # #endregion
    Storage = None

# #region agent log
try:
    _debug_log("app.py:30", "Before notifications import", "D", {})
except: pass
# #endregion
try:
    from .notifications import NotificationManager
    # #region agent log
    try:
        _debug_log("app.py:34", "NotificationManager imported", "D")
    except: pass
    # #endregion
except Exception as e:
    # #region agent log
    try:
        _debug_log("app.py:38", "NotificationManager import failed", "D", {"error":str(e),"traceback":traceback.format_exc()})
    except: pass
    # #endregion
    NotificationManager = None

try:
    from .workouts import WorkoutManager
except Exception as e:
    # #region agent log
    try:
        _debug_log("app.py:46", "WorkoutManager import failed", "A", {"error":str(e)})
    except: pass
    # #endregion
    WorkoutManager = None


class CreatineWaterReminder(toga.App):
    def startup(self):
        """Uygulama başlangıcı"""
        # #region agent log
        try:
            _debug_log("app.py:52", "startup() called", "B", {})
        except: pass
        # #endregion
        try:
            # #region agent log
            try:
                _debug_log("app.py:56", "Before Storage() init", "C", {})
            except: pass
            # #endregion
            self.storage = Storage() if Storage else None
            # #region agent log
            try:
                _debug_log("app.py:60", "Storage() created", "C", {"storage":str(self.storage)})
            except: pass
            # #endregion
        except Exception as e:
            # #region agent log
            try:
                _debug_log("app.py:64", "Storage init failed", "C", {"error":str(e),"traceback":traceback.format_exc()})
            except: pass
            # #endregion
            print(f"Storage başlatılamadı: {e}")
            # Basit fallback storage
            self.storage = None
        
        try:
            # #region agent log
            try:
                _debug_log("app.py:70", "Before NotificationManager() init", "D", {})
            except: pass
            # #endregion
            self.notification_manager = NotificationManager() if NotificationManager else None
            # #region agent log
            try:
                _debug_log("app.py:74", "NotificationManager() created", "D", {"manager":str(self.notification_manager)})
            except: pass
            # #endregion
        except Exception as e:
            # #region agent log
            try:
                _debug_log("app.py:78", "NotificationManager init failed", "D", {"error":str(e),"traceback":traceback.format_exc()})
            except: pass
            # #endregion
            print(f"NotificationManager başlatılamadı: {e}")
            # Bildirimler olmadan da çalışsın
            self.notification_manager = None
        
        try:
            self.workout_manager = WorkoutManager() if WorkoutManager else None
        except Exception as e:
            print(f"WorkoutManager başlatılamadı: {e}")
            self.workout_manager = None
        
        # #region agent log
        try:
            _debug_log("app.py:87", "Before UI creation", "B", {})
        except: pass
        # #endregion
        # Ana container
        try:
            main_box = toga.Box(style=Pack(direction=COLUMN, padding=20, flex=1))
            # #region agent log
            try:
                _debug_log("app.py:92", "main_box created", "B", {})
            except: pass
            # #endregion
        except Exception as e:
            # #region agent log
            try:
                _debug_log("app.py:96", "main_box creation failed", "B", {"error":str(e),"traceback":traceback.format_exc()})
            except: pass
            # #endregion
            raise
        
        # Başlık
        title = toga.Label(
            "Creatine Water Reminder",
            style=Pack(font_size=24, font_weight="bold", padding_bottom=20, text_align=CENTER)
        )
        main_box.add(title)
        
        # Su Bildirimleri Switch
        self.notification_switch = toga.Switch(
            "Su Bildirimleri",
            on_change=self.on_notification_toggle,
            style=Pack(padding=10)
        )
        self.notification_switch.value = self.storage.get_notifications_enabled() if self.storage else True
        main_box.add(self.notification_switch)
        
        # Okul Modu Switch
        self.school_mode_switch = toga.Switch(
            "Okuldayım",
            on_change=self.on_school_mode_toggle,
            style=Pack(padding=10)
        )
        self.school_mode_switch.value = self.storage.get_school_mode() if self.storage else False
        main_box.add(self.school_mode_switch)
        
        # Bugünün Antrenmanı başlığı
        workout_title = toga.Label(
            "Bugünün Antrenmanı",
            style=Pack(font_size=18, font_weight="bold", padding_top=20, padding_bottom=10)
        )
        main_box.add(workout_title)
        
        # Antrenman listesi
        self.workout_list = toga.MultilineTextInput(
            readonly=True,
            style=Pack(flex=1, padding=10, min_height=300)
        )
        self.update_workout_display()
        main_box.add(self.workout_list)
        
        # Scroll container
        scroll = toga.ScrollContainer(content=main_box)
        
        # #region agent log
        try:
            _debug_log("app.py:140", "Before MainWindow creation", "B", {})
        except: pass
        # #endregion
        try:
            self.main_window = toga.MainWindow(title=self.formal_name, size=(400, 700))
            # #region agent log
            try:
                _debug_log("app.py:144", "MainWindow created", "B", {})
            except: pass
            # #endregion
            self.main_window.content = scroll
            # #region agent log
            try:
                _debug_log("app.py:147", "Before window.show()", "B", {})
            except: pass
            # #endregion
            self.main_window.show()
            # #region agent log
            try:
                _debug_log("app.py:150", "window.show() completed", "B", {})
            except: pass
            # #endregion
        except Exception as e:
            # #region agent log
            try:
                _debug_log("app.py:153", "MainWindow/show failed", "B", {"error":str(e),"traceback":traceback.format_exc()})
            except: pass
            # #endregion
            raise
        
        # Bildirimleri başlat
        self.initialize_notifications()
        # #region agent log
        try:
            _debug_log("app.py:160", "startup() completed", "B", {})
        except: pass
        # #endregion
    
    def on_notification_toggle(self, widget):
        """Bildirim switch değiştiğinde"""
        try:
            enabled = widget.value
            if self.storage:
                self.storage.set_notifications_enabled(enabled)
            
            if self.notification_manager:
                if enabled:
                    # Bildirim manager'ı şimdi başlat
                    self.notification_manager._initialize_notification_center()
                    if not (self.storage and self.storage.get_school_mode()):
                        self.notification_manager.start_notifications()
                else:
                    self.notification_manager.stop_notifications()
        except Exception as e:
            print(f"Bildirim toggle hatası: {e}")
    
    def on_school_mode_toggle(self, widget):
        """Okul modu switch değiştiğinde"""
        try:
            school_mode = widget.value
            if self.storage:
                self.storage.set_school_mode(school_mode)
            
            if self.notification_manager:
                if school_mode:
                    # Okul modu açıldı - bildirimleri durdur
                    self.notification_manager.pause_notifications()
                else:
                    # Okul modu kapandı - bildirimler açıksa devam et
                    if self.storage and self.storage.get_notifications_enabled():
                        self.notification_manager.resume_notifications()
        except Exception as e:
            print(f"Okul modu toggle hatası: {e}")
    
    def initialize_notifications(self):
        """Bildirimleri başlat"""
        try:
            if self.storage and self.storage.get_notifications_enabled() and not self.storage.get_school_mode():
                if self.notification_manager:
                    self.notification_manager._initialize_notification_center()
                    self.notification_manager.start_notifications()
        except Exception as e:
            print(f"Bildirim başlatma hatası: {e}")
    
    def update_workout_display(self):
        """Bugünün antrenmanını göster"""
        if not self.workout_manager:
            self.workout_list.value = "Antrenman planı yüklenemedi."
            return
        
        today_workout = self.workout_manager.get_today_workout()
        if today_workout:
            display_text = f"{today_workout['day']} – {today_workout['type']}\n"
            if today_workout.get('location'):
                display_text += f"({today_workout['location']})\n"
            display_text += "\n"
            
            for exercise in today_workout['exercises']:
                display_text += f"• {exercise}\n"
            
            self.workout_list.value = display_text
        else:
            self.workout_list.value = "Bugün için antrenman planlanmamış."


def main():
    # #region agent log
    try:
        _debug_log("app.py:200", "main() called", "E", {})
    except: pass
    # #endregion
    try:
        app = CreatineWaterReminder()
        # #region agent log
        try:
            _debug_log("app.py:205", "CreatineWaterReminder() created", "E", {})
        except: pass
        # #endregion
        return app
    except Exception as e:
        # #region agent log
        try:
            _debug_log("app.py:210", "main() failed", "E", {"error":str(e),"traceback":traceback.format_exc()})
        except: pass
        # #endregion
        raise


if __name__ == "__main__":
    app = main()
    app.main_loop()

