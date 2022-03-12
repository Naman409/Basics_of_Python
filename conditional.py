def func_print(name):
    if len(name)<3:
        print("Inavlid User name. Keep the length between 3-15 ")
    elif len(name)>15:
        print("Too long name . Keep the length between 3-15")
    else:
        print("Welcome "+ name)

func_print("Naman")
func_print("Harshvardhansinghrathod")
func_print("Uv")