list_value1=[12,15,11,12,8,15,3,3]  
print("The initialized list is ",list_value1)  
res_list=[]  
for i in list_value1:  
    if i not in res_list:  
        res_list.append(i)  
#printing the list after removing duplicate elements  
print("The resultant list after removing duplicates is ",res_list)  
