# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 09:07:41 2024

@author: triki
"""

from mrjob.job import MRJob

class MRWordFreqCount(MRJob):
    def mapper(self,_,line):
        words=line.split(" ")
        for word in words:
            yield word,1
    
    def combiner(self,word,count):
        yield word,sum(count)
    
    
    def reducer(self,word,count):
        yield word,sum(count)
        


if __name__=='__main__':
    MRWordFreqCount.run()