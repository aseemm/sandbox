from anytree import Node, RenderTree
from anytree.exporter import DotExporter
import math
import sys
import argparse
import logging
from logging import critical, error, info, warning, debug

# https://www.analyticsvidhya.com/blog/2017/09/6-probability-distributions-data-science/?utm_source=blog&utm_medium=how-to-generate-random-numbers-in-python
# really a singleton class, but for now we won't bother explictly making it one
class hsc:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

# knobs for assigning subnet queues/class blocks to ports
subnet_port_map = [*range(0, 128)]
for idx, item in enumerate(subnet_port_map):
    subnet_port_map[idx] = 0

# Priority selector (0=low, 1=med, 2=high, 3=disabled)
# knobs for assigning subnet queues/class blocks to priorities
# knobs for assigning hq queues/class blocks to priorities
queue_pri_map = [*range(0, 1640)]
for idx, item in enumerate(queue_pri_map):
    queue_pri_map[idx] = 0

# knobs for credit generation to rate programming


# All rates represented in Kbps
root = Node("ROOT", cir=10, eir=0, queues=[*range(0, 1632)])
# Handle MCAST slightly differently
mcast = Node("MCAST", cir=10, eir=0, queues=[*range(1632, 1640)])

# NIP, TIP, EVC, PIQ, RECY
# nip = Node("NIP", parent=root, cir=10, eir=10, queues=[*range(1592, 1600)])
# tip = Node("TIP", parent=root, cir=10, eir=10, queues=[*range(1600, 1608)])
# evc = Node("EVC", parent=root, cir=10, eir=10, queues=[*range(1608, 1616)])
# piq = Node("PKI", parent=root, cir=10, eir=10, queues=[*range(1616, 1624)])
# recy = Node("RECY", parent=root, cir=10, eir=10, queues=[*range(1624, 1632)])

# 7 MSEs are connected to the SP Port
mse0 = Node("MSE[0]/HSCI0", parent=root, cir=10, eir=10, queues=[*range(1536, 1544)])
mse1 = Node("MSE[1]/HSCI1", parent=root, cir=10, eir=10, queues=[*range(1544, 1552)])
mse2 = Node("MSE[2]/IC0", parent=root, cir=10, eir=10, queues=[*range(1552, 1560)])
mse3 = Node("MSE[3]/IC1", parent=root, cir=10, eir=10, queues=[*range(1560, 1568)])
mse4 = Node("MSE[4]/IC2", parent=root, cir=10, eir=10, queues=[*range(1568, 1576)])
mse5 = Node("MSE[5]/IC3", parent=root, cir=10, eir=10, queues=[*range(1576, 1584)])
mse6 = Node("MSE[6]/IC4", parent=root, cir=10, eir=10, queues=[*range(1584, 1592)])

# 16 MSEs are connected to the HQ Port
mse7 = Node("MSE[7]", parent=root, cir=10, eir=10, queues=[*range(0, 32)])
mse8 = Node("MSE[8]", parent=root, cir=10, eir=10, queues=[*range(32, 64)])
mse9 = Node("MSE[9]", parent=root, cir=10, eir=10, queues=[*range(64, 96)])
mse10 = Node("MSE[10]", parent=root, cir=10, eir=10, queues=[*range(96, 128)])
mse11 = Node("MSE[11]", parent=root, cir=10, eir=10, queues=[*range(128, 160)])
mse12 = Node("MSE[12]", parent=root, cir=10, eir=10, queues=[*range(160, 192)])
mse13 = Node("MSE[13]", parent=root, cir=10, eir=10, queues=[*range(192, 224)])
mse14 = Node("MSE[14]", parent=root, cir=10, eir=10, queues=[*range(224, 256)])
mse15 = Node("MSE[15]", parent=root, cir=10, eir=10, queues=[*range(256, 288)])
mse16 = Node("MSE[16]", parent=root, cir=10, eir=10, queues=[*range(288, 320)])
mse17 = Node("MSE[17]", parent=root, cir=10, eir=10, queues=[*range(320, 352)])
mse18 = Node("MSE[18]", parent=root, cir=10, eir=10, queues=[*range(352, 384)])
mse19 = Node("MSE[19]", parent=root, cir=10, eir=10, queues=[*range(384, 416)])
mse20 = Node("MSE[20]", parent=root, cir=10, eir=10, queues=[*range(416, 448)])
mse21 = Node("MSE[21]", parent=root, cir=10, eir=10, queues=[*range(448, 480)])
mse22 = Node("MSE[22]", parent=root, cir=10, eir=10, queues=[*range(480, 512)])

