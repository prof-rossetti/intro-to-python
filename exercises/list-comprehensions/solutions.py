# total_comprehension.py

my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

#
# MAPPING
#

mapped_list = [n * 100 for n in my_numbers]
print("--------------")
print("MAPPED LIST:", mapped_list) #> [100, 200, 300, 400, 500, 600, 700]

#
# FILTERING
#

filtered_list = [n for n in my_numbers if n > 3]
print("--------------")
print("FILTERED LIST W/ MATCHES:", filtered_list) #> [4, 5, 6, 7]

no_matches = [n for n in my_numbers if n > 8]
print("--------------")
print("FILTERED LIST W/O MATCHES:", no_matches) #> [4, 5, 6, 7]

#
# MAPPING AND FILTERING
#

last_list = [n * 100 for n in my_numbers if n > 3]
print("--------------")
print("MAPPED AND FILTERED LIST:", last_list) #> [400, 500, 600, 700]
