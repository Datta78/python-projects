# Simple WhatsApp Message Sender - Dattatray Bhosale
# For Job Portfolio (using pywhatkit)

import pywhatkit
from datetime import datetime

def send_whatsapp_message():
    phone = input("Enter phone number with country code (e.g. +918767664008): ")
    message = input("Enter message: ")
    
    try:
        pywhatkit.sendwhatmsg_instantly(phone, message)
        print("✅ Message sent successfully!")
    except Exception as e:
        print("❌ Error:", e)

def schedule_message():
    phone = input("Enter phone number with country code: ")
    message = input("Enter message: ")
    hour = int(input("Enter hour (24-hour format): "))
    minute = int(input("Enter minute: "))
    
    try:
        pywhatkit.sendwhatmsg(phone, message, hour, minute)
        print(f"✅ Message scheduled for {hour}:{minute}")
    except Exception as e:
        print("❌ Error:", e)

def main():
    print("\n=== WhatsApp Message Sender ===")
    print("1. Send Message Now")
    print("2. Schedule Message")
    print("3. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        send_whatsapp_message()
    elif choice == "2":
        schedule_message()
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
