from tasktrack import remove_task_by_number

def test_remove_first_task():
    """Removing task 1 should remove the first task."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]

    # Act
    removed_task = remove_task_by_number(tasks, 1)

    # Assert
    assert removed_task == "Study"
    assert tasks == ["Exercise", "Read"]

def test_remove_middle_task():
    """Removing task 2 should remove the middle task."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]

    # Act
    removed_task = remove_task_by_number(tasks, 2)

    # Assert
    assert removed_task == "Exercise"
    assert tasks == ["Study", "Read"]

def test_remove_last_task():
    """Removing task 3 should remove the last task."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]

    # Act
    removed_task = remove_task_by_number(tasks, 3)

    # Assert
    assert removed_task == "Read"
    assert tasks == ["Study", "Exercise"]

def test_remove_task_number_out_of_bounds():
    """Entering 0 should not change the list."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    expected_tasks = ["Study", "Exercise", "Read"]

    # Act
    removed_task = remove_task_by_number(tasks, 0)

    # Assert
    assert removed_task is False
    assert tasks == expected_tasks

def test_remove_task_number_too_large():
    """A number beyond the list length should not change the list."""
    # Arrange
    tasks = ["Study", "Exercise"]
    expected_tasks = ["Study", "Exercise"]

    # Act
    removed_task = remove_task_by_number(tasks, 5)

    # Assert
    assert removed_task is False
    assert tasks == expected_tasks

def test_remove_final_task_from_list():
    """removing the final task from a list should return empty list"""
    # Arrange
    tasks = ["Study"]
    expected_tasks = []

    # Act
    removed_task = remove_task_by_number(tasks, 1)

    # Assert
    assert removed_task == "Study"
    assert tasks == expected_tasks