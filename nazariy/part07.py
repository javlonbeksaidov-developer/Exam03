"""7. Berilgan ro'yxatdagi barcha juft sonlarni yangi ro'yxatga yig'ib, uni qaytaruvchi funksiya yozing."""

even_numbers = []


def even(numbers):
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)


numbers = [2, 3, 4, 5, 6, 7, 8]

even(numbers)
print(even_numbers)
