# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 06:30:20 2024

@author: triki
"""

from mrjob.job import MRJob 

class MRmaxTempruture(MRJob):
    
    
    def mapper(self,_,line):
        (location,date,type,data,x,y,z,w)=line.split(',')
        if(type=='TMAX'):
            yield location,data
    
    
    
    def reducer(self, location, temperature):
        yield location , max(temperature)


if __name__ == '__main__':
    MRmaxTempruture.run()
        
        
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    