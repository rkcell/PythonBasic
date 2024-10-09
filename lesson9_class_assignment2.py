# 1. შექმენით 2 განზომილებიანი list (მატრიცა) მომხმარებლის მიერ შეტანილი რიცხვებით და ბოლოს გამოიტანეთ მატრიცა ციკლის საშუალებით (გამოიყენეთ ფუნქციები მაგ: create_matrix() or print_matrix() )
#
# 2. წინა მაგალითში შექმნილი მატრიცისთვის გამოიტანეთ რიცხვები, რომელიც მდებარეობს მთავარ დიაგონალზე და გამოიტანეთ მათი ჯამი
#
# 3. გააკეთეთ იგივე არამთავარი დიაგონალისთვის



dimension= int(input("Enter the Matrix dimension "))

matrix = []

# Insert data into the matrix
for i in range(dimension):
    row = []
    for j in range(dimension):
        value = int(input(f"Enter value for position ({i+1},{j+1}): "))
        row.append(value)
    matrix.append(row)

print("The matrix is:")
for row in matrix:
    print(row)

def main_diag_sum(matrix):
    sum = 0
    for i in range(dimension):
        sum+=matrix[i][i]
    return sum

print(main_diag_sum(matrix))


def notmain_diag_sum(matrix):
    sum = 0
    for i in reversed(range(dimension)):
        sum+=matrix[i][dimension-1-i]
    return sum

print(notmain_diag_sum(matrix))