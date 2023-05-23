def get_values(directory, vl):
    if isinstance(directory, dict):
        for direc in directory:
            get_values(directory[direc], vl)
    else:
        vl.append(directory)
        
        
a = {"production": {"hw": "foo", "livet": "bar"}, "dummy": {"hw": "baz"},
     "error_injection": {"hw": "koz", "livet": "foz"},
     "dummy_error_injection": {"hw": "dsf", "livet": "vax"}, "btst_model_all": {"livet": "vcv"},
     "production_3_0": {"hw": {"foo": {"bar": "bar"}}}}

vl = []

print(get_values(a, vl))
