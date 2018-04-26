def is_happy_number(input):
    if (input <= 0) or (input in [4, 16, 20, 37, 42, 58, 89, 142]):
        return False
    sum = 0
    while input:
      sum += (input % 10) ** 2
      input = int(input / 10)
    if sum == 1:
        return True
    return is_happy_number(sum)
if __name__ == '__main__':