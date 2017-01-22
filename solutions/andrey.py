def solve(rectangles):
    if not rectangles:
        return 0

    lines = []
    for left, right, height in rectangles:
        lines.append((left, height, True))
        lines.append((right, height, False))
    lines.sort(key=lambda k: k[0])

    area = 0
    prev_x = 0
    heights = [0]

    for x, height, is_start in lines:
        width = (x - prev_x)
        area += width * max(heights)
        heights.append(height) if is_start else heights.remove(height)
        prev_x = x

    return area
