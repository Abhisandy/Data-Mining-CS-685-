    • Languages Used : Python and C++

    • All required packages to run the program are in “requirements.txt” file, which will run automatically when .sh files are executed.

    • .sh file for each Ques_ are with name of Ques_ itself with .sh extension and “assign2.sh” will run the entire program.
	
    • Data Processing : 
      
    • For Q5 , I Consider Strongly Connected Graph.
      
    • Calculation of Diameter : I used Diameter function inside “Networkx” package to find out the diameter of each component of strongly connected graph. 
      
    • I used python for most of the questions but in one question we have to find shortest distance between all pairs, and in python it took lot of time to find shortest path for all pairs(both bfs on all and floyd warshall). So for this task i use C++ code which only take couple of minutes , here i used BFS because graph is unweighted.

    • While using path_finished.tsv, i deleted a row for which the path is unreacable , and also removed all those paths which have length 1. because in that case both source and destination is same, which will give shortest path as zero.	
       

