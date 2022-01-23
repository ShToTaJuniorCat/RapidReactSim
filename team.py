from robot import Robot
from math import ceil


class Team:
    #                     1 - 9999                            1 - 10
    def __init__(self, team_number: int, team_name: str, financial_status: int, robot: Robot):
        """
        A team object.
        Can calculate the chance of moving, the chance of climbing, the chance of shooting and the chance of collecting.

        :param team_number: Team's number. 1 - 9999.
        :param team_name: Team's name.
        :param financial_status: Team's financial status. 1 - 10, 1 is poorest 10 is richest.
        :param robot: Team's robot object.
        """
        self.team_number = team_number
        self.team_name = team_name
        self.financial_status = financial_status
        self.robot = robot
        self.cargo = 1
        self.alliance = None

    def __str__(self):
        return self.team_name + "#" + str(self.team_number)

    def calculate_move(self):
        """
        Calculates the least die score needed for the robot to move.

        :return: The least die score for robot movement
        """
        return 5 / self.financial_status

    #                            1 - 4              1 - 100
    def calculate_climb(self, protection_chance: int, target_rung: int):
        """
        Calculates the least die score needed for the robot to climb.

        :param target_rung: The rung the robot is trying to climb to. 1 - 4, 1 is low rung 4 is traversal.
        :param protection_chance: The die score the protection robot got. 1 - 100
        :return: The least die score needed to climb
        """

        if protection_chance == 0:
            return (20 * target_rung ** 2) / (self.financial_status * 2) / (self.robot.climb_const / 3)

        return (20 * target_rung ** 2) / (self.financial_status * 2) * \
               (ceil(protection_chance / 10) / (self.robot.climb_const / 3))

    #                             1 - 100
    def calculate_shoot(self, protection_chance: int, part: int):
        """
        Calculates the least die score needed for the robot to shoot.

        :param protection_chance: The die score the protection robot got. 1 - 100
        :return: The least die score needed shoot. qwertyuiop[] (Thanks to Luke for this masterpiece)
        """

        if protection_chance == 0:
            # If the protection chance is 0, we want to use a different equation since it would badly affect the result.
            return (40 / self.financial_status) / (self.robot.shoot_const / 3)

        return (40 / self.financial_status) * (ceil(protection_chance / 10) / (self.robot.shoot_const / 3))

    #                                   1 - 100
    def calculate_collection(self, protection_chance: int, part: int):
        """
        Calculates the least die score needed for the robot to collect CARGO.

        :param protection_chance: The die score the protection robot got. 1 - 100
        :return: The least die score needed to collect a CARGO.
        """
        if protection_chance == 0:
            return (20 / self.financial_status) / (self.robot.climb_const / 3)

        return (20 / self.financial_status) * (ceil(protection_chance / 25) / (self.robot.collection_const / 3))

    def shoot(self, score):
        """
        Decreases the number of CARGO in the robot and raises alliance's score.

        @param score: Score given for shot
        @return:
        """
        self.cargo -= 1
        self.alliance.raise_score(score)

    def update_alliance(self, alliance):
        """
        Updates team's alliance to given parameter alliance.

        @param alliance: The team's alliance
        """
        self.alliance = alliance
