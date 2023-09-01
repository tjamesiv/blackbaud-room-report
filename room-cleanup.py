import csv

# Read the CSV file and create a dictionary to store room information
rooms_report = {}
current_room = None
blocks = []

need_to_handle_first_class = False
first_class = None

with open('input.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row_number, row in enumerate(csv_reader, start=1):

        # Grab the list of blocks
        if row_number == 4:
            blocks = row

        # If there's a new room entry
        if row[1]:

            print(f"Found room {row[1]}")

            current_room = row[1]
            rooms_report[current_room] = []
            # blocks = [block.strip() for block in row[4:] if block.strip()]

        # If there's a class
        if row[2] or need_to_handle_first_class:

            if need_to_handle_first_class:
                need_to_handle_first_class = False

            print(f"Found class {row[2]}")

            # Deal with weird formatting for first class
            if current_room is None:
                print("a")
                first_class = row[2]
                need_to_handle_first_class = True
                
            else:
                column_index = None
                non_blank_count = 0
                # Iterate through the row elements and find the second non-blank entry
                for index, entry in enumerate(row):
                    if entry.strip() != "":
                        non_blank_count += 1
                        if non_blank_count == 2:
                            column_index = index  # Index of the second non-blank entry
                            break

                if column_index is not None:
                    course = row[2]
                    block = blocks[column_index]
                    teacher = row[column_index]
                    rooms_report[current_room].append(f"Block {block}: {course} ({teacher})")

# Write room information to a text file
with open('room_schedule.txt', 'w') as txt_file:
    for room, blocks in rooms_report.items():
        txt_file.write(f"{room}\n\n")
        for block_info in blocks:
            txt_file.write(f"{block_info}\n")
        txt_file.write('\n')