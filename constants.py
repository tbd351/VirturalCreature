L = 0.1
R = L/5
evalTime = 1500
popSize = 20
numGens = 200
numEnvs = 4
t_size = 5
m_rate = 3
tau = 0.3

def set_cons(name: str, val: float):
    globals()[name] = val