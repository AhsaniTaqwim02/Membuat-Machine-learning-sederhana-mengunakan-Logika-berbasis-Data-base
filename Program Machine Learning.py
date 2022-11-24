from sklearn.neighbors import NearestCentroid

# Database: Gerbang logika AND
# x = Data, Y = Target
x = [[0,0,1], [0,1,0], [1,0,0], [0,1,1], [1,1,0], [1,1,1], [0,0,2], [0,2,0], [2,0,0]]
y = [0,0,0,1,0,2]

#Training and classify
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

# Prediksi
print ("Logika AND Metode Desicion Tree")
print ("Logika = prediksi")
print ("0 0 1 = ", clf,predict([[0,0,1]]))
print ("0 1 0 = ", clf,predict([[0,1,0]]))
print ("1 0 0 = ", clf,predict([[1,0,0]]))
print ("0 1 1 = ", clf,predict([[0,1,1]]))
print ("1 1 0 = ", clf,predict([[1,1,0]]))
print ("1 1 1 = ", clf,predict([[1,1,1]]))
print ("0 0 2 = ", clf,predict([[0,0,2]]))
print ("0 2 0 = ", clf,predict([[0,2,0]]))
print ("2 0 0 = ", clf,predict([[2,0,0]]))
