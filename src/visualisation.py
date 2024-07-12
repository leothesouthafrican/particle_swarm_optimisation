import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import csv
from tqdm import tqdm
from src.pso import initialize_particles

# Known global optimum for the Rastrigin function in 2D (if inverted, adjust accordingly)
GLOBAL_OPTIMUM_X = 0
GLOBAL_OPTIMUM_Y = 0
GLOBAL_OPTIMUM_SCORE = 0  # This will change if we are using inverted_rastrigin_function

def visualize_pso(objective_function, bounds, num_particles=30, max_iter=100, inertia=0.5, cognitive=0.8, social=0.9, patience=10, optimize_for="max"):
    particles = initialize_particles(num_particles, bounds)
    global_best_position = np.random.uniform(low=bounds[:, 0], high=bounds[:, 1])
    global_best_score = -float('inf') if optimize_for == "max" else float('inf')

    # Open the log file at the beginning
    log_file = open("pso_log.csv", "w", newline="")
    log_writer = csv.writer(log_file)
    log_writer.writerow(["Iteration", "Particle", "Position X", "Position Y", "Score", "Global Best X", "Global Best Y", "Global Best Score", "Global Optimum X", "Global Optimum Y", "Global Optimum Score"])

    fig, ax = plt.subplots()
    x = np.linspace(bounds[0, 0], bounds[0, 1], 100)
    y = np.linspace(bounds[1, 0], bounds[1, 1], 100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([objective_function([xi, yi]) for xi, yi in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)

    contour = ax.contourf(X, Y, Z, levels=50, cmap='viridis')
    scat = ax.scatter([p.position[0] for p in particles], [p.position[1] for p in particles], c='red', s=10)  # Smaller dots
    global_best_marker, = ax.plot([], [], 'bo', markersize=10, label='Global Best')
    global_optimum_marker, = ax.plot([GLOBAL_OPTIMUM_X], [GLOBAL_OPTIMUM_Y], 'go', markersize=10, label='Global Optimum')
    
    # Add colorbar to the contour plot
    colorbar = fig.colorbar(contour, ax=ax)
    colorbar.set_label('Objective Function Value')

    no_improvement_counter = 0
    terminated_early = False

    # Create a tqdm progress bar
    progress_bar = tqdm(total=max_iter, desc="Optimizing", dynamic_ncols=True)

    def update(frame):
        nonlocal global_best_position, global_best_score, no_improvement_counter, terminated_early
        improvement = False

        for idx, particle in enumerate(particles):
            score = objective_function(particle.position)
            if (optimize_for == "max" and score > particle.best_score) or (optimize_for == "min" and score < particle.best_score):
                particle.best_score = score
                particle.best_position = particle.position.copy()  # Ensure it's a copy of the position
            if (optimize_for == "max" and score > global_best_score) or (optimize_for == "min" and score < global_best_score):
                global_best_score = score
                global_best_position = particle.position.copy()  # Ensure it's a copy of the position
                improvement = True
        
        for idx, particle in enumerate(particles):
            particle.velocity = (inertia * particle.velocity +
                                 cognitive * np.random.rand() * (particle.best_position - particle.position) +
                                 social * np.random.rand() * (global_best_position - particle.position))
            particle.position += particle.velocity
            particle.position = np.clip(particle.position, bounds[:, 0], bounds[:, 1])
            
            # Log particle data
            log_writer.writerow([frame + 1, idx, particle.position[0], particle.position[1], score,
                                 global_best_position[0], global_best_position[1], global_best_score,
                                 GLOBAL_OPTIMUM_X, GLOBAL_OPTIMUM_Y, GLOBAL_OPTIMUM_SCORE])
        
        if improvement:
            no_improvement_counter = 0
        else:
            no_improvement_counter += 1

        # Early termination if no improvement
        if no_improvement_counter >= patience:
            terminated_early = True
            ani.event_source.stop()  # Stop the animation

        # Update the scatter plot with the new positions
        scat.set_offsets([p.position for p in particles])
        # Update the global best marker
        global_best_marker.set_data([global_best_position[0]], [global_best_position[1]])
        
        # Update the tqdm progress bar
        progress_bar.set_postfix({"Global Best Score": f"{global_best_score:.4f}"})
        progress_bar.update(1)
        
        ax.legend()
        return scat, global_best_marker, global_optimum_marker

    ani = animation.FuncAnimation(fig, update, frames=max_iter, blit=True, repeat=False, interval=50)  # Adjust the interval to increase the frame rate
    plt.show()

    # Close the log file after the plot is closed
    log_file.close()

    # Close the progress bar
    progress_bar.close()

    return global_best_position, global_best_score, terminated_early