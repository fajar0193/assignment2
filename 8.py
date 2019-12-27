
def chop(lst):
    """
    Takes a list, modifies it, removing the first and last elements, and
    returns None.
    Input:  lst -- a list
    Output: None
"""
    del lst[0]                          # Removes the first element
    del lst[-1]                         # Removes the last element

def middle(lst):
    """
    Takes a list and returns a new list that contains all but the first and
    last elements.
    Input: lst -- a list
    Output: new -- new list with first and last elements removed
    """
    new = lst[1:]                       # Stores all but the first element
    del new[-1]                         # Deletes the last element
    return new


my_list = [1, 2, 3, 4]
my_list2 = [1, 2, 3, 4]

chop_list = chop(my_list)
print(my_list)                          # Should be [2,3]
print(chop_list)                        # Should be None

middle_list = middle(my_list2)
print(my_list2)                         # Should be unchanged
print(middle_list)                      # Should be [2,3]

fhand = open('exercise8_2.txt')
for line in fhand:
    words = line.split()

    if len(words) < 3:
        continue
    if words[0] != 'From':
        continue
    print(words[2])

fhand = open('exercise8_2.txt')
for line in fhand:
    words = line.split()

    if len(words) < 3:
        continue
    if words[0] != 'From':
        continue
    print(words[2])


my_list = []
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()                # Splits line into array of words
    for word in words:
        if word in my_list:
            continue                    # Discards duplicates
        my_list.append(word)            # Updates the list
print(sorted(my_list))                  # Alphabetical order

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])
    count += 1
print('There were %d lines in the file with From as the first word' % count)

my_list = []                        # Initialize array
while True:
    number = 0.0
    input_number = input('Enter a number: ')
    if input_number == 'done':
        break

    try:
        number = float(input_number)
    except ValueError:
        print('Invalid input')
        quit()

    my_list.append(input_number)

print('Maximum: ', max(my_list))
print('Minimum: ', min(my_list))
