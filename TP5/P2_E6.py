# Define global constant
A = ((5**.5 - 1)/2)  # Golden ratio φ

# Define functions

def alphabetPos(key):
    '''
    Explanation:
        Get the position in the alphabet for a given character.
    Info:
        This function is specific to letters from A-Z. (ϵ Ñ).
        The dictionary length is 27
        Not case sensitive
    Params:
        key: The letter from which the hash is to be obtained.
    Return:
        An integer with the hash (position) of the given letter in the alphabet.
    '''
    # Define dictionary length and result variable
    result = None

    # Store unicode value of key
    if key == 'Ñ' or key == 'ñ':
        result = 14
    else:
        # Define result using 26 letter alphabet
        result = ord(key) - ord('A')

        # Fix to consider ñ in alphabet and other unicode characters
        if result >= 14 and result <= 26:
            result += 1
        elif result > 26 and result <= 45:
            result -= 5 + 27 # lower case case, substract an alphabet
        elif result > 40:
            result -= 4 + 27 # lower case case

    # Return the position of the key in a 27 letter alphabet
    return result

def h(cpa):
    '''
    Explanation:
        Generates a hash from a given CPA (Código Postal Argentino).
    Params:
        cpa: An string of 8 characters, with numbers and letters (not case sensitive), A9999AAA.
    Return:
        A hash value that represent a given CPA. 'None' otherwise
    '''
    # Define hash value
    hashSum = None

    # Check length condition
    if len(cpa) != 8:
        hashSum = None
    else:
        # Get an unhashed integer that represents the cpa
        preHash = 0
        for i in range(0, 8):
            if i == 0 or i > 4:  # Letter case
                preHash += (alphabetPos(cpa[i])+1)*(27**i)
            else:  # Number case
                preHash += (int(cpa[i])+1)*(10**i)

        # Calc the hash of the preHash using the multiplication method (φ)
        hashSum = int(m*(preHash*A % 1))

    # Return the result value
    return hashSum


m = 27**4 + 10**4  # Possible different combinations

print(h('A0000AAA'))
print(h('B0000AAA'))
print(h('A1000AAA'))
print(h('A0100AAA'))
print(h('A0010AAA'))
print(h('A0001AAA'))
print(h('A0000BAA'))
print(h('A0000ABA'))
print(h('A0000AAB'))
