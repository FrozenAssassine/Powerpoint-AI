
def clean_bullet_points(points):
    data = ""
    for line in points.split("\n"):
        if line.startswith(("-", "●")):
            data = data + line.replace("-", "", 1).replace("●", "", 1).strip() + "\n"
        else:
            data = data + line.strip() + "\n"
    return data