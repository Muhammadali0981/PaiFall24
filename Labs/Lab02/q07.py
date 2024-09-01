# Name: Muhammad Ali
# Date: 1/9/24
# Desc: temp data

def calculate_average_temperature(lst):
    avg:int = sum(lst) / len(lst)
    print("Average temperature: ", avg)


def heighest_and_lowest_temperature(lst):

    max:int = lst[0]
    for i in range(1, len(lst)):
        if (max < lst[i]):
            max = lst[i]

    # calculates heighest temperature
    min:int = lst[0]
    for i in range(1, len(lst)):
        if (min > lst[i]):
            min = lst[i]
    print("Maximum: ", max, "\nMinimum: ", min)


def sort_ascending_order(lst):

    lst.sort()
    print("sorted list is: ", lst)


def remove_temperature(lst):

    day:str = int(input("Enter the day(0-8): "))
    lst.pop(day)
    print("Updated List: ", lst)



temperature = [24, 58, 79, 45, 67, 23, 19, 87]

calculate_average_temperature(temperature)
heighest_and_lowest_temperature(temperature)
sort_ascending_order(temperature)
remove_temperature(temperature)


