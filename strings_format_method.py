#The format() Method for Formatting Strings

#default(implicit) order
default_order = "{},{} and {}".format('John','Bill','Sean')
print("\n---Default Order---")
print(default_order)

#order using positional argument
positional_order ="{1},{0} and {2}".format('John','Bill','Sean')
print('\n---Positional Order---')
print(positional_order)

#order using keyword argument
keyword_order ="{c},{a} and {b}".format(a='John',b='Bill',c='Sean')
print('\n---Keyword Order---')
print(keyword_order)