# break out the HQ Ports further for each MSE
# 7
rt7 = Node("RT", parent=mse7, cir=10, eir=math.inf, queues=[])
non_rt7 = Node("NON-RT", parent=mse7, cir=10, eir=10, queues=[])

rtime_hi7 = Node("RTIME-HI", parent=rt7, cir=10, eir=10, queues=[])
rtime_med7 = Node("RTIME-MED", parent=rt7, cir=10, eir=10, queues=[])
rtime_lo7 = Node("RTIME-LO", parent=rt7, cir=10, eir=10, queues=[])

tun_hi7 = Node("TUN-HI", parent=non_rt7, cir=10, eir=10, queues=[])
tun_med7 = Node("TUN-MED", parent=non_rt7, cir=10, eir=10, queues=[])
tun_lo7 = Node("TUN-LO", parent=non_rt7, cir=10, eir=10, queues=[])

snet7 = Node("SNET", parent=non_rt7, cir=10, eir=10, queues=[])

def_hi7 = Node("DEF-HI", parent=snet7, cir=10, eir=10, queues=[])
def_med7 = Node("DEF-MED", parent=snet7, cir=10, eir=10, queues=[])
def_lo7 = Node("DEF-LO", parent=snet7, cir=10, eir=10, queues=[])

# 8
rt8 = Node("RT", parent=mse8, cir=10, eir=math.inf, queues=[])
non_rt8 = Node("NON-RT", parent=mse8, cir=10, eir=10, queues=[])

rtime_hi8 = Node("RTIME-HI", parent=rt8, cir=10, eir=10, queues=[])
rtime_med8 = Node("RTIME-MED", parent=rt8, cir=10, eir=10, queues=[])
rtime_lo8 = Node("RTIME-LO", parent=rt8, cir=10, eir=10, queues=[])

tun_hi8 = Node("TUN-HI", parent=non_rt8, cir=10, eir=10, queues=[])
tun_med8 = Node("TUN-MED", parent=non_rt8, cir=10, eir=10, queues=[])
tun_lo8 = Node("TUN-LO", parent=non_rt8, cir=10, eir=10, queues=[])

snet8 = Node("SNET", parent=non_rt8, cir=10, eir=10, queues=[])

def_hi8 = Node("DEF-HI", parent=snet8, cir=10, eir=10, queues=[])
def_med8 = Node("DEF-MED", parent=snet8, cir=10, eir=10, queues=[])
def_lo8 = Node("DEF-LO", parent=snet8, cir=10, eir=10, queues=[])

# 9
rt9 = Node("RT", parent=mse9, cir=10, eir=math.inf, queues=[])
non_rt9 = Node("NON-RT", parent=mse9, cir=10, eir=10, queues=[])

rtime_hi9 = Node("RTIME-HI", parent=rt9, cir=10, eir=10, queues=[])
rtime_med9 = Node("RTIME-MED", parent=rt9, cir=10, eir=10, queues=[])
rtime_lo9 = Node("RTIME-LO", parent=rt9, cir=10, eir=10, queues=[])

tun_hi9 = Node("TUN-HI", parent=non_rt9, cir=10, eir=10, queues=[])
tun_med9 = Node("TUN-MED", parent=non_rt9, cir=10, eir=10, queues=[])
tun_lo9 = Node("TUN-LO", parent=non_rt9, cir=10, eir=10, queues=[])

snet9 = Node("SNET", parent=non_rt9, cir=10, eir=10, queues=[])

