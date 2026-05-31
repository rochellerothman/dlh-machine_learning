-- Creates a procedure that computes and stores a user's weighted average score
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN p_user_id INT
)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT SUM(c.score * p.weight) / SUM(p.weight)
        FROM corrections c
        INNER JOIN projects p
            ON c.project_id = p.id
        WHERE c.user_id = p_user_id
    )
    WHERE id = p_user_id;
END$$

DELIMITER ;
