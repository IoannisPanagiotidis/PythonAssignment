#start the program
print("=======================1952942_Assingment_2_Ioannis_Panagiotidis====================")

#data validation function
def data_validation(up_limit, dn_limit, mssg):
    value = input(mssg + ': ')
    while True:
        try:
            while (float(value) < float(dn_limit) or float(value) > float(up_limit)):
                print('ERROR! Please enter a number between ' + str(dn_limit) + ' and ' + str(up_limit))
                value = input(mssg + ': ')
        except ValueError:
                print('Value ERROR! Please enter a number between ' + str(dn_limit) + ' and ' + str(up_limit))
                value = input(mssg + ': ')
        else:
            if (float(value) > float(dn_limit) or float(value) < float(up_limit)):
                return value


#dimention list definition
dimensions = [0,0,0,0,0]


#height input
dimensions[0] = data_validation(5, 2, "\nPlease enter the height of the room (between 2 and 5 meters)")


#length input (4 walls)
for i in range(1,5):
    dimensions[i] = data_validation(25, 1, "\nPlease enter the length of wall " + str(i) + " (between 1 and 25 meters)")
    
#display total area of the room
total_area = float(dimensions[0]) * (float(dimensions[1]) + float(dimensions[2]) + float(dimensions[3]) + float(dimensions[4]))
print ('\nThe total area of the room to paint is ' + str(round(total_area, 2)) + ' square meters.')


#paint dictionary definition
paint = {'luxury' : 1.75, 'standard' : 1.00, 'economy' : 0.45}


#paint selection and cost calculation
paint_selection = input("\nPlease select a paint type: (luxury, standard, economy): ")
while ((str(paint_selection) != 'luxury') and (str(paint_selection) != 'standard') and (str(paint_selection) != 'economy')):
    print("Error! Not acceptable answer.")
    paint_selection = input("\nPlease select a paint type: (luxury, standard, economy): ")

paint_cost = float(round((paint[paint_selection] * total_area),2))
print("\nThe total cost of your paint is going to be £" + str(paint_cost))


#undercoat calculation
undercoat = input("\nWould you like to use undercoat paint(£0.50 per square meter)? It is going to cost you £" + str(round((total_area * 0.50),2)) + " extra (yes // no): ")
while undercoat != "yes" and undercoat != "no":
    print("Error! Not acceptable answer.")
    undercoat = input("\nWould you like to use undercoat paint(£0.50 per square meter)? It is going to cost you £" + str(round((total_area * 0.50),2)) + " extra (yes // no): ")
if undercoat == "yes":
    undercoat_area = (total_area * 0.50) + paint_cost
    print("\nThe total cost of the paint is going to be £" + str(round(undercoat_area,2)))
if undercoat == "no":
    print("\nThe total cost of your paint is going to be £" + str(paint_cost))

























