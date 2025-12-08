Puzzle_input = list(tuple(map(int, line.split(","))) for line in open("08.input").readlines())

D = dict()  # Hopefully unique distance: d -> (box1, box2)
for n, box1 in enumerate(Puzzle_input):
    for box2 in Puzzle_input[n + 1 :]:
        d = sum((box1[k] - box2[k]) * (box1[k] - box2[k]) for k in range(3))
        if d in D:
            raise ValueError("Distances between junction boxes are not unique.")
        else:
            D[d] = (box1, box2)

Circ_IDs = dict()  # The id of each circuit the box belongs to, if any: box -> Circuit_ID
Circuit_members = dict()  # Members of each circuit: circ_ID --> set of boxes
Current_circuit = 0
for num_links, d in enumerate(sorted(D)):
    num_links += 1
    box1, box2 = D[d]
    if box1 not in Circ_IDs and box2 not in Circ_IDs:  # creating a new circuit
        Circ_IDs[box1] = Current_circuit
        Circ_IDs[box2] = Current_circuit
        Circuit_members[Current_circuit] = {box1, box2}
        Current_circuit += 1
    elif box2 not in Circ_IDs:  # add box2 to the circuit with box1
        Circ_IDs[box2] = Circ_IDs[box1]
        Circuit_members[Circ_IDs[box1]].add(box2)
        if len(Circuit_members[Circ_IDs[box1]]) == len(Puzzle_input):
            print(f"Part 2: {box1[0] * box2[0]}")
            break
    elif box1 not in Circ_IDs:  # add box1 to the circuit with box2
        Circ_IDs[box1] = Circ_IDs[box2]
        Circuit_members[Circ_IDs[box2]].add(box1)
        if len(Circuit_members[Circ_IDs[box2]]) == len(Puzzle_input):
            print(f"Part 2: {box1[0] * box2[0]}")
            break
    elif Circ_IDs[box1] != Circ_IDs[box2]:  # Merge the two circuits into the one with box1
        Circuit_members[Circ_IDs[box1]] |= Circuit_members[Circ_IDs[box2]]
        t = Circ_IDs[box2]
        for box in Circuit_members[Circ_IDs[box2]]:
            Circ_IDs[box] = Circ_IDs[box1]
        del Circuit_members[t]  # Delete the old box2 circuit
        if len(Circuit_members[Circ_IDs[box2]]) == len(Puzzle_input):
            print(f"Part 2: {box1[0] * box2[0]}")
            break
    else:  # nothing to do if both boxes are already on the same circuit
        pass
    if num_links == 999:  # Part 1 needs the answer caluclated at 1000 pairs
        p1 = sorted([len(t) for t in Circuit_members.values()], reverse=True)[:3]
        print(f"Part 1: {p1[0] * p1[1] * p1[2]}")
