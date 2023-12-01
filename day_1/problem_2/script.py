import re
DIGITS_MAP = {
  "one": 1, 
  "two": 2, 
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
  "zero": 0
}

input_file = open('input.txt', 'r')

# Initialise calibration accumulator
total_calibration = 0

for line in input_file.readlines():

  first_digit = None
  last_digit = None

  # Check for regular digits in the ine
  for index, char in enumerate(line): 
    if char.isdigit():
      if first_digit is None:
        first_digit = (index, char)
      last_digit = (index, char)

  # Get all written digits
  for digit in DIGITS_MAP.keys():
    ocurrences = [
      m.start() 
      for m in re.finditer(digit, line)
    ]
    for position in ocurrences:
      # Checks first digit for update
      if first_digit is None or position < first_digit[0]:
        first_digit = (position, DIGITS_MAP[digit])

      # Checks last digit for update
      if last_digit is None or position > last_digit[0]:
        last_digit = (position, DIGITS_MAP[digit])

  # print(f"First {first_digit[1]}; Last {last_digit[1]}")

  # Compose first and last digit from the line together to form
  # the calibration value for the line
  if first_digit is not None:
    calibration_value = int(f"{first_digit[1]}{last_digit[1]}")
  else:
    calibration_value = 0

  # Accumulate value
  total_calibration += calibration_value

print(f"Total calibration value is {total_calibration}")
