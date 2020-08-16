from tkinter import *
import time
import daytime


def tick():
    # get the current local time from the PC

    time2 = time.strftime('%H:%M:%S %Z(US/Central)')

    # time.tzset("US/Central")

    # if time string has changed, update it
    clock_chicago.config(text=time2)

    # calls itself every 200 milliseconds to update the time
    # display as needed could use >200 ms
    clock_chicago.after(200, tick)


def tick_2():
    # print(time.strftime('%H:%M:%S %Z(GMT+3)'))
    # print(time.strftime('%H'))

    kiev_hour=int(time.strftime("%H"))

    kiev_min_sec=time.strftime(":%M:%S %Z(GMT+3)")

    if kiev_hour >= 24:
        # kiev_hour = kiev_hour-24
        kiev_hour -= 24

    # get the kiev time

    time_3 = f"{kiev_hour}{kiev_min_sec}"

    clock_kiev.config(text=time_3)

    # calls itself every 200 milliseconds to update the time
    # display as needed could use >200 ms
    clock_kiev.after(200, tick_2)



root = Tk()

f_chicago = LabelFrame(text="Chicago time")
f_chicago.pack(side=LEFT)


clock_chicago = Label(f_chicago, font=('times', 20, 'bold'), bg='green')
clock_chicago.pack(side=LEFT)

tick()


f_kiev = LabelFrame(text="Kiev time")
f_kiev.pack(side=LEFT)

clock_kiev = Label(f_kiev, font=('times', 20, 'bold'), bg='green')
clock_kiev.pack(side=LEFT)

tick_2()


root.mainloop()