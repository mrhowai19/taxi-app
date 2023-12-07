import tkinter as tk
from tkinter import messagebox
import sqlite3
import crud
from model import Customer, Driver, Administrator, Booking
from create_tables import create_tables

WINDOW_SIZE = '1350x700'
GRID_SIZE: int = 9
FONT = 'Comic Sans MS'

userID = ""  # global variable


# define a global variable for the userID (e.g. customer_ID, driver_ID, or admin_ID)
# this userID would hold the value from the database of the ID from the examples above


class DB:  # creating a class DB with functions to perform various operations on the database.

    def __init__(self):  # constructor functor for class DB.
        # connects to a database called database.db
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor(
        )  # creating a cursor to navigate through the database
        self.conn.commit()  # commit functions saves everything to the database

    def __del__(self):  # destructor created for the class DB
        self.conn.close()  # closes the connection with the database


db = DB()


def _select_bookings_customer(user_class, crud_method, screen_move_method):
    # Execute function is to perform the SQL operations. Here, it produces all the rows from the table.
    #self.cur.execute("SELECT * FROM Booking WHERE Customer_ID= " % userID)
    # fetching all the rows one by one from the table and storing it in list rows
    #rows = self.cur.fetchall()
    return 
    result, message = crud_method(userID)

    if isinstance(result, user_class):
        return result
    
def _login_common(user_class, crud_method, screen_move_method):
    user_name = username_field.get()
    if not user_name:
        messagebox.showerror('Invalid Information', 'Please enter a username!')
        return

    pass_word = password_field.get()
    if not pass_word:
        messagebox.showerror('Invalid Information', 'Please enter a password!')
        return

    result, message = crud_method(user_name, pass_word)

    if isinstance(result, user_class):
        # messagebox.showinfo('Success', 'Logged in successfully.')
        global userID
        if user_class == Customer:
            userID = result.customer_id  # assign the userID global variable the value of customerID from the query result/function above.
        elif user_class == Driver:
            userID = result.driver_id  # assign the userID global variable the value of driverID from the query result/function above.
        elif user_class == Administrator:
            userID = result.admin_id  # assign the userID global variable the value of adminID from the query result/function above.
        # print (userID)
        # exit()
        screen_move_method()
    elif result is None:
        messagebox.showerror('Invalid Info', 'Bad username/password combination!')
    else:
        messagebox.showerror('Unknown Error', message)


def login_as_customer():
    _login_common(Customer, crud.login_as_customer, move_login_to_customer)


def login_as_driver():
    _login_common(Driver, crud.login_as_driver, move_login_to_driver)


def login_as_administrator():
    _login_common(Administrator, crud.login_as_administrator,
                  move_login_to_administrator)


def register_as_customer():
    values = []

    for fname, field in zip(registration_values, registration_fields):
        value = field.get()
        if not value:
            messagebox.showerror('Invalid Information', f'Please enter a {fname}!')
            return
        values.append(value)

    result, message = crud.register_as_customer(*values)

    if result:
        messagebox.showinfo('Success', 'Account created successfully.')
        move_registration_to_login()
    elif 'exists' in message:
        messagebox.showerror('Invalid Info', 'Account already exists!')
    else:
        messagebox.showerror('Unknown Error', message)


def make_booking(add_booking_values, add_booking_fields):
    values = []

    for NAME, field in zip(add_booking_values, add_booking_fields):
        value = field.get()
        if not value:
            messagebox.showerror('Invalid Information')
            return
        values.append(value)

    result, message = crud.create_booking(*values)

    if result:
        messagebox.showinfo('Success', 'Booking created successfully.')
        customer_add_booking_screen.destroy()
    elif 'exists' in message:
        messagebox.showerror('Invalid Info', 'Booking already exists!')
    else:
        messagebox.showerror('Unknown Error', message)


def select_bookings_customer():
    _select_bookings_customer(Booking, crud.bookings_select_statement,
                              customer_view_bookings_screen)


# DEFINE SCREEN

