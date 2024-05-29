# NOTE :- Do NOT use the inbuilt function for calculating KL Distance, Bhattacharyya Distance and 
# Cosine Distance directly, you can use functions required to build the distances from scratch like inverse of a matrix, etc. 


# Calculate the distance between the two normalized histograms H1 and H2 using each of the following methods:

# (a) KL Distance

# (b) Bhattacharyya Distance

from math import log2, sqrt,log

H1 = [ 0.24, 0.2, 0.16, 0.12, 0.08, 0.04, 0.12, 0.04]
H2 = [ 0.22, 0.23, 0.16, 0.13, 0.11, 0.08, 0.05, 0.02]

kl=sum([H1[i]*log2(H1[i]/H2[i]) for i in range(len(H1))])
print("KL Distance: ",kl)

bhattacharyya_coefficient=sum([sqrt(H1[i]*H2[i]) for i in range(len(H1))])
bhattacharyya=-log(bhattacharyya_coefficient)
print("Bhattacharyya Distance: ",bhattacharyya)














