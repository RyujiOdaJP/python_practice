def gen_chessboard(height=8, width=8):
    parent = []
    child = []

    if height < 2 or width < 2:
        return None

    else:
        while len(parent) != height:
            if len(parent) % 2 == 0:

                for i in range(width):
                    if i % 2 == 0:
                        child.append(1)

                    if i % 2 != 0:
                        child.append(0)

                for i in range(height):
                    parent.append(child)
                    child = []

                    if len(parent) % 2 != 0:
                        break

            if len(parent) % 2 != 0:
                for i in range(width):
                    if i % 2 != 0:
                        child.append(1)

                    if i % 2 == 0:
                        child.append(0)

                for i in range(height):
                    parent.append(child)
                    child = []

                    if len(parent) % 2 == 0:
                        break

        return parent

# print(gen_chessboard())
