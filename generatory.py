import random

def gen_input_man():
    input_man_list = ["I136.1","I136.2","I136.4","I136.5","I136.6","I137.0","I137.1","I137.6"]
    result = random.choice(input_man_list)
    return result

def gen_output_man():
    output_man_list = ["Q136.0","Q136.1","Q136.2","Q136.3"]
    result = random.choice(output_man_list)
    return result

def gen_memory_man():
    memory_man_list = ["M0.0","M0.1","M0.2","M0.3","M0.4","M0.6","M0.7","M1.1","M1.2","M1.3","M1.4","M1.5","M1.6","M1.7",]
    result = random.choice(memory_man_list)
    return result


#sorting module

def gen_input_tr():
    input_tr_list = ["I136.0","I136.1","I136.2","I136.3","I137.0","I137.1","I137.5"]
    result = random.choice(input_tr_list)
    return result

def gen_output_tr():
    output_tr_list = ["Q136.0","Q136.1","Q136.2","Q136.3"]
    result = random.choice(output_tr_list)
    return result

def gen_memory_tr():
    memory_tr_list = ["M0.0","M0.1","M0.4","M0.5","M0.6","M0.7","M1.0","M1.1","M1.2","M1.3","M1.5","M1.6","M1.7","M2.0","M2.1","M2.2","M2.3"]
    result = random.choice(memory_tr_list)
    return result



def gen_bool():
    bool_list=["true","false"]
    result = random.choice(bool_list)
    return result




