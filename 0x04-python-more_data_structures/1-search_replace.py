#!usr/bin/python3
def search_replace(my_list, search, replace):
    #def s_r_elm(lm):
        #return (lm if lm != search else replace)
    num = lambda x: x if x != search else replace   
    return list(map(num, my_list))
