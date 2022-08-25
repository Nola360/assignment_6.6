#Akinola Daramola Jr
#Programming Exercise 6.6
#Due Date: 07/24/2022


"""
Average of Numbers
Assume a file containing a series of integers is named numbers.txt and
exists on the computer’s disk.
Write a program that calculates the average of all the numbers stored in the file.
"""




#Declaring mainline function
def main():

    #Creating object of file 'numbers.txt'
    numbers_file = open('numbers.txt', 'r')

    #Initializing variables 'average', 'total' and 'number_of_lines'
    average = 0
    total = 0
    number_of_lines = 0

    #Constructing a for loop to iterate through object
    for digits in numbers_file:
    
        #Adding the sum of all digits in object file 'number.txt'    
        total += int(digits)

        #number_of_line value increases 1 unit every iteration until loop ends
        number_of_lines += 1
        #print(number_of_lines)
    
        
    #Calculating the average by dividing total by number of lines in file  
    average = total / number_of_lines

    #Displaying average of sum of digits added
    print(f"Average: {average:.2f}")


    #Closing numbers file
    numbers_file.close()

#Calling mainline function
main()
