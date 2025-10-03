def print_ball_motion_table(T, N):
    """
    Prints a table of the position, at different times, 
    of a ball thrown vertically from the ground level at 
    a velocity of 100 m/s. The interval [0,T] is split 
    into N parts, resulting into N+1 time points at which to 
    calculate and show the position of the ball, that is, N+1 
    rows in the table.
    """
    t = 0.0  # Initialize current time t to 0.0 (s) 
    i = 0  # Initialize loop counter to zero
    dt = T/N # Compute Delta_t (s)
    while i <= N: # Loop condition (compare integers!)
        y = 100*t - (0.5*9.8*(t**2))  # Compute y(t)
        print('time', '\tposition')         
        print(f"{t:5.2f} {y:7.2f}")
        i = i +1    # Increment loop counter i (by how much?)
        t = t + dt    # Increment current time t (by how much?)
        

print_ball_motion_table(10, 10)