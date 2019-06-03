from abstract_factory import *
from tank_factory import *
from plane_factory import *

def new_unit_with_shoot(factory):
    # создаем юнит
    unit = factory.create_unit()
    # создаем пулю/снаряд
    bullet = factory.create_bullet()
    # стреляем
    unit.shoot(bullet)

print('*** Tank ***')
# создаем фабрику танков и etc.
factory_for_tank = TankFactory()
# создаем танк, снаряд, и стреляем
new_unit_with_shoot(factory_for_tank)

print('*** Plane ***')
# создаем фабрику самолетов и etc.
factory_for_plane = PlaneFactory()
# создаем самолет, пулю, и стреляем
new_unit_with_shoot(factory_for_plane)

# попытка создать и использовать несовместимые объекты 
# print('*** fail ***')
# plane = PlaneUnit()
# bullet = TankBullet()
# plane.shoot(bullet)