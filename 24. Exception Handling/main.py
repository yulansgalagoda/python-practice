try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else:
    # only executes if there were no exceptions
    print(result)
finally:
    # these codes will run whether there was an exception or not.
    # best to close any opened files
    print("This will always execute")
