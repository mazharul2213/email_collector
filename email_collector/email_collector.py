fn = input("Enter File Name:") #inserting the file name from where we are going to extract the email
if len(fn) < 1 :               #condition that if we dont insert any file name than it will execute following command
    fn = "mbox.txt"            #this will take the mbox.txt as default file name.
    print("default file name activated")

fo = open(fn)                  #making the file readable
count = 0                      #set the count variable as 0
dt = list()                    #creating a list to store emails

for line in fo:                #creating a for loop to read lines in the file
    line = line.strip()        #separeting all lines in the document using strip function
    if line.startswith("From:"):  #if condition applied to find if a line starts with "From:"
        #print(line)
        data = line.split()    #using split function to separate all the words in a line
        print(data[1])
        email = data[1]        #storing the data of array position 1 into email variable
        count = count + 1      #incrementing the count variable to match if the list and count variable have same size
        print(count)
        if email not in dt:    #searching that if the email variable is already in the list. if not in the list than floowing command will execute
            dt.append(email)   #this will insert the email to the list using append function

print(dt)                      #here we are printing the list that have all the emails we need
size = len(dt)                 #using len function we are measuring the length of the list
if size == count:              #here we are compareing the size of the list with email counter.
    print("There were", size, "emails in the file with From as the first word")
else:
    print("Total emails are ", count , "in number and emails in the list are " , size , "in number")