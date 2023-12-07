ADMIN_TABLE = ''' CREATE TABLE IF NOT EXISTS Administrator (
                    Admin_ID Varchar(10) PRIMARY KEY NOT NULL,
                    Fname Varchar(20) NOT NULL,
                    Lname Varchar(20) NOT NULL,
                    Email Varchar(20) NOT NULL,
                    Telephone_No Varchar(10) NOT NULL,
                    Username Varchar(20) NOT NULL,
                    Password Varchar(20) NOT NULL
                    );
                    
INSERT INTO Administrator (Admin_ID, Fname, Lname, Email, Telephone_No, Username, Password)
VALUES
('MP211', 'Raul', 'Sagram', 'rsagram@gmail.com', '341-7746', 'RaoulS', 'S4gr4m'),
('MP315', 'Dario', 'Babwah', 'dbabwah@gmail.com', '343-8481', 'iiBabwahii', 'DarioWario'),
('MP136', 'John', 'Hudson', 'johnhudson@gmail.com', '494-7854', 'TheHudsonHornet', 'CarsHornet'),
('MP293', 'Fred', 'Hueston', 'freddyh@gmail.com', '620-6083', 'HiImFredHueston', 'Fred12345')
;
'''
