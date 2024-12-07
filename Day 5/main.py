def check_if_order_is_right(pages: list[list[int, int]], orders: list[int]) -> list[int, int] | int:
    ''' Return:
        int - middle page order if order is right
        (int, int) - of wrong page positions if order is not right
    '''

    # Cut page numbers if they are not in orders
    pages = [pages[i] for i in range(len(pages))\
              if pages[i][0] in orders and pages[i][1] in orders]
    
    for i in range(len(orders)):
        # Check the left side of the pages. Return false if a number is found before in orders
        for j in range(len(pages)):
            if pages[j][0] == orders[i] and pages[j][1] in orders[:i]:
                return pages[j][0], pages[j][1]
            elif pages[j][1] == orders[i] and pages[j][0] in orders[i+1:]:
                return pages[j][0], pages[j][1]

    return orders[len(orders)//2]


def change_order_position_to_right_format(pages: list[list[int, int]], orders: list[int]) -> int:
    while True:
        callback = check_if_order_is_right(pages, orders)
        if type(callback) != int:
            number1_idx = orders.index(callback[0])
            number2_idx = orders.index(callback[1])
            orders[number1_idx], orders[number2_idx] = orders[number2_idx], orders[number1_idx]
        else:
            
            return orders[len(orders)//2]


if __name__ == '__main__':
    pages = []
    orders = []
    with open('input.txt', 'r') as file:
        before_orders = True
        for line in file:
            line = line.split('\n')[0]  # Cut enter
            if line == "":
                before_orders = False
            elif before_orders:
                numbers = line.split('|')
                pages.append([int(numbers[0]), int(numbers[1])])
            else:
                numbers = line.split(',')
                orders.append([int(number) for number in numbers])

    sum1 = 0
    sum2 = 0
    for order in orders:
        answer = check_if_order_is_right(pages, order)
        if type(answer) == int:
            sum1 += answer
        else:
            sum2 += change_order_position_to_right_format(pages, order)

    print(sum1)
    print(sum2)
