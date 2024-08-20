# define main function to ask user to input time
def main():
    time = input("What time is it? ").strip()
    time_value = convert(time)
    if 7.0 <= time_value <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_value <= 13.0:
        print("lunch time")
    elif 18.0 <= time_value <= 19.0:
        print("dinner time")
    else:
        pass

def convert(time):
    if time.endswith("a.m."):
        hr, min = time.rstrip(" a.m.").split(":")
        time_value = int(hr) + int(min)/60
        return round(float(time_value), 2)
    elif time.endswith("p.m."):
        hr, min = time.rstrip(" p.m.").split(":")
        time_value = int(hr) + 12 + int(min)/60
        return round(float(time_value), 2)
    else:
        hr, min = time.split(":")
        time_value = int(hr) + int(min)/60
        return round(float(time_value), 2)

if __name__ == "__main__":
    main()
