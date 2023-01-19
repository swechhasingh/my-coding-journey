# Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

# Time complexity: O(N) and space complexity:O(N)
def is_happy_number(num: int):
    numbers = {}
    while num != 1:
        sum_sqs = 0
        while num != 0:
            sum_sqs += (num % 10) ** 2
            num = num // 10
        num = sum_sqs
        if num in numbers:
            return False
        else:
            numbers[num] = True
    return True


def find_sq_num(num):
    sum_sqs = 0
    while num != 0:
        sum_sqs += (num % 10) ** 2
        num = num // 10
    return sum_sqs


# space complexity: O(1)
def is_happy_number2(num: int):
    slow, fast = num, num
    while slow != 1:
        slow = find_sq_num(slow)
        fast = find_sq_num(find_sq_num(fast))
        if slow == fast:
            break
    return slow == 1


if __name__ == "__main__":
    print(f"Is 23 a happy number: {is_happy_number2(23)}")
    print(f"Is 12 a happy number: {is_happy_number2(12)}")
