# Do NOT use the inbuilt function for calculating KL Distance, Bhattacharyya Distance and Cosine Distance directly, 
# you can use functions required to build the distances from scratch like inverse of a matrix, etc.


# Compare two text files doc1.txt and doc2.txt using cosine distance.

# doc1.txt

# “ MATLAB is a program for solving engineering and mathematical problems. 
# The basic MATLAB objects are vectors and matrices, so you must be familiar with 
# these before making extensive use of this program.”

# doc2.txt

# “MATLAB works with essentially one kind of object, a rectangular numerical matrix. 
# Here is some basic information on using MATLAB matrix commands.”
# you can use the function CountVectorizer(), for converting the text to a matrix.


from sklearn.feature_extraction.text import CountVectorizer
from math import sqrt



def cosine_similarity(v1,v2):
    a=sum([v1[i]*v2[i] for i in range(len(v1))])
    b=sqrt(sum([v1[i]**2 for i in range(len(v1))]))
    c=sqrt(sum([v2[i]**2 for i in range(len(v2))]))
    return a/(b*c)
    

def cosine_distance(v1,v2):
    return 1-cosine_similarity(v1,v2)


f1=open("doc1.txt","r")
f2=open("doc2.txt","r")
doc1=f1.read()
doc2=f2.read()
f1.close()
f2.close()


vectorizer=CountVectorizer()
vectorizer.fit([doc1,doc2])
# print("Vocabulary: ", vectorizer.vocabulary_)
vector=vectorizer.transform([doc1,doc2]).toarray()
print(vector[0].shape,vector[1].shape)
print("Cosine Distance: ",cosine_distance(vector[0],vector[1]))








    
