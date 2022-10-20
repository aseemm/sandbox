import random
import matplotlib.pyplot as plt
import functools
from random import expovariate
import simpy
from SimComponents import PacketGenerator, PacketSink, SwitchPort, PortMonitor
import numpy as np
import pandas as pd

# uniform distribution
uniSamples = [random.random() for i in range(100000)]
fig, axis = plt.subplots()
axis.hist(uniSamples, bins=100, density=False) # to normalize, use density=True
axis.set_title("Histogram for uniform RNG")
axis.set_xlabel("x")
axis.set_ylabel("frequency")
fig.savefig("uniformDistribution.png")

# normal distribution
normSamples = [random.normalvariate(9.0, 2.0) for i in range(100000)]
fig, axis = plt.subplots()
axis.hist(normSamples, bins=100, density=False)
axis.set_title(r"Histogram of an Normal RNG $\mu = 9$ and $\sigma = 2$")
axis.set_xlabel("x")
axis.set_ylabel("frequency")
fig.savefig("normalDistribution.png")

# exponential distribution
normSamples = [random.expovariate(1.0) for i in range(100000)]
fig, axis = plt.subplots()
axis.hist(normSamples, bins=100, density=False)
axis.set_title(r"Histogram of an Exponential RNG")
axis.set_xlabel("x")
axis.set_ylabel("frequency")
fig.savefig("exponentialDistribution.png")

# create some interesting traffic patterns (qid, timestamp, size)
mean_pkt_size = 100
mean_input_rate = 0.5
num_queues = 1680
adist = functools.partial(random.expovariate, mean_input_rate) 
sdist = functools.partial(random.expovariate, 1/mean_pkt_size) 

env = simpy.Environment()  
# Create the packet generators and sink
# ps = PacketSink(env, debug=True)
pg = PacketGenerator(env, "EE283", adist, sdist, initial_delay=1)
# pg = PacketGenerator(env, "qid0", adist, sdist, initial_delay=100)
ps = PacketSink(env, debug=False, rec_arrivals=True, absolute_arrivals=True, rec_waits=True)
# Wire packet generators and sink together
pg.out = ps
# Run
env.run(until=10000)
# print("waits: {}".format(ps.waits))
# print("arrivals: {}".format(np.around(np.array(ps.arrivals)).astype(int)))
# print("sizes: {}".format(np.around(np.array(ps.sizes)).astype(int))) 
# print("received: {}, sent {}".format(ps.packets_rec, pg.packets_sent))

tstamp = np.around(np.array(ps.arrivals)).astype(int)
size = np.around(np.array(ps.sizes)).astype(int)
qid = np.random.randint(0,num_queues,(tstamp.size))
# print(tstamp, size, qid)

# TODO qid=0,1679 are sending packets
# TODO size needs to conform to Ethernet spec (min packet size, jumbo packets)
print("idx: timestamp, qid, size")
for i in range(tstamp.size):
    print("{}: {}, {}, {}".format(i, tstamp[i], qid[i], size[i]))

print(tstamp[0], tstamp[-1], np.sum(size))
print("packet rate = ", np.size(size)/(tstamp[-1]-tstamp[0]))
print("bandwidth rate = ", np.sum(size)/(tstamp[-1]-tstamp[0]))

# sorting multiple timestamps
# windowing performance



    
# # traffic generation
# def constArrival():  # Constant arrival distribution for generator 1
#     return 1.5

# def constArrival2():
#     return 2.0

# def constSize():
#     return 100.0 # bytes

# def distSize():
#     return expovariate(0.01)

# # Example 1 - Two packet generators and a sink
# # Create the SimPy environment
# env = simpy.Environment()  
# # Create the packet generators and sink
# ps = PacketSink(env, debug=True)
# pg = PacketGenerator(env, "EE283", constArrival, distSize)
# # pg2 = PacketGenerator(env, "SJSU", constArrival2, distSize)
# # Wire packet generators and sink together
# pg.out = ps
# # pg2.out = ps
# # Run
# env.run(until=20)

# Example 2 - Overloaded Switch Port
# env = simpy.Environment()  # Create the SimPy environment
# ps = PacketSink(env, debug=True) # debug: every packet arrival is printed
# pg = PacketGenerator(env, "SJSU", constArrival, constSize) # input rate is 533.3 bps, so should drop packets quickly
# switch_port = SwitchPort(env, rate=200.0, qlimit=300)
# # Wire packet generators and sinks together
# pg.out = switch_port
# switch_port.out = ps
# env.run(until=20)
# print("waits: {}".format(ps.waits)) # when received
# print("received: {}, dropped {}, sent {}".format(ps.packets_rec, switch_port.packets_drop, pg.packets_sent))

# Example 3 - M/M/1 Queueing System
# adist = functools.partial(random.expovariate, 0.5) # arrival rate, 0.5 packets/sec
# sdist = functools.partial(random.expovariate, 0.01)  # mean size 100 bytes

# samp_dist = functools.partial(random.expovariate, 1.0) 
# port_rate = 1000.0 # 1000 bps = 1000/8*100 = 1.25 packets/sec

# env = simpy.Environment()  # Create the SimPy environment
# # Create the packet generators and sink
# ps = PacketSink(env, debug=True, rec_arrivals=True)
# pg = PacketGenerator(env, "Greg", adist, sdist)
# switch_port = SwitchPort(env, port_rate, qlimit=10000)
# # Using a PortMonitor to track queue sizes over time
# pm = PortMonitor(env, switch_port, samp_dist)
# # Wire packet generators, switch ports, and sinks together
# pg.out = switch_port
# switch_port.out = ps
# # Run it
# env.run(until=8000)
# print("Last 10 waits: "  + ", ".join(["{:.3f}".format(x) for x in ps.waits[-10:]]))
# print("Last 10 queue sizes: {}".format(pm.sizes[-10:]))
# print("Last 10 sink arrival times: " + ", ".join(["{:.3f}".format(x) for x in ps.arrivals[-10:]]))
# print("average wait = {:.3f}".format(sum(ps.waits)/len(ps.waits)))
# print("received: {}, dropped {}, sent {}".format(switch_port.packets_rec, switch_port.packets_drop, pg.packets_sent))
# print("loss rate: {}".format(float(switch_port.packets_drop)/switch_port.packets_rec))
# print("average system occupancy: {:.3f}".format(float(sum(pm.sizes))/len(pm.sizes)))

# fig, axis = plt.subplots()
# axis.hist(ps.waits, bins=100, density=True)
# axis.set_title("Histogram for waiting times")
# axis.set_xlabel("time")
# axis.set_ylabel("normalized frequency of occurrence")
# fig.savefig("WaitHistogram.png")

# fig, axis = plt.subplots()
# axis.hist(ps.waits, bins=100, density=True)
# axis.set_title("Histogram for System Occupation times")
# axis.set_xlabel("number")
# axis.set_ylabel("normalized frequency of occurrence")
# fig.savefig("QueueHistogram.png")

# fig, axis = plt.subplots()
# axis.hist(ps.arrivals, bins=100, density=True)
# axis.set_title("Histogram for Sink Interarrival times")
# axis.set_xlabel("time")
# axis.set_ylabel("normalized frequency of occurrence")
# fig.savefig("ArrivalHistogram.png")

print("Reading in CSV file...")
# test = np.genfromtxt('sample.csv', delimiter=',', dtype=None)
test = np.genfromtxt('sample.csv', dtype={'names':('idx','timestamp','qid','plen','cmd'),'formats':('i','i','i', 'i', '')},delimiter=',')
print(test)



