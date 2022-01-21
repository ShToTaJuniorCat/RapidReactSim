from math import ceil
from random import randint
from alliance import Alliance
from team import Team
from robot import Robot


def roll_a_die(minimum=1, maximum=100):
    """
    Literally returns a random int @minimum - @maximum lol

    @param minimum: Minimum return value
    @param maximum: Maximum return value
    @return: Random value between @minimum and @maximum
    """
    return randint(minimum, maximum)


def get_task_calculate_function(task, team):
    """
    @param task: The task to perform
    @param team: The team performing the task
    @return: Function to calculate die roll score needed for the task to be successful
    """
    if task == "shoot":
        return team.calculate_shoot
    elif task == "collect":
        return team.calculate_collection
    elif task == "climb":
        return team.calculate_climb
    else:
        raise ValueError("Only possible tasks are 'shoot', 'collect' and 'climb'.")


def play_turn(team):
    possible_tasks = ["shoot", "climb", "collect"]

    while True:
        task = input(str(team) + ", You may shoot, climb or collect.\nWhat task do you want to perform? ")
        die_result = roll_a_die()

        try:
            success = die_result >= get_task_calculate_function(task, team)
            print(f"You rolled {die_result}.")

            if success:
                print("Well done! You completed the task successfully.")
        except ValueError:
            pass


def play_round(blue_alliance, red_alliance):
    print("For the blue alliance: ")
    for team in blue_alliance:
        print(str(team) + (" shoots." if roll_a_die(1, 100) >= team.calculate_shoot(roll_a_die(1, 100))
                           else " failed to shoot."))

    print()
    print("For the red alliance: ")
    for team in red_alliance:
        print(str(team) + (" shoots." if roll_a_die(1, 100) >= team.calculate_shoot(roll_a_die(1, 100))
                           else " failed to shoot."))


teams = [Team(254, "The Cheesy Poofs", 10, Robot(10, 10, 10)),
         Team(2212, "The Spikes", 3, Robot(7, 9, 4)),
         Team(1690, "Orbit", 8, Robot(10, 9, 9)),
         Team(3835, "Vulcan", 6, Robot(6, 8, 8)),
         Team(4586, "Primo", 7, Robot(9, 4, 5)),
         Team(5135, "Black Unicorns", 5, Robot(5, 3, 4))]

blue_alliance = Alliance(teams[0], teams[1], teams[2])
red_alliance = Alliance(teams[3], teams[4], teams[5])

print(blue_alliance)