# main.py

from objective_function import inverted_rastrigin_function
from visualisation import visualize_pso
import numpy as np

def get_user_input():
    use_defaults = input("Do you want to adjust the parameters? (yes/no): ").strip().lower()
    
    if use_defaults == "no":
        bounds = np.array([[-5.12, 5.12], [-5.12, 5.12]])
        num_particles = 30
        max_iter = 100
        inertia = 0.5
        cognitive = 0.8
        social = 0.9
        patience = 10
    else:
        bound_min = float(input("Enter the minimum bound: "))
        bound_max = float(input("Enter the maximum bound: "))
        bounds = np.array([[bound_min, bound_max], [bound_min, bound_max]])
        
        num_particles = int(input("Enter the number of particles: "))
        max_iter = int(input("Enter the number of iterations: "))
        inertia = float(input("Enter the inertia coefficient: "))
        cognitive = float(input("Enter the cognitive coefficient: "))
        social = float(input("Enter the social coefficient: "))
        patience = int(input("Enter the patience (number of iterations without improvement before termination): "))
    
    return bounds, num_particles, max_iter, inertia, cognitive, social, patience

def main():
    bounds, num_particles, max_iter, inertia, cognitive, social, patience = get_user_input()

    # Run PSO with visualization
    best_position, best_score = visualize_pso(
        inverted_rastrigin_function, bounds, num_particles, max_iter, inertia, cognitive, social, patience
    )

    print("Best Position:", best_position)
    print("Best Score:", best_score)

if __name__ == "__main__":
    main()
