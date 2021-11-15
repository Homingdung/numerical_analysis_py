![Applied Mathematics](https://img.shields.io/badge/math-applied%20mathematics-brightgreen)   ![Numerical Analysis](https://img.shields.io/badge/python-numerical%20anaylsis-green)

# Introduction 
>  ```CW_py``` is a collection of my coursework in year 2 rewritten by python, which includes numerical methods:

+ Nonlinear equations:
    + Bisection method ```bisection_func.py``` ```bisectionStop_func.py```
    + Fixed point method ```fpiter_func.py```
+ Linear system:
  + Direct methods:
     + Gaussian elimination ```forwElimPP_func.py```
     + LU decomposition```forwElimLU_funcc.py```
  + Iterative method:
    + Jacobi method ```jacobi_func.py```
+ Interpolation ```lagrangePoly.py``` ```polyInterpolation.py```
+ Numerical differentiation ```derivLagrangePoly.py``` ```polyDerivative```
+ ODE solver ```rungeKutta.py```



>  Additionaly, I add some interesting problems from physics, with my solutions by python and the corresponding physics background. These problems could be used as case study for scientific computing learning by python.

+ ```orbitCalculator.py```
+ ```trinityExplosion.py```
+ ```fieldsVisualize.py```
+ ```LorenzEq.py```
+ ```grepyModel.py``` 

# Background 

## Orbit for satellite 

>  ```orbitCalculator.py```  will calculate the length of orbit, average speed, and maximum speed of satellite

According to the  Kepler's laws, the orbit is an ellipse with major axis $a$ and minor axis $b$, satisfying the formula:

$$
\frac{x^2}{a^2}+\frac{y^2}{b^2} = 1
$$
![orbit](https://tva1.sinaimg.cn/large/008i3skNgy1gtd1q4hzcnj61320fmdgt02.jpg)



Geometrically, we can get write the formula for parameters: 

$$
\begin{eqnarray}
&&a=(h_1+h_2+2R)/2 \\
&&c=h_2+R-a=(h_2-h_1)/2\\
&&b=\sqrt{a^2-c^2}
\end{eqnarray}
$$

The length of the orbit is :
$$
L=4\int_0^{\pi/2}\sqrt{x^2+y^2}d\theta=4\int_0^{\pi/2}\sqrt{a^2cos^2\theta+b^2sin^2\theta}d\theta
$$


The area for the satellite passing by in time unit is:

$$
s=\frac{\pi ab}{T}
$$
The average speed of satellite is:

$$
v = L/T
$$


The maximum speed of satellite is:

$$
v_{max}=\frac{2s}{h_1+R}​
$$
Since we've already known that:
$$
\begin{eqnarray}
&&h_1=200km \\
&&h_2=51000km \\
&&R=6378km \\
&&T=16 h \\
\end{eqnarray}
$$
Therefore,  ```orbitCalculator.py```  will calculate the value for $L$​ , $v$​ and $v_{max}$​​.

## Trinity explosion

> ```trinityExplosion.py```  will use linear regression model to verify the dimensional analysis

[G. I. Taylor](https://en.wikipedia.org/wiki/G._I._Taylor) studied the movie of the Trinity test explosion, estimating the yield of the bomb. The method he used is what we called [dimension analysis](https://en.wikipedia.org/wiki/Dimensional_analysis).



![trinity](https://tva1.sinaimg.cn/large/008i3skNgy1gtd1qeszyvj60xc0q4wh502.jpg)

Dimensions of some physical variables:

$r$​ : the radius of the bomb cloud ~ $[L]$

$\rho$: density of air ~ $[ML^{-3}]$

$E$: energy released by the device ~ $[ML^2T^{-2}]$

$t$: time at which the bomb cloud reaches $r$ ~ $[T]$



Assuming that:
$$
r = f (\rho,E,t)
$$
Specifically:
$$
r = C\rho^xE^yt^z
$$
where $x,y,z$​​ are constants.



Based on their dimension:
$$
L = [ML^{-3}]^x[ML^2T^{-2}]^y[T]^z
$$


Expand both sides and equate corresponding exponents:

$$
\begin{eqnarray}
&&L: 1 = -3x+2y \\
&&M:0 = x + y   \\
&&T: 0 = -2y + z \\
\end{eqnarray}
$$
Solve this systems and we can get:

$$
x = -1/5, y = 1/5, z = 2/5
$$
Thus, we could get the relationship between these variables:

$$
r = C(\frac{t^2E}{\rho})^{1/5}
$$


we could also use linear regression to solve the constants by rewirte the model and fit it:

$$
r = at^b
$$
take the $log$ for both sides:
$$
log(r) = log(a) + blog(t)
$$
By linear regression, ```trinityExplosion.py```  will calculate the parameter for $a$​​ and $b$​​​ based on the data recorded, and we can get the value for parameter $b \approx 0.4094$​, which is nearly $2/5$

so:
$$
E \approx \rho e^c
$$
where $c = 5log(r)-2log(t)$​​​​,



Further calculation tells us that $E \approx 8.6418 \times10^{13} J$​​, since $1 kt = 4.1848 \times 10 ^{12}$​​, the total yield for bomb is $20.65 kt$​​​.



## Fields visualization
> ```fieldsVisualize.py``` will visualize the directional fields for certain function, with directions displayed by partial derivatives.

For given function $Z=f(x,y)$​, we will show the contour plot with the direction fields as well.



The gradient provides the directions, which is given by:

$$
\frac{\partial f}{\partial x}i+\frac{\partial f}{\partial y}j
$$
The vector has a magnitude:

$$
\sqrt{(\frac{\partial f}{\partial x})^2+(\frac{\partial f}{\partial y})^2}
$$
 and a direction:

$$
\theta = \tan^{-1} (\frac{\partial f / \partial y}{\partial f /\partial x})
$$
In this example, we use function $f(x,y)=y-x-2x^2-2xy-y^2$​



## Lorenz attractor

> ```LorenzEq.py``` will visualize the Lorenz equations 

The Lorenz equations originated from a miniature atmosphere model, which is described by the equations:
$$
\begin{eqnarray}
&&\dot{x} = -sx+sy\\
&&\dot{y} = -xz+rx-y\\ 
&&\dot{z} = xy-bz\\
\end{eqnarray}
$$

The variable $x$ denotes the clockwise circulation velocity , $y$ denotes the temperature difference between the ascending and descending columns of air and $z$ denotes the deviation from a strictly linear temperature profile in the vertical direction.



Commonly, the setting for the parameters is $s=10, r=28, b=8/3$



The trajectory of Lorenz equation is visualize by ```LorenzEq.py```



![Lorenz](https://tva1.sinaimg.cn/large/008i3skNgy1gtd1q3604ij60zk0qo41t02.jpg)

## Grey model for prediction

> ```greyModel.py``` will develop a grey model for predicting.

### Methods

Let the original data $\mathbf{x^{(0)}}=(x^{(0)}(1),x^{(0)}(2),...,x^{(0)}(n))$

+ Step 1: accumulate the original data to weaken the volatility.

$$
\mathbf{x^{(1)}}=(x^{(1)}(1),x^{(1)}(2),...,x^{(1)}(n))
$$

Where 
$$
x^{(0)}(t)=\sum_{t=1}^{n}x^{(0)}(t), \ t=1,2,...,n
$$


+ Step 2: Build a first order ODE:

$$
\frac{dx^{(1)}}{dt}+ax^{(1)}=b
$$

$a$ and $b$ are constants. Let's construct a matrix $\beta=(a,b)^T$, if we can get the parameters $\beta$, we could get the predicted value for $x^{(0)}$.

+ Step 3: make the average value for the accumlated sequence:

$$
\begin{equation}
\mathbf{B}=\left[\begin{array}{ccc}
0.5(x^{(1)}(1)+x^{(1)}(2))\\
0.5(x^{(1)}(2)+x^{(1)}(3))\\
.\\
.\\
0.5(x^{(1)}(n-1))+x^{(1)}(n))
\end{array}\right]
\end{equation}
$$

$$
\begin{equation}
\mathbf{Y_n}=(x^{(0)}(2),x^{(0)}(3),...,x^{(0)}(n))^T
\end{equation}
$$


+ Step 4: We use least square method to solve for $\beta$

$$
\beta=(\mathbf{B}^T\mathbf{B})^{-1}\mathbf{B}\mathbf{Y_n}
$$

+ Step 5: Once the parameters are known, we can solve for the ODE

$$
\hat{x}^{(1)}(t+1)=(x^{(0)}(1)-\frac{b}{a})exp(-at)+\frac{b}{a}
$$

+ Step 6: Get the original sequence 

$$
\hat{x}^{(0)}(t+1)=\hat{x}^{(1)}(t+1)-\hat{x}^{(1)}(t)
$$

+ Step 7: Once the model is selected, it must be tested to determine whether it is reasonable. We can calculate the residual.

$$
\epsilon^{(0)}(t)=\frac{x^{(0)}-\hat{x}^{(0)}(t)}{x^{(0)}(t)}
$$

The quality of the model is very high if $|\epsilon^{(0)}(t)|<0.1$. Actually, there are lots of model validation methods. For example, Posterior-variance-test, which is to test the statistical characteristics of the distribution of absolute residuals.

**Posterior-variance-test** [2]

1. Average value of the original sequence:

$$
\overline{x}^{(0)}= \frac{1}{n}\sum_{t=1}^{n}x^{(0)}(t)
$$

2. Mean square deviation of the original sequence:

$$
S_1 = \left(\frac{\sum_{t=1}^n(x^{(0)}(t)-\overline{x}^{(0)})^{2}}{n-1})^
{1/2}\right)
$$

3. Mean of residuals:

$$
\Delta(t) =|x^{(0)}(t)-\hat{x}^{(0)}(t)|, \ \overline{\Delta}=\frac{1}{n}\sum_{t=1}^n\Delta^{(0)}(t)
$$

4. Mean square deviation of residuals:

$$
S_2 = \left(\frac{\sum_{t=1}^n(\Delta^{(0)}(t)-\overline{\Delta}^{(0)})^{2}}{n-1})^
{1/2}\right)
$$

5. Variance ratio:

$$
C = \frac{S_2}{S_1}
$$



6. Mall residual probability:

$$
P=p\{|\Delta(t)-\overline{\Delta}|<0.6745\times S_1\}
$$

7. Test table: the ranks of forecase precision:


| The Value of P | The value of C | Forecast precision Grade |
| -------------- | -------------- | ------------------------ |
| $> 0.95$       | $<0.35$        | Grade one: excellent     |
| $>0.80$        | $<0.50$        | Grade two: good          |
| $>0.70$        | $<0.65$        | Grade three:qualified    |
| $\leq0.70$     | $\geq0.65$     | Grade four: unqualified  |


Keep in mind that only the model that passes the test can be used for prediction.

+ Step 8: prediction by our model

$$
\mathbf{\hat{x}^{(0)}}=[x^{(0)}(1),x^{(0)}(2),...,x^{(0)}(n), x^{(0)}(n+1),...,x^{(0)}(n+m)]
$$

### Example

Profits of a company from 1999-2008 are as follows: [89677, 99215, 109655, 120333, 135823, 159878, 182321, 209407, 246619, 300670], now we need to predict the profit for this company in the future. 

The true value and the predicted value could be seen as follows:

![greymodel](https://tva1.sinaimg.cn/large/008i3skNgy1gu7kqzz2s9j60zk0qoq4k02.jpg)

## Laplace method 

> ```Laplace_method.py``` will verify the Laplace method for asymptotic analysis of integral. 

$$
I(x)=\int_{7/4}^{\infty}e^{xf(t)}, f(t) = -7t^2+5t^3-t^4
$$

 Find the leading asymptotic behaviour of $I(x)$ when $x>>1$

Notice that $f(t)$ has a maximum point at $t=2$. Using Taylor series for $f(t)$ about $t=2$, we could get:
$$
f(t) \sim -4-(t-2)^2
$$

$$
I(x)\sim \int_{7/4}^{\infty} e^{x(-4-(t-2)^2)}dt=e^{-4x}\int_{7/4}^{\infty}e^{-x(t-2)^2}dt=e^{-4x}\int_{-\sqrt{x}/4}^{\infty}e^{-s^2}\frac{ds}{\sqrt{x}}
$$

Since here we use $s=\sqrt{x}(t-2)$ to do the substitution in order to construct special integrals we have already known.
$$
I(x)\sim \frac{e^{-4x}}{\sqrt{x}}\int_{-\infty}^{\infty}e^{-s^2}ds
$$


As $x$ approches infinity:
$$
I(x)\sim \sqrt{\frac{\pi}{x}}e^{-4x}
$$
Since we knew that: $\int_{-\infty}^{\infty}e^{-s^2}ds=\sqrt{\pi}$



Let's use numerical integration to double check our result: 

$I(10)\approx 1.85 \times10^{-18}$, while $\sqrt{\frac{\pi}{10}}e^{-40}\approx2.38\times10^{-18}$

$I(100)\approx3.7\times10^{-175}$,while $\sqrt{\frac{\pi}{100}}e^{-400}\approx3.4\times10^{-175}$





## Michaelis - Menton Model and Boundary layer theory

> ```boundaryLayer.py``` will visualize the exact solution plot for a singular ODE. 

### Introduction

[Michaelis-Menten Model](https://en.wikipedia.org/wiki/Michaelis%E2%80%93Menten_kinetics) is a classic model in enzyme dynamics. This article will explan how we use the ODE systems to model the enzyme reaction and solve it with boudary layer theory.

### Modeling 

Considering the following chemical reaction, where $E$ stands for the enzyme, $S$ stands for substrate, $ES$ is the binding, and $P$ is the product. 

![{\displaystyle {\ce {E{}+S<=>[{\mathit {k_{f}}}][{\mathit {k_{r}}}]ES->[k_{\ce {cat}}]E{}+P}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4bae00cd4d91917219daf235391295adeb36c84d)



The ODE systems are:
$$
\begin{aligned}
\frac{d[E]}{dt}&=-k_1^{+}[E][S]+k_1^{-}[ES]+k_2^{+}[ES]\\
\frac{d[S]}{dt}&= -k_1^{+}[E][S]+k_1^{-}[ES]\\
\frac{d[ES]}{dt}&=k_1^{+}[E][S]-k_1^{-}[ES]-k_2^{+}[ES]\\
\frac{d[P]}{dt}&=k_2^{+}{[ES]}

\end{aligned}
$$
where $k_1^+=k_f$, $k_1^-=k_r$, $k_2^+=k_{cat}$.

If we use conservation law, we find that :

$\dot{[E]}+\dot{[ES]}=0$, which is equaivalent to $[E]+[ES]=0=const=E_0$

$\dot{[S]}+\dot{[ES]}+\dot{[P]}=0$, which is equivalent to $[S]+[ES]+[P]=const=S_0$



At time t=0, we consider the initial conditions: $[E](0)=E_0$, $[S](0)=S_0$, $[ES](0)=S_0$, $[ES](0)=0$, $[P](0)=0$.

If we consider two ODEs when $t=0$:
$$
\begin{aligned}
&\frac{d[S]}{dt}_{t=0}=-k_1^+E_0[S]\\
&\frac{d[E]}{dt}_{t=0}=-k_1^{+}[E][S_0]
\end{aligned}
$$

> we want to see how $S$ evolves at the very beginning, so we keep it as variable, same for $E$



The LHS is the reaction rate, since we know that $S_0>>E_0$, so $\underbrace{-k_1^{+}[E][S_0]}_{fast\ rate}>>\underbrace{-k_1^+E_0[S]}_{slow \ rate}$.



### Nondimesionlization 

The advantage of nondimensionlizaton is that we could rescale our parameters such that we could reduce the number of our parameters, which could simplify our systems for further analytical solutions and paramter estimations. 

We plan to use two time scales for our systems. 

**Slow time scale**:

Choosing the variables: $t=\frac{\tau}{k_1^+E_0}$, $[S]=sS_0$, $[ES]=cE_0$, $\epsilon=\frac{E_0}{S_0}<<1$, and nondimesionlize the systems.
$$
\begin{aligned}
&\frac{ds}{d\tau}=k_sc-s(1-c)\\
&\epsilon\frac{dc}{d\tau}=s(1-c)-k_mc
\end{aligned}
$$


where $k_s=\frac{k_1^-}{k_1^+s_0}$, $k_m=\frac{k_2^++k_1^+}{k_1^+s_0}$

If $\epsilon \to 0$, then $0=s(1-c)-k_mc$, so $c=\frac{s}{s+k_m}$, which is a stationary solution. 

Substitute the stationary solution in the second equation we can get:

$\frac{ds}{d \tau}=\frac{s(k_s-k_m)}{s+k_m}$, $k_s-k_m=-\frac{k_2^+}{k_1+s_0}=-V_{max}$.

**Fast time scale**:

Choosing the variables: $t=\frac{T}{k_1^+S_0}$, $[S]=sS_0$, $[ES]=cE_0$, $\epsilon=\frac{E_0}{S_0}<<1$, and nondimesionlize the systems.
$$
\begin{aligned}
&\frac{ds}{dT}=\epsilon(k_sc-s(1-c))\\
&\frac{dc}{dT}=s(1-c)-k_mc
\end{aligned}
$$
If $\epsilon \to 0$, $\frac{dc}{dT}=-c(k_m+s)+s$.

**Tasking problem**:

Recall our intial conditions of this model are: $s(0)=1$, $c(0)=0$.

However, our equations cannot satisfy the initial condition on the slow time scale, when $\epsilon \to 0$.

$0=s(1-c)-k_mc$, so $c=\frac{s}{s+k_m}$, we can get that $c(0)=\frac{s(0)}{s(0)+k_m}=\frac{1}{1+k_m}$, while the inital condition is $c(0)=0$, which are inconsistent.



Considering the fast time scale:

when $\epsilon \to 0$, $\frac{ds}{d \tau}=0$, so $s=const=s(0)=1$. So our systems become:
$$
\frac{dc}{dT}=(1-c)-k_mc
$$
Solving the ODE:
$$
c(T)=Be^{-(1+k_m)T}+\frac{1}{1+k_m}
$$
Applying the intial condition: $c(0)=0$, so $B=\frac{-1}{1+k_m}$

Thus, 
$$
c(T)=\frac{1-e^{-(1+k_m)T}}{1+k_m}
$$


Back to slow time scale:

when $\epsilon \to 0$, we use the same skill:
$$
\frac{ds}{d\tau}=-\frac{V_{max}s}{s+k_m}
$$


Solving the ODE:
$$
s+k_m \ln{s}=-V_{max}\tau+A
$$
Now, there is one constant to be determined, i.e. $A$. We will use a skill called asymptotic matching which will be discussed later.

Taking the limit like below:
$$
\lim_{T \to \infty} c(T)=\frac{1}{1+k_m}, \lim_{\tau \to \infty} c(\tau)=\frac{s(0)}{s(0)+k_m}=\frac{1}{1+k_m}
$$
Matched!

Do the same: as $\tau \to 0$:
$$
k_m \ln s(0)+s(0)=A
$$
Thus, $A=1$

What we did above is one of the most important idea in boudary layer theory. Let's introduce it.

### Boundary layer theory

A boundary layer is a narrow region where the solution of a differential equation changes rapidly [9].  Considering the following equations:
$$
\epsilon y''+(1+\epsilon)y'+y=0, y(0)=0, y(1)=1.
$$
The exact solution is 
$$
y(x)=\frac{e^{-x}-e^{-x/\epsilon}}{e^{-1}-e^{-1/\epsilon}}
$$
If we plot the solution using python: 

![solutionplot](https://tva1.sinaimg.cn/large/008i3skNgy1gwge8meiudj30hs0dcgm1.jpg)

We found that, because of the term $e^{-x/\epsilon}$, which decays quickly as $\epsilon \to 0$, there is a sharp change of our solution which makes it become a singular problem. So that is the reason why we could not solve the Michaelis-Menten model using a normal way. One more thing is that the thickness of the boundary layer is $O(\epsilon)$.  If we recall that there is also a $\epsilon=\frac{E_0}{S_0}$ in Michaelis-Menten model, so it turns out that we could not capture what is going on at the very beginning by treating it as a regular problem. Actually, we could only solve it under two different time scales.



### Understanding time scale

It is very tricky for people to treat this problem in two different time scale at the first time. Let me put it in another way. Imaging that you want to capture the motion of an arrow on an England longbow (which is my favorite bow 😊). At the very begining, you cannot see the motion of the arrow unless you have a high-frequency camera since it moves so quickly. However, you can see the trajectory of the arrow if you stay far away from the acher (Not in front of him, you will die otherwise) just using your eyes, which is equivalent as using a low-frequncy camera. Thus, you can caputure the whole motion of the arrow using a high-frequency and low-frequency camera, which stand for two time scales. Considering the time units for these two cameras, you must use $s$ [second] as an unit for high-frequency camera while $h$ [hour] for low-frequency camera.



![longbow](https://tva1.sinaimg.cn/large/008i3skNgy1gwgemuwkfnj30el0bt3zm.jpg)
$$
fast \ time \ scale: 1 h = 3600 s, \tau=\frac{t}{\epsilon}\\
slow \ time \ scale: 1 s = \frac{1}{3600} h, T = \epsilon t
$$
This is exact what we did when solving the Michaelis-Menton model. Because of the existence of the boundary layer, our solution could not satisfy the boudary conditions. So we must work the general solution out with undetermined coefficients and using the asympotic matching skill to find the coefficients then get the final solution.





# References：

[1] Johansson, Robert, Robert Johansson, and Suresh John. *Numerical Python*. Vol. 1. Apress, 2019.

[2] Kincaid, David, David Ronald Kincaid, and Elliott Ward Cheney. *Numerical analysis: mathematics of scientific computing*. Vol. 2. American Mathematical Soc., 2009.

[3] Chapra, Steven C. *Applied numerical methods with MATLAB for engineers and scientists*. McGraw-Hill Higher Education, 2008.

[4] Sauer, Timothy. "Numerical Analysis Pearson Addison Wesley." (2006).

[5] Burden, Richard L., and J. Douglas Faires. "Numerical analysis 8th ed." *Thomson Brooks/Cole* (2005).

[6] 喻文健. *数值分析与算法*. Qing hua da xue chu ban she, 2015.

[7] Zhang, Zhen, Xiao Xu, and Zhan Wang. "Application of grey prediction model to short-time passenger flow forecast." *AIP Conference Proceedings*. Vol. 1839. No. 1. AIP Publishing LLC, 2017.

[8] 卓金武. "MATLAB 在数学建模中的应用." *北京: 北京航空航天大学出版社* (2011).
[9] Bender, Carl M., and Steven A. Orszag. *Advanced mathematical methods for scientists and engineers I: Asymptotic methods and perturbation theory*. Springer Science & Business Media, 2013.





