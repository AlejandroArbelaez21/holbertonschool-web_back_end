-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
CREATE TRIGGER email_validation
BEFORE UPDATE ON users FOR EACH ROW
BEGIN
	IF OLD.email <> NEW.email THEN
	   SET NEW.valid_email = 0;
END IF;
