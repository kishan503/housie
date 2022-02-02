import random
main_list = []
count = 13

while count > 1:
    ticket = random.randint(1,100)
    if ticket not in main_list:
        main_list.append(ticket)
        count -= 1

player_list = list(main_list[:6])
computer_list = list(main_list[-6:])

game_tickets = list(main_list)
random.shuffle(main_list)

print("\n\n                                MAIN TICKETS : ",end=" ")
for t in main_list:
    print(t,end=" ")
print("\n\n PLAYER TICKETS: ",end=" ")
for t in player_list:
    print(t,end=" ")
print("\n\n COMPUTER TICKETS: ",end=" ")
for t in computer_list:
    print(t,end=" ")
status = True
while status:
    start_game = int(input("\n\nPress 1 to play: "))
    if start_game == 1:
        status  =  True
        lucky_ticket = random.choice(main_list)
        print("\n\n                              !!!LUCKY TICKET!!! = ",lucky_ticket)
        if lucky_ticket in player_list:
            player_list.remove(lucky_ticket)
            if player_list == []:
                print("\n\n                      !!!PLAYER WON!!!")
                print()
                status = False
            else:
                print("\n                              ...PLAYER TABLE...")
                print("\n\n PLAYER TICKETS: ",end=" ")
                for t in player_list:
                    print(t,end=" ")
                print("\n\n COMPUTER TICKETS: ",end=" ")
                for t in computer_list:
                    print(t,end=" ")
        elif lucky_ticket in computer_list:
            computer_list.remove(lucky_ticket)
            if computer_list == []:
                print("\n\n                      !!!COMPUTER WON!!!")
                print()
                status = False
            else:
                print("\n                              ...COMPUTER TABLE...")
                print("\n\n COMPUTER TICKETS: ",end=" ")
                for t in computer_list:
                    print(t,end=" ")
                print("\n\n PLAYER TICKETS: ",end=" ")
                for t in player_list:
                    print(t,end=" ")
        elif lucky_ticket not in player_list:
            if lucky_ticket not in computer_list:
                print("\n\n                            ...TABLE TIE...")
                print("\n\n PLAYER TICKETS: ",end=" ")
                for t in player_list:
                    print(t,end=" ")
                print("\n\n COMPUTER TICKETS: ",end=" ")
                for t in computer_list:
                    print(t,end=" ")
    else:
        print("INVALID CHOICE")