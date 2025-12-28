"""
Kullanıcı ayarlarını saklama modülü
"""
import json
import os
from pathlib import Path


class Storage:
    """Kullanıcı ayarlarını JSON dosyasında saklar"""
    
    def __init__(self):
        # iOS için Documents dizini
        if hasattr(os, 'environ') and 'HOME' in os.environ:
            # iOS simülatör veya gerçek cihaz
            self.storage_path = Path(os.environ['HOME']) / 'Documents' / 'creatine_settings.json'
        else:
            # Fallback
            self.storage_path = Path.home() / 'Documents' / 'creatine_settings.json'
        
        # Varsayılan ayarlar
        self.default_settings = {
            'notifications_enabled': True,
            'school_mode': False
        }
    
    def _load_settings(self):
        """Ayarları yükle"""
        try:
            if self.storage_path.exists():
                with open(self.storage_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception:
            pass
        return self.default_settings.copy()
    
    def _save_settings(self, settings):
        """Ayarları kaydet"""
        try:
            self.storage_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.storage_path, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Ayarlar kaydedilemedi: {e}")
    
    def get_notifications_enabled(self):
        """Bildirimlerin açık olup olmadığını döndür"""
        settings = self._load_settings()
        return settings.get('notifications_enabled', True)
    
    def set_notifications_enabled(self, enabled):
        """Bildirimleri aç/kapa"""
        settings = self._load_settings()
        settings['notifications_enabled'] = enabled
        self._save_settings(settings)
    
    def get_school_mode(self):
        """Okul modunun açık olup olmadığını döndür"""
        settings = self._load_settings()
        return settings.get('school_mode', False)
    
    def set_school_mode(self, enabled):
        """Okul modunu aç/kapa"""
        settings = self._load_settings()
        settings['school_mode'] = enabled
        self._save_settings(settings)

