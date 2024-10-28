# ამოცანა N2. შექმენით პროგრამა – სპეციალური ტაბულა (5ქულა)
# პროგრამის მუშაობის ლოგიკა:მომხმარებელმა უნდა შეიტანოს 2 მთელი რიცხვი ( x და y )
# ასევე მომხმარებელმა უნდა შეიტანოს კვადრატის ან კუბის განმსაზღვრელი
# იდენტიფიკატორი: 2 ან 3იმისდა მიხედვით თუ რისი გამოთვლა სურს მომხმარებელს,
# პროგრამამ აწარმოოს გაანგარიშება შემდეგი ფორმულებით:
# - კვადრატისთვის:  ( x - y )2
# - კუბისთვის:           ( x - y )3
# პროგრამამ ასევე უნდა შეადგინოს პასუხების ტაბულა, რომელიც იქნება x რაოდენობის სტრიქონისგან და y რაოდენობის სვეტისგან შემდგარი.
# შედეგები დაიბეჭდოს ეკრანზე.

input_x=int(input("Please enter number x: "))
input_y=int(input("Please enter number y: "))
input_ident=int(input("Please select id 2 or 3: "))

result=(input_x-input_y)**input_ident

svetebi=[]  #creating the tabula line as list
for r in range(input_y):
    svetebi.append(result)

for s in range(input_x): #print x-number of lines
    print(*svetebi) #easy decompress the list