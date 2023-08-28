#Main functions
#here the statement defined in other functions file
''' if __name__=="__main__": 
    print("Hello World 2")
    main()'''
#the above statement will not work because main define above will not match to the file name of this file  
import M1_OtherFunctions
import M1_Task_06_CalculatorInPython
print(M1_OtherFunctions.add(1,2))
print(M1_OtherFunctions.sub(3,1))
print(M1_Task_06_CalculatorInPython.sub(3,1))
