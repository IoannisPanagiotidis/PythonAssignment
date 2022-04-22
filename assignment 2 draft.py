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

