#inputs: function, some iterables
#operation: applies this function to iterables
#output: new list

my_list = [1,2,3,4,5,6]
new_list = list(map(lambda a:(a*2),my_list))
#filter(function,iterable
print(new_list)