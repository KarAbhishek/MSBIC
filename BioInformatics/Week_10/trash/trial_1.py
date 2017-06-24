# Complete the function below.


def  melon_count(boxes, melons):
    end = len(boxes)
    ls = []
    for idx in range(len(melons)):
        ls.append(recurse(boxes, melons, 0, idx))
    return max(ls)


def recurse(boxes, melons, source_box, source_melon):
    if source_box >= len(boxes) or source_melon >= len(melons):
        if source_melon != len(melons):
            return 0
        else:
            return 1
    var = float('-inf')
    if boxes[source_box] >= melons[source_melon]:
        stub = recurse(boxes, melons, source_box + 1, source_melon + 1)
        var = 0 if stub == 0 else 1 + stub
    var2 = recurse(boxes, melons, source_box + 1, source_melon)
    return max([var, var2])


print(melon_count([2,1,2,2],[3,2,3,2]))