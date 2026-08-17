# Game Character Stats Tracker

A Python class modeling an RPG-style character with health, mana, and leveling
mechanics, built using object-oriented programming principles.

## Features
- Encapsulated stats (health, mana, level) using Python properties
- Automatic bounds-checking: health capped at 0–100, mana capped at 0–50
- Level-up system that restores health and mana to full
- Clean string representation for easy status display

## Example
```python
hero = GameCharacter('knight')
print(hero)
hero.level_up()
```

## What I'd add next
- `take_damage()` and `heal()` methods for combat interactions
- Persistent save/load of character state
