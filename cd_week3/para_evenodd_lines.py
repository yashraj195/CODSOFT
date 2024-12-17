def display_odd_even_lines(paragraph):
    lines = paragraph.split('\n')
    print("Odd position lines:", *lines[::2], sep="\n")
    print("\nEven position lines:", *lines[1::2], sep="\n")

# Input paragraph
paragraph = "\n".join(iter(input, ""))
display_odd_even_lines(paragraph)