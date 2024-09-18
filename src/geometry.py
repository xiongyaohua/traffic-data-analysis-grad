from typing import Optional, Sequence
import numpy as np
from pygame.math import Vector2, Vector3

Ray = tuple[Vector2, Vector2]
Segment = tuple[Vector2, Vector2]
Line = Vector3

epsilon = 1e-6 # Keep in sync with Vector2.epsilon

def _points_into_line(p1: Vector2, p2: Vector2) -> Vector3:
    a = p1.y - p2.y
    b = p2.x - p1.x
    c = p2.y * p1.x - p2.x * p1.y
    
    line = Vector3(a, b, c)
    return line / Vector2(a, b).length()

def _ray_into_line(p: Vector2, v: Vector2) -> Vector3:
    return _points_into_line(p, p + v)

def intersect_line_with_line(line1: Line, line2: Line) -> Optional[Vector2]:
    a1, b1, c1 = line1
    a2, b2, c2 = line2
    det = a1*b2 - b1*a2
    
    if np.abs(det) < epsilon:
        return None
    else:
        x = c2 * b1 - c1 * b2
        y = c1 * a2 - c2 * a1
        return Vector2(x/det, y/det)

def intersect_ray_with_segment(ray: Ray, segment: Segment) -> Optional[Vector2]:
    p, v = ray
    p1, p2 = segment
    line1 = _ray_into_line(p, v)
    line2 = _points_into_line(p1, p2)

    i = intersect_line_with_line(line1, line2)
    
    if not i:
        return None 
    
    if np.abs(p1.distance_to(i) + p2.distance_to(i) - p1.distance_to(p2)) > epsilon:
        return None

    if (i - p).dot(v) < 0.0:
        return None
    
    return i    

def intersect_ray_with_segments(ray: Ray, segments: Sequence[Segment]) -> Optional[Vector2]:
    p, v = ray
    points = [intersect_ray_with_segment(ray, segment) for segment in segments]
    points = [point for point in points if point is not None]
    
    if points:
        points.sort(key=lambda point: point.distance_to(p))
        return points[0]
    else:
        return None


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

    def test_intersect_ray_with_segment(self):
        p = Vector2(0, 0)
        v = Vector2(1, 1)

        p1 = Vector2(0, 10)
        p2 = Vector2(10, 0)
        p3 = Vector2(10, -10)

        i1 = intersect_ray_with_segment((p, v), (p2, p3))
        i2 = intersect_ray_with_segment((p, v), (p1, p2))
        self.assertEqual(i1, None)
        self.assertEqual(i2, Vector2(5, 5))

    def test_intersect_ray_with_segments(self):
        p = Vector2(0, 0)
        v = Vector2(1, 0)

        p1 = Vector2(10, 10)
        p2 = Vector2(10, -10)
        p3 = Vector2(20, 10)
        p4 = Vector2(20, -10)

        i1 = intersect_ray_with_segments((p, v), [(p1, p2), (p4, p3)])
        i2 = intersect_ray_with_segments((p, v), [(p4, p3), (p1, p2)])
        self.assertEqual(i1, Vector2(10, 0))
        self.assertEqual(i2, Vector2(10, 0))

if __name__ == "__main__":
    unittest.main()