def_hi9 = Node("DEF-HI", parent=snet9, cir=10, eir=10, queues=[])
def_med9 = Node("DEF-MED", parent=snet9, cir=10, eir=10, queues=[])
def_lo9 = Node("DEF-LO", parent=snet9, cir=10, eir=10, queues=[])

# 10
rt10 = Node("RT", parent=mse10, cir=10, eir=math.inf, queues=[])
non_rt10 = Node("NON-RT", parent=mse10, cir=10, eir=10, queues=[])

rtime_hi10 = Node("RTIME-HI", parent=rt10, cir=10, eir=10, queues=[])
rtime_med10 = Node("RTIME-MED", parent=rt10, cir=10, eir=10, queues=[])
rtime_lo10 = Node("RTIME-LO", parent=rt10, cir=10, eir=10, queues=[])

tun_hi10 = Node("TUN-HI", parent=non_rt10, cir=10, eir=10, queues=[])
tun_med10 = Node("TUN-MED", parent=non_rt10, cir=10, eir=10, queues=[])
tun_lo10 = Node("TUN-LO", parent=non_rt10, cir=10, eir=10, queues=[])

snet10 = Node("SNET", parent=non_rt10, cir=10, eir=10, queues=[])

def_hi10 = Node("DEF-HI", parent=snet10, cir=10, eir=10, queues=[])
def_med10 = Node("DEF-MED", parent=snet10, cir=10, eir=10, queues=[])
def_lo10 = Node("DEF-LO", parent=snet10, cir=10, eir=10, queues=[])

# 11
rt11 = Node("RT", parent=mse11, cir=10, eir=math.inf, queues=[])
non_rt11 = Node("NON-RT", parent=mse11, cir=10, eir=10, queues=[])

rtime_hi11 = Node("RTIME-HI", parent=rt11, cir=10, eir=10, queues=[])
rtime_med11 = Node("RTIME-MED", parent=rt11, cir=10, eir=10, queues=[])
rtime_lo11 = Node("RTIME-LO", parent=rt11, cir=10, eir=10, queues=[])

tun_hi11 = Node("TUN-HI", parent=non_rt11, cir=10, eir=10, queues=[])
tun_med11 = Node("TUN-MED", parent=non_rt11, cir=10, eir=10, queues=[])
tun_lo11 = Node("TUN-LO", parent=non_rt11, cir=10, eir=10, queues=[])

snet11 = Node("SNET", parent=non_rt11, cir=10, eir=10, queues=[])

def_hi11 = Node("DEF-HI", parent=snet11, cir=10, eir=10, queues=[])
def_med11 = Node("DEF-MED", parent=snet11, cir=10, eir=10, queues=[])
def_lo11 = Node("DEF-LO", parent=snet11, cir=10, eir=10, queues=[])

# 12
rt12 = Node("RT", parent=mse12, cir=10, eir=math.inf, queues=[])
non_rt12 = Node("NON-RT", parent=mse12, cir=10, eir=10, queues=[])

rtime_hi12 = Node("RTIME-HI", parent=rt12, cir=10, eir=10, queues=[])
rtime_med12 = Node("RTIME-MED", parent=rt12, cir=10, eir=10, queues=[])
rtime_lo12 = Node("RTIME-LO", parent=rt12, cir=10, eir=10, queues=[])

tun_hi12 = Node("TUN-HI", parent=non_rt12, cir=10, eir=10, queues=[])
tun_med12 = Node("TUN-MED", parent=non_rt12, cir=10, eir=10, queues=[])
tun_lo12 = Node("TUN-LO", parent=non_rt12, cir=10, eir=10, queues=[])

snet12 = Node("SNET", parent=non_rt12, cir=10, eir=10, queues=[])

def_hi12 = Node("DEF-HI", parent=snet12, cir=10, eir=10, queues=[])
def_med12 = Node("DEF-MED", parent=snet12, cir=10, eir=10, queues=[])
def_lo12 = Node("DEF-LO", parent=snet12, cir=10, eir=10, queues=[])

