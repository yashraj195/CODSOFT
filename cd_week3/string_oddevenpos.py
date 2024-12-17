# Function to display characters at odd and even positions
def display_positions(s):
    odd_chars = s[::2]  
    even_chars = s[1::2]  
    
    print("Characters at odd-numbered positions:", odd_chars)
    print("Characters at even-numbered positions:", even_chars)

# Input from the user
string = input("Enter a long string: ")
display_positions(string)