login_screen = tk.Tk()
# Create a variable name for an image
logo_img = tk.PhotoImage(file="1.png")
logo_img = logo_img.subsample(3)
login_screen.title('Cts taxi')  # Giving a title to
login_screen.geometry(WINDOW_SIZE)
login_screen.configure(bg="lime")
# Create a label widget using the image "logo_img"
logo_login_screen = tk.Label(login_screen, bg="lime", image=logo_img)
logo_login_screen.place(rely=0.0, relx=0.0, x=0, y=0, anchor="nw")

login_screen.rowconfigure([i for i in range(GRID_SIZE)], minsize=50)
login_screen.columnconfigure([i for i in range(GRID_SIZE)], minsize=50)
for i in range(GRID_SIZE):
    login_screen.columnconfigure(i, weight=1)
    login_screen.rowconfigure(i, weight=1)

registration_screen = tk.Toplevel()
registration_screen.title('CTS drop off')
registration_screen.geometry(WINDOW_SIZE)
registration_screen.configure(bg="green")
logo_registration_screen = tk.Label(registration_screen,
                                    bg="grey",
                                    image=logo_img)
logo_registration_screen.place(
    rely=0.0,
    relx=0.0,
    x=0,
    y=0,
)

registration_screen.rowconfigure([i for i in range(GRID_SIZE)], minsize=50)
registration_screen.columnconfigure([i for i in range(GRID_SIZE)], minsize=50)
for i in range(GRID_SIZE):
    registration_screen.columnconfigure(i, weight=1)
    registration_screen.rowconfigure(i, weight=1)

registration_screen.withdraw()

customer_screen = tk.Toplevel()
customer_screen.title('CTS tax - Customer')
customer_screen.geometry(WINDOW_SIZE)
customer_screen.configure(bg="white")
registration_screen.configure(bg="grey")
logo_customer_screen = tk.Label(customer_screen, bg="grey", image=logo_img)
logo_customer_screen.place(rely=0.0, relx=0.0, x=0, y=0, anchor="nw")

customer_screen.rowconfigure([i for i in range(GRID_SIZE)], minsize=50)
customer_screen.columnconfigure([i for i in range(GRID_SIZE)], minsize=50)
for i in range(GRID_SIZE):
    customer_screen.columnconfigure(i, weight=1)
    customer_screen.rowconfigure(i, weight=1)

customer_screen.withdraw()

driver_screen = tk.Toplevel()
driver_screen.title('CTS tax - Driver')
driver_screen.geometry(WINDOW_SIZE)
driver_screen.configure(bg="white")
logo_driver_screen = tk.Label(driver_screen, bg="white", image=logo_img)
logo_driver_screen.place(rely=0.0, relx=0.0, x=0, y=0, anchor="nw")

driver_screen.rowconfigure([i for i in range(GRID_SIZE)], minsize=50)
driver_screen.columnconfigure([i for i in range(GRID_SIZE)], minsize=50)
for i in range(GRID_SIZE):
    driver_screen.columnconfigure(i, weight=1)
    driver_screen.rowconfigure(i, weight=1)

driver_screen.withdraw()

administrator_screen = tk.Toplevel()
administrator_screen.title('Cts tax - Administrator')
administrator_screen.geometry(WINDOW_SIZE)
administrator_screen.configure(bg="white")
logo_administrator_screen = tk.Label(administrator_screen,
                                     bg="white",
                                     image=logo_img)
logo_administrator_screen.place(rely=0.0, relx=0.0, x=0, y=0, anchor="nw")

administrator_screen.rowconfigure([i for i in range(GRID_SIZE)], minsize=50)
administrator_screen.columnconfigure([i for i in range(GRID_SIZE)], minsize=50)
for i in range(GRID_SIZE):
    administrator_screen.columnconfigure(i, weight=1)
    administrator_screen.rowconfigure(i, weight=1)

administrator_screen.withdraw()


