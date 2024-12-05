def check_if_order_is_right(pages: list[list[int, int]], orders: list[int]) -> bool:
    # Cut page numbers if they are not in orders
    pages = [pages[i] for i in range(len(pages))\
              if pages[i][0] in orders and pages[i][1] in orders]
    
    for i in range(len(orders)):
        # Check the left side of the pages. Return false if a number is found before in orders
        for j in range(len(pages)):
            if pages[j][0] == orders[i] and pages[j][1] in orders[:i]:
                return False
            elif pages[j][1] == orders[i] and pages[j][0] in orders[i+1:]:
                return False

    return True

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

    sum = 0
    for order in orders:
        if check_if_order_is_right(pages, order):
            sum += order[len(order)//2]

    print(sum)