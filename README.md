# LCSTO

Program used to perform Roothan-Hartree-Fock calculation of 2-electron atoms using Slater-type basis functions for the work
```
  Exact separation of radial and angular correlation energies in two-electron atoms
  Anjana R.Kammath, Raghunathan Ramakrishnan
  Chem. Phys. Lett. 720, 93 (2019);
  https://doi.org/10.1016/j.cplett.2019.02.004
```

The atomic orbitals are selected as even-temperted basis functions which enables one to reproduce the Raffenetti's results discussed in 
```
  Even‐tempered atomic orbitals. II. Atomic SCF wavefunctions in terms of even‐tempered exponential bases
  Richard C. Raffenetti
  J. Chem. Phys. 59, 5936 (1973); 
  https://doi.org/10.1063/1.1679962
```

# Results

```
> python3 lcsto.py 
```

```
No. of Slater-type basis functions: 1
Optimal Exponents generated using alpha = 1.0567430313584043  and beta= 1.5968878373989417
1.6875000940323244
Total SCF energy in hartree: -2.8476562499999925 


No. of Slater-type basis functions: 2
Optimal Exponents generated using alpha = 0.7264139917022606  and beta= 2.0001879648028296
1.4529645236672442
2.906202153524698
Total SCF energy in hartree: -2.8616726261654484 


No. of Slater-type basis functions: 3
Optimal Exponents generated using alpha = 0.749928648239762  and beta= 1.9223677622417956
1.441638657357686
2.7713596797059616
5.327572505843489
Total SCF energy in hartree: -2.861676069768106 


No. of Slater-type basis functions: 4
Optimal Exponents generated using alpha = 0.8539215361563312  and beta= 1.660915600128609
1.4182916006878363
2.3556626451138034
3.9125568359097387
6.498426685152316
Total SCF energy in hartree: -2.8616798754451995 


No. of Slater-type basis functions: 5
Optimal Exponents generated using alpha = 0.9727669770197445  and beta= 1.4387371008406045
1.3995559403108662
2.0135930560271014
2.897031035701205
4.168066033350005
5.996751240934184
Total SCF energy in hartree: -2.8616799874587944 


No. of Slater-type basis functions: 6
Optimal Exponents generated using alpha = 1.0127793899328648  and beta= 1.37650670990211
1.394097625893154
1.918984736300528
2.641495365717408
3.6360360950853394
5.005028082331236
6.889454738577437
Total SCF energy in hartree: -2.861679993336619 


No. of Slater-type basis functions: 7
Optimal Exponents generated using alpha = 1.0553277042673397  and beta= 1.3126512487351576
1.3852772288313306
1.8183858842698246
2.386906501669169
3.1331758000301013
4.112767126416289
5.398628904247247
7.086516972617865
Total SCF energy in hartree: -2.8616799955799266 


No. of Slater-type basis functions: 8
Optimal Exponents generated using alpha = 1.0793557727796261  and beta= 1.2808563212659374
1.382499664459665
1.7707834343711994
2.2681191555073568
2.9051347577159574
3.7210602185498716
4.766143502740814
6.104745033546148
7.8193012659344205
Total SCF energy in hartree: -2.8616799956065635
```