def customer_add_booking_screen():
    customer_make_booking_screen = tk.Tk()
    customer_make_booking_screen.title('CTS tax - Customer Bookings')
    customer_make_booking_screen.geometry('650x450')
    customer_make_booking_screen.configure(bg="gold")

    add_booking_values = [
        'Pickup Address',
        'Destination',
        'Date of Trip',
        'Pickup Time',
    ]

    add_booking_labels = []
    add_booking_fields = []

    for INDEX, NAME in enumerate(add_booking_values):
        bk_label = tk.Label(customer_make_booking_screen,
                            text=f'{NAME}:',
                            bg="gold",
                            font=(FONT, 30))
        bk_label.grid(row=INDEX, column=3, sticky='E')
        add_booking_labels.append(label)

        bk_entry = tk.Entry(customer_make_booking_screen, font=(FONT, 20))
        bk_entry.grid(row=INDEX, column=4)
        add_booking_fields.append(entry)

    customer_add_booking_submit_button = tk.Button(customer_make_booking_screen,
                                                   text='Submit',
                                                   bg="black",
                                                   fg="gold",
                                                   command=make_booking,
                                                   font=(FONT, 20),
                                                   height=1,
                                                   width=20)
    customer_add_booking_submit_button.grid(column=4, pady=5)

    def validate_booking_info(addBookingWindow):
        booking_entry = bk_entry.get()

        if booking_entry == "":
            messagebox.showinfo("Warning!", "Enter a from address")
        else:
            messagebox.showinfo("Successful Registration",
                                "Thank you for your booking")
            addBookingWindow.destroy()

    customer_make_booking_screen.mainloop()


def customer_view_bookings_screen():
    customer_view_booking_screen = tk.Tk()
    customer_view_booking_screen.title('CTS tax - Customer Bookings')
    customer_view_booking_screen.geometry(WINDOW_SIZE)
    customer_view_booking_screen.configure(bg="gold")

    select_bookings_customer()

    customer_view_booking_screen.rowconfigure([i for i in range(GRID_SIZE)],
                                              minsize=50)
    customer_view_booking_screen.columnconfigure([i for i in range(GRID_SIZE)],
                                                 minsize=50)
    for i in range(GRID_SIZE):
        customer_view_booking_screen.columnconfigure(i, weight=1)
        customer_view_booking_screen.rowconfigure(i, weight=1)

    customer_cancel_booking_btn = tk.Button(customer_view_booking_screen,
                                            text='Cancel Booking',
                                            bg="black",
                                            fg="gold",
                                            font=(FONT, 20),
                                            height=1,
                                            width=20)
    customer_cancel_booking_btn.grid(column=4, row=1, sticky="EW")

    # creating the list space to display all the rows of the table
    list1 = tk.Listbox(customer_view_booking_screen, height=45, width=150)
    list1.grid(row=1, column=0, rowspan=6, columnspan=2)  # determining the size

    # creating a scrollbar for the window to scroll through the list entries
    sb1 = tk.Scrollbar(customer_view_booking_screen)
    sb1.grid(row=1, column=2, rowspan=6)

    # configuring the scroll function for the scrollbar object sb1
    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    list1.bind('<<ListboxSelect>>', select_bookings_customer)

    # customer_view_bookings_cancel_booking_btn

    customer_view_booking_screen.mainloop()


def driver_view_bookings_screen():
    driver_view_booking_screen = tk.Tk()
    driver_view_booking_screen.title('CTS tax - Driver Bookings')
    driver_view_booking_screen.geometry(WINDOW_SIZE)
    driver_view_booking_screen.configure(bg="gold")

    driver_view_booking_screen.rowconfigure([i for i in range(GRID_SIZE)],
                                            minsize=50)
    driver_view_booking_screen.columnconfigure([i for i in range(GRID_SIZE)],
                                               minsize=50)
    for i in range(GRID_SIZE):
        driver_view_booking_screen.columnconfigure(i, weight=1)
        driver_view_booking_screen.rowconfigure(i, weight=1)

    # creating the list space to display all the rows of the table
    list2 = tk.Listbox(driver_view_booking_screen, height=45, width=150)
    list2.grid(row=1, column=0, rowspan=6, columnspan=2)  # determining the size

    # creating a scrollbar for the window to scroll through the list entries
    sb2 = tk.Scrollbar(driver_view_booking_screen)
    sb2.grid(row=1, column=2, rowspan=6)

    # configuring the scroll function for the scrollbar object sb2
    list2.configure(yscrollcommand=sb2.set)
    sb2.configure(command=list2.yview)


