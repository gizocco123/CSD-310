INSERT INTO player (first_name, last_name, team_id)
	VALUES('John', 'Wiggins', 1);
    
SELECT 1 FROM team WHERE team_name = 'Team Gandalf';

UPDATE player
SET team_id = 2,
	first_name = 'John',
    last_name = 'Wiggins'
WHERE first_name = 'Sauron';

SELECT 2 FROM team WHERE team_name = 'Team Sauron';

DELETE FROM player
WHERE first_name = 'Sauron';

SELECT 2 FROM team WHERE team_name = 'Team Sauron'