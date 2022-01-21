class Robot:
    #                     1 - 10             1 - 10             1 - 10
    def __init__(self, climb_const: int, shoot_const: int, collection_const: int):
        """
        Robot object.
        Doesn't do anything remarkable, really.

        @param climb_const: How good is the robot's climbing. 1 - 10, 1 is 1/100 success rate and 10 is 99/100 success rate
        @param shoot_const: How good is the robot's shooting. 1 - 10, 1 is 1/100 success rate and 10 is 99/100 success rate
        @param collection_const: How good is the robot's collecting. 1 - 10, 1 is 1/100 success rate and 10 is 99/100 success rate
        """
        self.climb_const = climb_const
        self.shoot_const = shoot_const
        self.collection_const = collection_const