def admin_view_bookings_screen():
    admin_view_booking_screen = tk.Tk()
    admin_view_booking_screen.title('CTS tax - Customer Bookings')
    admin_view_booking_screen.geometry(WINDOW_SIZE)
    admin_view_booking_screen.configure(bg="white")

    admin_view_booking_screen.rowconfigure([i for i in range(GRID_SIZE)],
                                           minsize=50)
    admin_view_booking_screen.columnconfigure([i for i in range(GRID_SIZE)],
                                              minsize=50)
    for i in range(GRID_SIZE):
        admin_view_booking_screen.columnconfigure(i, weight=1)
        admin_view_booking_screen.rowconfigure(i, weight=1)

    admin_approve_booking_btn = tk.Button(admin_view_booking_screen,
                                          text='Approve Booking',
                                          bg="white",
                                          fg="lime",
                                          font=(FONT, 20),
                                          height=1,
                                          width=20)
    admin_approve_booking_btn.grid(column=4, row=1, sticky="EW")

    # creating the list space to display all the rows of the table
    list3 = tk.Listbox(admin_view_booking_screen, height=45, width=150)
    list3.grid(row=1, column=0, rowspan=6, columnspan=2)  # determining the size

    # creating a scrollbar for the window to scroll through the list entries
    sb3 = tk.Scrollbar(admin_view_booking_screen)
    sb3.grid(row=1, column=2, rowspan=6)

    # configuring the scroll function for the scrollbar object sb3
    list3.configure(yscrollcommand=sb3.set)
    sb3.configure(command=list3.yview)


# MOVEMENT FUNCTIONS


def move_login_to_registration():
    login_screen.withdraw()
    registration_screen.deiconify()


def move_login_to_customer():
    login_screen.withdraw()
    customer_screen.deiconify()


def move_login_to_driver():
    login_screen.withdraw()
    driver_screen.deiconify()


def move_login_to_administrator():
    login_screen.withdraw()
    administrator_screen.deiconify()


def move_registration_to_login():
    registration_screen.withdraw()
    login_screen.deiconify()


# Hello I am a ghost
def move_customer_to_login():
    customer_screen.withdraw()
    login_screen.deiconify()


def move_driver_to_login():
    driver_screen.withdraw()


login_screen.deiconify()


def move_administrator_to_login():
    administrator_screen.withdraw()


login_screen.deiconify()

# SETUP LOGIN SCREEN

greeting = tk.Label(login_screen,
                    text='Welcome to CTS DROPS!',
                    bg="white",
                    font=(FONT, 30))
greeting.grid(column=3, row=0, columnspan=3)

username_label = tk.Label(login_screen,
                          text='Username:',
                          bg="white",
                          font=(FONT, 30))
username_label.grid(column=4, row=1)

username = tk.StringVar()
username_field = tk.Entry(login_screen, textvariable=username, font=(FONT, 20))
username_field.grid(column=4, row=2)

password_label = tk.Label(login_screen,
                          bg="white",
                          text='Password:',
                          font=(FONT, 30))
password_label.grid(column=4, row=3)

password = tk.StringVar()
password_field = tk.Entry(login_screen, textvariable=password, font=(FONT, 20))
password_field.grid(column=4, row=4)

password_label = tk.Label(login_screen, text='', bg="lime", font=(FONT, 30))
password_label.grid(column=5, row=4)

customer_login_button = tk.Button(login_screen,
                                  text='Login as Customer',
                                  bg="black",
                                  fg="lime",
                                  command=login_as_customer,
                                  font=(FONT, 20),
                                  height=1,
                                  width=20)
customer_login_button.grid(column=4, row=7)

driver_login_button = tk.Button(login_screen,
                                text='Login as Driver',
                                bg="black",
                                fg="lime",
                                command=login_as_driver,
                                font=(FONT, 20),
                                height=1,
                                width=20)
driver_login_button.grid(column=3, row=7)

administrator_login_button = tk.Button(login_screen,
                                       text='Login as Administrator',
                                       bg="black",
                                       fg="lime",
                                       command=login_as_administrator,
                                       font=(FONT, 20),
                                       height=1,
                                       width=20)
administrator_login_button.grid(column=5, row=7)

