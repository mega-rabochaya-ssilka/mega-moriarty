def boxify(text):
    width = len(text) + 4
    print("+" + "-" * (width - 2) + "+")
    print("| " + text + " |")
    print("+" + "-" * (width - 2) + "+")

boxify("Привет, мир!")
# Вывод:
# +--------------+
# | Привет, мир! |
# +--------------+
