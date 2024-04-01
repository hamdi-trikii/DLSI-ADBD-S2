# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 08:37:17 2024

@author: triki
"""

from mrjob.step import MRStep
from mrjob.job import MRJob


class SpendByCustomer(MRJob):

    def mapper(self,_,line):
        (customerID,orderID,orderAmount)=line.split(',')
        yield customerID,float(orderAmount)
    
    
    def reducer(self, customerID, orders):
        yield customerID,sum(orders)
        
    def mapper_make_amounts_key(self,customerID,orderTotal):
        yield '%04.02f'%float(sum(orderTotal)),customerID
        
    def reducer_output_results(self,orderTotal,customerIDs):
        for customerID in customerIDs:
            yield orderTotal,customerID
            
    def step(self):
        return[
            MRStep(mapper=self.mapper,reducer=self.reducer)
            ,
            MRStep(mapper=self.mapper_make_amounts_key,reducer=self.reducer_output_results)
            ]
        

if __name__=='__main__':
    SpendByCustomer.run()