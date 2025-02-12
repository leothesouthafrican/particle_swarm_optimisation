# main.py

from src.objective_function import inverted_rastrigin_function, rastrigin_function
from src.visualisation import visualize_pso
import numpy as np

def get_user_input():
    use_defaults = input("Do you want to adjust the parameters? (yes/no): ").strip().lower()
    
    # Default parameters
    default_bounds = np.array([[-5.12, 5.12], [-5.12, 5.12]])
    default_num_particles = 30
    default_max_iter = 100
    default_inertia = 0.5
    default_cognitive = 0.8
    default_social = 0.9
    default_patience = 10
    default_optimize_for = "max"
    default_frame_rate = 50
    default_num_runs = 1
    
    if use_defaults == "no":
        bounds = default_bounds
        num_particles = default_num_particles
        max_iter = default_max_iter
        inertia = default_inertia
        cognitive = default_cognitive
        social = default_social
        patience = default_patience
        optimize_for = default_optimize_for
        frame_rate = default_frame_rate
        num_runs = default_num_runs
    else:
        bound_min = input(f"Enter the minimum bound (default {default_bounds[0, 0]}): ")
        bound_max = input(f"Enter the maximum bound (default {default_bounds[0, 1]}): ")
        bounds = np.array([
            [float(bound_min) if bound_min else default_bounds[0, 0], float(bound_max) if bound_max else default_bounds[0, 1]], 
            [float(bound_min) if bound_min else default_bounds[1, 0], float(bound_max) if bound_max else default_bounds[1, 1]]
        ])
        
        num_particles = input(f"Enter the number of particles (default {default_num_particles}): ")
        num_particles = int(num_particles) if num_particles else default_num_particles
        
        max_iter = input(f"Enter the number of iterations (default {default_max_iter}): ")
        max_iter = int(max_iter) if max_iter else default_max_iter
        
        inertia = input(f"Enter the inertia coefficient (default {default_inertia}): ")
        inertia = float(inertia) if inertia else default_inertia
        
        cognitive = input(f"Enter the cognitive coefficient (default {default_cognitive}): ")
        cognitive = float(cognitive) if cognitive else default_cognitive
        
        social = input(f"Enter the social coefficient (default {default_social}): ")
        social = float(social) if social else default_social
        
        patience = input(f"Enter the patience (number of iterations without improvement before termination, default {default_patience}): ")
        patience = int(patience) if patience else default_patience
        
        optimize_for = input(f"Is this a minimization or maximization task? (min/max, default {default_optimize_for}): ").strip().lower()
        optimize_for = optimize_for if optimize_for else default_optimize_for
        
        frame_rate = input(f"Enter the frame rate for the animation (default {default_frame_rate} ms): ")
        frame_rate = int(frame_rate) if frame_rate else default_frame_rate
        
        num_runs = input(f"Enter the number of runs (default {default_num_runs}): ")
        num_runs = int(num_runs) if num_runs else default_num_runs
    
    return bounds, num_particles, max_iter, inertia, cognitive, social, patience, optimize_for, frame_rate, num_runs

def main():
    try:
        bounds, num_particles, max_iter, inertia, cognitive, social, patience, optimize_for, frame_rate, num_runs = get_user_input()

        # Select the appropriate objective function
        objective_function = inverted_rastrigin_function if optimize_for == "max" else rastrigin_function

        # Run multiple PSO visualizations
        for run_id in range(num_runs):
            log_filename = f"pso_log_run_{run_id+1}.csv"
            print(f"Starting run {run_id+1}, logging to {log_filename}")
            visualize_pso(
                objective_function, bounds, num_particles, max_iter, inertia, cognitive, social, patience, optimize_for, frame_rate, log_filename
            )

    except KeyboardInterrupt:
        print("\nOptimization interrupted by user.")

if __name__ == "__main__":
    main()
