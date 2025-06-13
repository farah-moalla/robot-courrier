from controller import Robot

# Créer une instance du robot
robot = Robot()

# Durée d’un pas de simulation (en ms)
timestep = int(robot.getBasicTimeStep())

# Récupération des moteurs (assure-toi que ces noms existent dans ton .wbt)
left_motor = robot.getDevice("left_motor")
right_motor = robot.getDevice("right_motor")

# Configuration en mode vitesse infinie
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Vitesse de base (ajuste selon ton robot)
speed = 3.0

# Boucle principale
while robot.step(timestep) != -1:
    left_motor.setVelocity(speed)
    right_motor.setVelocity(speed)
