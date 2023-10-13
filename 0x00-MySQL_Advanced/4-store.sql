-- A Trigger that decreases items table when Order is made

DELIMITER //
CREATE TRIGGER decr_qty
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END;//
DELIMITER ;
