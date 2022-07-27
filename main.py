from sympy import symbols,roots,pprint,Pow,re,im
print(
    "Enter four numbers p,q,r & s to generate the sequence as follow \n f(n)= p*f(n-1) + q*f(n-2) + r*f(n-3) + s*f(n-4) \n 5th term in Seq = p x 4th term in Seq + q x 3rd term in Seq + r x 2nd term in Seq + s x 1st term in Seq"
)
p = float(input(" p = "))
q = float(input(" q = "))
r = float(input(" r = "))
s = float(input(" s = "))
n = int(input("\nEnter the no.of terms to be generated \n n = "))
f1 = int(input("\nEnter the first four numbers in the sequence \n f(1) = "))
f2 = int(input(" f(2) = "))
f3 = int(input(" f(3) = "))
f4 = int(input(" f(4) = "))
f0 = (f4 - f3 * p - f2 * q - f1 * r) / s
x = symbols('x')
eq = x**4-p*x**3-q*x**2-r*x-s
res = roots(eq)
resn = [key.evalf() for key in res.keys()]
print("\nThe following four ratios are obtained by the Quartic formula")
Alpha=complex(re(resn[0]),im(resn[0]))
print("Alpha = %s" % (Alpha))
Beta=complex(re(resn[1]),im(resn[1]))
print("Beta = %s" % (Beta))
Gamma=complex(re(resn[2]),im(resn[2]))
print("Gamma = %s" % (Gamma))
Lam=complex(re(resn[3]),im(resn[3]))
print("Lam = %s" % (Lam))
print("\nThe first %s numbers of sequence created using the above ratios are" %
      n)

for i in range(1, n + 1):
    N = (((Alpha**(i)) *
          (-f0 * Beta * Gamma * Lam +
           (f1 * (Beta * Gamma + Gamma * Lam + Beta * Lam)) - f2 *
           (Beta + Gamma + Lam) + f3)) /
         ((Alpha-Beta) * (Alpha - Gamma) * (Alpha-Lam))) + (((Beta**(i)) *
          (-f0 * Gamma * Lam * Alpha+
           (f1 * (Alpha * Gamma + Alpha * Lam + Gamma * Lam)) - f2 *
           (Gamma + Lam + Alpha) + f3)) /
         ((Beta-Gamma) * (Beta - Lam) * (Beta-Alpha))) + (((Gamma**(i)) *
          (-f0 * Alpha * Beta * Lam +
           (f1 * (Alpha * Beta + Beta * Lam + Alpha*Lam)) - f2 *
           (Lam + Alpha+Beta) + f3)) /
         ((Gamma-Lam) * (Gamma-Alpha) * (Gamma-Beta))) + (((Lam**(i)) *
          (-f0 * Alpha * Beta * Gamma +
           (f1 * (Alpha * Beta + Beta * Gamma + Alpha*Gamma)) - f2 *
           (Alpha+Beta+Gamma) + f3)) /
         ((Lam-Alpha) * (Lam-Beta) * (Lam-Gamma)))
    print("%s rounded off to " % N, end="")
    print(round(N.real))
print("\nThe above sequence is generated by the formula")
Alpha, Beta, Gamma, Lam, f0, f1, f2, f3, n = symbols('(Alpha) (Beta) (Gamma) (Lam) f(0) f(1) f(2) f(3) n', integer=True)
pprint(((Pow(Alpha,n)*(-f0*Beta*Gamma*Lam+f1*(Beta*Gamma+Gamma*Lam+Beta*Lam)-f2*(Beta+Gamma+Lam)+f3))/((Alpha-Beta)*(Alpha-Gamma)*(Alpha-Lam)))+((Pow(Beta,n)*(-f0*Alpha*Gamma*Lam+f1*(Alpha*Gamma+Alpha*Lam+Gamma*Lam)-f2*(Alpha+Gamma+Lam)+f3))/((Beta-Alpha)*(Beta-Gamma)*(Beta-Lam))) + ((Pow(Gamma,n)*(-f0*Alpha*Beta*Lam+f1*(Alpha*Beta+Beta*Lam+Alpha*Lam)-f2*(Alpha+Beta+Lam)+f3))/((Gamma-Alpha)*(Gamma-Beta)*(Gamma-Lam))) + ((Pow(Lam,n)*(-f0*Alpha*Beta*Gamma+f1*(Alpha*Beta+Beta*Gamma+Alpha*Gamma)-f2*(Alpha+Beta+Gamma)+f3))/((Lam-Alpha)*(Lam-Beta)*(Lam-Gamma))))
print(" Where f(0)->Zeroth num in seq")