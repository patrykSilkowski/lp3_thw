from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

  def enter(self):
    pass
    exit(1)


class Engine(object):

    def __init__(self, scene_map):
      self.scene_map = scene_map

    def play(self):
      current_scene = self.scene_map.opening_scene()
      last_scene = self.scene_map.next_scene('finished')

      while current_scene != last_scene:
        next_scene_name = current_scene.enter()
        current_scene = self.scene_map.next_scene(next_scene_name)

      # be sure to print out the last scene
      current_scene.enter()


class Death(Scene):

  quips = [
    "You died.",
    "You sucker!",
    "Such a looser.",
    "You're worse than your Daddy's jokes."
  ]

  def enter(self):
    print(Death.quips[randint(0, len(self.quips) - 1)])
    exit(1)


class CentralCorridor(Scene):

  def enter(self):
    print(dedent("""
      The Gothons of Planet Percal #25 have invaded your ship and destroyed your
      entire crew. You are the last surviving member and your last mission is to
      get the neutron destruct bomb from the Weapons Armory, put it in the 
      bridge, and blow the ship up after getting into escape pod.

      You're running down the central corridor to the Weapons Armory when a
      Gothon jumps out. He's blocking the door to the Armory and about to pull a
      weapon to blast you.
      """))

    action = input("> ")

    if action == "shoot":
      print(dedent("""
        Quick on the draw you yank out your blaster and fire it at the Gothon.
        Unfortunate, you misses and the monster eats you.
        """))
      return 'death'

    elif action == "dodge":
      print(dedent("""
        Like a world class boxer you dodge. In the middle of your artful dodge
        your foot slips and you bang your head on the metal wall and pass out.
        You wake up shortly after only to die as the Gothon stomps on your head
        and eats you.
        """))
      return 'death'

    elif action == "joke":
      print(dedent("""
        Lucky for you they made you learn Gothon insults in the academy. You
        tell then one Gothon joke you know.
        """))
      return 'laser_weapon_armory'

    else:
      print("DOES NOT COMPUTE!")
      return 'central_corridor'


class LaserWeaponArmory(Scene):

  def enter(self):
    print(dedent("""
      You do a dive roll into whe Weapon Armory, crouch and scan the room for
      more Gothons that might be hiding. There's keypad lock on the box and you
      need the code to get the bomb out. If you get the code wrong 3 times then
      the lock closes forever and you can't get the bomb. The code is single
      digit.
      """))

    code = f"{randint(0,9)}"
    guess_cnt = 0

    while guess_cnt < 3:
      print("BZZZEEDDD!")
      guess = input("[keypad]> ")
      guess_cnt += 1

      if guess == code:
        print(dedent("""
          The container clicks open and the seal breaks, letting gas out. You
          grab the neutron bomb and run as fast as you can to the bridge where
          you must place it in the right spot.
          """))
        return 'the_bridge'
      else:
        print(dedent("""
          Beeep! Beeep!
          """))
    else:
      print(dedent("""
        The lock buzzez one last time and then you hear a sickening melting
        sound as the mechanism is fused together. You decide to sit there, and
        finally the Gothons blow up the shi[ from their ship and you die.
        """))
      return 'death'


class TheBridge(Scene):

  def enter(self):
    print(dedent("""
      You burst onto the Bridge with the netron destruct bomb under your arm and
      surprise 5 Gothons who are trying to take control of the ship. Each of
      them has an even uglier clown costume than the last. They haven't pulled
      their weapons out yet, as they see the active bomb under your arm and
      don't want to set it off.
      """))

    action = input("> ")

    if action == "throw bomb":
      print(dedent("""
        In a panic you throw the bomb at the group of Gothons and make a leap
        for the door. Right as you drop it a Gothon shoots you right in the back
        killing you.
        """))
      return 'death'

    elif action == "plant bomb":
      print(dedent("""
        You point your blaster at the bomb under your arm and the Gothons put
        their hands up and start to sweat. You inch backward to the door, open
        it, and then carefully place the bomb on the floor, pointing your
        blaster at it. You then jump back through the door, punch the close
        button and blask the lock so the Gothons can't get out. Now that bomb is
        placed you run to the escape pod to get off this tin can.
        """))
      return 'escape_pod'

    else:
      print("DOES NOT COMPUTE!")
      return 'the_bridge'


class EscapePod(Scene):

  def enter(self):
    print(dedent("""
      You rush through the ship desperately trying to make it to the escape pod
      before the whole ship explodes. It seems like hardly any Gothons are on
      the ship, so your run is clear of interference. You get to the chamber
      with the escape pods, and now need to pick one to take. Some of them could
      be damaged but you don't have time to look. There's 3 pods, which one do
      you take?
      """))

    good_pod = randint(1, 3)
    guess = input("[pod #]> ")

    if int(guess) != good_pod:
      print(dedent("""
        You jump into pod {guess} and hit the eject button. The pod escapes out
        into the void of space, then implodes as the hull ruptures, crushing
        your body into jam jelly.
        """))
      return 'death'
    else:
      print(dedent("""
        You jump into pod {guess} and hit the eject button. The pod easily
        slider out into space heading to the planet below. As it flies to the
        planet, you look back and see your ship implode then explode like a
        bright star, taking out the Gothon ship at the same time. You win!
        """))
      return 'finished'


class Finished(Scene):

  def enter(self):
    print("You win! Good job.")
    return 'finished'


class Map(object):

  scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished(),
  }

  def __init__(self, start_scene):
    self.start_scene = start_scene

  def next_scene(self, scene_name):
    val = Map.scenes.get(scene_name)
    return val

  def opening_scene(self):
    return self.next_scene(self.start_scene)


# the run
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

