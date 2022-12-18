from django.db import models
from django.forms import CharField

class Note(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)
    body = models.TextField(null=True, help_text="Enter your notes here!")

class Character(models.Model):

    class CharRace(models.TextChoices):
        DRAGONBORN = "Dragonborn"
        DWARF = "Dwarf"
        ELF = "Elf"
        GNOME = "Gnome"
        HALF_ELF = "Half-Elf"
        HALFLING = "Halfling"
        HALF_ORC = "Half-Orc"
        HUMAN = "Human"
        TIEFLING = "Tiefling"

    class CharClass(models.TextChoices):
        BARBARIAN = "Barbarian"
        BARD = "Bard"
        CLERIC = "Cleric"
        DRIUD = "Druid"
        FIGHTER = "Fighter"
        MONK = "Monk"
        PALADIN = "Paladin"
        RANGER = "Ranger"
        ROGUE = "Rogue"
        SORCERER = "Sorcerer"
        WARLOCK = "Warlock"
        WIZARD = "Wizard"


    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)
    character_race = models.CharField(max_length=25, choices=CharRace.choices)
    character_class = models.CharField(max_length=25, choices=CharClass.choices)
    biography = models.TextField(max_length=500, null=True)
    