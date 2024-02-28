'''
this is an activity for GCIS 123 activity 2 by Zarak Khan , Khaled, Nour 

'''

decision=int(input("put in if you want 1 2 or 3 \n 1:do you want dhs to another currency \n 2: Do you want another currecny to dhs")) 
decision2=int(input("input the amount you wish to convert"))


#start out with the main introduction to the program 





print("Hello welcome o the Currency Converter ")
print('Here you can convert ')


#step 1 user input, if they want xyz to dhs or they want dhs to xyz 
 

def AskUserInputForCurrencyType():
    decision=int(input("put in if you want 1 2 or 3 \n 1:do you want dhs to another currency \n 2: Do you want another currecny to dhs")) 
    if decision ==1:
        print("hello")
        conversionXYZtoDHS()
    

    if decision == 2:
        print("number2")  

          




def conversionXYZtoDHS():
    print("hello")
    decision3=int(input("choose one of the following \n 1: do you want  RMB to dhs\n 2: do you want rubles to dhs \n 3:euros to DHS "))
    if decision3 ==2:
        convertedRMBtoDHs=decision2/2.5
        print(convertedRMBtoDHs)
    elif decision3 == 2:
        convertedRublestoDHS= decision2/5
        print(convertedRublestoDHS)
    elif decision3 == 3:
        ConvertedEuroToDhs = decision3*6.2   
    else:
        print("input the values listed above ")


    




def askUserAmount():
    print("hello")
    
    



def main():
    
    
    AskUserInputForCurrencyType()
    
    

main()


