def cross_validation(data):
    rows = data.shape[0]
    columns = data.shape[1]
    classes = set(data[:-1])

