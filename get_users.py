

users = [
    'https://github.com/AlCapone03',#andreas
    'https://github.com/DanielLystad', #dany l
    'https://github.com/DanielG-Hub', #daniel g
    'https://github.com/fredrikmskaret', #fredrik m
    'https://github.com/S1-69', #siki
    'github.com/chipzymango', #alex
    'github.com/daddyfister', #morten
    'https://github.com/Storm02r', #storm
]

def get_user_names(users):
    ret = []
    for u in users:
        uname = u.split('github.com/')[-1]
        ret.append(uname)
    return ret




