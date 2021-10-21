def sum_weights(weight1, weight2):
    totalweight = weight1 + weight2
    return totalweight


def calc_average_weight(weight1, weight2):
    total_weight = sum_weights(weight1, weight2)
    avg_weight = total_weight / 2
    return avg_weight


def run():
    print("Enter weight of first bot:")
    input1 = int(input())
    print("Enter weight of second bot:")
    input2 = int(input())
    print("Sum Or Average")
    input3 = input()
    if input3 == "Sum":
        print(sum_weights(input1, input2))

    elif input3 == "Average":
        print(calc_average_weight(input1, input2))


run()