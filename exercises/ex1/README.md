#resource consuming merge

Merging a list consisting of K elements with a list of L elements takes (K+L) resources. The resources required to merge more than two lists into one final list depends on the order in which the merges are performed. 

For example, consider the following three lists: 
list P consisting of 100, 
list Q consisting of 250, 
list R consisting of 1000. 

They can be merged into one in three ways: 
1. first merge P with Q, then merge the result with R; or 
2. first merge P with R, then merge the result with Q; or 
3. first merge R with Q, then merge the result with P. 

The resources needed to perform the above merges are respectively: 
merge P with Q: 350m; result with R: 1350; total: 1700; 
merge P with R: 1100; result with Q: 1350; total: 2450; 
merge Q with R: 1250; result with P: 1350; total: 2600. 

The first schema is the best. 

When the number of lists to merge is fewer than two, no merges are performed. 

##Task

Write a function: function solution($A); that, given an array A of length N describing the lengths of N lists, returns the smallest resource quantity required to merge these lists. 


##Example
For example, given array A:
 A[0] = 100 A[1] = 250 A[2] = 1000

Resut: 1700

Assumptions: 
N is an integer within the range [0..10,000]; 
each element of array A is an integer within the range [1..1,000]. 
