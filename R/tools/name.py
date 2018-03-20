
def file_name(split_point, fname):
    return str(split_point)+'_feature_'+fname+'.csv'


def feature_name(name, type, start_date=None, end_date=None):
    result = u''
    return result+type+'_'+name+'_'+str(start_date)+'_'+str(end_date)