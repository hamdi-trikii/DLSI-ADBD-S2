# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 06:10:00 2024

@author: triki
"""

from mrjob.job import MRJob
class MRRatingCounter(MRJob):
    
    def mapper(self,key,line):
        (userID,movieID,rating,timestamp)=line.split('\t')
        yield rating,1
    
    def reducer(self, rating,occurences):
        yield rating, sum(occurences)

if __name__== '__main__':
    MRRatingCounter.run()
    




















