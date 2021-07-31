#!/usr/bin/env python
# coding: utf-8

# In[2]:


UserMovieRatings = {
    'Amy': {'Family Plot':10, 'Rebecca':5, 'Spellbound':9, 'Star Trek':6}, 
    'Bill': {'Apocalypto':8, 'Braveheart':3, 'Rebecca':10, 'Spellbound':5, 'Star Trek':7}, 
    'Cathy': {'Spaceballs':7, 'The Ice Storm':4, 'Family Plot':5, 'Rebecca':9, 'Spellbound':1}, 
    'Dave': {'Braveheart':5, 'Rebecca':7, 'Spellbound':4}, 
    'Ernie': {'Apocalypto':3, 'Braveheart':8, 'Rebecca':1, 'Star Trek':7}, 
    'Fiona': {'The Ice Storm':3, 'Family Plot':10, 'Rebecca':6, 'Spellbound':10}}


# In[3]:


def manhattan(rating1 , rating2 ):
    distance = 0
    for item in rating1.keys():
        if item in rating2.keys():
            x = rating1[item]
            y = rating2[item]
            distance += pow(abs(x-y), 1)
    return distance 


# In[4]:


userX = 'Amy'
UserX = UserMovieRatings[userX]


# In[5]:


print(UserX)


# In[18]:


userX = 'Bill'
UserX = UserMovieRatings[userX]

manhattanList = []
for keyOfUserY,valueOfUserY in UserMovieRatings.items():
    if userX != keyOfUserY:
        distXY = manhattan(UserX,valueOfUserY)
        tup = (keyOfUserY, distXY)
        manhattanList.append(tup)

print("Manhattan distance between UserX and all other Users")        
print(manhattanList)        

from operator import itemgetter
print("Sorted List with Manhattan distance between UserX and all other Users")
sortedManhattanList = sorted(manhattanList, key=itemgetter(1))
print(sortedManhattanList)

print("The Neighbor with the Smallest Manhattan Distance is UserXNN")
UserXNN = sortedManhattanList[0]
print(UserXNN)

UserXNN_name = UserXNN[0]
print(UserXNN_name)


# In[19]:


userY = UserXNN_name
UserY = UserMovieRatings[userY]
print(UserY)


# In[22]:


recommendations = []
for key, value in UserY.items():
    if key not in UserX.keys():
        tup = (key, value)
        recommendations.append(tup)

print("Recommendations for UserX by UserY")        
print(recommendations)


# In[ ]:




