# pso.py

from particle import initialize_particles
import numpy as np

def pso(objective_function, bounds, num_particles=30, max_iter=100, inertia=0.5, cognitive=0.8, social=0.9, optimize_for="max"):
    particles = initialize_particles(num_particles, bounds)
    global_best_position = np.random.uniform(low=bounds[:, 0], high=bounds[:, 1])
    global_best_score = -float('inf') if optimize_for == "max" else float('inf')

    for _ in range(max_iter):
        for particle in particles:
            score = objective_function(particle.position)
            if (optimize_for == "max" and score > particle.best_score) or (optimize_for == "min" and score < particle.best_score):
                particle.best_score = score
                particle.best_position = particle.position.copy()  # Ensure it's a copy of the position
            if (optimize_for == "max" and score > global_best_score) or (optimize_for == "min" and score < global_best_score):
                global_best_score = score
                global_best_position = particle.position.copy()  # Ensure it's a copy of the position
        
        for particle in particles:
            particle.velocity = (inertia * particle.velocity +
                                 cognitive * np.random.rand() * (particle.best_position - particle.position) +
                                 social * np.random.rand() * (global_best_position - particle.position))
            particle.position += particle.velocity
            particle.position = np.clip(particle.position, bounds[:, 0], bounds[:, 1])
            
    return global_best_position, global_best_score
