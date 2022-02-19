#Algorithm Design: Dr. Pira
#Chapter2 Project by Amir Nematpour - 981830281
#Shahid Madani University

import Class as c

v = int(input("Enter number of v: ")) #Number of v.
print()

if __name__ == '__main__': #Run program.
    f = c.floyd(v)
    print(f.input_num.__doc__)
    f.input_num()
    print(f.run())

quit = input("Please Press Enter To Exit.")
