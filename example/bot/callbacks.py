from microconst import flag, key


# Usually people use StrEnum and auto()
# but this approach quickly hits the limit.
class Navigation:
    MAIN_MENU = flag()
    DEPOSIT_MENU = flag()


# Another helpful feature is declarit type of values you want to pass in a callback.
class Data:
    DEPOSIT = key(int)  # DEPOSIT("abc") wont work if you're using type checking.