# 13
rt13 = Node("RT", parent=mse13, cir=10, eir=math.inf, queues=[])
non_rt13 = Node("NON-RT", parent=mse13, cir=10, eir=10, queues=[])

rtime_hi13 = Node("RTIME-HI", parent=rt13, cir=10, eir=10, queues=[])
rtime_med13 = Node("RTIME-MED", parent=rt13, cir=10, eir=10, queues=[])
rtime_lo13 = Node("RTIME-LO", parent=rt13, cir=10, eir=10, queues=[])

tun_hi13 = Node("TUN-HI", parent=non_rt13, cir=10, eir=10, queues=[])
tun_med13 = Node("TUN-MED", parent=non_rt13, cir=10, eir=10, queues=[])
tun_lo13 = Node("TUN-LO", parent=non_rt13, cir=10, eir=10, queues=[])

snet13 = Node("SNET", parent=non_rt13, cir=10, eir=10, queues=[])

def_hi13 = Node("DEF-HI", parent=snet13, cir=10, eir=10, queues=[])
def_med13 = Node("DEF-MED", parent=snet13, cir=10, eir=10, queues=[])
def_lo13 = Node("DEF-LO", parent=snet13, cir=10, eir=10, queues=[])

# 14
rt14 = Node("RT", parent=mse14, cir=10, eir=math.inf, queues=[])
non_rt14 = Node("NON-RT", parent=mse14, cir=10, eir=10, queues=[])

rtime_hi14 = Node("RTIME-HI", parent=rt14, cir=10, eir=10, queues=[])
rtime_med14 = Node("RTIME-MED", parent=rt14, cir=10, eir=10, queues=[])
rtime_lo14 = Node("RTIME-LO", parent=rt14, cir=10, eir=10, queues=[])

tun_hi14 = Node("TUN-HI", parent=non_rt14, cir=10, eir=10, queues=[])
tun_med14 = Node("TUN-MED", parent=non_rt14, cir=10, eir=10, queues=[])
tun_lo14 = Node("TUN-LO", parent=non_rt14, cir=10, eir=10, queues=[])

snet14 = Node("SNET", parent=non_rt14, cir=10, eir=10, queues=[])

def_hi14 = Node("DEF-HI", parent=snet14, cir=10, eir=10, queues=[])
def_med14 = Node("DEF-MED", parent=snet14, cir=10, eir=10, queues=[])
def_lo14 = Node("DEF-LO", parent=snet14, cir=10, eir=10, queues=[])

# 15
rt15 = Node("RT", parent=mse15, cir=10, eir=math.inf, queues=[])
non_rt15 = Node("NON-RT", parent=mse15, cir=10, eir=10, queues=[])

rtime_hi15 = Node("RTIME-HI", parent=rt15, cir=10, eir=10, queues=[])
rtime_med15 = Node("RTIME-MED", parent=rt15, cir=10, eir=10, queues=[])
rtime_lo15 = Node("RTIME-LO", parent=rt15, cir=10, eir=10, queues=[])

tun_hi15 = Node("TUN-HI", parent=non_rt15, cir=10, eir=10, queues=[])
tun_med15 = Node("TUN-MED", parent=non_rt15, cir=10, eir=10, queues=[])
tun_lo15 = Node("TUN-LO", parent=non_rt15, cir=10, eir=10, queues=[])

snet15 = Node("SNET", parent=non_rt15, cir=10, eir=10, queues=[])

def_hi15 = Node("DEF-HI", parent=snet15, cir=10, eir=10, queues=[])
def_med15 = Node("DEF-MED", parent=snet15, cir=10, eir=10, queues=[])
def_lo15 = Node("DEF-LO", parent=snet15, cir=10, eir=10, queues=[])

# 16
rt16 = Node("RT", parent=mse16, cir=10, eir=math.inf, queues=[])
non_rt16 = Node("NON-RT", parent=mse16, cir=10, eir=10, queues=[])

