
def greet(name: str) -> str:
  """Function produces a greeting string with. It uses an f-string in the
  return statement, that inserts the value of parameter {name} to the 
  produced string."""
  return f"Hello {name}. How are you?"

# Create a list of friends to use in the next method. It would be nice if your 
# list was not the same as mine -- unless you are into LOTR as much as I am
# and you can prove it by reciting the One Ring's Tengwar in Black Speech.
my_friends = ["Frodo", "Sam", "Gandalf", "Saruman", "Elrond"]


def greet_friends(friends: list[str]) -> None:
  """Function takes a list of strings, parses it one string at a time, and
  passes the strign to the greet function whose output is then passed to
  the print statement, for display."""
  for name in friends:
    print(greet(name))


# We need the math module to computer square roots
import math

def solve_quadratic(a: float, b: float, c: float) -> None:
  """Basic solution to the quadratic equation. The equation
  a*x*x + b*x + c = 0
  has solutions in the real numbers if its discriminant is not negative.
  The discriminant is the quantity b*b-4*a*c. The function below computes
  the discriminant first. It then checks its sign -- if it's negative, the
  function prints "no real solutions" and stops. If the discriminant is not
  negative, the function computes the two solutions for the equation and 
  prints them. """
  # Compute the discriminant -- it's important to determine if the equation 
  # has no real solutions
  discriminant = b * b - 4 * a * c
  # Check for real solutions
  if discriminant < 0:
    print ("no real solutions")
  else:
    # Group common operations together
    common_factor = math.sqrt(discriminant)/(2*a)
    x1 = - b + common_factor # alternative x1 = (-b + math.sqrt(discriminant))/(2*a)
    x2 = - b - common_factor # alternative x2 = (-b - math.sqrt(discriminant))/(2*a)
    print(f"{x1=}\n{x2=}")
  
# Basic testing
solve_quadratic(1,2,3)
solve_quadratic(1,5,1)
greet_friends(my_friends)
