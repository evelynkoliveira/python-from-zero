python

def check_age():
    age = int(input("How old are you?"))

    if age >= 18:
        return "You are an adult."
    else:
        return "You are a minor."

  result = check_age()
  print(result)
