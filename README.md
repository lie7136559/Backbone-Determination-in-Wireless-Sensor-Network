# Backbone-Determination-in-Wireless-Sensor-Network
Algorithm Project

(1)Introduction and Summary

In part I of this project, the main work is generating random geometric Graph in unit square and unit disk. Given the number of vertices (N) and expected average degree (A) of each topology, calculating the estimated radius (r), number of edges (E), real average degree, maximum and minimum degree of the generated networks. For all the vertices in the graph, I use sweep method to draw the edges. In theory, sweep method cost less time than the brute force method, sweep method just need to compare vertices in certain range. And in Part 2, I use the smallest last ordering(DAVID&LELAND,1984) to color each vertex, and get the color set.

Strong part: sweep method can save much time more compared to brute force way, using set to check color runs faster than list in python.

Weak part: can not implement liner running time in smallest last ordering part, draw the graph and show the statistics graph using different software, so in order to get the all the result, I should run my code twice.

(2) Algorithm Descriptions:
Part 1:
Using Sweep method to find pairs of vertices, the step is first sort the all the vertices based on its X coordinate from small to large, than for each of the vertex from sorted order, only compare the X coordinate range from x to x+r. If next vertex is in the range, then calculate the distance between them to see if d<=r, if so, we find a pair. The time complexity is O(NlogN) for sort and O(rN^2) for searching.

Estimate r:

For Square:r= √𝐴𝑣𝑔𝐷𝑒𝑔𝑟𝑒𝑒/𝑁𝜋2

For Disk: r= √𝐴𝑣𝑔𝐷𝑒𝑔𝑟𝑒𝑒/𝑁2

Perform uniform distribution: For square, we only need to generate random number from 0 to 1 to give the value to location X and Y. But for the Disk, first generate random number theata from 0 to 2𝜋, andanother number r from 0 to 1, so x = r*sin(theta), and y = r*cos(theta).

Part 2:
Walkthrough of the smallest-last coloring algorithm(Step, Data and Flow chart):
For unit Square, N = 20 and r = 0.4, Plot 1 is sequential coloring plot, Plot 2 is color set size distribution.

Step:

1. Find the vertex with the min Degree using the Degree List.
Degree = [2, 3, 7, 8, 8, 8, 5, 11, 11, 9, 9, 8, 11, 8, 8, 5, 4, 4, 4, 3]
Degree_List = [[], [], [0], [1, 19], [16, 17, 18], [6, 15], [], [2], [3, 4, 5, 11, 13, 14], [9, 10], [], [7, 8, 12]] 

2. Find the vertices linked with this vertex using the adjacent list, for each linked vertex in Degree List, Degree minus one and update the Degree List. As how to find its location in Degree List, using another degree list in part 1(from index 0 to N represents the vertex number and the value means the Degree, For example Degree[5] = 10 means the vertex 5 has degree 10). So, for each vertex, we can know its degree, and in degree list we can know its location.

Smallest last ordering List =
[[11], [9, 11], [8, 9, 11], [7, 8, 9, 11], [4, 7, 8, 9, 11], [12, 4, 7, 8, 9, 11], [2, 4, 7, 8, 9, 11], [5, 2, 4, 7, 8, 9, 12], [13, 2, 7, 8, 9, 11, 12], [3, 4, 5, 7, 8, 12], [10, 3, 5, 7, 12], [14, 7, 8, 10, 12], [15, 8, 9, 11, 13], [18, 10, 14], [17, 10, 14, 18], [16, 10, 14, 17, 18], [6, 3, 10, 14], [19, 12, 13, 15], [1, 3, 6], [0, 1, 6]]

3. Coloring: Try to give current color 1 to each vertex in smallest last ordering, for the linked vertex I create a set to store them for each time, and check for the current color set to create another vertex set with the current color. And do the intersection between them, if the result is not empty, means the current color is occupied, so we try another color: current color + 1.
Color Set = {1: [11, 5, 14, 19, 1], 2: [9, 3, 18, 0], 3: [8, 10], 4: [7, 15, 17, 6], 5: [4, 13, 16], 6: [12, 2]}

Part 3 Walkthrongh:
Backbone Determination:
1. From Color 1 to Color 4, pick any 2 color, can get 6 pairs.
2. For each of the pairs, check the original adjacent list to draw the edge between the two independent sets.
3. For each graph, create a new adjacent list of it. And check each sublist of the adjacent list, if the length of the sublist is 1(the vertex just have one vertex nearby means degree is 1), delete the vertex, and update the adjacent list(delete the vertex from the nearby vertex’s sublist). Continue the loop until no sublist has length 1.
4. DFS: Do depth first search for each graph to get a path, for the largest path, draw the final graph only the vertex in the largest path(deleting the minor component)
5. Calculate the size of each graph(number of edges), and choose the largest two size of the graph as the final result.
