import asyncio as asy

def functia_1(tstop,bucla):
    print("Functia 1 apelata")
    if bucla.time() + 1.0 < tstop:
        bucla.call_later(1,functia_2,tstop,bucla)
    else:
        bucla.stop()

def functia_2(tstop,bucla):
    print("Functia 2 apelata")
    if bucla.time() + 1.0 < tstop:
        bucla.call_later(1,functia_3,tstop,bucla)
    else:
        bucla.stop()

def functia_3(tstop,bucla):
    print("Functia 3 apelata")
    if bucla.time() + 1.0 < tstop:
        bucla.call_later(1,functia_1,tstop,bucla)
    else:
        bucla.stop()

if __name__ == "__main__":
    bucla_asincrona = asy.get_event_loop()
    sfarsit_bucla = bucla_asincrona.time() + 6.0
    bucla_asincrona.call_soon(functia_1,sfarsit_bucla,bucla_asincrona)
    bucla_asincrona.run_forever()
    bucla_asincrona.close()

