m1 = int(input("Marks of 1st student:\n"))        # use int for timecasting(convert string type input into integer type)
m2 = int(input("Marks of 2nd student:\n"))
m3 = int(input("Marks of 3rd student:\n"))
m4 = int(input("Marks of 4th student:\n"))
m5 = int(input("Marks of 5th student:\n"))
m6 = int(input("Marks of 6th student:\n"))


markslist = [m1,m2,m3,m4,m5,m6]

markslist.sort()

print(markslist)