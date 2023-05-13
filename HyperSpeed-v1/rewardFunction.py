def reward_function(params):
    # Example of rewarding the agent to follow the center line and finish under 2 minutes, however the goal was to complete 1 lap in the student league under 3 minutes

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steps = params['steps']
    progress = params['progress']
    is_reversed = params['is_reversed']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to the center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # Additional reward for finishing the track under 2 minutes
    if is_reversed:
        target_time = 120  # Adjust if needed for a different target time in seconds
    else:
        target_time = 120  # Adjust if needed for a different target time in seconds

    current_time = steps * 0.1  # Assuming a step duration of 0.1 seconds
    time_ratio = current_time / target_time

    if progress == 100:  # Agent reached the finish line
        if time_ratio <= 1.0:
            reward += 10.0
        else:
            reward -= 10.0

    return reward
