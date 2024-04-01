# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 08:24:22 2024

@author: triki
"""

from mrjob.job import MRJob

class SpendByCustomer(MRJob):
    
    def mapper(self,_,line):
        (customerID,orderID,orderAmount)=line.split(',')
        yield customerID,float(orderAmount)
    
    
    def reducer(self, customerID, orders):
        yield customerID,'%04.02f'%float(sum(orders))

if __name__=='__main__':
    SpendByCustomer.run()
        