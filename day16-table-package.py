from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Pokemon name", "Type"]
table.add_rows(
    [
        ["Pikachu","Electric"],
        ["Squirtle","Water"],
        ["Charmander","Fire"]
    ]
)

table.align = "r"
print(table)
