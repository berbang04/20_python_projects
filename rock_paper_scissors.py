import random
print("welcome to rock paper scissors game:")
main_list=["rock","paper","scissors"]


while True:
    your_answer=str(input("enter your answer please: "))
    machie_answer=random.choice(main_list)

    if your_answer.lower()==machie_answer.lower():
        print("no one wins")
    elif your_answer.lower()=="rock":
        if machie_answer.lower()=="paper":
            print(" u lost")
            print(your_answer,machie_answer)
            
        else:
            print("u win")        
            print(your_answer,machie_answer)
    elif your_answer.lower()=="paper":
        if machie_answer.lower()=="rock":
            print(" u lost")
            print(your_answer,machie_answer)
            
        else:
            print("u win")        
            print(your_answer,machie_answer)
    elif your_answer.lower()=="scissors":
        if machie_answer.lower()=="rock":
            print(" u lost")
            print(your_answer,machie_answer)
            
        else:
            print("u win")        
            print(your_answer,machie_answer)
    else:
        exit()                        
            
