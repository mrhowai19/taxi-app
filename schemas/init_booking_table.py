BOOKING_TABLE = ''' CREATE TABLE IF NOT EXISTS Booking (
                    Booking_ID Varchar(10) PRIMARY KEY NOT NULL,
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
                    FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID),
                    FOREIGN KEY (Driver_ID) REFERENCES Driver(Driver_ID),
                    FOREIGN KEY (Admin_ID) REFERENCES Administrator(Admin_ID)
                    );
                    
INSERT INTO Booking
(Booking_ID, Customer_ID, Driver_ID, pickup_address, pickup_time, pickup_date, drop_off_address, Admin_ID, booking_date, cost_of_trip, paid, date_cancelled)
VALUES 
('B1258', 'S1940', 'N4150', '33, Mayfield Road, Valsayn, Port Of Spain', '8:00pm', '2021-04-20', 'Staubles Bay, Port Of Spain', 'MP211', '2021-04-19', 5, 1, 'NULL'),
('B1519', 'S2902', 'N3894', '32 Charlotte Street, Port Of Spain', '10:00pm', '2021-04-18', '3 Chootoo Road, San Juan', 'MP315', '2021-04-15', 10, 0, '2021-04-17'),
('B1375', 'S1746', 'N3989', 'Alexander St., Longdenville, Chaguanas', '5:00am', '2021-04-22', '10 Irving Street, San Juan', 'MP211', '2021-04-20', 10, 1, 'NULL')
;

'''