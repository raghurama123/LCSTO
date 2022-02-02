def int_S(ai,aj):
    int_S = 8 * (ai * aj)**(3.0/2.0) / (ai + aj)**3
    return int_S

def int_T(ai,aj,diag):
    if (diag):
        int_T = ai**2 - ai**2 / 2.0
    else:
        int_T = 4 * aj * ai**(3.0/2.0) * aj**(3.0/2.0) / (ai + aj)**2  - aj**2 * int_S(ai, aj) / 2.0
    return int_T

def int_Vne(ai, aj, Z, diag):
    if (diag):
        int_Vne = -Z * ai
    else:
        int_Vne = -Z * 4 * ai**(3.0/2.0) * aj**(3.0/2.0) / (ai + aj)**2
    return int_Vne
  
def int_Vee(ai, aj, ak, al):
  int_Vee = (ai+aj)**(-2) * (ai+aj+ak+al)**(-3) * (2 + 6 * (ai+aj)/(ai+aj+ak+al)) + \
            (ak+al)**(-2) * (ai+aj+ak+al)**(-3) * (2 + 6 * (ak+al)/(ai+aj+ak+al))
  int_Vee = int_Vee * 16 * (ai*aj*ak*al)**(3.0/2.0)
  return int_Vee