rtime_hi16 = Node("RTIME-HI", parent=rt16, cir=10, eir=10, queues=[])
rtime_med16 = Node("RTIME-MED", parent=rt16, cir=10, eir=10, queues=[])
rtime_lo16 = Node("RTIME-LO", parent=rt16, cir=10, eir=10, queues=[])

tun_hi16 = Node("TUN-HI", parent=non_rt16, cir=10, eir=10, queues=[])
tun_med16 = Node("TUN-MED", parent=non_rt16, cir=10, eir=10, queues=[])
tun_lo16 = Node("TUN-LO", parent=non_rt16, cir=10, eir=10, queues=[])

snet16 = Node("SNET", parent=non_rt16, cir=10, eir=10, queues=[])

def_hi16 = Node("DEF-HI", parent=snet16, cir=10, eir=10, queues=[])
def_med16 = Node("DEF-MED", parent=snet16, cir=10, eir=10, queues=[])
def_lo16 = Node("DEF-LO", parent=snet16, cir=10, eir=10, queues=[])

# 17
rt17 = Node("RT", parent=mse17, cir=10, eir=math.inf, queues=[])
non_rt17 = Node("NON-RT", parent=mse17, cir=10, eir=10, queues=[])

rtime_hi17 = Node("RTIME-HI", parent=rt17, cir=10, eir=10, queues=[])
rtime_med17 = Node("RTIME-MED", parent=rt17, cir=10, eir=10, queues=[])
rtime_lo17 = Node("RTIME-LO", parent=rt17, cir=10, eir=10, queues=[])

tun_hi17 = Node("TUN-HI", parent=non_rt17, cir=10, eir=10, queues=[])
tun_med17 = Node("TUN-MED", parent=non_rt17, cir=10, eir=10, queues=[])
tun_lo17 = Node("TUN-LO", parent=non_rt17, cir=10, eir=10, queues=[])

snet17 = Node("SNET", parent=non_rt17, cir=10, eir=10, queues=[])

def_hi17 = Node("DEF-HI", parent=snet17, cir=10, eir=10, queues=[])
def_med17 = Node("DEF-MED", parent=snet17, cir=10, eir=10, queues=[])
def_lo17 = Node("DEF-LO", parent=snet17, cir=10, eir=10, queues=[])

# 18
rt18 = Node("RT", parent=mse18, cir=10, eir=math.inf, queues=[])
non_rt18 = Node("NON-RT", parent=mse18, cir=10, eir=10, queues=[])

rtime_hi18 = Node("RTIME-HI", parent=rt18, cir=10, eir=10, queues=[])
rtime_med18 = Node("RTIME-MED", parent=rt18, cir=10, eir=10, queues=[])
rtime_lo18 = Node("RTIME-LO", parent=rt18, cir=10, eir=10, queues=[])

tun_hi18 = Node("TUN-HI", parent=non_rt18, cir=10, eir=10, queues=[])
tun_med18 = Node("TUN-MED", parent=non_rt18, cir=10, eir=10, queues=[])
tun_lo18 = Node("TUN-LO", parent=non_rt18, cir=10, eir=10, queues=[])

snet18 = Node("SNET", parent=non_rt18, cir=10, eir=10, queues=[])

def_hi18 = Node("DEF-HI", parent=snet18, cir=10, eir=10, queues=[])
def_med18 = Node("DEF-MED", parent=snet18, cir=10, eir=10, queues=[])
def_lo18 = Node("DEF-LO", parent=snet18, cir=10, eir=10, queues=[])

# 19
rt19 = Node("RT", parent=mse19, cir=10, eir=math.inf, queues=[])
non_rt19 = Node("NON-RT", parent=mse19, cir=10, eir=10, queues=[])

rtime_hi19 = Node("RTIME-HI", parent=rt19, cir=10, eir=10, queues=[])
rtime_med19 = Node("RTIME-MED", parent=rt19, cir=10, eir=10, queues=[])
rtime_lo19 = Node("RTIME-LO", parent=rt19, cir=10, eir=10, queues=[])

