### Basic Example ###
my_list = [1, 2, 3, 4]

my_tuple = tuple(my_list)
my_set = set(my_list)
my_string = str(my_list)

print ('\n')
print ('\n')
print ('### basic example ###')
print ('------------------------------')
print(my_tuple)     # (1, 2, 3, 4)
print(my_set)  # {1, 2, 3, 4}
print(my_string)    # "[1, 2, 3, 4]"
print ('------------------------------')
print ('\n')
### end basic example ###

### remove duplicates ###
my_numbers = [1, 2, 2, 3, 4, 4, 5]

no_duplicates= list(set(my_numbers))

print ('### remove duplicates ###')
print ('------------------------------')
print(my_numbers)
print(no_duplicates)
print ('------------------------------')
print ('\n')
### end remove duplicates ###

### convert string to list ###
my_text = "python"

list_letters = list(my_text)

print ('### convert string to list ###')
print ('------------------------------')
print(list_letters)
print ('------------------------------')
print ('\n')
### end convert string to list ###

### dictionary to iterable ###
person = {
    "name": "Ana", 
    "age": 25
}

person_keys = list(person)
person_values = list(person.values())
person_items = list(person.items())

print ('### dictionary to iterable ###')
print ('------------------------------')
print(person_keys)
print(person_values)
print(person_items)
print ('------------------------------')
print ('\n')
### dictionary to iterable ###

#####################################
### Conversions with Dictionaries ###
#####################################

### From Tuple List to Dictionary: Use dict() ###
my_peers = [("a", 1), ("b", 2)]
my_dictionary = dict(my_peers)  # {'a': 1, 'b': 2}

print ('### From Tuple List to Dictionary: Use dict() ###')
print ('------------------------------')
print(my_dictionary)
print ('------------------------------')
print ('\n')

### From Two Lists to a Dictionary: Using zip() and dict() ###
my_keys = ["name", "age"]
my_values = ["jeft", 30]
my_dictionary = dict(zip(my_keys, my_values)) # {'nombre': 'Ana', 'edad': 25}

print ('### From Two Lists to a Dictionary: Using zip() and dict() ###')
print ('------------------------------')
print(my_dictionary)
print ('------------------------------')
print ('\n')

#########################
### Useful Techniques ###
#########################

### join() para Cadenas ###
my_words = ["hellow", "Python"]
my_phrase = " ".join(my_words) # "hello Python"

print ('### join() para Cadenas ###')
print ('------------------------------')
print(my_phrase)
print ('------------------------------')
print ('\n')

### map(): Transforms elements of an iterable and converts them to another type. ###
my_numbers_string = ["1", "2", "3"]
my_numbers_integer = list(map(int, my_numbers_string)) # [1, 2, 3]

print ('### map(): Transforms elements of an iterable and converts them to another type. ###')
print ('------------------------------')
print(my_numbers_string)
print(my_numbers_integer)
print ('------------------------------')
print ('\n')
