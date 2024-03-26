0. List all databases
Write a script that lists all databases in MongoDB.
1. Create a database
Write a script that creates or uses the database my_db
2. Insert document
Write a script that inserts a document in the collection school:

The document must have one attribute name with value �~@~\Holberton school�~@~]
The database name will be passed as option of mongo command
.
.
.
12. Log stats
Write a Python script that provides some stats about Nginx logs stored in MongoDB:

Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it�~@~Ys a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
You can use this dump as data sample: dump.zip
13. Regex filter
Write a script that lists all documents with name starting by Holberton in the collection school:

The database name will be passed as option of mongo command
14. Top students
Write a Python function that returns all students sorted by average score:

Prototype: def top_students(mongo_collection):
mongo_collection will be the pymongo collection object
The top must be ordered
The average score must be part of each item returns with key = averageScore
15. Log stats - new version
Improve 12-log_stats.py by adding the top 10 of the most present IPs in the collection nginx of the database logs:

The IPs top must be sorted (like the example below)
