import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    # Setup
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Koch Snowflake")
    t = turtle.Turtle()
    t.speed(0)  # Fastest
    t.color("lightBlue")  # Set snowflake color

    # Move turtle to the center
    t.penup()
    t.goto(-150, 100)  # Adjust starting position as per your need
    t.pendown()

    # Prompt user for the level of recursion
    while True:
        try:
            level = int(input("Enter the level of recursion (an integer greater than or equal to 0): "))
            if level < 0:
                print("Please enter a non-negative integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    # Start filling
    t.begin_fill()

    # Draw the three Koch curves to form the snowflake
    for _ in range(3):
        koch_snowflake(t, level, 300)
        t.right(120)

      # End filling
    t.end_fill()

    # Hide turtle and display the snowflake
    t.hideturtle()

    # Close the turtle graphics window after clicking on it
    window.exitonclick()

if __name__ == "__main__":
    main()

