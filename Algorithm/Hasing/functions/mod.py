class ModHash:
    @staticmethod
    def num_hash(number: int, num_cells: int) -> int:
        return number % num_cells

    @staticmethod
    def string_hash(string: str, num_cells: int) -> int:
        return sum(map(ord, string)) % num_cells
