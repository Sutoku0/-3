# Имена агентов для каждого разведчика
cia_line = "Bond Smith Hunt"
mi6_line = "Bond Power Hunt"
kgb_line = "Petrov Hunt Ivanov"

cia = set(cia_line.split())
mi6 = set(mi6_line.split())
kgb = set(kgb_line.split())

agents_in_both = (cia & mi6) - kgb

print(' '.join(sorted(agents_in_both, reverse=True)))