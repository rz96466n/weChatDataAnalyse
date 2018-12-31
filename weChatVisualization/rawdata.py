def raw_data():
    import pandas as pd
    import copy
    import itchat
    friends = itchat.get_friends(update=True)
    friend = copy.copy(friends)
    df = pd.DataFrame(data=friend, )
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 200)

    return df;