-- Create trigger to reset valid_email only when email has been changed
DELIMITER //

CREATE TRIGGER reset_valid_email_on_email_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END //

DELIMITER ;
