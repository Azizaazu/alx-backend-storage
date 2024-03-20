0. We are all unique!
Write a SQL script that creates a table users following these requirements:

With these attributes:
id, integer, never null, auto increment and primary key
email, string (255 characters), never null and unique
name, string (255 characters)
If the table already exists, your script should not fail
Your script can be executed on any database
1. In and not out
Write a SQL script that creates a table users following these requirements:

With these attributes:
id, integer, never null, auto increment and primary key
email, string (255 characters), never null and unique
name, string (255 characters)
country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
If the table already exists, your script should not fail
Your script can be executed on any database
.
.
.
10. Safe divide
Write a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

Requirements:

You must create a function
The function SafeDiv takes 2 arguments:
a, INT
b, INT
And returns a / b or 0 if b == 0
11. No table for a meeting
Write a SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.

Requirements:

The view need_meeting should return all students name when:
They score are under (strict) to 80
AND no last_meeting date OR more than a month
12. Average weighted score
Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

Requirements:

Procedure ComputeAverageScoreForUser is taking 1 input:
user_id, a users.id value (you can assume user_id is linked to an existing users)
13. Average weighted score for all!
Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.

Requirements:

Procedure ComputeAverageWeightedScoreForUsers is not taking any input.
