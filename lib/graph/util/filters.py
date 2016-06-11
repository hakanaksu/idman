# removes falsy values from dictionary
def clean_dict(dict):
    return {k:v for (k,v) in dict.iteritems() if v}


#  removes all values from dict for which function does not return true
def filter_values(dict,function):
    return {k: v for (k, v) in dict.iteritems() if function(v)}


# removes all keys from dict for which function does not return true
def filter_keys(dict,function):
    return {k: v for (k, v) in dict.iteritems() if function(k)}


# removes all keys from the dictionary wich contain a certain keyword (in strict mode equality is checked)
def remove_certain_keys(dict,keyword,strict=False):
    if strict:
        return filter_keys(dict, lambda x: not keyword == x)
    else:
        return filter_keys(dict, lambda x:  keyword not in x)


def remove_author(commit):
    return remove_certain_keys(commit,"author")


def remove_committer(commit):
    return remove_certain_keys(commit,"committer")


def remove_signer(commit):
    return remove_certain_keys(commit,"signer")