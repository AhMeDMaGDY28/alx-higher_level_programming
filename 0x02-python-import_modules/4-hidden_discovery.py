#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = [name for name in dir(hidden_4) if not name.startswith("_")]
    names_sorted = sorted(names)
    for name in names_sorted:
        print(name)
