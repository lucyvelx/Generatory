import time
import database_inserts as dbi
import generatory as gen

while True:
    #zapis do db pre manipulacny modul
    dbi.man_input(gen.gen_input_man(),gen.gen_bool()) #vstupy
    dbi.man_output(gen.gen_output_man(),gen.gen_bool()) #vystupy
    dbi.man_memory(gen.gen_memory_man(),gen.gen_bool())#pamate

    dbi.tr_input(gen.gen_input_tr(),gen.gen_bool()) #vstupy
    dbi.tr_output(gen.gen_output_tr(),gen.gen_bool()) #vystupy
    dbi.tr_memory(gen.gen_memory_tr(),gen.gen_bool()) #pamate



    time.sleep(10)