#include<iostream>
#include <bits/stdc++.h> 
#include <fstream>
#include <sstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list> 
#include <stack> 
#define V1 4605
using namespace std;

void add_edge(vector<int> adj[], int src, int dest)
{
adj[src].push_back(dest);
//adj[dest].push_back(src);
}
// a modified version of BFS that stores predecessor
// of each vertex in array p
// and its distance from source in array d
bool BFS(vector<int> adj[], int src, int dest, int v,
int pred[], int dist[])
{
// a queue to maintain queue of vertices whose
// adjacency list is to be scanned as per normal
// DFS algorithm
list<int> queue;
// boolean array visited[] which stores the
// information whether ith vertex is reached
// at least once in the Breadth first search
bool visited[v];
// initially all vertices are unvisited
// so v[i] for all i is false
// and as no path is yet constructed
// dist[i] for all i set to infinity
for (int i = 0; i < v; i++) {
visited[i] = false;
dist[i] = INT_MAX;
pred[i] = -1;
}
// now source is first to be visited and
// distance from source to itself should be 0
visited[src] = true;
dist[src] = 0;
queue.push_back(src);
// standard BFS algorithm
while (!queue.empty()) {
int u = queue.front();
queue.pop_front();
for (int i = 0; i < adj[u].size(); i++) {
if (visited[adj[u][i]] == false) {
visited[adj[u][i]] = true;
dist[adj[u][i]] = dist[u] + 1;
pred[adj[u][i]] = u;
queue.push_back(adj[u][i]);
// We stop BFS when we find
// destination.
if (adj[u][i] == dest)
return true;
}
}
}
return false;
}
// utility function to print the shortest distance
// between source vertex and destination vertex
void printShortestDistance(vector<int> adj[], int s,
int dest, int v)
{
    fstream fout; 
  
    // opens an existing csv file or creates a new file. 
    fout.open("shrtpath.csv", ios::out | ios::app); 
// predecessor[i] array stores predecessor of
// i and distance array stores distance of i
// from s
int pred[v], dist[v];
if (BFS(adj, s, dest, v, pred, dist) == false) {
fout <<"NA";
fout<<"\n";
cout << "Given source and destination"
<< " are not connected";
return;
}
// vector path stores the shortest path
vector<int> path;
int crawl = dest;
path.push_back(crawl);
while (pred[crawl] != -1) {
path.push_back(pred[crawl]);
crawl = pred[crawl];
}
// distance from source is in distance array
cout << "Shortest path length is : "
<< dist[dest];
// printing path from source to destination
cout << "\nPath is::\n";
///////////////////



///////////////
for (int i = path.size() - 1; i >= 0; i--)
fout << path[i] << ",";
fout<<"\n";
}


int extractMaximum(string str) 
{ 
    int num = 0, res = 0; 
  
    // Start traversing the given string 
    for (int i = 0; i<str.length(); i++) 
    { 
        // If a numeric value comes, start converting 
        // it into an integer till there are consecutive 
        // numeric digits 
        if (str[i] >= '0' && str[i] <= '9') 
            num = num * 10 + (str[i]-'0'); 
  
        // Update maximum value 
        else
        { 
            res = max(res, num); 
  
            // Reset the number 
            num = 0; 
        } 
    } 
  
    // Return maximum value 
    return max(res, num); 
} 


// Driver program to test above functions
int main()
{
// no. of vertices
int v = 4605;
// array of vectors is used to store the graph
// in the form of an adjacency list
vector<int> adj[v];
// Creating graph given in the above diagram.
// add_edge function takes adjacency list, source
// and destination vertex as argument and forms
// an edge between them.
ifstream myFile;
myFile.open("edges.csv");
int c = 0; 
while(myFile.good()) {
        //cout<<c<<endl;
        string line;
        getline(myFile , line , '\n');
        //cout<<line<<endl;
        vector<string> result;
        stringstream s_stream(line);
        while(s_stream.good()) {
        string substr;
        getline(s_stream, substr, ','); 
        result.push_back(substr);
        if(result.size()==2)
        {
        c+=1;
        int k1 = extractMaximum(result.at(0));
        int i1 = extractMaximum(result.at(1)); 
        //cout<<k1<<" "<<i1<<endl;
        add_edge(adj, k1, i1);
        }

        }
        /*for(int i = 0; i<result.size(); i++) { 
        cout << result.at(i) << endl;
        }*/
}

//int source = 1, dest = 53;
//printShortestDistance(adj, source, dest, v);
////////////////

ifstream myFile1;
myFile1.open("temp.csv");
while(myFile1.good()) {
        //cout<<c<<endl;
        string line;
        getline(myFile1 , line , '\n');
        //cout<<line<<endl;
        vector<string> result;
        stringstream s_stream(line);
        while(s_stream.good()) {
        string substr;
        getline(s_stream, substr, ','); 
        result.push_back(substr);
        if(result.size()==2)
        {
        c+=1;
        int k1 = extractMaximum(result.at(0));
        int i1 = extractMaximum(result.at(1)); 
        //cout<<k1<<" "<<i1<<endl;
        printShortestDistance(adj, k1, i1, v);
        }

        }
        
}



////////////////
return 0;
}




