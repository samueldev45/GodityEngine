# Godity Engine (Framework)

<p align="center">
  <a href="pass">
    <img src="https://i.imgur.com/SDJK5fc.png" width="400" alt="Godity Engine Logo">
  </a>
</p>

## About Framework

Godity Engine is a **open-source** framework based on pygame, it is being developed for to facilitate work of game developers who use pygame to create 2D games.

## Release 0.9

- New parameter in sprite renderer component.
- New parameters in the Scene class.
- New parameters in the Camera component.
- New methods in the Scene class.
- New method in Animation component.
- New parameters in the Animation component.
- The attribute collide_objects of component BoxCollider is now a dict.
- The parameter frame_delay of Animation component does not longer obligatory.
- New class, Layer implemented in the core.
- The box_collider and platform objects inserted by Tiled now have a tag with their respective names.
- The updateChildrenPosition method parameters of the Transform component have been removed.
- New component Light.
- New methods in Entity class.
- The parent method of the Entity class has two new parameters.
- New methods in Vector2 class.
- Removed the alpha_background parameter of the Tilemap component, maps with a transparent background are now automatically recognized.
- New parameters in Tilemap component.
- The method add of Scene class have a new obligatory parameter called layer.
- Solved the bug of sprite sheets that were giving bugs of transparency with the color (0,0,0).
- Rotation of sprites that were buggy has been fixed.
- It is now possible to create layers and place them in any scene. 

## Dependencies

1. pygame
2. pytmx

## Installation

 - pip install godity

## API

https://samueldev45.github.io/godity/docs/
