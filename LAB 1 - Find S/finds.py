import csv
a=[]
with open('data.csv','r') as data1:
    for row in csv.reader(data1):
        a.append(row)
    print(a)
    print("The total number of training examples are : ",len(a))
num_attributes=len(a[0])-1
print("\n The initial hypothesis is : ")
hypothesis = ['0']*num_attributes
print(hypothesis)
for i in range(0,len(a)):
    if a[i][num_attributes]=='yes':
        for j in range(0,num_attributes):
            if hypothesis[j]=='0' or hypothesis[j]==a[i][j]:
                hypothesis[j]=a[i][j]
            else:
                hypothesis[j]='?'
    print("\n The hypothesis for the training example {} is :\n" .format(i+1),hypothesis)
print("\n The Maximally specific hypothesis for the training instances is")
print(hypothesis)
