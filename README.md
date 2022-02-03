# LCSTO

A code to perform Roothan-Hartree-Fock calculation of 2-electron atoms using Linear Combination of Slater-Type Orbitals. The code was used in the work
```
  Exact separation of radial and angular correlation energies in two-electron atoms
  Anjana R.Kammath, Raghunathan Ramakrishnan
  Chem. Phys. Lett. 720, 93 (2019);
  https://doi.org/10.1016/j.cplett.2019.02.004
```

The atomic orbitals are selected as even-tempered basis functions which enables one to reproduce Raffenetti's results discussed in 
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
Total SCF energy in hartree: -2.8616726261795122 


No. of Slater-type basis functions: 3
Optimal Exponents generated using alpha = 0.7499408016830662  and beta= 1.9223281763174245
1.441632333645436
2.7712904548568638
5.3273297261308805
Total SCF energy in hartree: -2.861676069768634 


No. of Slater-type basis functions: 4
Optimal Exponents generated using alpha = 0.8539359715379213  and beta= 1.6608861223138915
1.4182904044719638
2.3556188501984408
3.9124146577555963
6.498075209803723
Total SCF energy in hartree: -2.8616798754451898 


No. of Slater-type basis functions: 5
Optimal Exponents generated using alpha = 0.9727660298774556  and beta= 1.4387381556433136
1.399555603698359
2.0135940479852414
2.8970345868126404
4.168074198265708
5.9967673845972875
Total SCF energy in hartree: -2.8616799874588192 


No. of Slater-type basis functions: 6
Optimal Exponents generated using alpha = 1.0126741703805924  and beta= 1.3766453637479117
1.3940932016417054
1.9191719426725362
2.64201915711522
3.637123423575833
5.007029098444603
6.892903394524648
Total SCF energy in hartree: -2.8616799933368138 


No. of Slater-type basis functions: 7
Optimal Exponents generated using alpha = 1.0544538494759563  and beta= 1.3138750250065923
1.3854205778485196
1.8202694963653712
2.3916066300557888
3.142272220870482
4.128552992773725
5.424402666621619
7.126987189253304
Total SCF energy in hartree: -2.8616799955802787 


No. of Slater-type basis functions: 8
Optimal Exponents generated using alpha = 1.0766848654894963  and beta= 1.2843388236510225
1.382828173585639
1.7760199097744716
2.28101132170054
2.9295913976475356
3.7625879694327904
4.8324378065447995
6.206487487824474
7.971232839117276
Total SCF energy in hartree: -2.861679995605802
```
