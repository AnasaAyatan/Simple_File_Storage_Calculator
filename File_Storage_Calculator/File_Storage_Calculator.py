# creating a console application tht calculates the total amount of storage needed for a collection of image, executable, and system files.
# File size will all be calculated all in Kilobytes and then converted into Megabytes in the output (1024 Kilobyte = 1 Megabyte)
IMAGE_FILES = 100
EXECUTABLE_FILES = 2048
SYSTEM_FILES = 20

# ask the user to enter the number of image files, the number of executable files, and the number of system files.

# input
imageString = input("Enter the number of image files: ")
executableString = input("Enter the number of executable files: ")
systemString = input("Enter the number of system files: ")

# convert the input into a float-point number
image = float(imageString)
executable = float(executableString)
system = float(systemString)

# determine size of total files in each catagory
image *= IMAGE_FILES
executable *= EXECUTABLE_FILES
system *= SYSTEM_FILES

# calculate total file size of all catagory combined in Kilobytes
totalSizeInKB = image + executable + system

#calculate total file size of all catagory combined in Megabytes
totalSizeInMB = totalSizeInKB / 1024

#output 
print("Total amount of storage needed in Kilobytes: " + str(totalSizeInKB))
print("Total amount of storage needed in Megabytes: " + str(round(totalSizeInMB, 2)))