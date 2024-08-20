def main():
    plate = str(input("Plate: "))
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6:
        head_alpha = s.rstrip('0123456789')
        tail_num = s[len(head_alpha):]
        if head_alpha.isalpha() and len(head_alpha) >= 2:
            if not tail_num.startswith("0"):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

main()
