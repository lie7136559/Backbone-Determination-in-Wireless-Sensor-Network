# Backbone-Determination-in-Wireless-Sensor-Network
Algorithm Project

Introduction and Summary
In part I of this project, the main work is generating random geometric Graph in unit square and unit disk. Given the number of vertices (N) and expected average degree (A) of each topology, calculating the estimated radius (r), number of edges (E), real average degree, maximum and minimum degree of the generated networks. For all the vertices in the graph, I use sweep method to draw the edges. In theory, sweep method cost less time than the brute force method, sweep method just need to compare vertices in certain range. And in Part 2, I use the smallest last ordering(DAVID&LELAND,1984) to color each vertex, and get the color set.
Strong part: sweep method can save much time more compared to brute force way, using set to check color runs faster than list in python.
Weak part: can not implement liner running time in smallest last ordering part, draw the graph and show the statistics graph using different software, so in order to get the all the result, I should run my code twice.
