#Ex 4.19
import math
import random

class Polymer:
    """ A class representing a random-flight polymer in solution."""

    def __init__(self, N,a):
        """
        Initialize a Polymer object with N segments , each of length a"""

        self.N, self.a= N,a
        #self.xyz holds the segment position vectors as tuples
        self.xyz= [(None,None,None)]*N
        #end-to-end vectors
        self.R= None
        #make our polymer by assigning segment positions.

    def make_polymer(self):
        """
        Calculate the segment positions, center of mass and end-to-end
        distance for a random-flight polymer.
        """

        #Start our polymer off at a origin, (0,0,0)
        self.xyz[0]= x, y, z = cx, cy, cz= 0, 0, 0
        for i in range(1, self.N):
            #pick a random orientation for the next segment
            theta= math.acos(2*random.random()-1)
            phi= random.random()*2.*math.pi
            #Add on the corresponding displacement vector for this segment
            x += self.a* math.sin(theta)*math.cos(phi)
            y += self.a*math.sin(theta)* math.sin(phi)
            z += self.a* math.cos(theta)
            #store it, and update our center of mass sum
            self.xyz[i]=x,y,z
            cx,cy,cz= cx+x, cy+y, cz+z

        #calculate the position of the center of mass
        cx, cy, cz= cx/self.N, cy/self.N, cz/self.N

        #The end-to-end vector is the position of the last
        #segment, since we started at the origin.
        self.R= x,y,z

        #Finally, re-cnter our polymer on the center of mass
        for i in range(self.N):
            self.xyz[i]= (self.xyz[i][0]- cx,
                          self.xyz[i][1]- cy,
                          self.xyz[i][2]- cz)
        return self.xyz

    def calc_Rg(self):
        """
        Calculates and returns the radius of gyration, Rg. The polymer segment
        positions are already given relative to the center of mass, so
        this is just the rms position of the segments
        """

        self.Rg=0
        for x, y, z in self.xyz:
            self.Rg += x**2 + y**2 + z**2
        self.Rg= math.sqrt(self.Rg/self.N)
        return self.Rg
