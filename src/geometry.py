import numpy as np
from pygame.math import Vector2, Vector3

epsilon = 1e-6 # Keep in sync with Vector2.epsilon

def _points_into_line(p1: Vector2, p2: Vector2):
    a = p1.y - p2.y
    b = p2.x - p1.x
    c = p2.y * p1.x - p2.x * p1.y
    
    line = Vector3(a, b, c)
    return line.normalize()

def _ray_into_line(p, v):
    return _points_into_line(p, p + v)

def intersect_line_with_line(line1, line2):
    """line: ax + by + c = 0
    """
    a1, b1, c1 = line1
    a2, b2, c2 = line2
    det = a1*b2 - b1*a2
    
    if np.abs(det) < epsilon:
        return None
    else:
        x = c2 * b1 - c1 * b2
        y = c1 * a2 - c2 * a1
        return Vector2(x/det, y/det)

def ray_intersect_segment(ray, segment):
    pass

import unittest

class TestLineMethods(unittest.TestCase):
    def test_points_to_line(self):
        p1 = Vector2(0, 0)
        p2 = Vector2(2, 1)
        line = _points_into_line(p1, p2)
        self.assertEqual(line, Vector3(-0.447214, 0.894427, 0))

    def test_intersect_line_with_line(self):
        line1 = Vector3(1, 1, 0)
        line2 = Vector3(1, 0, 1)
        line3 = Vector3(2, 2, 4)

        p1 = intersect_line_with_line(line1, line2)
        p2 = intersect_line_with_line(line1, line3)
        self.assertEqual(p1, Vector2(-1, 1))
        self.assertEqual(p2, None)

if __name__ == "__main__":
    unittest.main()