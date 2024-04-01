# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 07:17:22 2024

@author: triki
"""
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
        
if __name__== "__main__":
    MRWordFreqCount.run()