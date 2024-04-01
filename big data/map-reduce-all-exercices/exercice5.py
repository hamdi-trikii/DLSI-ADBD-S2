# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 06:56:06 2024

@author: triki
"""

from mrjob.job import MRJob

class MRFriendsbyAge(MRJob):
    
    def mapper(self, _, line):
        id, name, age, num_friends = line.split(',')
        yield age, int(num_friends)
        
    def reducer(self, age, num_friends):
        friend_list = list(num_friends)
        average_friends = sum(friend_list) / len(friend_list) if friend_list else 0
        yield age, average_friends

if __name__ == '__main__':
    MRFriendsbyAge.run()
