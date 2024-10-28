# ამოცანა 3: (5ქულა)
# დაწერეთ პროგრამა რომელიც პირველ ნაბიჯზე მომხმარებლისგან მიიღებს შესატანი სტრიქონების რაოდენობას.
# მომხმარებელმა სტრიქონების შეტანა უნდა განახორციელოს წყვილ-წყვილად: სიტყვა და მისი სინონიმი.
# სიტყვა-სინონიმების შეტანის შემდეგ მომხმარებელმა უნდა დაწეროს საძიებო სიტყვა და პროგრამამ უკვე შეტანილი ინფორმაციის ბაზაზე
# იპოვოს მომხმარებლის მიერ საძიებო სიტყვის სინონიმი და გამობეჭდოს ეკრანზე.
#
# მაგალითად:
# 1 ნაბიჯი: პროგრამა ეკითხება მომხმარებელს რამდენი სტრიქონისგან შედგება მისი სიტყვა-სინონიმების ლექსიკონი, ვთქვათ შეიტანა მომხმარებელმა 2;
# 2 ნაბიჯი: მომხმარებელს შეაქვს 2 სტრიქონზე სიტყვა-სინონიმები დაშორებით, ვთქვათ:
#         Hi Hello           (პირველი სტრიქონი)
#         List Array        (მეორე სტრიქონი)
# 3 ნაბიჯი: მომხმარებელს შეაქვს სიტყვა რომლის სინონიმსაც ის ეძებს, ვთქვათ მან შეიტანა სიტყვა: List
# 4 ნაბიჯი: პროგრამა მიღებულ სიტყვას დაძებნის ლექსიკონში სინონიმის არსებობაზე და დაბეჭდავს ეკრანზე პასუხს: Array

synonym_dict={} #using key:value dict

how_many=int(input("Please enter synonyms dictionary lines you're going to fill: "))
for x in range(how_many):
    entry_line=input("Please input 2 synonym words separated by space (example: Hi Hello): ").strip().lower() #preformat before adding to dict
    mylist=entry_line.split()
    synonym_dict[mylist[0]]=mylist[1] # Create dictionary of synonyms

find_word=input("Please enter the word of which synonym you're looking for: ").strip().lower()

for x,y in synonym_dict.items(): #Search dictionary for keys or values to be equal to input and print if found
    if x==find_word:
        print(f"Synonym for '{find_word}' is '{y}'")
        break
    if y==find_word:
        print(f"Synonym for '{find_word}' is '{x}'")
        break




