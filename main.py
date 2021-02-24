import math

def step_activation_function(net):
    if net >= 0:
        return 1
    else:
        return 0

def sigmoidal_activation_function(net):
    out = 1 / (1 + math.exp(-net))
    if out >= 0.5:
        return [1, out]
    else:
        return [0, out]

def bool_function(x1, x2, x3, x4):
    return int(not(not(x3) and x4 and (not(x1) or x2)))

def correction_weight_step(wi, xi, t, y):
    ny = 0.3
    return round(wi + ny*xi*(t - y), 1)

def correction_weight_sigmoidal(wi, xi, t, y, net):
    ny = 0.3
    return round(wi + ny*xi*(t - y)*(net * (1 - net)), 4)

def neuron_step(vars, synaptic_weights):
    net = 0
    for iter in range(5):
        net += vars[iter] * synaptic_weights[iter]
    return step_activation_function(net)

def neuron_sigmoidal(vars, synaptic_weights):
    net = 0
    for iter in range(5):
        net += vars[iter] * synaptic_weights[iter]
    return sigmoidal_activation_function(net)

def learning(synaptic_weights, flag):
    alphabeth = [0, 1]
    E = 0
    Y = []
    for x1 in alphabeth:
        for x2 in alphabeth:
            for x3 in alphabeth:
                for x4 in alphabeth:
                    values = [1, x1, x2, x3, x4]
                    t = bool_function(x1, x2, x3, x4)
                    if flag == "step":
                        y = neuron_step(values, synaptic_weights)
                        Y.append(y)
                        if y != t:
                            E += 1
                    elif flag == "sigmoidal":
                        y = neuron_sigmoidal(values, synaptic_weights)
                        Y.append(y[0])
                        if y[0] != t:
                            E += 1
    print(0, Y, synaptic_weights, E)
    k = 1
    while 1:
        E = 0
        Y = []
        for x1 in alphabeth:
            for x2 in alphabeth:
                for x3 in alphabeth:
                    for x4 in alphabeth:
                        values = [1, x1, x2, x3, x4]
                        t = bool_function(x1, x2, x3, x4)

                        if flag == "step":
                            y = neuron_step(values, synaptic_weights)
                            Y.append(y)
                            if y != t:
                                E += 1
                            for iter in range(5):
                                synaptic_weights[iter] = correction_weight_step(synaptic_weights[iter], values[iter], t, y)

                        elif flag == "sigmoidal":
                            y = neuron_sigmoidal(values, synaptic_weights)
                            Y.append(y[0])
                            if y[0] != t:
                                E += 1
                            for iter in range(5):
                                synaptic_weights[iter] = correction_weight_sigmoidal(synaptic_weights[iter], values[iter], t, y[0], y[1])

        print(k, Y, synaptic_weights, E)
        k += 1
        if E == 0:
            break

synaptic_weights_step = [0, 0, 0, 0, 0]
learning(synaptic_weights_step, "step")
synaptic_weights_sigmoidal = [0, 0, 0, 0, 0]
learning(synaptic_weights_sigmoidal, "sigmoidal")
print(synaptic_weights_step)
print(synaptic_weights_sigmoidal)