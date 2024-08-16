def shortest_path(source, target):

from collections import deque

queue = deque([(source, [])])  # Queue of tuples (current_person, path_so_far)
visited = set()  # Set of visited persons
visited.add(source)  # Mark source as visited
while queue:
    current_person, path_so_far = queue.popleft()

    if current_person == target:
        return path_so_far

    for movie_id, neighbor in neighbors_for_person(current_person):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append((neighbor, path_so_far + [(movie_id, neighbor)]))

return None  # If no path is found
def shortest_path(source, target):
    from collections import deque

    # Initialize the queue with the source person and an empty path
    queue = deque([(source, [])])
    visited = set()  # Set of visited persons
    visited.add(source)  # Mark source as visited

    while queue:
        current_person, path_so_far = queue.popleft()

        # If we've reached the target, return the path so far
        if current_person == target:
            return path_so_far

        # Explore neighbors
        for movie_id, neighbor in neighbors_for_person(current_person):
            if neighbor not in visited:
                visited.add(neighbor)
                # Add to queue with updated path
                queue.append((neighbor, path_so_far + [(movie_id, neighbor)]))

    return None  # No path found
