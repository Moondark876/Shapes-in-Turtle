import turtle
import random
import time

#make a shape class
class Shape:
    def __init__(self, x, y, color, size=10):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.turtle.color(color)
        self.turtle.pensize(size)
        self.turtle.shape("circle")
        self.turtle.speed(1000)
        self.turtle.showturtle()

    def move(self, x, y):
        self.x = x
        self.y = y
        self.turtle.goto(x, y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_shape(self):
        return self.turtle.shape()

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    def get_turtle(self):
        return self.turtle

    def set_color(self, color):
        self.color = color
        self.turtle.color(color)

    def set_size(self, size):
        self.size = size
        self.turtle.pensize(size)

    def set_x(self, x):
        self.x = x
        self.turtle.goto(x, self.y)

    def set_y(self, y):
        self.y = y
        self.turtle.goto(self.x, y)

    def hide(self):
        self.turtle.hideturtle()

    def show(self):
        self.turtle.showturtle()

    def destroy(self):
        self.turtle.clear()
        self.turtle.hideturtle()
        self.turtle.clear()

    def set_shape(self, shape):
        self.turtle.shape(shape)

    def set_color(self, color):
        self.turtle.color(color)
        
    def set_size(self, size):
        self.turtle.pensize(size)