def validBracketSequence(sequence):
   
    if len(sequence) == 0:
        return True

    print("New seq " + sequence)

    ascii_index = ord(sequence[0])
    #look for the chars asked for in the code signal test, we only need the opening "bracket" '(', '[', '{'
    if checkForExpressionBrackets(ascii_index):
        #Lets first check for outer matching brackets
        current_sequence = sequence
        sequence = checkForOuterBrackets(sequence, ascii_index)
        if current_sequence != sequence:
            return(validBracketSequence(sequence))
        
             
    else:
        return checkForExpressionBrackets(ascii_index)
      
    return False

def checkForExpressionBrackets(ascii_index):
    if ascii_index == 40 or ascii_index == 91 or ascii_index == 123:
        return True
    else:
        return False
   
def checkForImediatClosingBracket(sequence, ascii_index):
    #first lets get the open and close brackets
    opening_bracket, closing_bracket = getOpeningAndClosingBrackets(ascii_index)

    #lets check to see if the open and closing brakets are adjacent 
    if sequence[0] == opening_bracket and sequence[1] == closing_bracket:
        #they are adjacent brackets, lets remove them and move on if neeed be
        clean_sequence = ""
        for char in range(2, len(sequence)):
            clean_sequence += (sequence[char]) # build a new string minus the brackets

        return clean_sequence
    else: # if no adjacent closing bracket found just return and move on
        return sequence  
    


def checkForOuterBrackets(sequence, ascii_index):
    #first lets get the open and close brackets
    opening_bracket, closing_bracket = getOpeningAndClosingBrackets(ascii_index)

    print(closing_bracket)
    #first lets check to see if the brackets are actually closing brackets of the whole expression
    if sequence[0] == opening_bracket and sequence[len(sequence) - 1] == closing_bracket:
        
        #if these are true open and closing brakets remove them and move on
        sequence = sequence.lstrip(opening_bracket)
        sequence = sequence.rstrip(closing_bracket)
    else: # if they aren't true open and closing lets check to see if they are adjacent to one another.
        sequence = checkForImediatClosingBracket(sequence, ascii_index) 

    return sequence

def getOpeningAndClosingBrackets(ascii_index):
    opening_bracket = chr(ascii_index)
    if ascii_index == 40:
        closing_bracket = chr(ascii_index + 1)
    else:
        closing_bracket = chr(ascii_index + 2)

    return opening_bracket, closing_bracket

print(validBracketSequence("{[]}"))