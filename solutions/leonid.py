def solve(rectangles):
    if not rectangles:
        return 0

    area = 0

    x_points = set()
    for start, end, height in rectangles:
        x_points.add(start)
        x_points.add(end)
    x_points = sorted(x_points)

    prev_x = x_points[0]
    for x in x_points:
        max_height = 0
        for x1, x2, height in rectangles:
            if x1 < x <= x2:
                max_height = max(max_height, height)
        width = x - prev_x
        area += width * max_height
        prev_x = x

    return area
