# Asteroids (Pygame)

A 2D Asteroids clone built in Python with Pygame, demonstrating object-oriented programming, 2D vector physics, and collision detection.

> **Curriculum Note:** This project was built as a guided project in the [Boot.dev](https://www.boot.dev) Backend Developer Path to practice OOP inheritance, game loops, and 2D vector mathematics.

---

## What It Does

A recreation of the classic arcade Asteroids game where the player controls a triangular spaceship, rotates, accelerates, shoots bullets, and destroys incoming asteroids that split into smaller fragments upon collision.

---

## Technical & Architectural Features

- **Language:** Python 3.13 (`uv` package manager)
- **Framework:** `pygame`
- **Class Hierarchy & OOP:**
  - `CircleShape`: Abstract base class handling 2D positions, velocities, radii, and circular collision checks (`collides_with`).
  - `Player`: Inherits from `CircleShape`, manages ship drawing (triangles), rotation with delta time, movement vectors, and shooting cooldowns.
  - `Asteroid`: Inherits from `CircleShape`, handles velocity, randomized trajectories, and recursive splitting into smaller asteroids when hit.
  - `Shot`: Inherits from `CircleShape`, represents fired projectiles with high velocity and automatic lifetime cleanup.
  - `AsteroidField`: Manages edge-spawning rates and random size variations.
- **Physics & Math:** 2D vector calculation via `pygame.Vector2`, delta-time (`dt`) frame-rate independence, and circle-circle collision detection.
- **State Logging:** Custom `logger.py` that periodically captures game events and snapshots to JSONL (`game_events.jsonl`).

---

## How to Run

### 1. Prerequisites & Setup
Clone the repository and install dependencies with `uv`:

```bash
uv sync
```

### 2. Launch the Game
```bash
uv run python main.py
```

### Controls
- **W / S**: Move Forward / Backward
- **A / D**: Rotate Left / Right
- **Spacebar**: Fire Shots