'''
import time


def room_height():
    height = float(input("Enter the height of the room, (between 2 and 5 meters): "))
    while height < 2 or height > 5 or height == '':
        print("ERROR!: Please enter a number between 2 and 5")
        height = float(input("\nEnter the height of the room, (between 2 and 5 meters): "))
    else:
        return height

def wall1():
    length1 = float(input("\nEnter the length of the first wall, (between 1 and 25 meters): "))  
    while length1 < 1 or length1 > 25:
        print("ERROR!: Please enter a number between 1 and 25")
        length1 = float(input("\nEnter the length of the first wall, (between 1 and 25 meters): "))
    else:
        return length1

def wall2():
    length2 = float(input("\nEnter the length of the second wall, (between 1 and 25 meters): "))    
    while length2 < 1 or length2 > 25:
        print("ERROR!: Please enter a number between 1 and 25")
        length2 = float(input("\nEnter the length of the second wall, (between 1 and 25 meters): "))
    else:
        return length2

def wall3():
    length3 = float(input("\nEnter the length of the third wall, (between 1 and 25 meters): "))
    while length3 < 1 or length3 > 25:
        print("ERROR!: Please enter a number between 1 and 25")
        length3 = float(input("\nEnter the length of the third wall, (between 1 and 25 meters): "))
    else:
        return length3

def wall4():
    length4 = float(input("\nEnter the length of the forth wall, (between 1 and 25 meters): "))    
    while length4 < 1 or length4 > 25:
        print("ERROR!: Please enter a number between 1 and 25")
        length4 = float(input("\nEnter the length of the forth wall, (between 1 and 25 meters): "))
    else:
        return length4

def total():
    totalArea = height * (length1 + length2 + length3 + length4)
    return float(round(totalArea,2))


def choose_paint():
    paint = input("\nWhich paint type would you like to use? (luxury // standard // economy): ")
    while paint != "luxury" and paint != "standard" and paint != "economy":
        print("ERROR! Please choose between (luxury // standard // economy)")
        paint = input("\nWhich paint type would you like to use? (luxury // standard // economy): ")
    else:
        if paint == "luxury":
            luxury_paint = total() * 1.75
            undercoat_paint = total() * 0.50
            undercoat_luxury = luxury_paint + undercoat_paint
            print("\nThe total price for luxury paint is going to be £" + str(round(luxury_paint,2)))
            time.sleep(1)
            under = input(("\nWould you like to use undercoat paint(£0.50 per square meter)? It is going to cost £" + str(round(undercoat_paint,2)) + " extra (yes // no): "))
            while under != 'yes' and under != 'no':
                print("ERROR! Please choose between (yes // no)")
                under = input(("\nWould you like to use undercoat paint(£0.50 per square meter)? It is going to cost £" + str(round(undercoat_paint,2)) + " extra (yes // no): "))
            else:
                if under == 'yes':
                    print("\nThe total price is going to be £" + str(round(undercoat_luxury,2)))
                if under == 'no':
                    print("\nThe total price for luxury paint stays £" + str(round(luxury_paint,2)))   
        if paint == "standard":
            standard_paint = total() * 1.00
            undercoat_paint = total() * 0.50
            undercoat_standard = standard_paint + undercoat_paint
            print("\nThe total price for standard paint is going to be £" + str(round(standard_paint,2)))
            time.sleep(1)
            under = input(("\nWould you like to use undercoat paint(£0.50 per square meter)? It is going to cost £" + str(round(undercoat_paint,2)) + " extra (yes // no): ")) 
            while under != 'yes' and under != 'no':
                print("ERROR! Please choose between (yes // no)")
                under = input(("\nWould you like to use undercoat paint(£0.50 per square meter)? It is going to cost £" + str(round(undercoat_paint,2)) + " extra (yes // no): ")) 
            else:
                if under == 'yes':
                    print("\nThe total price is going to be £" + str(round(undercoat_standard,2)))
                if under == 'no':
                    print("\nThe total price for standard paint stays £" + str(round(standard_paint,2)))  
        if paint == "economy":
            economy_paint = total() * 0.45
            undercoat_paint = total() * 0.50
            undercoat_economy = economy_paint + undercoat_paint   
            print("\nThe total price for economy paint is £" + str(round(economy_paint,2)))
            time.sleep(1)
            under = input(("\nWould you like to use undercoat paint(£0.50 per square meter)? It is going to cost £" + str(round(undercoat_paint,2)) + " extra (yes // no): "))
            while under != 'yes' and under != 'no':
                print("ERROR! Please choose between (yes // no)")
                under = input(("\nWould you like to use undercoat paint(£0.50 per square meter)? It is going to cost £" + str(round(undercoat_paint,2)) + " extra (yes // no): "))
            else:
                if under == 'yes':
                    print("\nThe total price is going to be £" + str(round(undercoat_economy,2)))
                if under == 'no':
                    print("\nThe total price for economy paint stays £" + str(round(economy_paint,2)))
                    
    

height = room_height()
length1 = wall1()
length2 = wall2()
length3 = wall3()
length4 = wall4()
print("\nThe total area of the room is " + str(total()) + " square metres.")
time.sleep(1)
choose_paint()
'''












