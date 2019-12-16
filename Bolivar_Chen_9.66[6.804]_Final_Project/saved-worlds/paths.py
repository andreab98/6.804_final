def push(obj, l, depth):
    while depth:
        l = l[-1]
        depth -= 1
    l.append(obj)

def path_parser(path_str):
    groups = []
    depth = 0
    s1,s2 = "",""
    s2_ = False
    done,start = False,False
    nums = "-1234567890."
    for char in range(len(path_str)-1):
        if path_str[char] == '(' and path_str[char+1] in nums:
            start = True
        elif path_str[char] == ')' and path_str[char-1] in nums:
            pass
        else:
            if start:
                if len(s2)<13:
                    done = False
                    if s2_:
                        s2+=path_str[char]
                    else:
                        if path_str[char]==" ":
                            s2_ = True
                        else:
                            s1+=path_str[char]
                elif len(s2)==13:
                    done  = True
                    s2_ = False
                if done:
                    push((float(s1),float(s2)), groups, depth)
                    s2 = ""
                    s1 = ""
                    start = False
            if path_str[char] == '(':
                push([], groups, depth)
                depth += 1
            elif path_str[char] == ')':
                depth -= 1

    return groups

#
# path_str = world1_path.path_1
# ''
# g = (path_parser(path_str))
# for j in g[0]:
#     print(j[0])
#     print(j[1])
