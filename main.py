from random import randint
from alliance import Alliance
from team import Team
from robot import Robot


def roll_a_die(minimum=1, maximum=100):
    """
    Literally returns a random int @minimum - @maximum lol

    @param minimum: Minimum return value
    @param maximum: Maximum return value
    @return: Random value between @minimum and @maximum inclusive
    """
    return randint(minimum, maximum)


def get_task_calculate_function(task: str, team: Team):
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


def task_to_score(task: str, part: int, autonomous = False):
    """
    Returns score granted for successfully performing a stated task.

    @param task: Task performed
    @param part: Part of the game element the task was performed upon. For climbing 1-4, for shooting 1-2 (1 is lower HUB).
    @param autonomous: Was the task performed during autonomous round.
    @return: Score granted for performing the task
    """

    if task == "shoot" and part == 1:
        return 1 * (int(autonomous) + 1)
    elif task == "shoot" and part == 2:
        return 2 * (int(autonomous) + 1)
    elif task == "climb" and part == 1:
        return 4
    elif task == "climb" and part == 2:
        return 6
    elif task == "climb" and part == 3:
        return 10
    elif task == "climb" and part == 4:
        return 15
    elif task == "collect":
        return 0
    else:
        # Not a valid input
        raise ValueError("Wrong parameters. Allowed parameters are task = shoot with part = 1/2,\
         task = climb with part = 1/2/3/4 and task = collect.")


def play_turn(team, autonomous=False):
    possible_tasks = ["shoot", "climb", "collect"]

    # Ask the team what it wants to do
    while True:
        task = input(str(team) + ", You may shoot, climb or collect.\nWhat task do you want to perform? ")
        part = 0
        if task == "shoot" or task == "climb":
            part = int(input(f"To what part do you want to {task}? 1 for lower HUB, 1-4 for RUNGs. "))

        die_result = roll_a_die()
        protection_score = roll_a_die()

        try:
            try:
                success = die_result >= get_task_calculate_function(task, team)(protection_score, part)
                print(f"You rolled {die_result}.")

                if success:
                    print("Well done! You completed the task successfully.")
                    score = task_to_score(task, part, autonomous)
                    team.shoot(score)
                    print(f"You got {score} score.")
                    return
            except ValueError:

        except ValueError:
            print("Incorrect input!")
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

for team in blue_alliance.get_teams():
    play_turn(team)

print(blue_alliance.score)
