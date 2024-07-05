"""Euclidean"""
def main(num_q1, num_q2, num_p1, num_p2):
    """EuclideanDistance2D"""
    distance = (((num_q1 - num_p1)**2 + (num_q2 - num_p2)**2)**0.5)
    print(distance)
main(float(input()), float(input()), float(input()), float(input()))