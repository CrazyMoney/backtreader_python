
s = '1,2,3;2,3,4;3,4,5'
def meanPoints(s:str):
    s = s.replace(' ','')
    group_list = s.split(';')
    print(group_list)
    result__list  = []
    if len(group_list):
        for  m in group_list:
            print(m)
            m_list = [ float(i) for i  in m.split(',')]
            if len(m_list):
                m_sum = sum(m_list)/len(m_list)
                result__list.append(str(m_sum))
    return result__list


def indexPerPoints(x,y):
    res = (x-y)/x
    return res

# def so2Points(s1,s2,s3)