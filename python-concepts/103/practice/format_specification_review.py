def format_floating_point(value):
    print(f"{value:.2f}")

def format_as_character():
    print(f"{58:c}{45:c}{41:c}")

def format_with_spaces():
    print(f"{"hello":<15}, {"world":>15}")

def format_money_with_comma():
    print(f"${50000000:,.2f}")

if __name__ == '__main__':
    format_floating_point(3.143456677)
    format_as_character()
    format_with_spaces()
    format_money_with_comma()