# Particle Swarm Optimization

This project implements Particle Swarm Optimization (PSO) to find the global optimum of a given objective function. The project includes visualization to show the progress of the optimization process.

## Features

- PSO implementation for both minimization and maximization tasks
- Dynamic parameter adjustment via command-line input
- Visualization of particles and global best position using Matplotlib
- Logging of particle positions and scores to `pso_log.csv`

## Installation

### Prerequisites

- Python 3.12 or later
- Poetry for dependency management

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/leothesouthafrican/particle_swarm_optimisation.git
   cd particle_swarm_optimisation
   ```

2. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

3. Activate the virtual environment:

   ```bash
   poetry shell
   ```

## Usage

1. Run the main script:

   ```bash
   python main.py
   ```

2. When prompted, choose whether to adjust parameters or use the default settings.

3. Follow the prompts to enter any custom parameters or press Enter to accept the defaults.

### Parameters

- **Bounds**: Range for the search space (e.g., `[-5.12, 5.12]`)
- **Number of Particles**: Number of particles in the swarm (default: 30)
- **Maximum Iterations**: Maximum number of iterations (default: 100)
- **Inertia Coefficient**: Inertia coefficient (default: 0.5)
- **Cognitive Coefficient**: Cognitive coefficient (default: 0.8)
- **Social Coefficient**: Social coefficient (default: 0.9)
- **Patience**: Number of iterations without improvement before termination (default: 10)
- **Optimization Task**: Specify if the task is minimization (`min`) or maximization (`max`)

## Project Structure

```plaintext
.
├── main.py
├── poetry.lock
├── pyproject.toml
└── src
    ├── objective_function.py
    ├── particle.py
    ├── pso.py
    └── visualisation.py
```

### File Descriptions

- `main.py`: Entry point of the program. Handles user input and initiates the PSO process.
- `src/objective_function.py`: Contains the Rastrigin function and its inverted version.
- `src/pso.py`: Implements the PSO algorithm.
- `src/particle.py`: Defines the Particle class used in PSO.
- `src/visualisation.py`: Handles the visualization of the PSO process using Matplotlib.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `pyproject.toml`: Configuration file for Poetry.
- `pso_log.csv`: Logs particle positions and scores during optimization (added to `.gitignore`).

## Visualization

The progress of the optimization process is visualized using Matplotlib. The plot shows the positions of the particles, the global best position, and the global optimum. The color map represents the value of the objective function.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss any changes.

## Acknowledgements

This project is based on the Particle Swarm Optimization algorithm and uses Matplotlib for visualization.

---

**Author**: Leo
**GitHub**: [leothesouthafrican](https://github.com/leothesouthafrican)