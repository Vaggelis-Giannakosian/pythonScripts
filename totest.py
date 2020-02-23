


def do_stuff(num):
    try:
        if num or num == 0:
            return int(num) + 5
        return 'please enter number'
    except ValueError as err:
        return err