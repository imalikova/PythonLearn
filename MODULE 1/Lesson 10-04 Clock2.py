from tkinter import *
import time


def tick_chicago():

    time1 = time.strftime('%H:%M:%S')

    clock_chicago.config(text=time1)

    clock_chicago.after(200, tick_chicago)


def tick_current():

    time2 = time.strftime('Hour: %H Minute: %M Second: %S')

    clock_current.config(text=time2)

    clock_current.after(200, tick_current)


def tick_timeleft():

    left_hour = 24-int(time.strftime("%H"))
    left_minute = 60-int(time.strftime("%M"))
    left_second = 60-int(time.strftime("%S"))

    clock_timeleft.config(text=f"{left_hour}:{left_minute}:{left_second}")

    clock_timeleft.after(200, tick_timeleft)


root = Tk()

frame_chicago = LabelFrame(text="Chicago clock")
frame_chicago.pack(fill=X)

clock_chicago = Label(frame_chicago, font=('times', 20, 'bold'), bg='green')
clock_chicago.pack(fill=X)

tick_chicago()


frame_current = LabelFrame(text="Current time")
frame_current.pack(fill=X)

clock_current = Label(frame_current, font=('times', 20, 'bold'), bg='yellow')
clock_current.pack(fill=X)

tick_current()


frame_timeleft = LabelFrame(text="Time left until the new day")
frame_timeleft.pack(fill=X)

clock_timeleft = Label(frame_timeleft, font=('times', 20, 'bold'), bg='red')
clock_timeleft.pack(fill=X)

tick_timeleft()

root.mainloop()