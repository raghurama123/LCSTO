# LCSTO

A code to perform Roothan-Hartree-Fock calculation of 2-electron atoms using Linear Combination of Slater-Type Orbitals. The code was used in the work
```
  Exact separation of radial and angular correlation energies in two-electron atoms
  Anjana R.Kammath, Raghunathan Ramakrishnan
  Chem. Phys. Lett. 720, 93 (2019);
  https://doi.org/10.1016/j.cplett.2019.02.004
```

The atomic orbitals are selected as even-tempered basis functions which enables one to reproduce Raffenetti's results from 
```
  Even‐tempered atomic orbitals. II. Atomic SCF wavefunctions in terms of even‐tempered exponential bases
  Richard C. Raffenetti
  J. Chem. Phys. 59, 5936 (1973); 
  https://doi.org/10.1063/1.1679962
```

The purpose of sharing the code and the following results is to demonstrate, how with a simple 'toy' program, historical results in quantum chemistry may be reproduced. 

# Results
```
=======================================================================
No. of basis functions                 SCF energy (hartree)
-----------------------------------------------------------------------
                               This code               Rafenetti's work
 1                         -2.847 656 250 000 
 2                         -2.861 672 626 180
 3                         -2.861 676 069 769        -2.861 679 036 686 
 4                         -2.861 679 875 445        -2.861 679 875 316 
 5                         -2.861 679 987 459        -2.861 679 986 833 
 6                         -2.861 679 993 337        -2.861 679 987 495 
 7                         -2.861 679 995 580        -2.861 679 994 968 
 8                         -2.861 679 995 606        -2.861 679 995 610 
12                                                   -2.861 679 995 615
=======================================================================
```

# Sample run

```
> python3 lcsto.py 
```

```
No. of Slater-type basis functions: 1
Optimal Exponents generated using alpha = 1.0567284642370978  and beta= 1.5969097269003423
1.687499963232682
Total SCF energy in hartree: -2.8476562499999982 


No. of Slater-type basis functions: 2
Optimal Exponents generated using alpha = 0.7264028021946469  and beta= 2.0002189508643307
1.4529646509106866
2.906247429687532
Total SCF energy in hartree: -2.8616726261795105 


No. of Slater-type basis functions: 3
Optimal Exponents generated using alpha = 0.7499408016830662  and beta= 1.9223281763174245
1.441632333645436
2.7712904548568638
5.3273297261308805
Total SCF energy in hartree: -2.861676069768634 


No. of Slater-type basis functions: 4
Optimal Exponents generated using alpha = 0.8539368519660311  and beta= 1.6608849915181203
1.4182909011346119
2.3556180713011874
3.912410700373003
6.498064212904418
Total SCF energy in hartree: -2.8616798754451778 
```
