"""
Creatine Water Reminder - Ana uygulama dosyası
"""
# #region agent log
import json, time, traceback
try:
    with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
        f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"A","location":"app.py:8","message":"Module import start","data":{},"timestamp":int(time.time()*1000)})+"\n")
except: pass
# #endregion
import toga
# #region agent log
try:
    with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
        f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"A","location":"app.py:12","message":"toga imported","data":{},"timestamp":int(time.time()*1000)})+"\n")
except: pass
# #endregion
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from datetime import datetime

# #region agent log
try:
    with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
        f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"A","location":"app.py:18","message":"Before storage import","data":{},"timestamp":int(time.time()*1000)})+"\n")
except: pass
# #endregion
try:
    from .storage import Storage
    # #region agent log
    try:
        with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
            f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"A","location":"app.py:22","message":"Storage imported","data":{},"timestamp":int(time.time()*1000)})+"\n")
    except: pass
    # #endregion
except Exception as e:
    # #region agent log
    try:
        with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
            f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"A","location":"app.py:26","message":"Storage import failed","data":{"error":str(e),"traceback":traceback.format_exc()},"timestamp":int(time.time()*1000)})+"\n")
    except: pass
    # #endregion
    Storage = None

# #region agent log
try:
    with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
        f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"D","location":"app.py:30","message":"Before notifications import","data":{},"timestamp":int(time.time()*1000)})+"\n")
except: pass
# #endregion
try:
    from .notifications import NotificationManager
    # #region agent log
    try:
        with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
            f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"D","location":"app.py:34","message":"NotificationManager imported","data":{},"timestamp":int(time.time()*1000)})+"\n")
    except: pass
    # #endregion
except Exception as e:
    # #region agent log
    try:
        with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
            f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"D","location":"app.py:38","message":"NotificationManager import failed","data":{"error":str(e),"traceback":traceback.format_exc()},"timestamp":int(time.time()*1000)})+"\n")
    except: pass
    # #endregion
    NotificationManager = None

try:
    from .workouts import WorkoutManager
except Exception as e:
    # #region agent log
    try:
        with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
            f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"A","location":"app.py:46","message":"WorkoutManager import failed","data":{"error":str(e)},"timestamp":int(time.time()*1000)})+"\n")
    except: pass
    # #endregion
    WorkoutManager = None


class CreatineWaterReminder(toga.App):
    def startup(self):
        """Uygulama başlangıcı"""
        # #region agent log
        try:
            with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"B","location":"app.py:52","message":"startup() called","data":{},"timestamp":int(time.time()*1000)})+"\n")
        except: pass
        # #endregion
        try:
            # #region agent log
            try:
                with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                    f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"C","location":"app.py:56","message":"Before Storage() init","data":{},"timestamp":int(time.time()*1000)})+"\n")
            except: pass
            # #endregion
            self.storage = Storage() if Storage else None
            # #region agent log
            try:
                with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                    f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"C","location":"app.py:60","message":"Storage() created","data":{"storage":str(self.storage)},"timestamp":int(time.time()*1000)})+"\n")
            except: pass
            # #endregion
        except Exception as e:
            # #region agent log
            try:
                with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                    f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"C","location":"app.py:64","message":"Storage init failed","data":{"error":str(e),"traceback":traceback.format_exc()},"timestamp":int(time.time()*1000)})+"\n")
            except: pass
            # #endregion
            print(f"Storage başlatılamadı: {e}")
            # Basit fallback storage
            self.storage = None
        
        try:
            # #region agent log
            try:
                with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                    f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"D","location":"app.py:70","message":"Before NotificationManager() init","data":{},"timestamp":int(time.time()*1000)})+"\n")
            except: pass
            # #endregion
            self.notification_manager = NotificationManager() if NotificationManager else None
            # #region agent log
            try:
                with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                    f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"D","location":"app.py:74","message":"NotificationManager() created","data":{"manager":str(self.notification_manager)},"timestamp":int(time.time()*1000)})+"\n")
            except: pass
            # #endregion
        except Exception as e:
            # #region agent log
            try:
                with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                    f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"D","location":"app.py:78","message":"NotificationManager init failed","data":{"error":str(e),"traceback":traceback.format_exc()},"timestamp":int(time.time()*1000)})+"\n")
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
            with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"B","location":"app.py:87","message":"Before UI creation","data":{},"timestamp":int(time.time()*1000)})+"\n")
        except: pass
        # #endregion
        # Ana container
        try:
            main_box = toga.Box(style=Pack(direction=COLUMN, padding=20, flex=1))
            # #region agent log
            try:
                with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                    f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"B","location":"app.py:92","message":"main_box created","data":{},"timestamp":int(time.time()*1000)})+"\n")
            except: pass
            # #endregion
        except Exception as e:
            # #region agent log
            try:
                with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                    f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"B","location":"app.py:96","message":"main_box creation failed","data":{"error":str(e),"traceback":traceback.format_exc()},"timestamp":int(time.time()*1000)})+"\n")
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
            with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"B","location":"app.py:140","message":"Before MainWindow creation","data":{},"timestamp":int(time.time()*1000)})+"\n")
        except: pass
        # #endregion
        try:
            self.main_window = toga.MainWindow(title=self.formal_name, size=(400, 700))
            # #region agent log
            try:
                with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                    f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"B","location":"app.py:144","message":"MainWindow created","data":{},"timestamp":int(time.time()*1000)})+"\n")
            except: pass
            # #endregion
            self.main_window.content = scroll
            # #region agent log
            try:
                with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                    f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"B","location":"app.py:147","message":"Before window.show()","data":{},"timestamp":int(time.time()*1000)})+"\n")
            except: pass
            # #endregion
            self.main_window.show()
            # #region agent log
            try:
                with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                    f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"B","location":"app.py:150","message":"window.show() completed","data":{},"timestamp":int(time.time()*1000)})+"\n")
            except: pass
            # #endregion
        except Exception as e:
            # #region agent log
            try:
                with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                    f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"B","location":"app.py:153","message":"MainWindow/show failed","data":{"error":str(e),"traceback":traceback.format_exc()},"timestamp":int(time.time()*1000)})+"\n")
            except: pass
            # #endregion
            raise
        
        # Bildirimleri başlat
        self.initialize_notifications()
        # #region agent log
        try:
            with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"B","location":"app.py:160","message":"startup() completed","data":{},"timestamp":int(time.time()*1000)})+"\n")
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
        with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
            f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"E","location":"app.py:200","message":"main() called","data":{},"timestamp":int(time.time()*1000)})+"\n")
    except: pass
    # #endregion
    try:
        app = CreatineWaterReminder()
        # #region agent log
        try:
            with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"E","location":"app.py:205","message":"CreatineWaterReminder() created","data":{},"timestamp":int(time.time()*1000)})+"\n")
        except: pass
        # #endregion
        return app
    except Exception as e:
        # #region agent log
        try:
            with open(r"c:\Users\admin\Desktop\New folder (5)\.cursor\debug.log", "a", encoding="utf-8") as f:
                f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":"E","location":"app.py:210","message":"main() failed","data":{"error":str(e),"traceback":traceback.format_exc()},"timestamp":int(time.time()*1000)})+"\n")
        except: pass
        # #endregion
        raise


if __name__ == "__main__":
    app = main()
    app.main_loop()

