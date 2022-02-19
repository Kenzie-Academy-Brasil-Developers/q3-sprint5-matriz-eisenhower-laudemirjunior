def data_to_patch(query, data):
    for key, value in data.items():
        setattr(query, key, value)
    
    return query