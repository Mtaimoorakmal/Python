employee = ID , Name , Desg , DpId
department  = ID , Name , Location

with emplyCount {
select count(ID) as empNum
from epmloyee
group by Dpid}
select name form department where (select empNum from emplyCount where empNum > 5)


std  = Id , Name , Score 

with nth_score {
select score from std order by score Desc limit 4}

select name from std where score = {select score form th_score limit 1}



make a function to return the number is even or odd without using any conditional statement

return list of peak Elements from the given list [1,4,3,0,5,2], A peak element is an element that is strictly greater than its neighbors.

Find all departments with more than 5 employees.

Write sql query to find student names whose score is 4th highest in the class

