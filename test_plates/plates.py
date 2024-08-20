def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        if s[0:2].isalpha():
            for _ in s:
                if _.isdigit():
                    if _ != "0" and s[s.index(_):len(s)].isdigit():
                        return True
                    else:
                        return False
                else:
                    continue
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
