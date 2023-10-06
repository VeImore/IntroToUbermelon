#Accesses Text Folder
log_file = open("um-server-01.txt")

#Defines Function
def generate_sales_reports(log_file):
    #Starts Loop To Go Through Each Line 
    for line in log_file:
        #Strips Empty Spaces In Lines
        line = line.rstrip()
        #Selects The Index Of The Day
        day = line[0:3]
        #Checks If Day Is A String
        if day == "Tue":
            #Prints Indicated Line
            print(line)
#Calls Function
generate_sales_reports(log_file)
