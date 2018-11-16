import sys

file_path = r'c:\temp\data_input\orders.csv'
 

with open(file_path, "r") as file:
     
        for line in file:
            
            line = line.replace('\n','')
            order = line.split(',')
         
            try:  
                pharmacy_name = order[0]
                item = order[1]
                amount = int(order[2])

                print('Order from drugstore %s, item "%s", amounr %d' %(pharmacy_name, item, amount))
                        
            except:
                print('Problem with line:', line)
                print(sys.exc_info()[0])

print() 
print("Processing finished")

