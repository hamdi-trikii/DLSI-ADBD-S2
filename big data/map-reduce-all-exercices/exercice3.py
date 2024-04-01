# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 06:46:20 2024

@author: triki
"""
#i just copied exercice2 file 

from mrjob.job import MRJob 

class MRmaxTempruture(MRJob):
    
    def makefahrenheit(self,temperature):
        fahrenheit=(float(temperature)/10.0)*1.8+32.0
        return fahrenheit
    
    
    def mapper(self,_,line):
        (location,date,type,data,x,y,z,w)=line.split(',')
        if(type=='TMAX'):
            temperature=self.makefahrenheit(data)
            yield location,temperature
    
    
    
    def reducer(self, location, temperature):
        yield location , max(temperature)


if __name__ == '__main__':
    MRmaxTempruture.run()
        