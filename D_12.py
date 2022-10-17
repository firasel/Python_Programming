def do_something(work):
    print('Start the work')
    work()
    print('Done with the work')


def practice_coding():
    print('I am practicing python')


do_something(practice_coding)


def do_something2():
    print('Inside the function do_something')

    def inner_function():
        print('Inside the inner function')
    inner_function()

    def second_function():
        print('Inside the inner second function')
    return second_function


# second = do_something2()
# print(type(second))
# second()

do_something2()()
