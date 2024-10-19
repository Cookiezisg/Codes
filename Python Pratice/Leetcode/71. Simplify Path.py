class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = ['']
        period_tag = 0
        for i in path:
            if i == '/' and path_list[-1] != '':
                path_list.append('')
            elif i == '/' and path_list[-1] == '':
                continue
            else:
                path_list[-1] = path_list[-1]+i

        if path_list[-1] == '':
            path_list.pop()

        new_path_list=[]
        for i in path_list:
            if i == '.':
                continue
            elif i == '..':
                if new_path_list == []:
                    continue
                else:
                    new_path_list.pop()
            else:
                new_path_list.append(i)

        the_path_list = ''
        for i in new_path_list:
            the_path_list=the_path_list+'/'
            the_path_list=the_path_list+i

        
        if new_path_list == []:
            return '/'
        else:
            return the_path_list





solution = Solution()
path = "/../"
print(solution.simplifyPath(path))