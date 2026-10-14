def arrange_seating():
    students = []
    number_of_students = int(input("Number of students: "))
    for i in range(number_of_students):
        name = input("Student name: ")
        students.append(name)
    seats_per_room = int(input("Seats per room: "))
    rooms = {}
    unassigned = set()
    room_number = 1
    i = 0
    while i + seats_per_room <= len(students):
        rooms[room_number] = students[i:i + seats_per_room]
        room_number += 1
        i += seats_per_room
    remaining_students = students[i:]
    if len(remaining_students) >= 2:
        rooms[room_number] = remaining_students
    else:
        unassigned = set(remaining_students)
    for room, names in rooms.items():
        print(f"Room {room}: {names}")
    print("Unassigned:", unassigned)
arrange_seating()