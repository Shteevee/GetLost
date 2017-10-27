import pygame, sys, math
from pygame.locals import *

"""
Car class with following methods:
    -getPos
    -setSpeed
    -setRotate
    -move
    -updateRight
    -updateLeft
    -updateUp
    -updateDown

Initialise with starting coords
"""
class Car:
    #initialise car instance
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.right = 0
        self.left = 0
        self.up = 0
        self.down = 0
        self.speed = 0
        self.maxSpeed = 10
        self.maxReverse = -3
        self.direction = 0
        self.rad = 0
        self.image = None

    #Return a tuple of coords
    def getPos(self):
        return (self.x, self.y)
    
    #Work out the speed, accelerate to cap
    def setSpeed(self):
        self.speed += (self.up+self.down)
        if self.speed > self.maxSpeed: self.speed = self.maxSpeed
        if self.speed < self.maxReverse: self.speed = self.maxReverse

    #Work out the angle in radians
    def setRotate(self):
        self.direction += (self.right+self.left)
        self.rad = self.direction * (math.pi/180)

    #Take the angle and speed and move the car
    def move(self):
        self.x += -self.speed * math.sin(self.rad)
        self.y += -self.speed * math.cos(self.rad)

    def updateRight(self, r):
        self.right = r

    def updateLeft(self, l):
        self.left = l

    def updateUp(self, u):
        self.up = u

    def updateDown(self, d):
        self.down = d
