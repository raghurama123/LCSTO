import numpy as np
from numpy import linalg as npla
from scipy import optimize

def eigen(A):
    eigenValues, eigenVectors = npla.eig(A)
    idx = np.argsort(eigenValues)
    eigenValues = eigenValues[idx]
    eigenVectors = eigenVectors[:,idx]
    return (eigenValues, eigenVectors)

def int_S(ai,aj):
    int_S = 8 * (ai * aj)**(3.0/2.0) / (ai + aj)**3
    return int_S

def int_T(ai,aj,diag):
    if diag == 'true':
        int_T = ai**2 - ai**2 / 2.0
    else:
        int_T = 4 * aj * ai**(3.0/2.0) * aj**(3.0/2.0) / (ai + aj)**2  - aj**2 * int_S(ai, aj) / 2.0
    return int_T

def int_Vne(ai, aj, Z, diag):
    if diag == 'true':
        int_Vne = -Z * ai
    else:
        int_Vne = -Z * 4 * ai**(3.0/2.0) * aj**(3.0/2.0) / (ai + aj)**2
    return int_Vne
  
def int_Vee(ai, aj, ak, al):
  int_Vee = (ai+aj)**(-2) * (ai+aj+ak+al)**(-3) * (2 + 6 * (ai+aj)/(ai+aj+ak+al)) + \
            (ak+al)**(-2) * (ai+aj+ak+al)**(-3) * (2 + 6 * (ak+al)/(ai+aj+ak+al))
  int_Vee = int_Vee * 16 * (ai*aj*ak*al)**(3.0/2.0)
  return int_Vee

def energy(param):

  zeta=np.zeros(N_zeta)
  S=np.zeros([N_zeta,N_zeta])
  T=np.zeros([N_zeta,N_zeta])
  Vne=np.zeros([N_zeta,N_zeta])
  Vee=np.zeros([N_zeta,N_zeta,N_zeta,N_zeta])
  occ=np.zeros([N_zeta,N_zeta])
  SMH=np.zeros([N_zeta,N_zeta])
  C=np.zeros([N_zeta,N_zeta])
  P=np.zeros([N_zeta,N_zeta])
  F=np.zeros([N_zeta,N_zeta])
  G=np.zeros([N_zeta,N_zeta])
  H=np.zeros([N_zeta,N_zeta])

  alpha=np.abs(param[0])
  beta=np.abs(param[1])
  for i_zeta in range(N_zeta):
    zeta[i_zeta] = alpha * beta**(i_zeta+1)

  for i in range(0,N_zeta):
    S[i,i] = int_S(zeta[i], zeta[i])
    T[i,i] = int_T(zeta[i], zeta[i], 'true')
    Vne[i,i] = int_Vne(zeta[i], zeta[i], Z, 'true')
    H[i,i] = T[i,i] + Vne[i,i]
    for j in range(i+1,N_zeta):
      S[i,j] = int_S(zeta[i], zeta[j])
      S[j,i] = S[i,j]
      T[i,j] = int_T(zeta[i], zeta[j], 'false')
      T[j,i] = T[i,j]
      Vne[i,j] = int_Vne(zeta[i], zeta[j], Z, 'false')
      Vne[j,i] = Vne[i,j]

      H[i,j] = T[i,j] + Vne[i,j]
      H[j,i] = H[i,j]

  for i in range(0,N_zeta):
    for j in range(i,N_zeta):
      for k in range(i,N_zeta):
        for l in range(k,N_zeta):
          Vee_tmp = int_Vee(zeta[i], zeta[j], zeta[k], zeta[l])
          Vee[i,j,k,l] = Vee_tmp
          Vee[j,i,k,l] = Vee_tmp
          Vee[i,j,l,k] = Vee_tmp
          Vee[j,i,l,k] = Vee_tmp
          Vee[k,l,i,j] = Vee_tmp
          Vee[l,k,i,j] = Vee_tmp
          Vee[k,l,j,i] = Vee_tmp
          Vee[l,k,j,i] = Vee_tmp

  E,V=eigen(S)

  for i in range(N_zeta):
    SMH[i,i]=1/np.sqrt(E[i])

  X = np.matmul(V, np.matmul(SMH, np.transpose(V)))

  occ[0,0]=2
  P = np.matmul(C, np.matmul(occ, np.transpose(C)))

  eold = 99999
  d_energy = eold

  i_scf=0

  while d_energy > e_scf_thresh: # begin SCF cycle

    i_scf = i_scf + 1

    for i in range(0,N_zeta):
      for j in range(i,N_zeta):
        F[i,j] = H[i,j]
        for k in range(N_zeta):
          for l in range(N_zeta):
            F[i,j] = F[i,j] + P[k,l] * ( Vee[i,j,l,k] - Vee[i,k,l,j]/2.0 )
        F[j,i] = F[i,j]

    F1 = np.matmul(X, np.matmul(F, np.transpose(X)))

    E,V=eigen(F1)

    C = np.matmul(X, V)
    P = np.matmul(C, np.matmul(occ, np.transpose(C)))

    enew = np.trace(np.matmul(P,(F+H)/2))

    d_energy = np.abs(enew - eold)

    eold = enew # end SCF cycle

  return  enew

#=== parameters
Z=2.0        # Nuclear charge
alpha=1.0    # 
beta=1.5     # alpha, beta are parameters to generate the STO exponents

param=np.array([alpha,beta])

convergence_options={'ftol': 1e-14, 'maxiter': 15000}

e_scf_thresh = 1e-14

for i_zeta in range(1,5):

  N_zeta = i_zeta

  result=optimize.minimize(energy,param,method='Nelder-Mead',options=convergence_options)
  param=result.x

  param=result.x
  alpha=np.abs(param[0])
  beta=np.abs(param[1])
  zeta=np.zeros(N_zeta)
  for i_zeta in range(i_zeta):
    zeta[i_zeta] = alpha * beta**(i_zeta+1)

  escf=result.fun

  print('\nNo. of Slater-type basis functions:',i_zeta+1)

  print('Optimal Exponents generated using alpha =',alpha,' and beta=',beta)
  for i_zeta in range(N_zeta):
    print(zeta[i_zeta])

  print('Total SCF energy in hartree:',escf,'\n')

