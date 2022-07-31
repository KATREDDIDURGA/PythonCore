#user defined functions take lambda as input
#inputs: function, some iterables
#operation: applies this function to iterables
#output: new list that satisfies the function
my_list = [1,2,3,4,5,6]
new_list = list(filter(lambda a:(a/3==2),my_list))
#filter(function,iterable
print(new_list)