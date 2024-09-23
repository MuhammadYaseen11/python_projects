import tkinter as tk
import random

# Snake Game class
class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        # Game constants
        self.game_width = 800
        self.game_height = 800
        self.snake_size = 20
        self.snake_color = "green"
        self.food_color = "red"
        self.bg_color = "black"

        # Set up canvas
        self.canvas = tk.Canvas(self.root, bg=self.bg_color, height=self.game_height, width=self.game_width)
        self.canvas.pack()

        # Initialize the game
        self.snake = [(100, 100), (80, 100), (60, 100)]  # Starting coordinates of the snake
        self.snake_direction = "Right"  # Initial direction
        self.food_position = self.set_new_food_position()
        self.game_running = True
        self.score = 0

        # Bind the keyboard controls
        self.root.bind("<KeyPress>", self.change_direction)

        # Start the game
        self.update()

    # Function to set a new food position
    def set_new_food_position(self):
        x = random.randint(0, (self.game_width // self.snake_size) - 1) * self.snake_size
        y = random.randint(0, (self.game_height // self.snake_size) - 1) * self.snake_size
        return (x, y)

    # Function to handle direction changes
    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.snake_direction != "Down":
            self.snake_direction = "Up"
        elif key == "Down" and self.snake_direction != "Up":
            self.snake_direction = "Down"
        elif key == "Left" and self.snake_direction != "Right":
            self.snake_direction = "Left"
        elif key == "Right" and self.snake_direction != "Left":
            self.snake_direction = "Right"

    # Function to move the snake and update the game
    def update(self):
        if self.game_running:
            # Move the snake
            self.move_snake()

            # Check if the snake has collided with itself or the walls
            if self.check_collisions():
                self.game_over()
                return

            # Check if the snake has eaten the food
            if self.snake[0] == self.food_position:
                self.snake.append(self.snake[-1])  # Grow the snake
                self.food_position = self.set_new_food_position()  # Place new food
                self.score += 1  # Update the score

            # Redraw everything
            self.canvas.delete(tk.ALL)  # Clear the canvas
            self.draw_snake()
            self.draw_food()

            # Update the game every 100ms
            self.root.after(100, self.update)

    # Function to move the snake
    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.snake_direction == "Up":
            new_head = (head_x, head_y - self.snake_size)
        elif self.snake_direction == "Down":
            new_head = (head_x, head_y + self.snake_size)
        elif self.snake_direction == "Left":
            new_head = (head_x - self.snake_size, head_y)
        elif self.snake_direction == "Right":
            new_head = (head_x + self.snake_size, head_y)

        # Update the snake's body
        self.snake = [new_head] + self.snake[:-1]

    # Function to check collisions
    def check_collisions(self):
        head_x, head_y = self.snake[0]

        # Check if the snake hits the walls
        if head_x < 0 or head_x >= self.game_width or head_y < 0 or head_y >= self.game_height:
            return True

        # Check if the snake runs into itself
        if (head_x, head_y) in self.snake[1:]:
            return True

        return False

    # Function to draw the snake
    def draw_snake(self):
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + self.snake_size, y + self.snake_size, fill=self.snake_color)

    # Function to draw the food
    def draw_food(self):
        x, y = self.food_position
        self.canvas.create_rectangle(x, y, x + self.snake_size, y + self.snake_size, fill=self.food_color)

    # Function to end the game
    def game_over(self):
        self.game_running = False
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(self.game_width / 2, self.game_height / 2, text=f"Game Over! Score: {self.score}",
                                fill="white", font=("Arial", 24))

# Main function to run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
