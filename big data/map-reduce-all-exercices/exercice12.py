# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 06:01:40 2024

@author: triki
"""

from mrjob.job import MRJob
from mrjob.step import MRStep
class find_movie_most_rated(MRJob):
    def steps(self):
        return[
            MRStep(mapper=self.mapper,reducer=self.reducer_nb)
            ,
            MRStep(reducer=self.reducer_find_max)
            ]
    def mapper(self,_,line):
        (user,movie,rating,timestamp)=line.split('\t')
        yield movie,1;
    def reducer_nb(self,movie,value):
        yield None,(sum(value),movie)
        
    def reducer_find_max(self, movie, counts):
        yield max(counts)



if __name__=='__main__':
    find_movie_most_rated.run()