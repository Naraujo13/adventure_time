
input_file = open('input.txt', 'r')

# Initialise calibration accumulator
total_calibration = 0

for line in input_file.readlines():

  # Get all digits from this line
  digits = [
    char 
    for char in line if char.isdigit()
  ]
  
  # Compose first and last digit from the line together to form
  # the calibration value for the line
  if digits:
    calibration_value = int(f"{digits[0]}{digits[-1]}")
  else:
    calibration_value = 0

  # Accumulate value
  total_calibration += calibration_value

print(f"Total calibration value is {total_calibration}")