show_registration_button = tk.Button(login_screen,
                                     text='Register as Customer',
                                     # Shorten this to New Customer? might be less text
                                     bg="black",
                                     fg="lime",
                                     command=move_login_to_registration,
                                     font=(FONT, 20),
                                     height=1,
                                     width=20)
show_registration_button.grid(column=4, row=8)

registration_values = (
    'Email',
    'First Name',
    'Last Name',
    'Address',
    'Username',
    'Password',
    'Phone Number',
    'Payment Method:',
)

registration_labels = []  # :O this is smart
registration_fields = []

for index, name in enumerate(registration_values):
    label = tk.Label(registration_screen, text=f'{name}:', bg="grey", font=(FONT, 25, "bold",))
    label.grid(row=index, column=3, sticky='E')
    registration_labels.append(label)

    entry = tk.Entry(registration_screen, font=(FONT, 20))
    entry.grid(row=index, column=4)
    registration_fields.append(entry)

register_as_customer_button = tk.Button(registration_screen, text='Register as Customer', bg="black", fg="lime",
                                        command=register_as_customer, font=(FONT, 20), height=1, width=20)
register_as_customer_button.grid(column=4, row=8)

registration_back_button = tk.Button(registration_screen, text='Back', bg="black", fg="lime",
                                     command=move_registration_to_login, font=(FONT, 20), height=1, width=20)
registration_back_button.grid(column=8, row=8)

# SETUP DRIVER SCREEN

driver_view_bookings_button = tk.Button(driver_screen,
                                        text="View Assigned Bookings",
                                        bg="black",
                                        fg="lime",
                                        command=driver_view_bookings_screen,
                                        font=(FONT, 20),
                                        height=1,
                                        width=20)
driver_view_bookings_button.grid(column=3, row=3, columnspan=3, sticky="nsew")

driver_logout_button = tk.Button(driver_screen,
                                 text="Logout",
                                 bg="black",
                                 fg="lime",
                                 command=move_driver_to_login,
                                 font=(FONT, 20),
                                 height=1,
                                 width=20)
driver_logout_button.grid(column=3, row=5, columnspan=3, sticky="nsew")

# SETUP CUSTOMER SCREEN

customer_greeting = tk.Label(customer_screen,
                             text="Welcome!",
                             bg="white",
                             font=(FONT, 30))
customer_greeting.grid(column=3, row=0, columnspan=3, rowspan=2)

create_booking_button = tk.Button(customer_screen,
                                  text="Make a Booking",
                                  bg="black",
                                  fg="lime",
                                  command=customer_add_booking_screen,
                                  font=(FONT, 20),
                                  height=1,
                                  width=20)
create_booking_button.grid(column=3, row=2, columnspan=3, sticky="nsew")

customer_view_bookings_button = tk.Button(
    customer_screen,
    text="View all Bookings",
    bg="black",
    fg="lime",
    command=customer_view_bookings_screen,
    font=(FONT, 20),
    height=1,
    width=20)
customer_view_bookings_button.grid(column=3,
                                   row=4,
                                   columnspan=3,
                                   sticky="nsew")

customer_logout_button = tk.Button(customer_screen,
                                   text="Logout",
                                   bg="black",
                                   fg="lime",
                                   command=move_customer_to_login,
                                   font=(FONT, 20),
                                   height=1,
                                   width=20)
customer_logout_button.grid(column=3, row=6, columnspan=3, sticky="nsew")

# SETUP ADMINISTRATOR SCREEN

admin_view_bookings_button = tk.Button(administrator_screen,
                                       text="View Bookings",
                                       bg="black",
                                       fg="lime",
                                       command=admin_view_bookings_screen,
                                       font=(FONT, 20),
                                       height=1,
                                       width=20)
admin_view_bookings_button.grid(column=3, row=3, columnspan=3, sticky="nsew")

admin_logout_button = tk.Button(administrator_screen,
                                text="Logout",
                                bg="black",
                                fg="lime",
                                command=move_administrator_to_login,
                                font=(FONT, 20),
                                height=1,
                                width=20)
admin_logout_button.grid(column=3, row=5, columnspan=3, sticky="nsew")

# LAUNCH
create_tables()
login_screen.mainloop()
