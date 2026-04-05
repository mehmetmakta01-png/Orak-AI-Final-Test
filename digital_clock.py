import datetime
import pytz
import tkinter as tk

class DigitalClock:
    def __init__(self, master):
        self.master = master
        master.title("Digital Clock")
        self.label = tk.Label(master, font=('calibri', 40, 'bold'), bg='black', fg='white')
        self.label.pack(pady=20)
        self.update_time()

    def update_time(self):
        now = datetime.datetime.now()
        time_zones = {
            'Istanbul': 'Europe/Istanbul',
            'New York': 'America/New_York',
            'London': 'Europe/London',
            'Tokyo': 'Asia/Tokyo',
            'Sydney': 'Australia/Sydney'
        }
        time_strings = []
        for city, tz in time_zones.items():
            local_time = datetime.datetime.now(pytz.timezone(tz))
            time_strings.append(f'{city}: {local_time.strftime('%Y-%m-%d %H:%M:%S')}')
        self.label.config(text='\n'.join(time_strings))
        self.master.after(1000, self.update_time)

if __name__ == '__main__':
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()