from absl  import app 
from absl  import flags
from numpy import random
import time
import numpy as np
import pso
import os
FLAGS = flags.FLAGS
def minimize( bounds, file ,optimize , num_particles = 32, gen = 50,topology = 'star', verbose=False, seed = 19520109, num_func = 1,num_dimensions = 2):
    err_best_g=-1                   # best error for group
    pos_best_g=[]                   # best position for group
    # establish the swarm
    swarm=[]
    #alibotto = pso.Particle(3,4,(1,2))
    #print(type(pso.Particle))
    for i in range(0,num_particles):
        swarm.append(pso.Particle(num_dimensions,num_func,bounds,optimize))

    # begin optimization loop
    i=0
    while i<gen:
        if verbose: print(f'iter: {i:>4d}, best solution: {err_best_g:10.6f}')
            
        # cycle through particles in swarm and evaluate fitness
        for j in swarm:
            j.evaluate(1)
            # determine if current particle is the best (globally)
            #print(err_best_g == -1,)
            #print(swarm[j].position_i,  swarm[j].err_i)
            if abs(j.err_i-optimize)<abs(err_best_g-optimize-optimize) or err_best_g==-1:
                pos_best_g=list(j.position_i)
                err_best_g = j.err_i
            #print(err_best_g)
        #xit()
        #if i == 0:
        for j in swarm:
            #swarm[j].pos_best_neighbor_i = swarm[j].position_i.copy()
            #swarm[j].err_best_neighbor_i = swarm[j].err_best_i
            #print(swarm.index(j))
            index = swarm.index(j)
            if topology == 'ring':
                j.update_neighbor_position(swarm[(index-1 + num_particles )%num_particles])
                j.update_neighbor_position(swarm[(index+1)%num_particles])
                j.update_neighbor_position(j)
            else:
                for z in swarm:
                    j.update_neighbor_position(z)
        #exit()
        # cycle through swarm and update velocities and position
        for j in swarm:
            j.update_velocity()
        for j in swarm:
            j.update_position(bounds)
        for j in swarm:
            j.evaluate(0)
        # for j in range(0,num_particles):
        #     #swarm[j].pos_best_neighbor_i = swarm[j].position_i.copy()
        #     if topology == 'ring':
        #         swarm[j].update_neighbor_position(swarm[(j-1 + num_particles )%num_particles])
        #         swarm[j].update_neighbor_position(swarm[(j+1)%num_particles])
        #         swarm[j].update_neighbor_position(swarm[j])
        #     else:
        #         for z in swarm:
        #             swarm[j].update_neighbor_position(z)
        #print(pso.Particle.count)
        if pso.Particle.count > 1e6:
            break
        i+=1
    #for i in range(num_particles):
    #    print(swarm[i].err_best_neighbor_i)
    #exit()
    # print final results
    #print('\nFINAL SOLUTION:')
    #print(f'   > {pos_best_g}')
    #print(f'   > {err_best_g}\n')
    file.write("-Random seed: "+ str(seed+19520109) + "\n")
    file.write("      +objective value: " + str(err_best_g) + "\n")
    file.write("      +best solution: ")
    for i in pos_best_g:
        file.write(str(i) + ' ')
    file.write('\n')
    return err_best_g
# flags.DEFINE_string('topology','star', 'topology = ')
# flags.DEFINE_integer('gen',500,'gen = ')
# flags.DEFINE_integer('num_particles',32,'num_particles = ')
# flags.DEFINE_string('costFunc','rosenbrock','costFunc = ')
# flags.DEFINE_integer('time',10 ,'time = ')
# flags.DEFINE_integer('num_dimensions',2, 'num_dimensions')
bounds = [(-5.12,5.12),(-1e9,1e9),(-512,512),(-5,5)]
optimize = [0,0]
# def main(argv):
#     #np.random.seed(19520109)
#     seed(19520209)
#     num_func = 4
#     if FLAGS.costFunc == 'rastrigin':
#         num_func = 1
#     if FLAGS.costFunc == 'rosenbrock':
#         num_func = 2
#     if FLAGS.costFunc == 'eggholder':
#         num_func = 3
#     print(minimize(x,bounds[num_func-1],FLAGS.num_particles,FLAGS.gen,FLAGS.topology,True,19520109,num_func,FLAGS.num_dimensions))

# if __name__ == '__main__':
#   app.run(main)
#global count
topologies = ['star','ring']
prop_sizes = [128,256,512,1024,2048]
function_types = ['rastrigin','rosenbrock']
for topology in topologies:
    for prop_size in prop_sizes:
        for function_type in function_types:
            logs_dir = "C://Users//RainbowShine//Desktop//logs//" + topology + "_" + str(prop_size) + "_" + function_type  + ".txt"
            file1 = open(logs_dir,"w")
            tong = 0
            a = []
            for i in range(10):
                seconds = time.time()
                pso.Particle.count = 0
                random.seed(19520109+i)
                print(topology + '_', function_type + '_' + str(prop_size))
                a.append(minimize(bounds[function_types.index(function_type)],file1,optimize[function_types.index(function_type)],prop_size,1000000,topology,False,i,function_types.index(function_type)+1,10))
                print(time.time()-seconds)
            for i in a:
                tong+=i
            tong = tong / 10
            tmp = 0
            for i in a:
                tmp += (abs(i-tong)**2)
            tmp = np.sqrt(tmp/9)
            print(tmp,tong)
            file1.write("std = " + str(tmp) + "mean = " + (str(tong)))
            file1.close()
            

