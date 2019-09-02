import math  
def calculateDistance(x1,y1,up,down,right,left):
  x2 = x1 + right - left
  y2 = y1 + up - down
  dist = math.sqrt((x2 - x1)^2 + (y2 - y1)^2)
  dist = int(dist)
  return dist  
calculateDistance(0,0,5,3,3,2)
