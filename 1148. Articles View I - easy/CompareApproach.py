import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    n = views.shape[0]
    lst = set()
    for i in range(n):
        if views['author_id'][i] == views['viewer_id'][i]:
            lst.add(views['author_id'][i])
    lst = list(lst)
    items = {'id':sorted(lst)}
    df = pd.DataFrame(items)
    return df
