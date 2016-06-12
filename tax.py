US_SINGLE_FEDERAL = [
        (0, 9275, 0.1),
        (9275, 37650, 0.15),
        (37650, 91150, 0.25),
        (91150, 190150, 0.28),
        (190150, 413350, 0.33),
        (413350, 415050, 0.35),
        (415050, 1e3000, 0.396)]

US_SINGLE_CAL = [
        (0, 7850, 0.01),
        (7850, 18610, 0.02),
        (18610, 29372, 0.04),
        (29472, 40773, 0.06),
        (40773, 51530, 0.08),
        (51530, 263222, 0.093),
        (263222, 315866, 0.103),
        (315866, 526443, 0.113),
        (526443, 1e3000, 0.123)]

US_SOCIAL_SECURITY = [(0, 106800, 0.0565)]

CAN_SINGLE_FEDERAL = [
        (0, 45282, 0.15),
        (45282, 90563, 0.206),
        (90563, 140448, 0.26),
        (140448, 200000, 0.29),
        (200000, 1e3000, 0.33)]

CAN_SINGLE_ONTARIO = [
        (0, 41536, 0.0505),
        (41536, 83075, 0.0915),
        (83075, 150000, 0.1116),
        (150000, 220000, 0.1216),
        (220000, 1e3000, 0.1316)]

CAN_EI = [(0, 1e3000, 0.0173)]
CAN_CPP = [(0, 44800, 0.0495)]

SF_TAXES = [US_SINGLE_FEDERAL, US_SINGLE_CAL, US_SOCIAL_SECURITY]
TORONTO_TAXES = [CAN_SINGLE_FEDERAL, CAN_SINGLE_ONTARIO, CAN_EI, CAN_CPP]

def CalcTax(brackets, v):
    tax = 0
    for b in brackets:
        if v > b[0]:
            tax += (min(v, b[1]) - b[0]) * b[2]
    return tax

def TorontoTax(v):
    tax = 0
    for tax_kind in TORONTO_TAXES:
        tax += CalcTax(tax_kind, v)
    return tax

def SFTax(v):
    tax = 0
    for tax_kind in SF_TAXES:
        tax += CalcTax(tax_kind, v)
    return tax
