import os, os.path
import sqlite3

from settings import DATABASE_FILE

from crud import (
    customers_insert_statement, 
    drivers_insert_statement, 
    administrators_insert_statement, 
    bookings_insert_statement
)

# CREATE STATEMENTS
customer_create_statement = '''CREATE TABLE Customers 
        (Customer_ID Varchar(10) PRIMARY KEY NOT NULL,
        FName Varchar(20) NOT NULL,
        LName Varchar(20) NOT NULL,
        Address Varchar(50) NOT NULL,
        Email Varchar(20) NOT NULL,
        Username Varchar(20) NOT NULL,
        Password Varchar(20) NOT NULL,
        Telephone_No Varchar(20) NOT NULL,
        Payment_Method Varchar(15) NOT NULL);'''

driver_create_statement = '''CREATE TABLE Driver
        (Driver_ID Varchar(10) PRIMARY KEY NOT NULL,
        Fname Varchar(20) NOT NULL,
        Lname Varchar(20) NOT NULL,
        Date_of_Birth DATE NOT NULL,
        Driver_License_Num Varchar(20) NOT NULL,
        Expiry_Date DATE NOT NULL,
        License_Plate Varchar(10) NOT NULL,
        Shift_Start_Time TIME NOT NULL,
        Shift_End_Time TIME NOT NULL,
        Username Varchar(20) NOT NULL,
        Password Varchar(20) NOT NULL,
        Number_of_passengers INTEGER NOT NULL);'''

administrator_create_statement = '''CREATE TABLE Administrator
        (Admin_ID Varchar(10) PRIMARY KEY NOT NULL,
        Fname Varchar(20) NOT NULL,
        Lname Varchar(20) NOT NULL,
        Email Varchar(20) NOT NULL,
        Telephone_No Varchar(10) NOT NULL,
        Username Varchar(20) NOT NULL,
        Password Varchar(20) NOT NULL);'''
booking_create_statement = '''CREATE TABLE Booking
        (Booking_ID Varchar(10) PRIMARY KEY NOT NULL,
        Customer_ID Varchar(10) NOT NULL,
        Driver_ID Varchar(10),
        pickup_address Varchar(50) NOT NULL,
        pickup_time TIME NOT NULL,
        pickup_date DATE NOT NULL,
        drop_off_address Varchar(50) NOT NULL,
        Admin_ID Varchar(10),
        booking_date DATE NOT NULL,
        cost_of_trip CURRENCY NOT NULL,
        paid BIT NOT NULL,
        date_cancelled DATE NOT NULL,
        FOREIGN KEY (Customer_ID) REFERENCES Customers (Customer_ID),
        FOREIGN KEY (Driver_ID) REFERENCES Driver (Driver_ID),
        FOREIGN KEY (Admin_ID) REFERENCES Administrator (Admin_ID));'''

create_statements = {
    'Customers': customer_create_statement,
    'Drivers': driver_create_statement,
    'Administrators': administrator_create_statement,
    'Bookings': booking_create_statement
}

# TABLE DATA
customers_data = [
    ('S1940', 'Anan', 'Jones', '33, Mayfield Road, Valsayn, Port Of Spain', 'ananjones@gmail.com', 'Ananjones69', 'Cats1968', '722-3173', 'Check'),
    ('S2902', 'Billy', 'Butcher', '32 Charlotte Street, Port Of Spain', 'bbutcher7@gmail.com', 'ButcherMan123', '123Butcher', '732-3171', 'Cash'),
    ('S1746', 'John', 'Lewis', 'Alexander St., Longdenville, Chaguanas', 'johnlewiss@gmail.com', 'LewisJohn', 'Lewis4John', '694-5124', 'Credit Card'),
    ('S1627', 'Patrick', 'Scott', '26b Queen Street, Port Of Spain', 'patscott@gmail.com', 'PatrickScott111', 'BookLover7', '632-1298', 'Cash'),
    ('S2621', 'Carl', 'Johnson', '37b Wrightson Road, Port Of Spain', 'cjjohnson@gmail.com', 'CoolGuyCarl', '1868002137', '716-1827', 'Cash'),
    ('S3986', 'Matt', 'Mercer', '99 Tragarete Road, Port Of Spain', 'mattmercer@gmail.com', 'MattFromWiiSports', 'Champion00', '715-1786', 'Check'),
    ('S1247', 'John', 'Dalton', '250 Helen Street, Marabella', 'johndalton@gmail.com', 'DaltonDoser', '9991357', '619-4242', 'Credit Card'),
    ('S3097', 'Savin', 'Mano', '75 Rodney Road, Endeavour, Chaguanas', 'savinmanowork@gmail.com', 'MachoMano', 'MachoMan:3', '424-2564', 'Credit Card'),
]

