def recurser(boxes, melons, visited = 'All True'):
    for box_id, box in enumerate(boxes):
        # box is visited
        recurser(boxes, melons)