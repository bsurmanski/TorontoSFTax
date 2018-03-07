# format for bracket (bracket start$, bracket end$, tax%)

class USA:

  class Federal:
    INCOME_SINGLE = [
        (0, 9525, 0.1),
        (9625, 38700, 0.12),
        (38700, 82500, 0.22),
        (82500, 157500, 0.24),
        (157500, 200000, 0.32),
        (200000, 500000, 0.35),
        (500000, float('inf'), 0.37)]
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

  class Washington:
    INCOME_SINGLE = [(0, float('inf'), 0.0)]



class Canada:

  class Federal:
    INCOME_SINGLE = [
        (0, 46605, 0.15),
        (46606, 93208, 0.205),
        (93208, 144489, 0.26),
        (144489, 205842, 0.29),
        (205842, float('inf'), 0.33)]
    EI = [(0, float('inf'), 0.0173)]
    CPP = [(0, 44800, 0.0495)]

  class Ontario:
    INCOME_SINGLE = [
        (0, 42960, 0.0505),
        (42960, 85923, 0.0915),
        (85923, 150000, 0.1116),
        (150000, 220000, 0.1216),
        (220000, float('inf'), 0.1316)]

  class Quebec:
    INCOME_SINGLE = [
        (0, 43055, 0.15),
        (43055, 86105, 0.20),
        (86105, 104765, 0.24),
        (104765, float('inf'), 0.2575)
    ]

  class BC:
    INCOME_SINGLE = [
        (0, 39676, 0.0506),
        (39676, 79353, 0.077),
        (79353, 91107, 0.1050),
        (91107, 110630, 0.1229),
        (110630, 150000, 0.1470),
        (150000, float('inf'), 0.168)
    ]


SF_TAXES = [USA.Federal.INCOME_SINGLE,
            USA.California.INCOME_SINGLE,
            USA.Federal.SOCIAL_SECURITY]

SEATTLE_TAXES = [USA.Federal.INCOME_SINGLE,
                 USA.Washington.INCOME_SINGLE,
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

def SeattleTax(v):
  return CityTaxes(SEATTLE_TAXES, v)
