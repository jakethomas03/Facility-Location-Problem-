# Facility Location Problem

![Python badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

This repository showcases my Computer Science project that resolves the Facility Location Problem for cities listed in the data file miles.dat. A description of what this problem is and an in-depth explanation of how my Python program solves can be found in the description. An explanation of how to run the program to see the visualization output on Google Earth can be found in the How to Run Program. The Python code that runs the algorithms and creates the KML files is in the project1Phase3.py file, and the KML code that creates the visualizations is in visualization300.kml and visualization800.kml. 


1. [Problem Description](#Problem-Description)
2. [Data Description](#Data-Description)
3. [How to Run Program](#How-to-Run-Program)
4. [Additional Documentation](#Additional-Documentation)


## Problem Description 

The Facility Location Problem (FLP) is a classic optimization problem that determines the best location for a factory or warehouse to be placed based on geographical demands, facility costs, and transportation distances (Cantlebary). For this project, our assignment focused only on distances between facilities and cities that are served. These factories/warehouses (facilities), serve any amount of cities within a specified distance and serve the city that they are located in. 

The goal of this project is to find the most efficient facility locations for cities that are within 300 miles and 800 miles of a facility, such that there are the least amount of facilities possible and every city is served. 

This problem is complex and requires lots of different algorithms. For example, the function countUnservedCities finds the cities that are "nearby" a given city using the function nearbyCities. It then counts how many of these nearby cities have not been served yet and returns this number to the locateFacilities function.

Additionally, the program includes functions such as getCoordinates, getPopulation, and getDistance, which each return the respective characteristic about whichever city you are searching for within the data.

## Data Description

The miles.dat data file contains the city name, state, coordinates, population, and distance in miles from each of the cities above it, for 128 cities from 1949 mileage data. 

Ex. 

Yakima, WA [4660,12051] 49826 
<br>1513 2410</br>

= 

City Name, State Abbreviation [Latitude, Longitude] Population
<br>Distance from Yankton SD,  Distance from Youngstown OH</br>


## How to Run Program

There are 2 ways to run the program, the first being to download the Python file and run it, which will create the two KML files on your local computer. Or you may just download the already created visualization300.kml and visualization800.kml files in this repository onto your computer and skip the Python step. 

After the KML files have been downloaded, go to Google Earth and click File. Then click import KML files and import both files. You then should be able to view the visualizations created for each distance. Please ensure you only view one of the files at a time for accurate results. 

## Additional Documentation

Citations: 

Credit to my professor Sriram Pemmaraju for creating this extremely interesting and engaging project. 

Cantlebary, Liz, and Lawrence Li. “Facility Location Problem.” Facility Location Problem - Cornell University Computational Optimization Open Textbook - Optimization Wiki, 21 Dec. 2020, optimization.cbe.cornell.edu/index.php?title=Facility_location_problem#:~:text=The%20Facility%20Location%20Problem%20(FLP,facility%20costs%2C%20and%20transportation%20distances. 
