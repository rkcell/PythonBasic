# ლეონარდს სტუმრად მოუვიდა თავისი  ბიძაშვილი დეივიდი. ლეონარდი ქვეყნის მარკების შეგროვებით იყო გატაცებული
# და თითქმის ყველა ქვეყნის მარკა აქვს (ზოგის რამდენიმე ცალი ეგზემპლარიც). ლეონარდმა გადაწყვიტა ბიძაშვილისთვის
# ის მარკები ეჩუქებინა, რომლებიც რამდენიმეცალი ჰქონდა ერთნაირი. მაგალითად ჩინეთის მარკა 5 ცალი ჰქონდა და ერთს დეივიდს აჩუქებდა.
# თუმცა ამერიკის მხოლოდ ერთი ჰქონდა და იმას ვერ აჩუქებდა. (რუსეთის საერთოდ არ ჰქონდა). მოკლედ, ძალიან დაიბნა და გადაწყვიტა,
# რომ პროგრამა დაეწერა. ყველა ქვეყანას უკან აწერია უნიკალური კოდი, რაც დაგეხმარებათ ამ ქვეყნების გაფილტვრაში.
# მაგალითად: ჩინეთი - 1, საქართველო - 2, იაპონია - 3 და ა.შ. (ეს შეგიძლიათ თქვენით მიანიჭოთ)

number_of_countries=int(input("Please enter the number how many countries stamps total exists: "))
stamps={} #Using dictionary
for x in range(number_of_countries): #Creating stamps library
    code_country=int(input(f"Please enter the country code N{x+1}: "))
    num_stamps= int(input("Please enter how many stamps you have of this country: "))
    stamps[code_country]=num_stamps

sharing_codes=set() #Creating a set for stamps countries to share
for stamp,total in stamps.items():
    if total>1:
        sharing_codes.add(stamp)

if len(sharing_codes)>0:
    print("The list to share stamps is: ", sharing_codes)
else:
    print("All stamps are unique, have nothing to share currently...")