'''
import time

#start the program
print("=======================1952942_Assingment_2_Ioannis_Panagiotidis====================")

#data validation function
def data_validation(up_limit, dn_limit, msg):
    value = float(input(msg + ": "))
    while (float(value) < float(dn_limit) or float(value) > float(up_limit)):
        print('Error! Not acceptable value. Please enter a number between ' + str(dn_limit) + ' and ' + str(up_limit))
        value = float(input(msg + ": "))
    return value


#dimention list definition
dimmensions = [0,0,0,0,0]


#height input
time.sleep(1)
dimmensions[0] = data_validation(5, 2, "\nPlease enter the height of the room (between 2 and 5 meters)")


#length input for the 4 walls
for i in range(1,5):
    dimmensions[i] = data_validation(25, 1, "\nPlease enter the length of room " + str(i) + " (between 1 and 25 meters)")
    
#display of the total area of the room
area = float(dimmensions[0]) * (float(dimmensions[1]) + float(dimmensions[2]) + float(dimmensions[3]) + float(dimmensions[4]))
print ('\nThe total area of the room to paint is ' + str(round(area, 2)) + ' square meters.')

#paint dictionary definition
paint = {'luxury' : 1.75, 'standard' : 1.00, 'economy' : 0.45}


#paint selection and cost calculation
time.sleep(1)
paint_selection = input("\nPlease select a paint type: (luxury, standard, economy): ")
while ((str(paint_selection) != 'luxury') and (str(paint_selection) != 'standard') and (str(paint_selection) != 'economy')):
    print("Error! Not acceptable answer.")
    paint_selection = input("\nPlease select a paint type: (luxury, standard, economy): ")

paint_cost = float(round((paint[paint_selection] * area),2))
print("\nThe total cost of your paint is going to be £" + str(paint_cost))


#undercoat calculation function
time.sleep(1)
undercoat = input("\nWould you like to use undercoat paint(£0.50 per square meter)? It is going to cost £" + str(round((area * 0.50),2)) + " extra (yes // no): ")
while undercoat != "yes" and undercoat != "no":
    print("Error! Not acceptable answer.")
    undercoat = input("\nWould you like to use undercoat paint(£0.50 per square meter)? It is going to cost £" + str(round((area * 0.50),2)) + " extra (yes // no): ")
if undercoat == "yes":
    undercoat_area = (area * 0.50) + paint_cost
    print("\nThe total cost of the paint is going to be £" + str(round(undercoat_area,2)))
if undercoat == "no":
    print("\nThe total cost of your paint is going to be £" + str(paint_cost))
'''













'''
import time


def room_height():
    height = float(input("Enter the height of the room, (between 2 and 5 meters): "))
    while height < 2 or height > 5 or height == '':
        print("ERROR!: Please enter a number between 2 and 5")
        height = float(input("\nEnter the height of the room, (between 2 and 5 meters): "))
    else:
        return height

def wall1():
    length1 = float(input("\nEnter the length of the first wall, (between 1 and 25 meters): "))  
    while length1 < 1 or length1 > 25:
        print("ERROR!: Please enter a number between 1 and 25")
        length1 = float(input("\nEnter the length of the first wall, (between 1 and 25 meters): "))
    else:
        return length1

def wall2():
    length2 = float(input("\nEnter the length of the second wall, (between 1 and 25 meters): "))    
    while length2 < 1 or length2 > 25:
        print("ERROR!: Please enter a number between 1 and 25")
        length2 = float(input("\nEnter the length of the second wall, (between 1 and 25 meters): "))
    else:
        return length2

def wall3():
    length3 = float(input("\nEnter the length of the third wall, (between 1 and 25 meters): "))
    while length3 < 1 or length3 > 25:
        print("ERROR!: Please enter a number between 1 and 25")
        length3 = float(input("\nEnter the length of the third wall, (between 1 and 25 meters): "))
    else:
        return length3

def wall4():
    length4 = float(input("\nEnter the length of the forth wall, (between 1 and 25 meters): "))    
    while length4 < 1 or length4 > 25:
        print("ERROR!: Please enter a number between 1 and 25")
        length4 = float(input("\nEnter the length of the forth wall, (between 1 and 25 meters): "))
    else:
        return length4

def total():
    totalArea = height * (length1 + length2 + length3 + length4)
    return float(round(totalArea,2))


def choose_paint():
    paint = input("\nWhich paint type would you like to use? (luxury // standard // economy): ")
    while paint != "luxury" and paint != "standard" and paint != "economy":
        print("ERROR! Please choose between (luxury // standard // economy)")
        paint = input("\nWhich paint type would you like to use? (luxury // standard // economy): ")
    else:
        if paint == "luxury":
            print("\nThe total price for luxury paint is  £" + str(round(total() * 1.75)))
            time.sleep(1)
            print("\nWould you like to use undercoat paint(£0.50 per square meter)? The total price is going to be £" + str(round((total() * 1.75) + (total() * 0.50), 2)))
            under = input("yes // no: ")
            while under != 'yes' and under != 'no':
                print("ERROR! Please choose between (yes // no)")
                under = input("\nyes // no: ")
            else:
                if under == 'yes':
                    print("\nThe total price is going to be £" + str(round((total() * 1.75) + (total() * 0.50), 2)))
                if under == 'no':
                    print("\nThe total price for luxury paint is  £" + str(round(total() * 1.75), 2))       
        if paint == "standard":
            print("\nThe total price for standard paint is  £" + str(round(total() * 1.00), 2))
            time.sleep(1)
            print("\nWould you like to use undercoat paint(£0.50 per square meter)? The total price is going to be £" + str(round((total() * 1.00) + (total() * 0.50), 2)))
            under = input("yes // no: ")
            while under != 'yes' and under != 'no':
                print("ERROR! Please choose between (yes // no)")
                under = input("\nyes // no: ")
            else:
                if under == 'yes':
                    print("\nThe total price is going to be £" + str(round((total() * 1.00) + (total() * 0.50), 2)))
                if under == 'no':
                    print("\nThe total price for standard paint is  £" + str(round(total() * 1.00), 2))  
        if paint == "economy":
            print("\nThe total price for economy paint is  £" + str(round(total() * 0.45), 2))
            time.sleep(1)
            print("\nWould you like to use undercoat paint(£0.50 per square meter)? The total price is going to be £" + str(round((total() * 0.45) + (total() * 0.50), 2)))
            under = input("yes // no: ")
            while under != 'yes' and under != 'no':
                print("ERROR! Please choose between (yes // no)")
                under = input("\nyes // no: ")
            else:
                if under == 'yes':
                    print("\nThe total price is going to be £" + str(round((total() * 0.45) + (total() * 0.50), 2)))
                if under == 'no':
                    print("\nThe total price for economy paint is  £" + str(round(total() * 0.45), 2))
                    
    

height = room_height()
length1 = wall1()
length2 = wall2()
length3 = wall3()
length4 = wall4()
print("\nThe total area of the room is " + str(total()) + " square metres.")
time.sleep(1)
choose_paint()
'''








