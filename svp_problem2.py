import gmpy2
from fpylll import IntegerMatrix, LLL
x=gmpy2.mpz("3dd89f01e0e9908e1b96706b67d30fcea4bd104d25d234b7fe4bea608949ad8a853c8547038c63fc32163ec5f5fa6d85f80a3a0fa0f30610104cdc4629ad1bf34c954553514db4b1df7a08d8d88925d70a95b3185ba9822886ab96291551dff31bd9af19659192d4f6edf0242cdc1ac6a0c7fa93ec8cb60340c2e436189e6f86",16)       
p=gmpy2.mpz("f49b3ab15d332fdc800cb45baba55913061a1c16eb89da63b0188a0d0d979adbb22e95c0bbdc9cfbca5d581e44ad9984340fc5e7d05f5e4618c0b2d19d8e50b59b007bdb80fe707e264ca97cbb81e743324ece0b529f2b87835e91490c843e6fb3027d2c6bfca63bc901f42d5597a7b90488c1ea5224879392f22f0e6747edc1",16)
M = IntegerMatrix(2, 2)
M[0, 0] = 1
M[0, 1] = int(x)            
M[1, 0] = 0
M[1, 1] = int(p)
M_LLL = LLL.reduction(M)
short_vector = M_LLL[0]
norm_short_vector = short_vector.norm()
