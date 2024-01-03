# Facility Location Problem

This repository showcases my Computer Science project that resolves the Facility Location Problem for cities listed in the data file miles.dat. A description of what this problem is and an in-depth explanation of how my Python program solves can be found in the description. An explanation of how to run the program to see the visualization output on Google Earth can be found in the How to Run Program. The Python code that runs the algorithms and creates the kml files is in the project1Phase3.py file, and the kml code that creates the visualizations is in visualization300.kml and visualization800.kml. 


1. [Project Title](#Project-title)
2. [Description](#Description)
3. [How to Run Program](#How-to-Run-Program)
4. [Additional Documentation](#Additional-Documentation)

## Project Title

**Facility Location Problem**

## Description 

The Facility Location Problem (FLP) is a classic optimization problem that determines the best location for a factory or warehouse to be placed based on geographical demands, facility costs, and transportation distances (Cantlebary). For this project, our assignment focused only on distances between facilities and cities that are served. These factories/warehouses (facilities), serve any amount of cities within a specified distance and serve the city that they are located in. 

The goal of this project is to find the most efficient facility locations for cities that are within 300 miles and 800 miles of a facility, such that there are the least amount of facilities possible and every city is served. 

This problem is complex and requires lots of different algorithms. For example, the function countUnservedCities finds the cities that are "nearby" a given city using the function nearbyCities. It then counts how many of these nearby cities have not been served yet and returns this number to the locateFacilities function.


## How to Run Program



## Additional Documentation

Citations: 

Cantlebary, Liz, and Lawrence Li. “Facility Location Problem.” Facility Location Problem - Cornell University Computational Optimization Open Textbook - Optimization Wiki, 21 Dec. 2020, optimization.cbe.cornell.edu/index.php?title=Facility_location_problem#:~:text=The%20Facility%20Location%20Problem%20(FLP,facility%20costs%2C%20and%20transportation%20distances. 
