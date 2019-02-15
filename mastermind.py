import random

number_of_digits = 4
secret_code = str(random.randint(10**(number_of_digits-1), 10**(number_of_digits)-1))
##secret_code = '1244'

first_list = ['*','*','*','*','W','B']
secret_list = []
players_list = []
rep_list = []
epanal = []
counter_of_tries = 10
dict_print ={}

##for i in range(number_of_digits):
##    secret_list.append('*')




for i in range(number_of_digits):
    secret_list.append(secret_code[i])

##print(secret_list)    
print('                                                              ','W','B')
j = 1

flag = 0 
while (j < counter_of_tries+1 ) :

    ##read and validate players code
    valid_player_code = 0
    while (valid_player_code == 0):      
        players_code = input(str(number_of_digits) +' digits or Q to quit _')
        ##players_code = input('_')
        if (players_code == 'Q'  or players_code == 'q'
            or (len(players_code) == number_of_digits and players_code.isdigit() == True)):                
                valid_player_code = 1
    #############################################
    if (players_code == 'Q'  or players_code == 'q'):  
        print('Canceled')
        break
    epanal.clear()
    players_list.clear()
    whites = 0
    blacks = 0


    for i in range(number_of_digits):
        players_list.append(players_code[i])



    for i in range(number_of_digits):
        cur_digit = players_list[i]
        if cur_digit not in epanal:
            counter1 = secret_list.count(cur_digit)
            if counter1 > 0 :
                counter2 = players_list.count(cur_digit)
                if counter1 > counter2 :
                    whites = whites + counter2
                else:
                    whites = whites + counter1 
                if counter2 > 1:
                    epanal.append(cur_digit)

    for i in range(number_of_digits):
        if secret_list[i]== players_list[i]:
            blacks = blacks + 1
            whites = whites -1

    ##players_list.append(whites)
    ##players_list.append(blacks)                            
    print('                                       ',j,players_list,whites,blacks)
    ##update dict
    ###################################################
    
    j=j+1
    if (blacks == number_of_digits) :
        print('                                           ','SUCCESSFULL') 
        break
print('                                       ',secret_list)      
    
    
    


     
 


    
