    LeetCode Logo

Problem List
Debugging...
Debugging...
DCC BadgeSolve today's Daily Challenge to refresh your streak!
Avatar
pawaneleven
Access all features with our Premium subscription!
myLists
My Lists
notebook
Notebook
submissions
Submissions
progress
Progress
points
Points

Try New Features
Orders
My Playgrounds
Settings
Appearance

    Sign Out

Premium
Description
Description
Editorial
Editorial
Solutions
Solutions
Accepted
Submissions
Submissions
Code
Code
Code Sample
Testcase
Testcase
Test Result
Accepted
Runtime: 69 ms
Case 1
Input
Activity =
| player_id | device_id | event_date | games_played |
| --------- | --------- | ---------- | ------------ |
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
Output
| player_id | first_login |
| --------- | ----------- |
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |
Expected
| player_id | first_login |
| --------- | ----------- |
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |
Contribute a testcase
Input
1
{"headers":{"Activity":["player_id","device_id","event_date","games_played"]},"rows":{"Activity":[[1,2,"2016-03-01",5],[1,2,"2016-05-02",6],[2,3,"2017-06-25",1],[3,1,"2016-03-02",0],[3,4,"2018-07-03",5]]}}
Output
1
2
3
4
5
| player_id | first_login |
| --------- | ----------- |
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |
Expected
1
2
3
4
5
| player_id | first_login |
| --------- | ----------- |
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |
All Submissions
Accepted
12 / 12 testcases passed
pawaneleven
pawaneleven
submitted at Jun 10, 2025 18:04
Runtime
3990ms
Beats5.00%
Analyze Complexity
Code
MySQL

# Write your MySQL query statement below
SELECT player_id, event_date first_login FROM Activity b WHERE 
event_date = (SELECT min(event_date) FROM Activity a WHERE a.player_id = b.player_id)

More challenges
512. Game Play Analysis II
0/5
Runtime: 455ms
sql

# Write your MySQL query statement below
select player_id,min(event_date) as first_login  from Activity group by player_id ;

