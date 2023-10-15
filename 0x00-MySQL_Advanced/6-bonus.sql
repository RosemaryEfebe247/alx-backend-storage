-- A stored procedure to adds a new correction for students
DELIMITER //

CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    DECLARE store_project_id INT;
    -- Check if the project exists, and if not, create it
    SELECT id INTO store_project_id FROM projects WHERE name = project_name;
    IF store_project_id IS NULL THEN
        -- Project doesn't exist, so create it
        INSERT INTO projects (name) VALUES (project_name);
        SET store_project_id = LAST_INSERT_ID();
    END IF;
    -- Insert the correction for the user
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, store_project_id, score);
END //
DELIMITER ;
