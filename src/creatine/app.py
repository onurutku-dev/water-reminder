"""
Creatine Water Reminder - Ana uygulama dosyası
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from datetime import datetime

from .storage import Storage
from .notifications import NotificationManager
from .workouts import WorkoutManager


class CreatineWaterReminder(toga.App):
    def startup(self):
        """Uygulama başlangıcı"""
        self.storage = Storage()
        self.notification_manager = NotificationManager()
        self.workout_manager = WorkoutManager()
        
        # Ana container
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=20, flex=1))
        
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
        self.notification_switch.value = self.storage.get_notifications_enabled()
        main_box.add(self.notification_switch)
        
        # Okul Modu Switch
        self.school_mode_switch = toga.Switch(
            "Okuldayım",
            on_change=self.on_school_mode_toggle,
            style=Pack(padding=10)
        )
        self.school_mode_switch.value = self.storage.get_school_mode()
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
        
        self.main_window = toga.MainWindow(title=self.formal_name, size=(400, 700))
        self.main_window.content = scroll
        self.main_window.show()
        
        # Bildirimleri başlat
        self.initialize_notifications()
    
    def on_notification_toggle(self, widget):
        """Bildirim switch değiştiğinde"""
        enabled = widget.value
        self.storage.set_notifications_enabled(enabled)
        
        if enabled and not self.storage.get_school_mode():
            self.notification_manager.start_notifications()
        else:
            self.notification_manager.stop_notifications()
    
    def on_school_mode_toggle(self, widget):
        """Okul modu switch değiştiğinde"""
        school_mode = widget.value
        self.storage.set_school_mode(school_mode)
        
        if school_mode:
            # Okul modu açıldı - bildirimleri durdur
            self.notification_manager.pause_notifications()
        else:
            # Okul modu kapandı - bildirimler açıksa devam et
            if self.storage.get_notifications_enabled():
                self.notification_manager.resume_notifications()
    
    def initialize_notifications(self):
        """Bildirimleri başlat"""
        if self.storage.get_notifications_enabled() and not self.storage.get_school_mode():
            self.notification_manager.start_notifications()
    
    def update_workout_display(self):
        """Bugünün antrenmanını göster"""
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
    return CreatineWaterReminder()


if __name__ == "__main__":
    app = main()
    app.main_loop()