'''
rooms = 0
for i in range(1,5):
    room = float(input("Put the height of room " + str(rooms + i) + ": "))
'''










































'''
time.sleep(1)
print("\nWould you like to use undercoat paint? The total price is going to be",undercoat_paint())
under = input("Yes // No: ")
'''








'''
total1 = 100
paint_type = ''

while paint_type != 'luxury' and paint_type != 'standard' and paint_type != 'economy':
    # Ask the user for a name.
    paint_type = input("\nWhich paint type would you like to use? (luxury // standard // economy): ")
    print("ERROR! Please choose between (luxury // standard // economy)")
else:
    if paint_type == "luxury":
            print("\nThe total price for luxury paint is  £",total1 * 1.75)
    if paint_type == "standard":
            print("\nThe total price for this type of paint is going to be",total1 * 1.00)
    if paint_type == "economy":
            print("\nThe total price for this type of paint is going to be",total1 * 0.45)
'''

            
        













'''
a  = float(56.388)
print(round(a,2))
print(a)
print(1.9675869658)
print(round(1.9675869658,2))

b = (a * 1.75)
print(round(b,2))
'''























'''
def luxury_quality()
    luxury = total1 * 1.75
    return luxury
    

def standard_quality():
    standard = total1 * 1.00
    return standard

def economy_quality():
    economy = total1 * 0.45
    return economy
'''
'''
print("\nThe luxury quality paint is going to cost " + "£" + str(luxury_quality()))
print("\nThe standard quality paint is going to cost " + "£" + str(standard_quality()))
print("\nThe economy quality paint is going to cost " + "£" + str(economy_quality()))
'''




'''
import time




def height():
    height = ''
    while height < '2' or height > '5':
        print('Enter the height of the first wall, (between 2 and 5 meters): ')
        height = input()
    return height

def length():
    length = ''
    while length < '1' or length > '25':
        print('Enter the length of the first wall, (between 1 and 25 meters): ')
        length = input()
    return length


def find_totall_space():
    totall = height() * length()
    return total


def main_loop():
    height()
    length()
    find_totall_space()
    
main_loop()
'''



'''
    while length < '1' and length > '25':
        print("First wall length ERROR: Please enter a number between 1 and 25")
        length = input
        return length
    


def enter_wall():
    print("\nEnter the height of the first wall, (between 2 and 5 meters): ")
    time.sleep(100000)
    print("\nEnter the height of the second wall, (between 2 and 5 meters): ")
'''


