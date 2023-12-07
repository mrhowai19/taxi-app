CUSTOMER_TABLE = ''' CREATE TABLE IF NOT EXISTS Customers (
                                Customer_ID Varchar(10) PRIMARY KEY NOT NULL,
                                FName Varchar(20) NOT NULL,
                                LName Varchar(20) NOT NULL,
                                Address Varchar(50) NOT NULL,
                                Email Varchar(20) NOT NULL,
                                Username Varchar(20) NOT NULL,
                                Password Varchar(20) NOT NULL,
                                Telephone_No Varchar(20) NOT NULL,
                                Payment_Method Varchar(15) NOT NULL
                                );
                                
    INSERT INTO Customers 
    ( Customer_ID, FName, LName, Address, Email, Username, Password, Telephone_No, Payment_Method) 
    VALUES 
    ('S1940', 'Anan', 'Jones', '33, Mayfield Road, Valsayn, Port Of Spain', 'ananjones@gmail.com', 'Ananjones69', 'Cats1968', '722-3173', 'Check'),
    ('S2902', 'Billy', 'Butcher', '32 Charlotte Street, Port Of Spain', 'bbutcher7@gmail.com', 'ButcherMan123', '123Butcher', '732-3171', 'Cash'),
    ('S1746', 'John', 'Lewis', 'Alexander St., Longdenville, Chaguanas', 'johnlewiss@gmail.com', 'LewisJohn', 'Lewis4John', '694-5124', 'Credit Card'),
    ('S1627', 'Patrick', 'Scott', '26b Queen Street, Port Of Spain', 'patscott@gmail.com', 'PatrickScott111', 'BookLover7', '632-1298', 'Cash'),
    ('S2621', 'Carl', 'Johnson', '37b Wrightson Road, Port Of Spain', 'cjjohnson@gmail.com', 'CoolGuyCarl', '1868002137', '716-1827', 'Cash'),
    ('S3986', 'Matt', 'Mercer', '99 Tragarete Road, Port Of Spain', 'mattmercer@gmail.com', 'MattFromWiiSports', 'Champion00', '715-1786', 'Check'),
    ('S1247', 'John', 'Dalton', '250 Helen Street, Marabella', 'johndalton@gmail.com', 'DaltonDoser', '9991357', '619-4242', 'Credit Card'),
    ('S3097', 'Savin', 'Mano', '75 Rodney Road, Endeavour, Chaguanas', 'savinmanowork@gmail.com', 'MachoMano', 'MachoMan:3', '424-2564', 'Credit Card');              
'''