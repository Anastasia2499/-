# def test_function():
#     def inner_function():
#         text = "Я в области видимости функции test_function"
#         return text
#     return inner_function()
#
# print(inner_function())   - функция  inner_function находится в локальном пространстве для функции test_function,
#                               а значит мы не можем ее достать



def test_function():
    def inner_function():
        text = "Я в области видимости функции test_function"
        return text
    return inner_function()

print(test_function()) 