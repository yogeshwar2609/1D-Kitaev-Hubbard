from HamiltonianPy import *
from HamiltonianPy.Misc import mpirun
from source import *
import numpy as np
import mkl

# tbatasks
def tbatasks(parameters,lattice,job='APP'):
    import HamiltonianPy.FreeSystem as TBA
    tba=tbaconstruct(parameters,lattice,[t1,t2])
    if job=='APP':
        if len(lattice.vectors)==1:
            eb=EB(name='EB',path=KSpace(reciprocals=lattice.reciprocals,segments=[(-0.5,0.5)],end=True,nk=401),run=TBA.TBAEB)
        elif len(lattice.vectors)==0:
            eb=EB(name='EB',run=TBA.TBAEB)
        tba.register(eb)
        tba.summary()
    elif job=='GSE':
        kspace=KSpace(reciprocals=lattice.reciprocals,nk=200) if len(lattice.vectors)>0 else None
        GSE=tba.gse(filling=0.5,kspace=kspace)
        tba.log.open()
        tba.log<<Info.from_ordereddict({'Total':GSE,'Site':GSE/len(lattice)/(1 if kspace is None else kspace.rank('k'))})<<'\n'
        tba.log.close()

# edtasks
def edtasks(parameters,basis,lattice,job='APP'):
    import HamiltonianPy.ED as ED
    ed=edconstruct(parameters,basis,lattice,[t1,t2,Um])
    if job=='APP':
        el=ED.EL(name='EL',path=BaseSpace(['U',np.linspace(0,40.0,401)]),ns=1,nder=2,run=ED.EDEL)
        ed.register(el)
        ed.summary()
    elif job=='GSE':
        GSE=ed.eig(k=1)[0]
        ed.log.open()
        ed.log<<Info.from_ordereddict({'Total':GSE,'Site':GSE/len(lattice)})<<'\n'
        ed.log.close()

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
    #tbatasks(parameters,S4('1P-1O',nneighbour),job='APP')
    #for m in [20,40,60]:
    #    tbatasks(parameters,S4('%sO-1O'%m,nneighbour),job='APP')
    #tbatasks(parameters,S4('%sO-1O'%m,nneighbour),job='GSE')

    # ed tasks
    #edtasks(parameters,FBasis((8*m,4*m)),S4('%sP-1O'%m,nneighbour),job='APP')
    #edtasks(parameters,FBasis((8*m,4*m)),S4('%sO-1O'%m,nneighbour),job='GSE')

    # dmrg
    #dmrgconstruct(parameters,S4.cylinder(0,'1O-1O',nneighbour),[t1,t2,U],[PQN(8*(i+1)) for i in xrange(m/2)],core='idmrg')
