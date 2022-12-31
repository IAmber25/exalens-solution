def apartmentHunting(blocks, reqs):
    # Initialize minimum distance to a very large value
    min_distance = float("inf")
    # Initialize optimal block index to -1
    optimal_block_index = -1
    
    # Iterate through each block
    for i, block in enumerate(blocks):
        # Initialize distance to 0
        distance = 0
        # Iterate through each requirement
        for req in reqs:
            # Check if the requirement is present in the current block
            if block[req]:
                # If the requirement is present, set distance to 0 and break the loop
                distance = 0
                break
            # If the requirement is not present, increment the distance by 1
            distance += 1
        # Update the minimum distance if the current distance is smaller
        if distance < min_distance:
            min_distance = distance
            optimal_block_index = i
    
    return optimal_block_index
