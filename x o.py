list1=[' ' , '1' , ' ' ,'|',' ','2',' ','|',' ','3',' ']
list2=[' ' , '4' , ' ' ,'|',' ','5',' ','|',' ','6',' ']
list3=[' ' , '7' , ' ' ,'|',' ','8',' ','|',' ','9',' ']
truee = True
while True:
    for i in list1:
        print(i, end="")
    print()
    for k in list2:
        print(k, end="")
    print()
    for j in list3:
        print(j, end="")
    print()
    if(truee == True):
        print("player1 :")
        cell = int(input("enter the number of the cell")) 
        truee =False
        shape = 'X'
    elif(truee == False):
        print("player2 :")
        cell = int(input("enter the number of the cell"))
        truee = True
        shape = 'O'
    if(cell == 1):
        list1[1] = shape
    elif(cell == 2):
        list1[5] = shape
    elif(cell == 3):
        list1[9] = shape
    elif(cell == 5):
        list2[5] = shape
    elif(cell == 6):
        list2[9] = shape
    elif(cell == 7):
        list3[1] = shape
    elif(cell == 8):
        list3[5] = shape
    elif(cell == 9):
        list3[9] = shape
    if(list1[1]=='X' and list1[5]=='X' and list1[9]=='X') or (list1[1]=='X' and list2[1]=='X' and list3[1]=='x') or (list2[1]=='X' and list2[5]=='x' and list2[9]=='X') or (list1[5]=='X' and list2[5]=='X' and list3[5]=='X') or (list3[1]=='X' and list3[5]=='X' and list3[9]=='X') or (list1[9]=='X' and list2[9]=='X' and list3[9]=='X') or (list1[1]=='X' and list2[5]=='X' and list3[9]=='X') or (list1[9]=='X' and list2[5]=='x' and list3[1]=='X'):
        print ("player1 is the winner")
    if(list1[1]=='O' and list1[5]=='O' and list1[9]=='O') or (list1[1]=='O' and list2[1]=='O' and list3[1]=='O') or (list2[1]=='O' and list2[5]=='O' and list2[9]=='O') or (list1[5]=='O' and list2[5]=='O' and list3[5]=='O') or (list3[1]=='O' and list3[5]=='O' and list3[9]=='O') or (list1[9]=='O' and list2[9]=='O' and list3[9]=='O') or (list1[1]=='O' and list2[5]=='O' and list3[9]=='O') or (list1[9]=='O' and list2[5]=='O' and list3[1]=='O'):
        print ("player2 is the winner")
    
        
