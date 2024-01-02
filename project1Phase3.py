#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Jake
"""
                    ##################
                    #PROJECT 1 PHASE 1
                    ##################


# Function that calls the load functions 

def loadData(cityList, coordList, popList, distanceList):
    
    cityList = loadCityData(cityList)
    coordList = loadCoordData(coordList)
    popList = loadPopData(popList)
    distanceList = loadDistanceData(distanceList)
    
    
# Functions that load the data from each line of the file into its respective list
    
def loadCityData(cityList):

    f = open("miles.dat")

    for line in f:
    
        if ("A" <= line[0]) and (line[0] <= "Z"):
      
            commaIndex = line.index(",")
            leftBracketIndex = line.index("[")
            cityName = line[:commaIndex]
            stateName = line[commaIndex + 1:leftBracketIndex]
            cityList.append(cityName + stateName)
    

def loadCoordData(coordList):

    f = open("miles.dat")

    for line in f:
        
        if ("A" <= line[0]) and (line[0] <= "Z"):
            
            pieces = line.split(",")
            coords = [int(pieces[1].split("[")[1]), int(pieces[2].split("]")[0])]
            coordList.append(coords)
      

def loadPopData(popList):

    f = open("miles.dat")
    
    for line in f:
        
        if ("A" <= line[0]) and (line[0] <= "Z"):
    
            pieces = line.split(",")
            pop = pieces[2].split("]")[1]
            popList.append(int(pop))
        

def loadDistanceData(distanceList):

    with open("miles.dat") as f:
        
        emptyList = []
        distanceList.append(emptyList)
        distances = []
        
        for line in f:
            
            if line[0].isdigit():
                
                splitDist = line.split()
            
                for ind in splitDist:
                    
                    i = 0
                      
                    while i < len(ind) and ind[i].isdigit():
                        
                        i += 1
                        
                    distances.append(int(ind[:i]))
    
            else:
                
                if distances:
                    
                    distances.reverse()
                    distanceList.append(distances)
                    distances = []
                    
        if distances:
            
            distances.reverse()
            distanceList.append(distances)
        

# Function that returns a specific cities coordinates

def getCoordinates(cityList, coordList, name):

    if name in cityList:
        
        ind = cityList.index(name)
        return coordList[ind]
    

# Function that returns a specific cities population

def getPopulation(cityList, popList, name):

    if name in cityList:
        
        ind = cityList.index(name)
        return popList[ind]
    
    
# Function that returns the distance between the first city and the second city
    
def getDistance(cityList, distanceList, name1, name2):
    
    index1 = cityList.index(name1)
    index2 = cityList.index(name2)
    
    if index1 == index2:
        
        return 0
    
    elif index1 < index2:
        
        return distanceList[index2][index1]
    
    else:
        
        return distanceList[index1][index2]



# Function that returns a list of cities that are within r distance of the specified city


def nearbyCities(cityList, distanceList, name, r):

    nearbyList = [] 
    i = cityList.index(name) 
    j = 0 

    for d in distanceList[i]: 
        
        if d <= r: 
            
            nearbyList += [cityList[j]]
            
        j += 1 
        
    j = i + 1 
      
    while j < len(distanceList): 
        
        if distanceList[j][i] <= r: 
            
            nearbyList += [cityList[j]] 
            
        j += 1 
        
    return nearbyList




            ##################
            #PROJECT 1 PHASE 2
            ##################


# Function that counts unserved cities within r distance of city index i 

def countUnservedCities(cityList, served, distances, r, i):

    count = 0
    nearbyList = nearbyCities(cityList, distances, cityList[i], r)
    nearbyList.append(cityList[i])
    
    for city in nearbyList:
        
        cityIndex = cityList.index(city)
        
        if not served[cityIndex]:
            
            count += 1
            
    return count
 

# Function that returns a list of cities where facilities should be located in order to serve
# all cities in the city list, such that all cities are within r distance of a facility


def locateFacilities(cityList, distanceList, r):

    facilities = []
    served = [False] * 128
    
    while not all(served):
        
        max_unserved = -1
        max_index = -1
        
        for i in range(len(cityList)):
            
            unserved = countUnservedCities(cityList, served, distanceList, r, i)
            
            if unserved > max_unserved:
                
                max_unserved = unserved
                max_index = i
                
        facilities.append(cityList[max_index])
        served[max_index] = True
        nearbyList = nearbyCities(cityList, distanceList, cityList[max_index], r)
        nearbyServes = []
    
        for i in range(len(nearbyList)):
            
            ind = cityList.index(nearbyList[i])
            served[ind] = True
            nearbyServes.append(nearbyList[i])
                                                                                
        
    return facilities



            ##################
            #PROJECT 1 PHASE 3
            ##################


# Functions that write kml code into a text file in order to create a Google Earth visual


# Display for distance 300


def display300(fac300, cityList, distanceList, coordList):

    f = open('visualization300.kml', 'a')
    
    f.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n')
    f.write('<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n')
    
    f.write('<Document>\n')
    
    nearbyList = locateFacilities(cityList, distanceList, 300)
    
    f.close()
    
    insertFacilities300(fac300, cityList, coordList, nearbyList)
    insertNearbyCities300(fac300, cityList, coordList, nearbyList, distanceList)
    insertLines300(fac300, cityList, coordList, distanceList, nearbyList)
    
    
    f = open('visualization300.kml', 'a')
    f.write('</Document>\n')
    f.write('</kml>')
    f.close()


# Display for distance 800


def display800(fac800, cityList, distanceList, coordList):

    f = open('visualization800.kml', 'a')
    
    f.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n')
    f.write('<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n')
    
    f.write('<Document>\n')
    
    nearbyList = locateFacilities(cityList, distanceList, 800)
    
    f.close()
    
    insertFacilities800(fac800, cityList, coordList, nearbyList)
    insertNearbyCities800(fac800, cityList, coordList, nearbyList, distanceList)
    insertLines800(fac800, cityList, coordList, distanceList, nearbyList)
    
    f = open('visualization800.kml', 'a')
    f.write('</Document>\n')
    f.write('</kml>')
    f.close()



# Insert facility pins for distance 300 


def insertFacilities300(fac300, cityList, coordList, nearbyList):

    f = open('visualization300.kml', 'a')
    
    f.write('<Style id="facilitiesColor">\n')
    f.write('<IconStyle>\n')
    f.write('<color>ff00ff00</color>\n') 
    f.write('</IconStyle>\n')
    f.write('</Style>\n')


    for i in range(len(nearbyList)):
    
        fac300coords = getCoordinates(cityList, coordList, fac300[i])
    
        
        formattedLong = '-'+str(fac300coords[1])[:-2]+'.'+str(fac300coords[1])[-2:]
        formattedLat = str(fac300coords[0])[:-2]+'.'+str(fac300coords[0])[-2:]
        
        f = open('visualization300.kml', 'a')
        f.write('<Placemark>\n')
        f.write('<name>'+fac300[i]+'</name>\n')
        f.write('<description>Facility</description>\n')
        f.write('<styleUrl>#facilitiesColor</styleUrl>\n')
        f.write('<Point>\n')
        f.write('<coordinates>'+formattedLong+','+formattedLat+',0</coordinates>\n')
        f.write('</Point>\n')
        f.write('</Placemark>\n')
    
        
    f.close()
    
# Insert city pins for distance 300 

def insertNearbyCities300(fac300, cityList, coordList, nearbyList, distanceList):

    f = open('visualization300.kml', 'a')
    
    f.write('<Style id="nearbyCitiesColor">\n')
    f.write('<IconStyle>\n')
    f.write('<color>ffff00ff</color>\n') 
    f.write('</IconStyle>\n')
    f.write('</Style>\n')
    
    for i in range(len(cityList)):
        
        if cityList[i] not in fac300:
    
            nearbyCitiesCoords300 = getCoordinates(cityList, coordList, cityList[i])
            formattedLong = '-'+str(nearbyCitiesCoords300[1])[:-2]+'.'+str(nearbyCitiesCoords300[1])[-2:]
            formattedLat = str(nearbyCitiesCoords300[0])[:-2]+'.'+str(nearbyCitiesCoords300[0])[-2:]
    
            
            f = open('visualization300.kml', 'a')
            f.write('<Placemark>\n')
            f.write('<name>'+cityList[i]+'</name>\n')
            f.write('<description>City within 300 miles of facility</description>\n')
            f.write('<styleUrl>#nearbyCitiesColor</styleUrl>\n')
            f.write('<Point>\n')
            f.write('<coordinates>'+formattedLong+','+formattedLat+',0</coordinates>\n')
            f.write('</Point>\n')
            f.write('</Placemark>\n')
    
        
    f.close()


# Insert facility pins for distance 800


def insertFacilities800(fac800, cityList, coordList, nearbyList):

    f = open('visualization800.kml', 'a')
    
    f.write('<Style id="facilitiesColor">\n')
    f.write('<IconStyle>\n')
    f.write('<color>ff00ffff</color>\n') 
    f.write('</IconStyle>\n')
    f.write('</Style>\n')
    
    
    
    for i in range(len(nearbyList)):
    
        fac800coords = getCoordinates(cityList, coordList, fac800[i])
    
        
        formattedLong = '-'+str(fac800coords[1])[:-2]+'.'+str(fac800coords[1])[-2:]
        formattedLat = str(fac800coords[0])[:-2]+'.'+str(fac800coords[0])[-2:]
        f = open('visualization800.kml', 'a')
        f.write('<Placemark>\n')
        f.write('<name>'+fac800[i]+'</name>\n')
        f.write('<description>Facility</description>\n')
        f.write('<styleUrl>#facilitiesColor</styleUrl>\n')
        f.write('<Point>\n')
        f.write('<coordinates>'+formattedLong+','+formattedLat+',0</coordinates>\n')
        f.write('</Point>\n')
        f.write('</Placemark>\n')
        
    f.close()
    
    
# Insert city pins for distance 800 

def insertNearbyCities800(fac800, cityList, coordList, nearbyList, distanceList):

    f = open('visualization800.kml', 'a')
    
    f.write('<Style id="nearbyCitiesColor">\n')
    f.write('<IconStyle>\n')
    f.write('<color>ff0090ff</color>\n')
    f.write('</IconStyle>\n')
    f.write('</Style>\n')
    
    for i in range(len(cityList)):
        if cityList[i] not in fac800:
                nearbyCitiesCoords800 = getCoordinates(cityList, coordList, cityList[i])
                formattedLong = '-'+str(nearbyCitiesCoords800[1])[:-2]+'.'+str(nearbyCitiesCoords800[1])[-2:]
                formattedLat = str(nearbyCitiesCoords800[0])[:-2]+'.'+str(nearbyCitiesCoords800[0])[-2:]
                    
                f = open('visualization800.kml', 'a')
                f.write('<Placemark>\n')
                f.write('<name>'+cityList[i]+'</name>\n')
                f.write('<description>City within 800 miles of facility</description>\n')
                f.write('<styleUrl>#nearbyCitiesColor</styleUrl>\n')
                f.write('<Point>\n')
                f.write('<coordinates>'+formattedLong+','+formattedLat+',0</coordinates>\n')
                f.write('</Point>\n')
                f.write('</Placemark>\n')
    
        
    f.close()


# Insert lines for distance 300 

def insertLines300(fac300, cityList, coordList, distanceList, nearbyList):

    f = open('visualization300.kml', 'a')
    
    f.write('<Style id="yellowLine">\n')
    f.write('<LineStyle>\n')
    f.write('<color>ff00ffff</color>\n')
    f.write('<width>2</width>\n')
    f.write('</LineStyle>\n')
    f.write('</Style>\n')
    
    maxDist = 10000000
    
    for i in range(len(cityList)):
        
        if cityList[i] not in fac300:
            
            cityIndex = -1
            facIndex = -1
            
            for facility in range(len(fac300)):
                
                distance = getDistance(cityList, distanceList, cityList[i], fac300[facility])
                
                if cityIndex == -1 or distance < maxDist:
                    
                    maxDist = distance
                    cityIndex = i
                    facIndex = facility
            
    
            
            fac300coords = getCoordinates(cityList, coordList, fac300[facIndex])
            fac300LineCoords = getCoordinates(cityList, coordList, cityList[cityIndex])
        
    
            formattedLong1 = '-'+str(fac300coords[1])[:-2]+'.'+str(fac300coords[1])[-2:]
            formattedLat1 = str(fac300coords[0])[:-2]+'.'+str(fac300coords[0])[-2:]
            formattedLong2 = '-'+str(fac300LineCoords[1])[:-2]+'.'+str(fac300LineCoords[1])[-2:]
            formattedLat2 = str(fac300LineCoords[0])[:-2]+'.'+str(fac300LineCoords[0])[-2:]
        
            f.write('<Placemark>\n')
            f.write('<name>Edge</name>\n')
            f.write('<description>A yellow line: '+fac300[facIndex]+' to '+cityList[cityIndex]+'</description>\n')
            f.write('<styleUrl>#yellowLine</styleUrl>\n')
            f.write('<LineString>\n')
            f.write('<coordinates>'+formattedLong1+','+formattedLat1+',0,'+formattedLong2+','+formattedLat2+',0</coordinates>\n')
            f.write('</LineString>\n')
            f.write('</Placemark>\n')
            
    f.close()
    
    
# Insert lines for distance 800 

def insertLines800(fac800, cityList, coordList, distanceList, nearbyList):

    f = open('visualization800.kml', 'a')
    
    f.write('<Style id="redLine">\n')
    f.write('<LineStyle>\n')
    f.write('<color>9f0000ff</color>\n')
    f.write('<width>1</width>\n')
    f.write('</LineStyle>\n')
    f.write('</Style>\n')
    
    maxDist = 10000000
    
    for i in range(len(cityList)):
        
        if cityList[i] not in fac800:
            
            cityIndex = -1
            facIndex = -1
            
            for facility in range(len(fac800)):
                
                distance = getDistance(cityList, distanceList, cityList[i], fac800[facility])
                
                if cityIndex == -1 or distance < maxDist:
                    
                    maxDist = distance
                    cityIndex = i
                    facIndex = facility
            
    
            
            fac800coords = getCoordinates(cityList, coordList, fac800[facIndex])
            fac800LineCoords = getCoordinates(cityList, coordList, cityList[cityIndex])
                
    
            formattedLong1 = '-'+str(fac800coords[1])[:-2]+'.'+str(fac800coords[1])[-2:]
            formattedLat1 = str(fac800coords[0])[:-2]+'.'+str(fac800coords[0])[-2:]
            formattedLong2 = '-'+str(fac800LineCoords[1])[:-2]+'.'+str(fac800LineCoords[1])[-2:]
            formattedLat2 = str(fac800LineCoords[0])[:-2]+'.'+str(fac800LineCoords[0])[-2:]
        
            f.write('<Placemark>\n')
            f.write('<name>Edge</name>\n')
            f.write('<description>A red line: '+fac800[facIndex]+' to '+cityList[cityIndex]+'</description>\n')
            f.write('<styleUrl>#redLine</styleUrl>\n')
            f.write('<LineString>\n')
            f.write('<coordinates>'+formattedLong1+','+formattedLat1+',0,'+formattedLong2+','+formattedLat2+',0</coordinates>\n')
            f.write('</LineString>\n')
            f.write('</Placemark>\n')
            
    f.close()
        
        
# Main
    
def main():
    
    cityList = []
    coordList = []
    popList = []
    distanceList = []
    
   
    
    loadData(cityList, coordList, popList, distanceList)
    
    fac300 = locateFacilities(cityList, distanceList, 300)
    fac800 = locateFacilities(cityList, distanceList, 800)
    
    display300(fac300, cityList, distanceList, coordList)
    display800(fac800, cityList, distanceList, coordList)




if __name__ == "__main__":
    main()


