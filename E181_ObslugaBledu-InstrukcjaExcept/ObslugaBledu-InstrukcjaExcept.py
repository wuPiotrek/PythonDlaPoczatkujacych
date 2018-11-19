import sys
 
file_path = r'c:\temp\data_input\orders.csv'
 
 
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
 
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %
                (pharmacy_name, item, amount))
            
        except ValueError as e:
            print('Error occurs > problem with conversion to integer in line:\n', line)

        except IndexError as e:
            print('Error occurs > there are not enought fields in line:\n', line)

        except:
            print("Problem with line %s" % line)
            print(sys.exc_info()[0])
 
print("Processing finished")
