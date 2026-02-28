while True:
    try:
        age = int(input('Please enter your age: '))
        print(f'You are {age} years old')
    # except ValueError:
    #     print('Please enter a number')
    # except ZeroDivisionError:
    #     print('Please enter number greater than zero')
    except (ValueError, ZeroDivisionError) as err:
        print(err)
    else:
        print('Thank you!')
        break
        