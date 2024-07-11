# pso.py

from particle import initialize_particles
import numpy as np

def pso(objective_function, bounds, num_particles=30, max_iter=100, inertia=0.5, cognitive=0.8, social=0.9):
    particles = initialize_particles(num_particles, bounds)
    global_best_position = np.random.uniform(low=bounds[:, 0], high=bounds[:, 1])
    global_best_score = -float('inf')  # Since we are maximizing

    for _ in range(max_iter):
        for particle in particles:
            score = objective_function(particle.position)
            if score > particle.best_score:  # Note the inversion here
                particle.best_score = score
                particle.best_position = particle.position.copy()  # Ensure it's a copy of the position
            if score > global_best_score:  # Note the inversion here
                global_best_score = score
                global_best_position = particle.position.copy()  # Ensure it's a copy of the position
        
        for particle in particles:
            particle.velocity = (inertia * particle.velocity +
                                 cognitive * np.random.rand() * (particle.best_position - particle.position) +
                                 social * np.random.rand() * (global_best_position - particle.position))
            particle.position += particle.velocity
            particle.position = np.clip(particle.position, bounds[:, 0], bounds[:, 1])
            
    return global_best_position, global_best_score
