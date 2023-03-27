#Challenge #3
#We have a nested object. We would like a function where you pass in the object and a key and
#get back the value.
#The choice of language and implementation is up to you.
#Example Input
#object = {“a”:{“b”:{“c”:”d”}}}
#key = a/b/c
#object = {“x”:{“y”:{“z”:”a”}}}
#key = x/y/z
#value = a


def getKey(obj: dict):
    keys = list(obj)
    return keys[0]
def getvalue(obj: dict, key: str):
    # print(obj, key, isFound)
    if type(obj) is not dict:
        return None
    if (key in obj.keys()) :
        if type(obj[key]) is dict:
            return getvalue(obj[key], getKey(obj[key]), True)
        else:
            # print(f'obj[getKey(obj)]: {obj[getKey(obj)]}')
            return obj[getKey(obj)]
    else:
        nestedKey = getKey(obj)
        return getvalue(obj[nestedKey], key)

if __name__ == '__main__':
    obj = {'x': {'y': {'z': 'a'}}}
    value = getvalue(obj, 'z')
    print(value)
 