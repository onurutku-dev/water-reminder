"""
Kullanıcı ayarlarını saklama modülü
"""
import json
import os
from pathlib import Path

# #region agent log
def _debug_log(location, message, hypothesis_id, data=None):
    try:
        if hasattr(os, 'environ') and 'HOME' in os.environ:
            log_path = os.path.join(os.environ['HOME'], 'Documents', 'debug.log')
        else:
            try:
                log_path = os.path.join(os.path.expanduser('~'), 'Documents', 'debug.log')
            except:
                log_path = 'debug.log'
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps({"sessionId":"debug-session","runId":"run1","hypothesisId":hypothesis_id,"location":location,"message":message,"data":data or {},"timestamp":int(__import__('time').time()*1000)})+"\n")
    except Exception as e:
        print(f"DEBUG LOG ERROR: {e}")
# #endregion


class Storage:
    """Kullanıcı ayarlarını JSON dosyasında saklar"""
    
    def __init__(self):
        # #region agent log
        try:
            _debug_log("storage.py:13", "Storage.__init__() called", "C")
        except: pass
        # #endregion
        # iOS için Documents dizini
        try:
            if hasattr(os, 'environ') and 'HOME' in os.environ:
                # iOS simülatör veya gerçek cihaz
                self.storage_path = Path(os.environ['HOME']) / 'Documents' / 'creatine_settings.json'
                # #region agent log
                try:
                    _debug_log("storage.py:19", "Using HOME env", "C", {"path":str(self.storage_path)})
                except: pass
                # #endregion
            else:
                # Fallback
                self.storage_path = Path.home() / 'Documents' / 'creatine_settings.json'
                # #region agent log
                try:
                    _debug_log("storage.py:24", "Using Path.home()", "C", {"path":str(self.storage_path)})
                except: pass
                # #endregion
        except Exception as e:
            # #region agent log
            try:
                _debug_log("storage.py:28", "Path creation failed", "C", {"error":str(e),"traceback":traceback.format_exc()})
            except: pass
            # #endregion
            raise
        
        # Varsayılan ayarlar
        self.default_settings = {
            'notifications_enabled': True,
            'school_mode': False
        }
        # #region agent log
        try:
            _debug_log("storage.py:35", "Storage.__init__() completed", "C", {})
        except: pass
        # #endregion
    
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

