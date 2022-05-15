import datetime

# takes two dates in DATETIME Y-m-d format and returns a list with all the dates between those days
def daterange(initial,final):
    dr=[]
    while initial <= final:
        dr.append(initial)
        initial+=datetime.timedelta(days=1)
    return dr

#Perfoms a models Query search and returns None instead of an DoesnotExist exception
def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None

