"""
Antrenman planı verileri
"""
from datetime import datetime


class WorkoutManager:
    """Antrenman planı yönetimi"""
    
    def __init__(self):
        # Haftalık antrenman planı
        self.workouts = {
            'wednesday': {
                'day': 'Çarşamba',
                'type': 'PUSH',
                'location': 'Gym',
                'exercises': [
                    'Bench Press 4x6–8',
                    'Incline Dumbbell Press 3x10',
                    'Dumbbell Shoulder Press 3x6–10',
                    'Lateral Raise 3x12–15',
                    'Triceps Pushdown 3x10–12',
                    'Overhead Triceps Extension 3x10',
                    'Opsiyonel: Dips 1 set max'
                ]
            },
            'saturday': {
                'day': 'Cumartesi',
                'type': 'PULL',
                'location': 'Gym',
                'exercises': [
                    'Lat Pulldown 4x8–12',
                    'Cable Row 3x8–12',
                    'Chest Supported Row 3x8',
                    'Shoulder Shrug 3x12–15',
                    'Barbell Curl 3x10',
                    'Hammer Curl 3x8',
                    'Zottman Curl 2x12–15',
                    'Dead Hang 3x10–20 sn',
                    'Negative Pull-up 2–3x3–5'
                ]
            },
            'sunday': {
                'day': 'Pazar',
                'type': 'LEGS',
                'location': 'Gym',
                'exercises': [
                    'Leg Press 4x12',
                    'Leg Curl 4x12',
                    'Leg Extension 3x12',
                    'Adductor Machine 3x12–15',
                    'Standing Calf Raise 3x12–15',
                    'Plank 2–3x40–50 sn'
                ]
            },
            'monday': {
                'day': 'Pazartesi',
                'type': 'Evde PUSH',
                'location': '20 dk',
                'exercises': [
                    'Incline Push-up 3x10',
                    'Diz üstü şınav 2x8',
                    'Wall push-up 2x12',
                    'Bench dips 3x8',
                    'Side lateral raise (şişe) 3x15'
                ]
            },
            'wednesday_home': {
                'day': 'Çarşamba',
                'type': 'Evde PULL + Core',
                'location': '20 dk',
                'exercises': [
                    'Inverted row 3x10',
                    'Dead hang 3x10–15 sn',
                    'Su şişesi curl 3x12',
                    'Hammer curl 3x10',
                    'Side plank 2x20–30 sn',
                    'Dead bug 2x8'
                ]
            }
        }
    
    def get_today_workout(self):
        """Bugünün antrenmanını döndür"""
        today = datetime.now()
        day_name = today.strftime('%A').lower()
        
        # Türkçe gün isimlerine göre eşleştirme
        day_mapping = {
            'monday': 'monday',
            'tuesday': None,  # Salı için antrenman yok
            'wednesday': 'wednesday',  # Çarşamba için gym var, ama evde de var
            'thursday': None,
            'friday': None,
            'saturday': 'saturday',
            'sunday': 'sunday'
        }
        
        workout_key = day_mapping.get(day_name)
        
        if workout_key == 'wednesday':
            # Çarşamba için gym antrenmanını döndür
            # (İsteğe bağlı: hafta içi/evde kontrolü yapılabilir)
            return self.workouts.get('wednesday')
        
        if workout_key:
            return self.workouts.get(workout_key)
        
        return None
    
    def get_all_workouts(self):
        """Tüm antrenmanları döndür"""
        return self.workouts

