from HamiltonianPy import *
from HamiltonianPy.Misc import mpirun
from source import *
import numpy as np
import mkl

mkl.set_num_threads(1)

# When using log files, set it to be False
Engine.DEBUG=False

# Run the engines. Replace 'f' with the correct function
#mpirn(f,parameters,bcast=True)

# tba
parameters,terms=[0.0,1.0],[t1,t2]
# bulk
#tbaconstruct(parameters,S4('1P-1O',nneighbour),terms,job='APP')
# edge
#for m in [20,40,60]:
#    tbaconstruct(parameters,S4('%sO-1O'%m,nneighbour),terms,job='APP')
# GSE
#tbaconstruct(parameters,S4('2O-1O',nneighbour),terms,job='GSE')

# ed
m=2
parameters,terms=[0.0,1.0,0.0],[t1,t2,Um]
#edconstruct(parameters,FBasis((8*m,4*m)),S4('%sP-1O'%m,nneighbour),terms,job='APP')
#edconstruct(parameters,FBasis((8*m,4*m)),S4('%sO-1O'%m,nneighbour),terms,job='GSE')

# dmrg
m=2
parameters,terms=[0.0,1.0,0.0],[t1,t2,U]
#dmrgconstruct(parameters,S4.cylinder(0,'1O-1O',nneighbour),terms,[PQN(8*(i+1)) for i in xrange(m/2)],core='idmrg')
