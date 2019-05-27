from lib import *
from sampler import *
from agents import *
from emulator import *
from simulators import *
from visualizer import *

db_type = 'PairSamplerDB'; db = 'randjump_100,1(10, 30)[]_'; Sampler = PairSampler

fld = os.path.join('data',db_type,db+'B')

print(fld)

db = pickle.load(open(os.path.join(str("..//" + fld), 'db.pickle'),'rb'))
