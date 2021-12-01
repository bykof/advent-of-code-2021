import string 

with open('input', 'r') as input_file:
    lines = list(map(lambda line: int(line), input_file.readlines()))
    
    if len(lines) <= 0:
        print('input has no lines, please fill out')
    
    previous_sum = None
    increases_counter = 0
    letters = list(string.ascii_uppercase)
    
    for i in range(len(lines)):
        sum = lines[i]
        
        for j in range(1, 3):
            if i + j < len(lines):
                sum += lines[i + j]
        suffix = f'{letters[i % len(letters)]}: {sum}'
        
        if previous_sum == None:
            print(f'{suffix} (N/A - no previous measurement)')
        else :
            if sum > previous_sum:
                print(f'{suffix} (increased)')
                increases_counter += 1
            elif sum == previous_sum:
                print(f'{suffix} (no change)')
            else:
                print(f'{suffix} (decreased)')
        previous_sum = sum
    
    print(f'Number of increases: {increases_counter}')
    


        



