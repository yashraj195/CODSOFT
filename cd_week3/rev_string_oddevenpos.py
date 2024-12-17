def process_string(s):
    reversed_string = s[::-1]  
    odd_chars = reversed_string[::2] 
    even_chars = reversed_string[1::2]  
    
    print("Reversed String:", reversed_string)
    print("Characters at odd-numbered positions:", odd_chars)
    print("Characters at even-numbered positions:", even_chars)

# Input from the user
string = input("Enter a string: ")
process_string(string)