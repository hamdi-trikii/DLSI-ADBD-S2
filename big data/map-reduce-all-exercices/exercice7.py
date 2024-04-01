# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 07:34:36 2024

@author: triki
"""

from mrjob.step import MRStep
import re
from mrjob.job import MRJob


REGEXP=re.compile(r"[\w']+")

class MRWordFreqCount(MRJob):
    
    def mapper(self,_,line):
            words=REGEXP.findall(line)
            for word in words:
                yield word.lower(),1
    
    
    def reducer(self, word, values):
        yield word,sum(values)
        
    
    #mrstep
    def mapper_make__counts_key(self,word,count):
        yield '%04d'%int(count),word
    
    
    def reducer_output_words(self,count,words):
        for word in words:
            yield count,word
    
    def steps(self):
        return[
            MRStep(mapper=self.mapper,reducer=self.reducer)
            ,
            MRStep(mapper=self.mapper_make__counts_key,reducer=self.reducer_output_words)
            ]
            
        
if __name__== "__main__":
    MRWordFreqCount.run()
        
        
        
        
        
