import re
import random
import sqlite3
from sqlite3 import Connection
from datetime import datetime

from model import Customer, Driver, Administrator, Booking

DATABASE_FILE = 'database.db'

safe_field_name_pattern = re.compile('^[a-zA-Z_]+$')


def generate_id(leading_character, id_field_name, class_name, table_name_human, statement):
    while True:
        proposed_id = f'{leading_character}{random.randrange(8999) + 1000}'
        result, _ = _generic_select_one_matching(class_name, table_name_human, statement, {id_field_name: proposed_id})
        if not result:
            return proposed_id


# INSERTS

# Statements used to insert into a given table.

def insert_customer(Customer_ID, FName, LName, Address, Email, Username, Password, Telephone_No, Payment_Method) -> str:
    return f"INSERT INTO Customers \
    (Customer_ID,FName,LName,Address,Email,Username,Password,Telephone_No,Payment_Method) \
    VALUES \
    ({Customer_ID}, {FName}, {LName}, {Address}, {Email}, {Username},{Password}, {Telephone_No}, {Payment_Method})"


def insert_driver(Driver_ID,Fname,LName,Date_of_Birth,Driver_License_Num,Expiry_Date,License_Plate,Shift_Start_Time,Shift_End_Time,Username,Password,Number_Of_Passengers) VALUES (?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    return f"INSERT INTO Drivers \
    (Driver_ID,FName,LName,Date_of_Birth,Driver_License_Num,Expiry_Date,License_Plate,Shift_Start_Time,SHift_End_Time,Username,Password,Number_of_Passengers) VALUES (?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    ({Driver_ID}, {FName}, {LName}, {Date_of_Birth}, {Driver_License_Num}, {Expiry_Date}, {Shift_Start_Time}, {Shift_End_Time}, {Username} {Password}, {Number_of_Passengers})"

def insert_administrators(Admin_ID,FName,LName,Email,Telephone_No,Username,Password) VALUES (?, ?, ?, ?, ?, ?, ?)'
    return f"INSERT INTO Administrators
    (Admin_ID,FName,LName,Email,Telephone_No,Username,Password) VALUES (?, ?, ?, ?, ?, ?, ?)'
    ({Admin_ID}, {FName}, {LName}, {Email}, {Telephone_No}, {Username}, {Password})"

def insert_bookings(Booking_ID,Customer_ID,Driver_ID,pickup_address,pickup_time,pickup_date,drop_off_address,Admin_ID,booking_date,cost_of_trip,paid,date_cancelled) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    return f"INTER INTO Bookings
    (Booking_ID,Customer_ID,Driver_ID,pickup_address,pickup_time,pickup_date,drop_off_address,Admin_ID,booking_date,cost_of_trip,paid,date_cancelled) VAlLUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'    
    ({Booking_ID}, {Customer_ID}, {Driver_ID}, {pickup_address}, {pickup_time}, {pickup_date}, {drop_off_address}, {Admin_ID}, {booking_date}, {cost_of_trip}, {paid}, {date_cancelled})"

# A generic insert method that can be called for any table.
# table_name_human: the human readable name of the table
# statement: the insert statement for this table
# data: the model instance to be inserted
def crud_insert(data: str):
    conn: Connection or None = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        conn.execute(data)
        conn.commit()
    except Exception as e:
        return e
    finally:
        conn.close()


@staticmethod
def _insert_customer(customer) -> None:
    """IDK why yall wrote it this way - but pass customer data in to this function"""
    crud_insert(data=insert_customer(customer))


# A method that calls _generic_insert with the params for Drivers
def _insert_driver(driver):
    return  # TODO


# A method that calls _generic_insert with the params for Administrators
def _insert_administrator(administrator):
    return  # TODO


# A method that calls _generic_insert with the params for Bookings
def _insert_booking(booking):
    return  # TODO


# SELECTS

# Statements used to select from a given table.

customers_select_statement = 'SELECT Customer_ID,FName,LName,Address,Email,Username,Password,Telephone_No,Payment_Method FROM Customers'

drivers_select_statement = 'SELECT Driver_ID,Fname,LName,Date_of_Birth,Driver_License_Num,Expiry_Date,License_Plate,Shift_Start_Time,Shift_End_Time,Username,Password,Number_Of_Passengers FROM Driver'

administrators_select_statement = 'SELECT Admin_ID,FName,LName,Email,Telephone_No,Username,Password FROM Administrator'

bookings_select_statement = 'SELECT Booking_ID,Customer_ID,Driver_ID,pickup_address,pickup_time,pickup_date,drop_off_address,Admin_ID,booking_date,cost_of_trip,paid,date_cancelled FROM Booking'


# A generic select method that can be called for any table. It returns all results.
# class_name: the class to instantiate when returning
# table_name_human: the human readable name of the table
# statement: the select statement for this table
# data: the fields and values to filter by
def _generic_select_all(class_name, table_name_human, statement, data=None):
    try:
        conn = sqlite3.connect(DATABASE_FILE)

        try:
            if data and (expected_params := statement.count('?')):
                if expected_params != len(data):
                    return False, "Invalid number of parameters for query."
                rows = [class_name.from_row(row) for row in conn.execute(statement, data)]
            else:
                rows = [class_name.from_row(row) for row in conn.execute(statement)]
        except:
            return False, f'Error while reading data from {table_name_human}.'

    except:
        return False, 'Could not create database connection.'
    finally:
        if conn:
            conn.close()

    return rows, f'Successfully read data from {table_name_human}.'


# A generic select method that can be called for any table when there is a need to filter the results.
# This modifies a generic select statement to contain the WHERE clauses for the provided filters in data.
# This returns the all results that match all the filters.
# class_name: the class to instantiate when returning
# table_name_human: the human readable name of the table
# statement: the select statement for this table
# data: the fields and values to filter by
def _generic_select_all_matching(class_name, table_name_human, statement, data):
    filters = []
    values = []

    for field_name, field_value in data.items():
        if not re.match(safe_field_name_pattern, field_name):
            return False, f'Provided field name ({field_name}) is invalid.'
        filters.append(f'{field_name} = ?')
        values.append(field_value)

    new_statement = f'{statement} WHERE '
    new_statement += ' AND '.join(filters)

    return _generic_select_all(class_name, table_name_human, new_statement, values)


# A generic select method that can be called for any table when there is a need to filter the results.
# This modifies a generic select statement to contain the WHERE clauses for the provided filters in data.
# This returns the first value that matches all the filters.
# class_name: the class to instantiate when returning
# table_name_human: the human readable name of the table
# statement: the select statement for this table
# data: the fields and values to filter by
def _generic_select_one_matching(class_name, table_name_human, statement, data):
    result, message = _generic_select_all_matching(class_name, table_name_human, statement, data)
    if isinstance(result, list):
        if result:
            return result[0], 'Matching entity found.'
        else:
            return None, 'No matching entities found.'
    else:
        return result, message


# UPDATES

# A generic update method that can be called for any method.
# This builds an update statement from the provided information.
# table_name_actual: the actual table name to update as defined in the database
# table_name_human: the human readable name of the table
# update_data: the fields and values to update
# query_data: the fields and values to filter by
def _generic_update_all_matching(table_name_human, table_name_actual, update_data, query_data=None):
    update_fields = []
    query_fields = []
    values = []

    for field_name, field_value in update_data.items():
        if not re.match(safe_field_name_pattern, field_name):
            return False, f'Provided field name ({field_name}) is invalid.'
        update_fields.append(f'{field_name} = ?')
        values.append(field_value)

    statement = f'UPDATE {table_name_actual} SET ' + ', '.join(update_fields)

    if query_data:
        for field_name, field_value in query_data.items():
            if not re.match(safe_field_name_pattern, field_name):
                return False, f'Provided field name ({field_name}) is invalid.'
            update_fields.append(f'{field_name} = ?')
            values.append(field_value)

        statement = f'{statement} WHERE '
        statement += ' AND '.join(query_fields)

    try:
        conn = sqlite3.connect(DATABASE_FILE)

        try:
            conn.execute(statement, values)
        except:
            return False, f'Error while updating data in {table_name_human}.'

    except:
        return False, 'Could not create database connection.'
    finally:
        if conn:
            conn.commit()
            conn.close()

    return True, f'Successfully update data in {table_name_human}.'


# Login

# A method that returns a customer from the database if one exists with this username and password.
# username: the username of the customer trying to login
# password: the password of the customer trying to login
def login_as_customer(username, password):
    return _generic_select_one_matching(Customer, 'customer', customers_select_statement,
                                        {'Username': username, 'Password': password})


# A method that returns a driver from the database if one exists with this username and password.
# username: the username of the driver trying to login
# password: the password of the driver trying to login
def login_as_driver(username, password):
    return _generic_select_one_matching(Driver, 'driver', drivers_select_statement,
                                        {'Username': username, 'Password': password})


# A method that returns a administrator from the database if one exists with this username and password.
# username: the username of the administrator trying to login
# password: the password of the administrator trying to login
def login_as_administrator(username, password):
    return _generic_select_one_matching(Administrator, 'administrator', administrators_select_statement,
                                        {'Username': username, 'Password': password})


# A method that registers a new customer given their information.
# params: their information
def register_as_customer(email, first_name, last_name, address, username, password, telephone_number, payment_method):
    result, _ = _generic_select_one_matching(Customer, 'customer', customers_select_statement, {'Username': username})
    if result:
        return False, 'Account with that username already exists!'

    generated_id = generate_id('S', 'Customer_ID', Customer, 'customer', customers_select_statement)

    new_cus = Customer(generated_id, first_name, last_name, address, email, username, password, telephone_number,
                       payment_method)
    return _insert_customer(new_cus)


def select_booking_customer(customer_id):
    return _generic_select_all_matching(Booking, 'booking', bookings_select_statement, {'Customer_ID': customer_id})


# A method that creates a new booking with the minimal amount of information.
# At this time, values such as the DriverID and AdminID are not known.
# Fields such as the booking date are set automatically.
def create_booking(customer_id, pickup_address, pickup_datetime, drop_off_address):
    cost_of_trip = 10

    generated_id = generate_id('B', 'Booking_ID', Booking, 'booking', bookings_select_statement)
    new_booking = Booking(generated_id, customer_id, None, pickup_address, pickup_datetime, drop_off_address, None,
                          datetime.now(), cost_of_trip, False, None)
    return _insert_booking(new_booking)


# A method that cancels a booking
# booking_id: the id of the booking to be approved
def cancel_booking(booking_id):
    result, _ = _generic_select_one_matching(Booking, 'booking', bookings_select_statement, {'Booking_ID': booking_id})
    if not result:
        return False, 'No such booking exists!'
    return _generic_update_all_matching('booking', 'Bookings', {'date_cancelled': datetime.now().strftime(r'%y-%m-%d')},
                                        {'Booking_ID': booking_id})


# A method that approves a booking
# booking_id: the id of the booking to be approved
# administrator_id: the id of the administrator who approved the booking
# driver_id: the id of the driver assigned to the booking
def approve_booking(booking_id, administrator_id, driver_id):
    result, _ = _generic_select_one_matching(Booking, 'booking', bookings_select_statement, {'Booking_ID': booking_id})
    if not result:
        return False, 'No such booking exists!'

    result, _ = _generic_select_one_matching(Administrator, 'administrator', administrators_select_statement,
                                             {'Admin_ID': administrator_id})
    if not result:
        return False, 'No such admin exists!'

    result, _ = _generic_select_one_matching(Driver, 'driver', drivers_select_statement, {'Driver_ID': driver_id})
    if not result:
        return False, 'No such driver exists!'

    return _generic_update_all_matching('booking', 'Bookings', {'Driver_ID': driver_id, 'Admin_ID': administrator_id},
                                        {'Booking_ID': booking_id})
