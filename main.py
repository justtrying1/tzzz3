with open('numbers', 'r') as file:
    data = file.read().replace('\n', '')
    numbers = data.split(" ")
    numbers = [int(token) for token in numbers]


    def find_min(array):
        return min(array)


    def find_max(array):
        return max(array)


    def find_sum(array):
        return sum(array)


    def find_prod(array):
        a = 1
        for i in array:
            a *= i
        return a


    print("Минимальное:", find_min(numbers))
    print("Максимальное:", find_max(numbers))
    print("Сумма:", find_sum(numbers))
    print("Произведение:", find_prod(numbers))