'''
def choose_paint():
    paint = ''
    while paint != 'luxury' and paint != 'standard' and paint != 'economy':
        print("Which paint type would you like to use? (luxury // standard // economy): ")
        paint = input()
    return paint

def enter_paint_type(choosen_paint):
    paint_type1 = (luxury)
    paint_type2 = (standard)
    paint_type3 = (economy)
    if paint_type1 == (choosen_paint):
        print(total1 * 1.75)
    if paint_type2 == int(choosen_paint):
            print(total1 * 1.00)
    if paint_type3 == int(choosen_paint):
            print(total1 * 0.45)
    else:
        print("Please choose one of the three")


choose_paint()
'''







'''
total1 = 100


def choose_paint():
    paint = input("Which paint type would you like to use? (luxury // standard // economy): ")
    while paint != "luxury" and paint != "standard" and paint != "economy":
        print("ERROR! Please choose between (luxury // standard // economy)")
        paint = input("\nWhich paint type would you like to use? (luxury // standard // economy): ")
    else:
        if paint == "luxury":
            print("\nThe total price for this type of paint is going to be",total1 * 1.75)
        if paint == "standard":
            print("\nThe total price for this type of paint is going to be",total1 * 1.00)
        if paint == "economy":
            print("\nThe total price for this type of paint is going to be",total1 * 0.45)
            
            



choose_paint()
'''











'''
def choose_paint():
    paint = input("Which paint type would you like to use? (luxury // standard // economy): ")
    while paint != "luxury" and paint != "standard" and paint != "economy":
        print("ERROR! Please choose between (luxury // standard // economy)")
        paint = input("\nWhich paint type would you like to use? (luxury // standard // economy): ")
    else:
        print("\nThe total price for this type of paint is going to be",total1 * 1.75)
    while paint != "standard":
        print("ERROR! Please choose between (luxury // standard // economy)")
        paint = input("\nWhich paint type would you like to use? (luxury // standard // economy): ")
    else:
        print("\nThe total price for this type of paint is going to be",total1 * 1.00)
    while paint != "economy":
        print("ERROR! Please choose between (luxury // standard // economy)")
        paint = input("\nWhich paint type would you like to use? (luxury // standard // economy): ")
    else:
        print("\nThe total price for this type of paint is going to be",total1 * 0.45)
'''



'''
def choose_paint():
    paint = input("Which paint type would you like to use? (luxury // standard // economy): ")
    while paint == "luxury":
        print("\nThe total price for this type of paint is going to be",total1 * 1.75)
    else:
        print("ERROR! Please choose between (luxury // standard // economy)")
        paint = input("\nWhich paint type would you like to use? (luxury // standard // economy): ")
        
choose_paint()       
'''

'''
 elif paint == "standard":
        print("The total price for this type of paint is going to be",total1 * 1.00)
    elif paint == "economy":
        print("The total price for this type of paint is going to be",total1 * 0.45)
    else:
        print("Please choose one of the three")
'''


'''
def room_height():
    height = float(input("Enter the height of the room, (between 2 and 5 meters): "))
    while height < 2 or height > 5:
        print("ERROR!: Please enter a number between 2 and 5")
        height = float(input("\nEnter the height of the room, (between 2 and 5 meters): "))
    else:
        return height
'''



'''
def choose_paint():
    paint = ''
    while paint != 'luxury' and paint != 'standard' and paint != 'economy':
        print("Which paint type would you like to use? (luxury // standard // economy): ")
        paint = input()
    return paint

def enter_paint_type(choosen_paint):
    paint_type1 = (luxury)
    paint_type2 = (standard)
    paint_type3 = (economy)
    if paint_type1 == int(choosen_paint):
        print(total1 * 1.75)
    if paint_type2 == int(choosen_paint):
            print(total1 * 1.00)
    if paint_type3 == int(choosen_paint):
            print(total1 * 0.45)
    else:
        print("Please choose one of the three")
'''



'''
def kalimera(num1m,num2h,msg):
    msg = input(msg + ": ")
    while num1m < msg and num2h > msg:
        print("Error")
        msg = input("put your name" + ":")
    return msg

        
list1 = [0,0,0,0,0]

height[0] = kalimera(1, 5, "put the height")
'''


    
    
