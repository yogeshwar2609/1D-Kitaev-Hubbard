from HamiltonianPy import *
from HamiltonianPy.Misc import mpirun
from source import *
import numpy as np
import mkl

# tbatasks
def tbatasks(parameters,lattice,job='EB'):
    import HamiltonianPy.FreeSystem as TBA
    tba=tbaconstruct(parameters,lattice,[t1,t2])
    if job=='EB':
        if len(lattice.vectors)==1:
            tba.register(EB(name='EB',path=KSpace(reciprocals=lattice.reciprocals,segments=[(-0.5,0.5)],end=True,nk=401),run=TBA.TBAEB))
        elif len(lattice.vectors)==0:
            tba.register(EB(name='EB',run=TBA.TBAEB))
    if job=='GSE':
        tba.register(TBA.GSE(name='GSE',filling=0.5,kspace=KSpace(reciprocals=lattice.reciprocals,nk=200) if len(lattice.vectors)>0 else None,run=TBA.TBAGSE))
    tba.summary()

# edtasks
def edtasks(parameters,basis,lattice,job='EL'):
    import HamiltonianPy.ED as ED
    ed=edconstruct(parameters,basis,lattice,[t1,t2,Um])
    if job=='EL': ed.register(ED.EL(name='EL',path=BaseSpace(['U',np.linspace(0,40.0,401)]),ns=1,nder=2,run=ED.EDEL))
    if job=='GSE': ed.register(GSE(name='GSE',run=ED.EDGSE))
    ed.summary()

if __name__=='__main__':
    mkl.set_num_threads(1)

    # When using log files, set it to be False
    Engine.DEBUG=True

    # Run the engines. Replace 'f' with the correct function
    #mpirn(f,parameters,bcast=True)

    # parameters
    m=2
    parameters=[0.0,1.0,0.0]

    # tba tasks
    #tbatasks(parameters,S4('1P-1O',nneighbour),job='EB')
    #for m in [20,40,60]:
    #    tbatasks(parameters,S4('%sO-1O'%m,nneighbour),job='EB')
    #tbatasks(parameters,S4('%sO-1O'%m,nneighbour),job='GSE')

    # ed tasks
    #edtasks(parameters,FBasis((8*m,4*m)),S4('%sP-1O'%m,nneighbour),job='EL')
    #edtasks(parameters,FBasis((8*m,4*m)),S4('%sO-1O'%m,nneighbour),job='GSE')

    # dmrg
    #dmrgconstruct(parameters,S4.cylinder(0,'1O-1O',nneighbour),[t1,t2,U],[PQN(8*(i+1)) for i in xrange(m/2)],core='idmrg')
