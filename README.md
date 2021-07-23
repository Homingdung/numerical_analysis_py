# numerical_analysis_py

## Introduction 
I choose to upload the python file for my CW in year 2, which including some main numerical methods for mathematical problems, like root-finding problem, linear system, interpolation, derivative of interpolation and ODE solver. 

Additionaly, I add two interesting problems from physics, ```orbitCalculatro.py``` and ```trinityExplosion.py```. The below is the basic background information of these two physical problems

## Background 

### Orbit for satellite

###  

### Trinity Explosion

G. I. Taylor studied the movie of the Trinity test explosion, estimating the yield of the bomb. The method he used is what we called dimension analysis.

Dimensions of some physical variables:

$r$​ : the radius of the bomb cloud ~ $[L]$

$\rho$: density of air ~ $[ML^{-3}]$

$E$: energy released by the device ~ $[ML^2T^{-2}]$

$t$: time at which the bomb cloud reaches $r$ ~ $[T]$



Assuming that $r = f (\rho,E,t)$, that is :$r = C\rho^xE^yt^z$, where $x,y,z$ are constants. Based on their dimension:



$L = [ML^{-3}]^x[ML^2T^{-2}]^y[T]^z$

 

Expand both sides and equate corresponding exponents:

$L: 1 = -3x+2y$

$M:0 = x + y$

$T: 0 = -2y + z$



solve this systems and we can get:



$x = -1/5, y = 1/5, z = 2/5$



we could get the relationship between these variables:



$r = C(\frac{t^2E}{\rho})^{1/5}$



we could also use linear regression to solve the constants by rewirte the model and fit it:



$r = at^b$



take the $log$ for both sides:



$log(r) = log(a) + blog(t)$​​​



```trinityExplosion```  will calculate the parameter for $a$ and $b$ based on the data recorded.



$b \approx 0.4094$



so $E \approx \rho e^c$​, where $c = 5log(r)-2log(t)$​



By calculation, $E \approx 8.6418 \times10^{13} J$​, since $1 kt = 4.1848 \times 10 ^{12}$​, the total yield for bomb is $20.65 kt$​​.





References：

喻文健. *数值分析与算法*. Qing hua da xue chu ban she, 2015.
