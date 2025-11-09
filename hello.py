# My first Python program on GitHub
# Created by Bastien Accot
def main():
    print("Hello, World!")
    print("I'm Bastien and i will attend MIT!")
    current_year = 2025
    birth_year = 2009
    my_age = current_year - birth_year
    print(f"I am {my_age} years old and I am passionate about computer science and electronics!")
    print("\nMy passions:")
    passions = ["programmation", "Artificial Intelligence", "Robotics", "Electronics", "Innovation"]
    for passion in passions:
        print(f"  - {passion}")
    
    print("\nMy goal: Join MIT to become a great engineer!")

if __name__ == "__main__":
    main()