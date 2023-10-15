-- Create a function that divides
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
BEGIN
    IF b == 0 THEN
	RETURN 0;
    RETURN a / b;
    END IF;
END; //
DELIMITER ;
