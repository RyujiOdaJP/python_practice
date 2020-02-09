class MatrixModule:

    @staticmethod
    def gen_empty_matrix(height, width):
        parent = []
        child = []

        if height <= 0 or width <= 0:
            return None

        else:
            for i in range(width):
                child.append('')

            for i in range(height):
                parent.append(child)

            return parent

    @staticmethod
    def gen_value_matrix(value, height, width):
        emp = MatrixModule.gen_empty_matrix(height, width)

        for i in range(height):
            for j in range(width):
                emp[i][j] = value

        return emp


# print(MatrixModule.gen_empty_matrix(3, 3))
# print(MatrixModule.gen_value_matrix('A', 0, 1))
