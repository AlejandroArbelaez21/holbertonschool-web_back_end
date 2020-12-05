-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser
    (IN user_id INT) 
BEGIN
UPDATE users SET average_score = 
(SELECT AVG(score) FROM corrections WHERE corrections.user_id=user_id
GROUP BY corrections.user_id)
WHERE id=user_id;
END//
DELIMITER ;
