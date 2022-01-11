import matplotlib .pyplot as plt
import psutil as p

dict1={}

count=0
for process in p.process_iter():
    count=count+1
    if count<=6:
        name=process.name()
        cpuUsage=p.cpu_percent()
        print("name: ",name," = Cpu Usage: ",cpuUsage)
        dict1.update({name:cpuUsage})
        
keymax=max(dict1,key=dict1.get)
keymin=min(dict1,key=dict1.get)
print(keymax,keymin)
list1=[keymax,keymin]

app=dict1.values()
maxapp=max(app)
minapp=min(app)

list2=[maxapp,minapp]

plt.figure(figsize=(15,7))
plt.xlabel("Applications")
plt.ylabel("Usage")
plt.bar(list1,list2,width=0.6,color=("Red","Blue","Green","Yellow","Cyan"))
plt.show()        
