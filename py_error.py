import sys
try:
    i = 1 / 0
except ZeroDivisionError as err:
    print(err)
else:
    print("unexcept error")

#%%
try:
    raise Exception("引起异常")
except Exception as ex:
    print(ex)


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError("自定义异常")
except Exception as ex:
    print(ex)

# %%
