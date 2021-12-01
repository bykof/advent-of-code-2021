with open('input', 'r') as input_file:
    lines = list(map(lambda line: int(line), input_file.readlines()))
    
    if len(lines) <= 0:
        print('input has no lines, please fill out')
    
    previous_line = None
    increases_counter = 0

    for line in lines:
        if previous_line == None:
            print('(N/A - no previous measurement)')
        else :
            if line > previous_line:
                print("(increased)")
                increases_counter += 1
            elif line == previous_line:
                print('(no change)')
            else:
                print('(decreased)')
        previous_line = line
    
    print(f'Number of increases: {increases_counter}')
