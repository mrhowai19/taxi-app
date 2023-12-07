DRIVER_TABLE = '''  CREATE TABLE IF NOT EXISTS Driver (
                    Driver_ID Varchar(10) PRIMARY KEY NOT NULL,
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
                    Number_of_passengers INTEGER NOT NULL
                    );
                    
INSERT INTO Driver 
(Driver_ID, Fname, Lname, Date_of_Birth, Driver_License_Num, Expiry_Date, License_Plate, Shift_Start_Time, Shift_End_Time, Username, Password, Number_of_passengers) 
VALUES 
('N4150', 'Nicky', 'Dean', '2000-01-12', '298 055 876', '2024-05-07', 'BRT224', '6:00pm', '1:00am', 'DeanNicky', 'YesIAmDean', 1),
('N3894', 'Lila', 'Compton', '1990-06-05', '522 841 692', '2021-08-24', 'M67EMW', '6:00 pm', '1:00am', 'LilaFromCompton', 'Compton999', 1),
('N3989', 'Brant', 'Armstrong', '1993-05-26', '811 726 782', '2023-06-25', '6ABJ092', '1:00am', '8:00am', 'BrantArmstrong', 'StrongArms', 4),
('N4005', 'Zane', 'Truesdale', '2000-05-24', '917 444 371', '2021-06-28', 'DZN7639', '1:00am', '8:00am', 'ZaneTruesdale23', '23Jordan23', 1),
('N4098', 'Raul', 'Menendez', '1996-09-11', '989 081 978', '2023-09-07', 'PKG063', '8:00am', '6:00pm', 'LeaderOfCordisDie', 'Nicaraguan', 4),
('N3954', 'James', 'Woods', '1987-11-16', '056 896 824', '2024-06-05', 'ZMZ912', '8:00am', '6:00pm', 'WoodenJames', 'Carp3nt3r1', 4),
('N4078', 'Joey', 'Wheeler', '1999-12-19', '280 473 188', '2025-05-07', 'RAL3814', '8:00am', '6:00pm', 'ImJoeyWheeler', 'WheelerK', 4)
;
'''