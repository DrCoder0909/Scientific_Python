def str_vector(v):
    assert type(v) is list or type(v) is tuple,\
        'argument to str_vector must be a list or tuple'
    assert len(v) in (2, 3), \
        'Vector must be 2D or 3D in string vector'
    unit_vectors = ["i", "j", "k"]
    s = []
    for i, component in enumerate(v):
        s.append("{}{}".format(component, unit_vectors[i]))
        return "+".join(s).replace("+-", "-")


str_vector((2, 3, 4))
