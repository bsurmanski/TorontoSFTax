# format for bracket (bracket start$, bracket end$, tax%)

class USA:

  class Federal:
    INCOME_SINGLE = [
        (0, 9275, 0.1),
        (9275, 37650, 0.15),
        (37650, 91150, 0.25),
        (91150, 190150, 0.28),
        (190150, 413350, 0.33),
        (413350, 415050, 0.35),
        (415050, float('inf'), 0.396)]
    SOCIAL_SECURITY = [(0, 106800, 0.0565)]

  class California:
    INCOME_SINGLE = [
        (0, 7850, 0.01),
        (7850, 18610, 0.02),
        (18610, 29372, 0.04),
        (29472, 40773, 0.06),
        (40773, 51530, 0.08),
        (51530, 263222, 0.093),
        (263222, 315866, 0.103),
        (315866, 526443, 0.113),
        (526443, float('inf'), 0.123)]



class Canada:

  class Federal:
    INCOME_SINGLE = [
        (0, 45282, 0.15),
        (45282, 90563, 0.206),
        (90563, 140448, 0.26),
        (140448, 200000, 0.29),
        (200000, float('inf'), 0.33)]
    EI = [(0, float('inf'), 0.0173)]
    CPP = [(0, 44800, 0.0495)]

  class Ontario:
    INCOME_SINGLE = [
        (0, 41536, 0.0505),
        (41536, 83075, 0.0915),
        (83075, 150000, 0.1116),
        (150000, 220000, 0.1216),
        (220000, float('inf'), 0.1316)]

  class Quebec:
    INCOME_SINGLE = [
        (0, 42390, 0.16),
        (42390, 84780, 0.20),
        (84780, 103150, 0.24),
        (103150, float('inf'), 0.2575)
    ]

  class BC:
    INCOME_SINGLE = [
        (0, 38898, 0.0506),
        (38898, 77797, 0.077),
        (77797, 89320, 0.1050),
        (89320, 108460, 0.1229),
        (108460, float('inf'), 0.1470)
    ]


SF_TAXES = [USA.Federal.INCOME_SINGLE,
            USA.California.INCOME_SINGLE,
            USA.Federal.SOCIAL_SECURITY]

TORONTO_TAXES = [Canada.Federal.INCOME_SINGLE,
                 Canada.Federal.EI,
                 Canada.Federal.CPP,
                 Canada.Ontario.INCOME_SINGLE]

MONTREAL_TAXES = [Canada.Federal.INCOME_SINGLE,
                  Canada.Federal.EI,
                  Canada.Federal.CPP,
                  Canada.Quebec.INCOME_SINGLE]

VANCOUVER_TAXES = [Canada.Federal.INCOME_SINGLE,
                   Canada.Federal.EI,
                   Canada.Federal.CPP,
                   Canada.BC.INCOME_SINGLE]


def CalcTax(brackets, v):
    tax = 0
    for b in brackets:
        if v > b[0]:
            tax += (min(v, b[1]) - b[0]) * b[2]
    return tax

def CityTaxes(tax_lst, v):
  tax = 0
  for tax_kind in tax_lst:
    tax += CalcTax(tax_kind, v)
  return tax

def TorontoTax(v):
  return CityTaxes(TORONTO_TAXES, v)

def SFTax(v):
  return CityTaxes(SF_TAXES, v)

def MontrealTax(v):
  return CityTaxes(MONTREAL_TAXES, v)

def VancouverTax(v):
  return CityTaxes(VANCOUVER_TAXES, v)
