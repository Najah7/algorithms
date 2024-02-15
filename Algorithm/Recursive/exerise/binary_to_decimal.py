def to_decimal(binary):
    if binary == 0:
        return 0

    return binary % 10 + 2 * to_decimal(binary // 10)


"""
NOTE: code represents the method below

 )24 - 0
 ￣
 )12 - 0
 ￣
 )6 - 0
 ￣
 )3 - 1
 ￣
 )1 - 1
 ￣
          
"""


def to_binary(decimal):
    if decimal == 0:
        return 0

    return decimal % 2 + 10 * to_binary(decimal // 2)


print(to_decimal(1011) == 11)
print(to_binary(11) == 1011)
print(to_binary(24) == 11000)
