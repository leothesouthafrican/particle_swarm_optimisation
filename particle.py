# particle.py

import numpy as np

class Particle:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.best_position = position
        self.best_score = float('inf')

def initialize_particles(num_particles, bounds):
    particles = []
    for _ in range(num_particles):
        position = np.random.uniform(low=bounds[:, 0], high=bounds[:, 1])
        velocity = np.random.uniform(low=-1, high=1, size=bounds.shape[0])
        particles.append(Particle(position, velocity))
    return particles
