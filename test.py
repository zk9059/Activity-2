#test for activity 2 
'''
Docsstrings

Activity 2 done by 




'''






#listed here are all the conversion rates in variables




Aed_to_Eruo=0.25
Aed_to_British_pound= 0.22
Aed_to_Dollars= 0.27


Dollar_to_AED= 3.67
British_Pound_to_Aed= 4.65
Euro_to_AED= 3.98



def Menu():
    print("          Main Menu  ")
    print("welcome to the Currency Converter ")
    print('------------------------------------')
    print("")


def Conversion_direction_selection(Money,Amount):
    print("select one of the following options:")
    selection=int(input("Select the conversion direction: \n 1. AED to other currencies \n 2. Other currencies to AED \n 3. Exit"))
    if selection ==1:
        print("decision 1 ")
        
        AED_to_other_currencies(Money)
    elif selection== 2:
        print("decsion 2")  
        Other_currencies_to_Aed(Amount)

    else:
        print('exiting program' )
        exit()    


#THIS IS FOR OTHER CURRENCIES TO AED


def Other_currencies_to_Aed(Amount):
    print('enter choices 1 2 or 3')
    print('1. Euro (EUR) to AED')
    print('2. British Pound (GBP) to AED')
    print('3. Dollar to AED')
    print('4. Exit')
    Choice_Currency = int(input('enter subchoice here '))
    if Choice_Currency ==1 :
        eur_to_aed(Amount)
    elif Choice_Currency == 2:
        britishPound_to_aed(Amount)
    elif Choice_Currency==3:
        dollar_to_aed(Amount)
    else:
        exit()        




def dollar_to_aed(Amount):
    Converted_Result= Amount*Dollar_to_AED
    print('the amount in aed is ' + str(Converted_Result))


def britishPound_to_aed(Amount):
    Converted_Result= Amount*British_Pound_to_Aed
    print('the amount in AED is '+ str(Converted_Result))


def eur_to_aed(Amount):
    Converted_Result= Amount*Euro_to_AED
    print(Amount +' in AED is '+ Converted_Result )















        

def Amount_to_be_Converted():
    print("input the amount of money you would like to convert")
    Amount= float(input(""))
    return Amount

#the following code is for AED to other currencies 
        

def AED_to_other_currencies(Money):

    #decide which currecny you want to take 
    print('money ')
    print("Enter Choice 1/2/3 ")
    print("1. AED to Euro (EUR)")
    print('2. AED to British Pound (GBP)')
    print("3. AED to US Dollar")
    print("4. AED to Exit")
    Which_currency=int(input(''))

    if Which_currency ==1:
        aed_to_eur(Money)
    elif Which_currency == 2:
        aed_to_britishPound(Money)
    elif Which_currency ==3:
        aed_to_dollar(Money)    
    else:
        exit()    


            






def aed_to_britishPound(Money):
    Converted_result= Money*Aed_to_British_pound
    print(Money+' in British Pounds'+ Converted_result)





def aed_to_eur(Money):
    print(Money)
    Converted_Result=Money*Aed_to_Eruo
    print(Money+'in Euros is '+ str(Converted_Result))


def aed_to_dollar(Money):
    print("Aed to dollar")    
    Converted_Result= Money*Aed_to_Dollars
    print(Money+" in dollars is "+ str(Converted_Result))







def main():
    Menu()
    Money= Amount_to_be_Converted()
    Amount= Amount_to_be_Converted()


    Conversion_direction_selection(Money,Amount)
    #amount = Amount_to_be_Converted()
    
    







    












main()









