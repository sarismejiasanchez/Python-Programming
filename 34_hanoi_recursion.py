# RECURSION: TOWER OF HANOI

# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    """
    Solves the Tower of Hanoi problem using recursion.

    The Tower of Hanoi is a mathematical puzzle where you have three towers (source, helper, destination)
    and a number of disks of different sizes. The goal is to move all the disks from the source tower
    to the destination tower following these rules:
        1. Only one disk can be moved at a time.
        2. A disk can only be placed on top of a larger disk or on an empty tower.
        3. All disks start on the source tower.

    This function prints the steps required to move the disks from the source tower to the destination tower.

    Args:
        disks (int): The number of disks to be moved.
        source (str): The name of the source tower.
        helper (str): The name of the helper (intermediate) tower.
        destination (str): The name of the destination tower.

    Returns:
        None: The function prints the steps to solve the Tower of Hanoi problem.

    Example:
        >>> hanoi(3, 'A', 'B', 'C')
        Disk 1 moves from tower A to tower C
        Disk 2 moves from tower A to tower B
        Disk 1 moves from tower C to tower B
        Disk 3 moves from tower A to tower C
        Disk 1 moves from tower B to tower A
        Disk 2 moves from tower B to tower C
        Disk 1 moves from tower A to tower C
    """
    # Base condition
    if (disks == 1):
        print(f"Disk {disks} moves from tower {source} to tower {destination}")
        return
    
    # Recursive call to move the top (disks - 1) disks from the source tower to the helper tower.
    # This step uses the destination tower as an intermediate tower.
    # It breaks the problem into a smaller subproblem by temporarily moving the smaller disks
    # to the helper tower, leaving the largest disk on the source tower.
    hanoi(disks -1, source, destination, helper)
    print(f"Disk {disks} moves from tower {source} to tower {destination}")
    
    # Recursive call to move the top (disks - 1) disks from the helper tower to the destination tower.
    # This step uses the source tower as an intermediate tower.
    # It completes the process by transferring the smaller disks from the helper tower to the destination tower,
    # placing them on top of the largest disk that was previously moved.
    hanoi(disks -1, helper, source, destination)
    
# Driver code
disks = int(input("Enter of disks to be displaced: "))

"""
Tower names passed as arguments:
    Source: A
    Helper: B
    Destination: C
"""
# Actual function call
hanoi(disks, 'A', 'B', 'C')