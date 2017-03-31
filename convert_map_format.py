import sys

fs=open(sys.argv[1])
ft=open(sys.argv[2],"w")
temp=[]
count=1
for line in fs:
  line=line.replace("\n","")
  temp=line.split("\t")
  for i in xrange(len(temp)-1):
    ft.write(temp[i]+"\t"+str(count))
    ft.write("\n")
  count+=1  
ft.close()
fs.close()
