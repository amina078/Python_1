input_girls = int(input ("please enter the number of girls that come to the party: "))
input_boys = int(input ("please enter the number of boys that come to the party: "))
number_of_people = input_girls + input_boys
if input_girls == input_boys and number_of_people >= 20:
    print("The party is excellent")
elif number_of_people >= 20 and input_girls != input_boys:
    print("Quite a cool party!")
elif number_of_people < 20 and input_girls > 0:
    print("Average party ... ")
elif input_girls == 0:
    print("Sausage party")
    