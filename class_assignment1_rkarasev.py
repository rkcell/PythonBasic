# დავწეროთ პროგრამა, რომელიც:
#
# 1) მიიღებს საჭადრაკო დაფის 2 უჯრის კოორდინატებს (x1,x2 და y1,y2);
# 2) შეტანილი უჯრების მიხედვით გამოავლინოს არის თუ არა ორივე უჯრა ერთი და იგივე ფერის, თუ კი მაშინ გამოიტანოს ეკრანზე შეტყობინება "YES", თუ არა - "NO";
# 3) პირობის ოპერატორების გამოყენებით გააკონტროლეთ, რომ მომხმარებელმა შეიტანოს უჯრების კოორდინატები 1-8-ს დიაპაზონში;
# 4) დაწერილი კოდი აქვე ატვირთეთ "py" ფაილის სახით.
#
# შენიშვნა: ჭადრაკის უჯრების დასანომრად გამოიყენეთ დიაპაზონი (1-8)

# O , 1
# 1,  O

input_string_x1x2= input("Please enter chessboard coordinates in range of 1-8 of X1 and X2 separated by space:")
input_string_y1y2= input("Please enter chessboard coordinates in range of 1-8 of Y1 and Y2 separated by space:")

x1 = int(input_string_x1x2[0])
x2 = int(input_string_x1x2[2])
y1 = int(input_string_y1y2[0])
y2 = int(input_string_y1y2[2])

#checking the input integers are in range of 1-8 or program finishes with alert message
if x1 not in range(1,9) or x2 not in range(1,9) or y1 not in range(1,9) or y2 not in range(1,9):
    print ("Incorrect data input, restart the program and try again")
else:
#program continues:
#reducing chessboard to 2x2 matrix by module operation %2, results to be 0 or 1 as white or black, like following:
# O , 1
# 1,  O

    fx1=x1%2
    fx2=x2%2
    fy1=y1%2
    fy2=y2%2

#checking and printing out the results
    if fx1==fx2:
        if fy1==fy2:
            print("YES")
        else:
            print("NO")
    elif fy1==fy2:
        print("NO")
    else:
        print("YES")