tun_hi19 = Node("TUN-HI", parent=non_rt19, cir=10, eir=10, queues=[])
tun_med19 = Node("TUN-MED", parent=non_rt19, cir=10, eir=10, queues=[])
tun_lo19 = Node("TUN-LO", parent=non_rt19, cir=10, eir=10, queues=[])

snet19 = Node("SNET", parent=non_rt19, cir=10, eir=10, queues=[])

def_hi19 = Node("DEF-HI", parent=snet19, cir=10, eir=10, queues=[])
def_med19 = Node("DEF-MED", parent=snet19, cir=10, eir=10, queues=[])
def_lo19 = Node("DEF-LO", parent=snet19, cir=10, eir=10, queues=[])

# 20
rt20 = Node("RT", parent=mse20, cir=10, eir=math.inf, queues=[])
non_rt20 = Node("NON-RT", parent=mse20, cir=10, eir=10, queues=[])

rtime_hi20 = Node("RTIME-HI", parent=rt20, cir=10, eir=10, queues=[])
rtime_med20 = Node("RTIME-MED", parent=rt20, cir=10, eir=10, queues=[])
rtime_lo20 = Node("RTIME-LO", parent=rt20, cir=10, eir=10, queues=[])

tun_hi20 = Node("TUN-HI", parent=non_rt20, cir=10, eir=10, queues=[])
tun_med20 = Node("TUN-MED", parent=non_rt20, cir=10, eir=10, queues=[])
tun_lo20 = Node("TUN-LO", parent=non_rt20, cir=10, eir=10, queues=[])

snet20 = Node("SNET", parent=non_rt20, cir=10, eir=10, queues=[])

def_hi20 = Node("DEF-HI", parent=snet20, cir=10, eir=10, queues=[])
def_med20 = Node("DEF-MED", parent=snet20, cir=10, eir=10, queues=[])
def_lo20 = Node("DEF-LO", parent=snet20, cir=10, eir=10, queues=[])

# 21
rt21 = Node("RT", parent=mse21, cir=10, eir=math.inf, queues=[])
non_rt21 = Node("NON-RT", parent=mse21, cir=10, eir=10, queues=[])

rtime_hi21 = Node("RTIME-HI", parent=rt21, cir=10, eir=10, queues=[])
rtime_med21 = Node("RTIME-MED", parent=rt21, cir=10, eir=10, queues=[])
rtime_lo21 = Node("RTIME-LO", parent=rt21, cir=10, eir=10, queues=[])

tun_hi21 = Node("TUN-HI", parent=non_rt21, cir=10, eir=10, queues=[])
tun_med21 = Node("TUN-MED", parent=non_rt21, cir=10, eir=10, queues=[])
tun_lo21 = Node("TUN-LO", parent=non_rt21, cir=10, eir=10, queues=[])

snet21 = Node("SNET", parent=non_rt21, cir=10, eir=10, queues=[])

def_hi21 = Node("DEF-HI", parent=snet21, cir=10, eir=10, queues=[])
def_med21 = Node("DEF-MED", parent=snet21, cir=10, eir=10, queues=[])
def_lo21 = Node("DEF-LO", parent=snet21, cir=10, eir=10, queues=[])

# 22
rt22 = Node("RT", parent=mse22, cir=10, eir=math.inf, queues=[])
non_rt22 = Node("NON-RT", parent=mse22, cir=10, eir=10, queues=[])

rtime_hi22 = Node("RTIME-HI", parent=rt22, cir=10, eir=10, queues=[])
rtime_med22 = Node("RTIME-MED", parent=rt22, cir=10, eir=10, queues=[])
rtime_lo22 = Node("RTIME-LO", parent=rt22, cir=10, eir=10, queues=[])

tun_hi22 = Node("TUN-HI", parent=non_rt22, cir=10, eir=10, queues=[])
tun_med22 = Node("TUN-MED", parent=non_rt22, cir=10, eir=10, queues=[])
tun_lo22 = Node("TUN-LO", parent=non_rt22, cir=10, eir=10, queues=[])

snet22 = Node("SNET", parent=non_rt22, cir=10, eir=10, queues=[])

