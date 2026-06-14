def good_integer(num):
  digit_sum = 0
  square_sum = 0
  while num > 0:
    rem = num % 10
    digit_sum += rem
    square_sum += rem ** 2
    num = num//10
  if square_sum - digit_sum >= 50:
    return True
  else:
    return False
