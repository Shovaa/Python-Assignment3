
#for counting the lowercse , uppercase, symbol and number from the given words from user.
def count_chars(str):
     upper_char, lower_char, number, special_char = 0, 0, 0, 0
     for i in range(len(str)):
          if str[i] >= 'A' and str[i] <= 'Z': upper_char += 1 #counts uppercase
          elif str[i] >= 'a' and str[i] <= 'z': lower_char += 1 #counts lowercase
        
          elif str[i] >= '0' and str[i] <= '9': number += 1#counts number
          else: special_char += 1 #counts special symbol
     return upper_char, lower_char, number, special_char
           
str = input("Enter the words:")
print("Original Substrings:",str)
u, l, n, s = count_chars(str)
print('\nUpper case characters: ',u)
print('Lower case characters: ',l)
print('Number case: ',n)
print('Special case characters: ',s)