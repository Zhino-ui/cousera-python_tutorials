def upper_case(name):
    return name.upper()

if __name__ == "__main__":
    name = "Maxwell"
    name_upper = upper_case(name)
    print(f"Upper case name is {name_upper}")

    print("dunder name", __name__)