from HamiltonianPy import *

__all__=['name','nneighbour','idfmap','qnsmap','t1','t2','U','Um','S4']

# The configs of the model
name='OKH'
nneighbour=1

# idfmap
idfmap=lambda pid: Fermi(norbital=1,nspin=2,nnambu=1)

# qnsmap
qnsmap=lambda index: PQNS(1)

# kitaev hopping
def kitaev_hopping(bond):
    theta=azimuthd(bond.rcoord)
    if abs(theta)<RZERO:
        return sigmax('sp') if bond.spoint.pid.site%4 in (0,3) else sigmay('sp')
    elif abs(theta-180)<RZERO:
        return sigmax('sp') if bond.spoint.pid.site%4 in (1,2) else sigmay('sp')
    else:
        return sigmaz('sp')

# terms
t1=lambda *parameters: Hopping('t1',parameters[0])
t2=lambda *parameters: Hopping('t2',parameters[1],indexpacks=kitaev_hopping)
U=lambda *parameters: Hubbard('U',parameters[2])
Um=lambda *parameters: Hubbard('U',parameters[2],modulate=True)

# cluster
S4=Square('S1').tiling((2,2))
