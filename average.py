fh=open("output 4.txt",'w')
def average(a);
return sum(a)/len(a)
a=[1,3,5,7,9]
average=average(a)
fh.write("the average of given list is:"+str(average))
fh.close
