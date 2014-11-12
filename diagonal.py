def diagonal(text, right_to_left =False):
    """
    'diagonal' is a function that prints it's argument text diagonally.
    If the argument right_to_left is set to 'False' then the direction of
    the text will be left to right, and if it is set to 'True' then it 
    will be from right to left.
    """
    if not right_to_left:
        spaces = 0
        increment = 1
        #Sets the text to begin from the left (0 spaces) and increase by an
        #increment of 1 space for each letter
    
    elif right_to_left:
        spaces = len(text) - 1
        increment = -1
        #Sets the text to begin from the right (the length of the text) and
        #decrease by an increment of 1 space for each letter
    
    for letter in text:
        print(" "*spaces + letter)
        spaces = spaces + increment
        #Prints the text on seperate lines, assigning one letter to each line
        #and moving further left or right for the next letter depending on 
        #increment
#---------------------------------------------------------------------------
diagonal("Diagonal Text", right_to_left=False)
diagonal("Diagonal Text", right_to_left=True)