import keyword
# show keyWords in Python 
help("keywords")

# check keyword
print(keyword.iskeyword("def"))

# another way to show keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print('False' in keyword.kwlist)

