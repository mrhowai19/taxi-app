from datetime import datetime
from typing import Optional
from dataclasses import dataclass

@dataclass
class Customer():
    customer_id: str
    first_name: str
    last_name: str
    address: str
    email: str
    username: str
    password: str
    telephone_number: str
    payment_method: str

    @classmethod
    def from_row(cls, row):
        in_customer_id, in_fname, in_lname, in_address, in_email, in_username, in_password, in_telephone_no, in_payment_method = row
        customer_id = in_customer_id
        first_name = in_fname
        last_name = in_lname
        address = in_address
        email = in_email
        username = in_username
        password = in_password
        telephone_number = in_telephone_no
        payment_method = in_payment_method
        return cls(customer_id, first_name, last_name, address, email, username, password, telephone_number, payment_method)

    def to_param(self):
        return (
            self.customer_id,
            self.first_name,
            self.last_name,
            self.address,
            self.email,
            self.username,
            self.password,
            self.telephone_number,
            self.payment_method
        )

@dataclass
class Driver():
    driver_id: str 
    first_name: str
    last_name: str
    date_of_birth: datetime
    license_number: str
    license_expiry: datetime
    license_plate: str
    shift_start_time: str
    shift_end_time: str
    username: str
    password: str
    number_of_passengers: int

    @classmethod
    def from_row(cls, row):
        in_driver_id, in_fname, in_lname, in_date_of_birth, in_driver_license_num, in_expiry_date, in_license_plate, in_shift_start_time, in_shift_end_time, in_username, in_password, in_number_of_passengers = row
        driver_id = in_driver_id
        first_name = in_fname
        last_name = in_lname
        date_of_birth = datetime.strptime(in_date_of_birth, r'%Y-%m-%d')
        license_number = in_driver_license_num
        license_expiry = datetime.strptime(in_expiry_date, r'%Y-%m-%d')
        license_plate = in_license_plate
        shift_start_time = in_shift_start_time
        shift_end_time = in_shift_end_time
        username = in_username
        password = in_password
        number_of_passengers = in_number_of_passengers
        return cls(driver_id, first_name, last_name, date_of_birth, license_number, license_expiry, license_plate, shift_start_time, shift_end_time, username, password, number_of_passengers)

    def to_param(self):
        return (
            self.driver_id,
            self.first_name,
            self.last_name,
            self.date_of_birth.strftime(r'%Y-%m-%d'),
            self.license_number,
            self.license_expiry.strftime(r'%Y-%m-%d'),
            self.license_plate,
            self.shift_start_time,
            self.shift_end_time,
            self.username,
            self.password,
            self.number_of_passengers,
        )

@dataclass
class Administrator():
    admin_id: str
    first_name: str
    last_name: str
    email: str
    telephone_number: str
    username: str
    password: str

    @classmethod
    def from_row(cls, row):
        in_admin_id, in_fname, in_lname, in_email, in_telephone_no, in_username, in_password = row
        admin_id = in_admin_id
        first_name = in_fname
        last_name = in_lname
        email = in_email
        telephone_number = in_telephone_no
        username = in_username
        password = in_password
        return cls(admin_id, first_name, last_name, email, telephone_number, username, password)

    def to_param(self):
        return (
            self.admin_id,
            self.first_name,
            self.last_name,
            self.email,
            self.telephone_number,
            self.username,
            self.password,
        )

@dataclass
class Booking():
    booking_id: str
    customer_id: str
    driver_id: Optional[str]
    pickup_address: str
    pickup_datetime: datetime
    drop_off_address: str
    admin_id: Optional[str]
    booking_date: datetime
    cost_of_trip: int
    paid: bool
    date_cancelled: Optional[datetime]

    @property
    def is_passed(self):
        return self.pickup_datetime < datetime.now()

    @property
    def is_approved(self):
        return None != self.admin_id

    @property
    def is_cancelled(self):
        return None != self.date_cancelled

    @classmethod
    def from_row(cls, row):
        in_booking_id, in_customer_id, in_driver_id, in_pickup_address, in_pickup_time, in_pickup_date, in_drop_off_address, in_admin_id, in_booking_date, in_cost_of_trip, in_paid, in_date_cancelled = row
        booking_id = in_booking_id
        customer_id = in_customer_id
        driver_id = in_driver_id
        pickup_address = in_pickup_address
        pickup_datetime = datetime.strptime(f'{in_pickup_date} {in_pickup_time}', r'%Y-%m-%d %-I:%M%p')
        drop_off_address = in_drop_off_address
        admin_id = in_admin_id
        booking_date = datetime.strptime(in_booking_date, r'%Y-%m-%d')
        cost_of_trip = in_cost_of_trip
        paid = in_paid
        try:
            date_cancelled = datetime.strptime(in_date_cancelled, r'%Y-%m-%d')
        except:
            date_cancelled = None
        return cls(booking_id, customer_id, driver_id, pickup_address, pickup_datetime, drop_off_address, admin_id, booking_date, cost_of_trip, paid, date_cancelled)

    def to_param(self):
        return (
            self.booking_id,
            self.customer_id,
            self.driver_id if self.driver_id else 'NULL',
            self.pickup_address,
            self.pickup_datetime.strftime(r'%-I:%M%p').lower(),
            self.pickup_datetime.strftime(r'%Y-%m-%d'),
            self.drop_off_address,
            self.admin_id if self.admin_id else 'NULL',
            self.booking_date.strftime(r'%Y-%m-%d'),
            self.cost_of_trip,
            self.paid,
            self.date_cancelled.strftime(r'%Y-%m-%d') if self.date_cancelled else 'NULL',
        )