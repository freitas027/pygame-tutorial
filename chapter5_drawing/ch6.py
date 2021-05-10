"""
Creates a text drawing with the following pattern:
      1      
    1 2 1    
  1 2 3 2 1  
1 2 3 4 3 2 1
  1 2 3 2 1  
    1 2 1    
      1

User will input the very central digit (number 4 in the example above).
"""

nmax = int(input('Type the number of the central digit: '))

# Create the central row with Ascending and descending order. Ex: 1 2 3 4 3 2 1
central_numbers = list(range(1, nmax+1))
central_numbers = central_numbers + central_numbers[-2::-1]

# Calculate the length of the central row with 
max_width = len(' '.join(map(str, central_numbers)))

# For each number in the middle row
for i in central_numbers:
    row = list(range(1, i+1))
    row = row + row[-2::-1]
    # Create a formatting string with the pattern: "{} {} {}" and replace with numbers
    numbers = ' '.join(["{}"]*len(row)).format(*row)
    # Use the ^ specification of format to place the number in the middle in respect of the widest row
    final_result = '{:^{max_width}}'.format(numbers, max_width=max_width)
    # Print the row
    print(final_result)
    