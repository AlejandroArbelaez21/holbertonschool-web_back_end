-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
DELIMITER //
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus (IN user_id INT,
       IN project_name VARCHAR(255),
       IN score INT)
BEGIN

INSERT INTO projects(name)
SELECT project_name FROM DUAL
WHERE NOT EXISTS (SELECT * FROM projects WHERE name = project_name LIMIT 1);

INSERT INTO corrections(user_id, project_id, score)
VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);

END;//
DELIMITER ;
