import csv

# Read the CSV file and create a dictionary to store room information
rooms = {}
current_room = None
blocks = []

with open('input.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row_number, row in enumerate(csv_reader, start=1):

        # Grab the list of blocks
        if row_number == 4:
            blocks = row
            print(blocks)

        # If there's a new room entry
        if row[1]:
            current_room = row[1]
            rooms[current_room] = []
            # blocks = [block.strip() for block in row[4:] if block.strip()]
        # If there's a class
        if row[2]:
            non_blank_columns = [index for index, value in enumerate(row) if value != ""]
            if len(non_blank_columns) == 1:
                column_index = non_blank_columns[0] # This is the column where the block is for that class
                block = row[4]

                # Need to decide data structure to associate each room with a block/teacher/enrollment triple

        if current_room and row[i + offset]:
            instructor = row[i]
            rooms[current_room].append(f"Block {blocks.pop(0)}: {instructor}")

# Write room information to a text file
with open('room_schedule.txt', 'w') as txt_file:
    for room, blocks in rooms.items():
        txt_file.write(f"{room}\n\n")
        for block_info in blocks:
            txt_file.write(f"{block_info}\n")
        txt_file.write('\n')