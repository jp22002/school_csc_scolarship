def print_names(people):
    people_place = 0
    while people_place != (len(people)):
        to_print = people[people_place][0]
        name_place = 1
        while name_place != (len(people[people_place])):
            name = people[people_place][name_place]
            to_print +=  " " +name 
            name_place += 1
        print(to_print)
        people_place += 1
    
print_names([["John","Smith"],["James","Peyroux"]])
