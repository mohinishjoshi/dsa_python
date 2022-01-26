def flatten(arr):
    output_arr = []
    for elm in arr:
        if type(elm) is list:
            output_arr.extend(flatten(elm))
        else:
            output_arr.append(elm)

    return output_arr


print(flatten([1, 2, 3, [4, 5, [6, [7]]]]))
