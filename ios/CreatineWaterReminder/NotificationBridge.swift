//
// NotificationBridge.swift
// iOS native notification bridge for Creatine Water Reminder
//

import Foundation
import UserNotifications

@objc(NotificationBridge)
class NotificationBridge: NSObject {
    
    static let shared = NotificationBridge()
    
    private let notificationCenter = UNUserNotificationCenter.current()
    private let reminderIdentifier = "creatine_water_reminder"
    
    override init() {
        super.init()
        requestAuthorization()
    }
    
    // MARK: - Authorization
    
    @objc func requestAuthorization() {
        let options: UNAuthorizationOptions = [.alert, .sound, .badge]
        notificationCenter.requestAuthorization(options: options) { granted, error in
            if let error = error {
                print("Notification authorization error: \(error)")
            } else if granted {
                print("Notification authorization granted")
            } else {
                print("Notification authorization denied")
            }
        }
    }
    
    // MARK: - Notification Management
    
    @objc func startNotifications() {
        // Önce mevcut bildirimleri temizle
        stopNotifications()
        
        // Bildirim içeriği
        let content = UNMutableNotificationContent()
        content.title = "Su İçme Hatırlatıcısı"
        content.body = "Creatine alıyorsun, su içmeyi unutma 💧"
        content.sound = .default
        content.badge = 1
        
        // Her 2 saatte bir tekrarla (7200 saniye)
        let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 7200, repeats: true)
        
        // Bildirim isteği
        let request = UNNotificationRequest(
            identifier: reminderIdentifier,
            content: content,
            trigger: trigger
        )
        
        // Bildirimi ekle
        notificationCenter.add(request) { error in
            if let error = error {
                print("Error adding notification: \(error)")
            } else {
                print("Notifications started (every 2 hours)")
            }
        }
    }
    
    @objc func stopNotifications() {
        // Bekleyen bildirimleri iptal et
        notificationCenter.removePendingNotificationRequests(withIdentifiers: [reminderIdentifier])
        
        // Teslim edilmiş bildirimleri temizle
        notificationCenter.removeDeliveredNotifications(withIdentifiers: [reminderIdentifier])
        
        print("Notifications stopped")
    }
    
    @objc func pauseNotifications() {
        stopNotifications()
        print("Notifications paused")
    }
    
    @objc func resumeNotifications() {
        startNotifications()
        print("Notifications resumed")
    }
}

