def generate_combination_table(rows):
    total_combinations = 2 ** rows
    table = []
    for i in range(total_combinations):
        string = format(i, f'0{rows}b')
        table.append(string)
    return table


# -----------------------------------------------------------------------------------------------------
FILENAME = "pyramid_sample_input.txt" # PLEASE CHANGE THE FILENAME & DIRECTORY BEFORE RUNNING PROGRAM |
# -----------------------------------------------------------------------------------------------------
# assuming that the first line is always going to state the target in the same format as the sample input file given.
file = open(FILENAME, "r")
input_file = file.read() # list of all characters in the input
target = 0 # variable for target
index_of_initial_row = 0 # variable for the first row index
list_of_all_num = [] # 2D list for holding all numbers

# getting the integer version of the target from the input file
for i in range(8, len(input_file)):
	if input_file[i] == "\n":
		index_of_initial_row = i + 1
		break
	target = input_file[8:i+1]
target = int (target)

# putting th tree into a 2D list
temp_list = [] # temporary list for putting a line of numbers into
num_index = index_of_initial_row # to start from the current line
for i in range(index_of_initial_row, len(input_file)):
	if input_file[i] == "\n":
		temp_list.append(int(input_file[num_index:i]))
		list_of_all_num.append(temp_list)
		temp_list = []
		num_index = i + 1
		continue
	if input_file[i] == ",":
		temp_list.append(int(input_file[num_index:i]))
		num_index = i + 1
		continue

# traversing through the tree to get the target value
combination_table = generate_combination_table(len(list_of_all_num) - 1)
combination_found = 0
for i in combination_table:
	product = list_of_all_num[0][0]
	recurring_index = 0
	for j in range(len(i)):
		if int(i[j]) == 1:
			recurring_index += 1
		product *= list_of_all_num[j + 1][recurring_index]
	if product == target:
		combination_found = i
		break

# making it into L and R format
combination = ""
for i in combination_found:
	if int(i) == 0:
		combination += "L"
	else:
		combination += "R"

print(combination)