import pywhatkit as kit
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to send the WhatsApp message
def send_whatsapp_message():
    phone = phone_entry.get()
    message = message_entry.get("1.0", tk.END)
    hour = int(hour_entry.get())
    minute = int(minute_entry.get())

    # Validate phone number and time
    if not phone or not message.strip():
        messagebox.showerror("Error", "Please fill all fields.")
        return
    
    current_time = datetime.now()
    if hour < current_time.hour or (hour == current_time.hour and minute <= current_time.minute):
        messagebox.showerror("Error", "Time cannot be in the past.")
        return

    # Send the message
    try:
        kit.sendwhatmsg(phone, message.strip(), hour, minute)
        messagebox.showinfo("Success", "Message scheduled successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send message: {e}")

# GUI setup
app = tk.Tk()
app.title("WhatsApp Message Scheduler")

# Phone number input
tk.Label(app, text="Phone Number (with country code):").pack(pady=5)
phone_entry = tk.Entry(app, width=30)
phone_entry.pack(pady=5)

# Message input
tk.Label(app, text="Message:").pack(pady=5)
message_entry = tk.Text(app, height=5, width=40)
message_entry.pack(pady=5)

# Time input
tk.Label(app, text="Schedule Time (24-hour format):").pack(pady=5)
time_frame = tk.Frame(app)
time_frame.pack(pady=5)

tk.Label(time_frame, text="Hour:").pack(side=tk.LEFT)
hour_entry = tk.Entry(time_frame, width=5)
hour_entry.pack(side=tk.LEFT)

tk.Label(time_frame, text="Minute:").pack(side=tk.LEFT)
minute_entry = tk.Entry(time_frame, width=5)
minute_entry.pack(side=tk.LEFT)

# Send button
send_button = tk.Button(app, text="Send Message", command=send_whatsapp_message)
send_button.pack(pady=20)

app.mainloop()