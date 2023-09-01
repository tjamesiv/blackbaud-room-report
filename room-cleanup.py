import csv

# Read the CSV file and create a dictionary to store room information
rooms_report = {}
current_blocks = []
blocks = []


with open('input.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row_number, row in enumerate(csv_reader, start=1):

        # Grab the list of blocks
        if row_number == 4:
            blocks = row

        # If there's a new room entry
        if row[1]:
            current_room = row[1]
            print(f"Found room {current_room}")
            print(current_blocks)
            rooms_report[current_room] = []
            for course, block, teacher in current_blocks:
                rooms_report[current_room].append(f"Block {block}: {course} ({teacher})")
                current_blocks = [] # Reset

        # If there's a class
        if row[2]:
            current_class = row[2]
            print(f"Found class {current_class}")

             # Initialize an empty list to store non-blank entries and their indices
            non_blank_entries = []

            # Flag to track if the first non-blank element has been encountered
            found_first_non_blank = False

            # Iterate through the array
            for column_index, item in enumerate(row):
                if item:  # Check if the item is not blank (truthy)
                    if found_first_non_blank:
                        non_blank_entries.append((column_index, item))
                    else:
                        found_first_non_blank = True

            for column_index, item in non_blank_entries:
                if column_index is not None:
                    print(column_index)
                    block = blocks[column_index]
                    teacher = row[column_index].lstrip()
                    current_blocks.append((current_class, block, teacher))
                    

# Write room information to a text file
with open('room_schedule.txt', 'w') as txt_file:
    for room, blocks in rooms_report.items():
        txt_file.write(f"{room}\n\n")
        for block_info in blocks:
            txt_file.write(f"{block_info}\n")
        txt_file.write('\n')