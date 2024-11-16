from tkinter import Tk,Canvas,Toplevel,Entry,Label,Button,StringVar,messagebox,Frame
from datetime import date,datetime
event_list = [
    ["New Year",'01/01/25'],
    ["Halloween",'31/10/25'],
    ["Christmas",'07/01/25']

]

def get_events():
    list_events = []
    for event in event_list:
        event_date = datetime.strptime(event[1],'%d/%m/%y').date()
        list_events.append([event[0],event_date])
    return list_events

def days_between_days(date1,date2):
    time_between = str(date1-date2)
    number_of_days = time_between.split(' ')
    return number_of_days[0]

def show_countdown():
    root = Tk()
    root.title("Countdown Calendar")
    canvas_frame = Frame(root)
    canvas_frame.pack(fill="both",expand=True)

    button_frame = Frame(root)
    button_frame.pack(pady=20)

    def refresh_display():
        c.delete("all")
        c.create_text(100,50,anchor='w',fill='orange',font = 'Arial 28 bold underline',text='My countdown Calendar')
        today = date.today()

        vertical_space = 100
        events = get_events()

        for event in events:
            even_name = event[0]
            days_until = days_between_days(event[1],today)
            display = f'It is {days_until}, days until {even_name}'
            c.create_text(100, vertical_space,anchor='w',fill='lightblue',font = 'Arial 28 bold underline',text=display)
            vertical_space+=50

    def open_add_event_window():
        add_event_window = Toplevel(root)
        add_event_window.title("add event")

        Label(add_event_window,text="Event Name: ").grid(row = 0,column=0,padx = 10, pady = 5)
        Label(add_event_window, text="event date (dd/mm/yy): ").grid(row=1,column=0,padx=10,pady=5)

        event_name_var = StringVar()
        event_date_var = StringVar()

        event_name_entry = Entry(add_event_window,textvariable=event_name_var)
        event_date_entry = Entry(add_event_window, textvariable=event_date_var)

        event_name_entry.grid(row=0,column=1,padx=10,pady=5)
        event_date_entry.grid(row=1,column=1,padx=10,pady=5)

        def add_event():
            event_name = event_name_var.get()
            event_date_str = event_date_var.get()

            try:
                event_date = datetime.strptime(event_date_str,'%d/%m/%y').date()
                event_list.append([event_name,event_date_str])
                refresh_display()
                add_event_window.destroy()
                messagebox.showinfo("Success",f" Event '{event_name}' added Successfully!")
            except ValueError:
                messagebox.showerror("Error","Date format should be in dd/mm/yy.")



        Button(add_event_window,text="Add event",command=add_event).grid(row=2,column=0,columnspan=2,pady=10)


    c = Canvas(canvas_frame,width=800,height=600,bg="black")
    c.pack()
    refresh_display()

    add_event_button = Button(button_frame,text = "Add Event",command=open_add_event_window)
    add_event_button.pack()
    root.mainloop()


def Verify_password():
    if password_var.get() == "Smart":
        login_window.destroy()
        show_countdown()
    else:
        messagebox.showerror("Error", "incorrect password")

login_window = Tk()
login_window.title("login")

Label(login_window,text="enter password").pack(pady=10)
password_var = StringVar()
password_entry = Entry(login_window,textvariable=password_var, show="*")
password_entry.pack(pady=5)
Button(login_window,text="SUbmit",command=Verify_password).pack(pady=10)
login_window.mainloop()