def_hi22 = Node("DEF-HI", parent=snet22, cir=10, eir=10, queues=[])
def_med22 = Node("DEF-MED", parent=snet22, cir=10, eir=10, queues=[])
def_lo22 = Node("DEF-LO", parent=snet22, cir=10, eir=10, queues=[])

# And a bunch of subnet queues, initially mapped to MSE[7]
subnet_pool = []
for idx in range(128):
    subnet_pool.append(Node("SNET-POOL["+str(idx)+"]-HI", parent=snet7, cir=10, eir=10, queues=[]))
    subnet_pool.append(Node("SNET-POOL["+str(idx)+"]-MED", parent=snet7, cir=10, eir=10, queues=[]))
    subnet_pool.append(Node("SNET-POOL["+str(idx)+"]-LO", parent=snet7, cir=10, eir=10, queues=[]))    

# fix tree for programmed subnet to port mapping
thisdict = {
    0: snet7,
    1: snet8,
    2: snet9,
    3: snet10,
    4: snet11,
    5: snet12,
    6: snet13,
    7: snet14,
    8: snet15,
    9: snet16,
    10: snet17,
    11: snet18,
    12: snet19,
    13: snet20,
    14: snet21,
    15: snet22            
}
for idx, item in enumerate(subnet_port_map):
    subnet_pool[3*idx + 0].parent = thisdict[item]
    subnet_pool[3*idx + 1].parent = thisdict[item]
    subnet_pool[3*idx + 2].parent = thisdict[item]

# fix tree for programmed queue to priority mapping
# for HQ pools
# realtime = 8-15
# tunnel = 16-23
# default = 24-31
# Priority selector (0=low, 1=med, 2=high, 3=disabled)
for idx, item in enumerate(queue_pri_map):
    if idx in range(8, 16) and item == 0:
        rtime_lo7.queues.append(idx)
    if idx in range(8, 16) and item == 1:
        rtime_med7.queues.append(idx)
    if idx in range(8, 16) and item == 2:
        rtime_hi7.queues.append(idx)

        
# for shared subnet pools



# TODO print only the first/last for each array
for pre, fill, node in RenderTree(root):
    if not len(node.queues) == 0:
        print("%s%s (cir=%s, eir=%s, queues=[%s...%s])" % (pre, node.name, node.cir, node.eir, node.queues[0], node.queues[-1]))
    else: 
        print("%s%s (cir=%s, eir=%s)" % (pre, node.name, node.cir, node.eir))    


for pre, fill, node in RenderTree(mcast):
    print("%s%s (cir=%s, eir=%s, queues=[%s...%s])" % (pre, node.name, node.cir, node.eir, node.queues[0], node.queues[-1]))


# TODO pick a scheme to come up with random rates for 1680 queues that sum up to 40G    

# check invariance at each level
print(snet7.children)
print(non_rt7.children)
print(rt7.children)
print(mse0.children)



# policy
# profile: queue -> port

# fix the port rate -> modifying the MSE CIRs

# invariance checks - sumtree

# random profile can just add up the nodes

# Build the QoS Tree with default mappings
# EIR=CIR=open
# Subnet Queues mapped evenly to HQ Port Maps

# TODO what is a queue is disabeld and we are still sending traffic to it?

def parse_arguments():
    """Read arguments from a command line."""
    parser = argparse.ArgumentParser(description='Arguments get parsed via --commands')
    parser.add_argument('-v', metavar='verbosity', type=int, default=2,
        help='Verbosity of logging: 0 -critical, 1- error, 2 -warning, 3 -info, 4 -debug')

    args = parser.parse_args()
    verbose = {0: logging.CRITICAL, 1: logging.ERROR, 2: logging.WARNING, 3: logging.INFO, 4: logging.DEBUG}
    logging.basicConfig(format='%(message)s', level=verbose[args.v], stream=sys.stdout)
    
    return args
    
    
def main():
    print("Hello world")
    test = hsc("aseem", 23)
    test.description()
    print(test)
    pass

if __name__ == '__main__':
    args = parse_arguments()
    main()