drivers_data = [
    ('N4150', 'Nicky', 'Dean',  '2000-01-12', '298 055 876', '2024-05-07', 'BRT224', '6:00pm', '1:00am', 'DeanNicky', 'YesIAmDean', 1),
    ('N3894', 'Lila', 'Compton',  '1990-06-05', '522 841 692', '2021-08-24', 'M67EMW', '6:00 pm', '1:00am', 'LilaFromCompton', 'Compton999', 1),
    ('N3989', 'Brant', 'Armstrong',  '1993-05-26', '811 726 782', '2023-06-25', '6ABJ092', '1:00am', '8:00am', 'BrantArmstrong', 'StrongArms', 4),
('N4005', 'Zane', 'Truesdale',  '2000-05-24', '917 444 371', '2021-06-28', 'DZN7639', '1:00am', '8:00am', 'ZaneTruesdale23', '23Jordan23', 1),
    ('N4098', 'Raul', 'Menendez',  '1996-09-11', '989 081 978', '2023-09-07', 'PKG063', '8:00am', '6:00pm', 'LeaderOfCordisDie', 'Nicaraguan', 4),
    ('N3954', 'James', 'Woods',  '1987-11-16', '056 896 824', '2024-06-05', 'ZMZ912', '8:00am', '6:00pm', 'WoodenJames', 'Carp3nt3r1', 4),
    ('N4078', 'Joey', 'Wheeler',  '1999-12-19', '280 473 188', '2025-05-07', 'RAL3814', '8:00am', '6:00pm', 'ImJoeyWheeler', 'WheelerK', 4)
]

administrators_data = [
    ('MP211', 'Raul', 'Sagram', 'rsagram@gmail.com', '341-7746', 'RaoulS', 'S4gr4m'),
    ('MP315', 'Dario', 'Babwah', 'dbabwah@gmail.com', '343-8481', 'iiBabwahii', 'DarioWario'),
    ('MP136', 'John', 'Hudson', 'johnhudson@gmail.com', '494-7854', 'TheHudsonHornet', 'CarsHornet'),
    ('MP293', 'Fred', 'Hueston', 'freddyh@gmail.com', '620-6083', 'HiImFredHueston', 'Fred12345')
]

bookings_data = [
    ('B1258', 'S1940', 'N4150', '33, Mayfield Road, Valsayn, Port Of Spain', '8:00pm', '2021-04-20', 'Staubles Bay, Port Of Spain', 'MP211', '2021-04-19', 5, 1, 'NULL'),
    ('B1519', 'S2902', 'N3894', '32 Charlotte Street, Port Of Spain', '10:00pm', '2021-04-18', '3 Chootoo Road, San Juan', 'MP315', '2021-04-15', 10, 0, '2021-04-17'),
    ('B1375', 'S1746', 'N3989', 'Alexander St., Longdenville, Chaguanas', '5:00am', '2021-04-22', '10 Irving Street, San Juan', 'MP211', '2021-04-20', 10, 1, 'NULL')
]

insert_statements_and_data = (
    ('Customers', customers_data, customers_insert_statement),
    ('Drivers', drivers_data, drivers_insert_statement),
    ('Administrators', administrators_data, administrators_insert_statement),
    ('Bookings', bookings_data, bookings_insert_statement)
)

def create_tables(remove_existing_file=False):
    if DATABASE_FILE != ':memory:' and os.path.isfile(DATABASE_FILE):
        if remove_existing_file:
            try:
                os.remove(DATABASE_FILE)
            except:
                return False, 'Failed to remove existing database file.'
        else:
            return False, 'Database file exists.'
    try:
        conn =  sqlite3.connect(DATABASE_FILE)
        cur = conn.cursor()
        table_name = "unspecified"
        try:
            for table_name, create_statement in create_statements.items():
                cur.execute(create_statement)
        except:
            return False, f"Error while creating {table_name} table."

    except:
        return False, "Could not create database connection."
    finally:
        if conn:
            conn.close()
    
    return True, "Successfully created tables."

def populate_tables():
    try:
        conn =  sqlite3.connect(DATABASE_FILE)
        
        table_name = "unspecified"
        try:
            for table_name, insert_data, insert_statement in insert_statements_and_data:
                conn.executemany(insert_statement, insert_data)
        except:
            return False, f"Error while populating {table_name} table."

    except:
        return False, "Could not create database connection."
    finally:
        if conn:
            conn.commit()
            conn.close()
    
    return True, "Successfully populated tables."

if __name__ == "__main__":
    result, message = create_tables(remove_existing_file=True)
    print(message)
    if result:
        _, message = populate_tables()
        print(message)

