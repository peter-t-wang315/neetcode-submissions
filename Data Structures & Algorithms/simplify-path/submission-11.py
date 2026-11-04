class Solution:
    def simplifyPath(self, path: str) -> str:
        l = 0
        dirs = []
        # iterate through path
        # have left and right indexes and continue incrementing right until we hit a /
        # take the substring of left to right and check the string
        # if substring is ., do nothing
        # if substring is .., pop the stack
        # if substring is anything else, add to stack
        # reset l/r
        for i in range(len(path)):
            if path[i] == "/":
                sub = path[l: i]
                if sub == "." or len(sub) == 0:
                    l = i+1
                    continue
                if sub == "..":
                    if len(dirs) > 0:
                        dirs.pop()
                else:
                    dirs.append(sub)
                l = i+1
        sub = path[l:]
        if sub == "..":
            if len(dirs) > 0:
                dirs.pop()
        elif len(sub) != 0 and sub != ".":
            dirs.append(sub)

        return "/" + "/".join(dirs)