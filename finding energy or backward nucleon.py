import math
import matplotlib.pyplot as plt
m_N = 0.94
def energy_finder(p_0, n = 2, m_N = 0.94):
    b = -2*m_N*(n*p_0**2 + (n**2+1)*m_N*math.sqrt(m_N**2 + p_0**2) + 2*n*m_N**2)
    a = (n**2+1)*m_N**2 + 2*n*m_N*math.sqrt(m_N**2 + p_0**2)
    c = (n**2+1)*m_N**4 + (n**2+1)*m_N**2*p_0**2 + 2*n*m_N**3*math.sqrt(m_N**2 + p_0**2)
    D = b**2 - 4*a*c
    try:
        E_p = (-b/2-math.sqrt(D/4))/a
        #print(p_0, E_p, math.sqrt(p_0**2 + m_N**2) - E_p)
    except:
        E_p = None
    return E_p
p_0 = [i/10 for i in range (0,2010)]
E_0 = list(map(energy_finder, p_0))
plt.plot(p_0, E_0, label = 'Equation (7)')
plt.xscale('log')
plt.axis((0.1, 200, 0.9, 1.2))
plt.xlabel('$p_0$, GeV')
plt.ylabel('$E_1^*$, GeV')
plt.plot([0, 1000], [1.18, 1.18],'g--', label = '1.18 GeV')
plt.legend()
plt.show()


print(energy_finder(100000000000))
