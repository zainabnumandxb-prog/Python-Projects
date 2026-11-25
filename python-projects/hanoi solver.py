def hanoi_solver(n: int) -> str:

    rod_a = list(range(n, 0, -1))
    rod_b = []
    rod_c = []

    moves = []


    def record_state():
        moves.append(f"{rod_a} {rod_b} {rod_c}")

    record_state()

    def move_disks(disks, source, target, auxiliary):
        if disks == 1:
            disk = source.pop()
            target.append(disk)
            record_state()
            return


        move_disks(disks - 1, source, auxiliary, target)

        disk = source.pop()
        target.append(disk)
        record_state()

        move_disks(disks - 1, auxiliary, target, source)

    move_disks(n, rod_a, rod_c, rod_b)

    return "\n".join(moves)


print(hanoi_solver(2))