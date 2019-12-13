def push(obj, l, depth):
    while depth:
        l = l[-1]
        depth -= 1

    l.append(obj)

def path_parser(path_str):
    groups = []
    depth = 0
    # l = []
    s1 = ""
    s2  = ""
    s2_ = False
    a = False #add
    s1_ = True
    for char in path_str:
        if char == '(':
            push([], groups, depth)
            depth += 1
            s2_=False
            s1 = ""
            s2 = ""
            s1_ = False
        elif char == ')':
            depth -= 1
            # l.append((s1,s2))
            s2_=False
            s1_ = False
        else:
            if char != ",":
                if s2_:
                    s2+=char
                else:
                    s1+=char
            else:
                s2_ = True
            if s2_ and len(s2)>17 :
                push((s1,s2), groups, depth)
    # return groups
    return groups

import path_data

path_str = path_data.path1
path_str = path_str.replace(" ", ",")
print(path_parser(path_str))


# print(path_parser('(a(b(c)(d)e)(f)g)'))
