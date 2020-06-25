from listmanager import SimpleListManager

def test_itemlist_SimpleListManager_insert_task():
    # Arrange
    expectedList = ["one"]
    sm = SimpleListManager()
    task = "one"
    # Act
    sm.insert_task(task)
    # Assert
    assert len(sm.listOfItems) == 1 and sm.listOfItems[0] == expectedList[0]

def test_itemlist_SimpleListManager_delete_task():
    # Arrange
    expectedList = ["two"]
    sm = SimpleListManager()
    sm.insert_task("one")
    sm.insert_task("two")
    task = "one"
    # Act
    sm.delete_task(task)
    # Assert
    assert len(sm.listOfItems) == 1 and sm.listOfItems[0] == expectedList[0] 

def test_itemlist_SimpleListManager_get_tasks():
    # Arrange
    expectedList = ["one", "two"]
    sm = SimpleListManager()
    taskOne = "one"
    taskTwo = "two"
    # Act
    sm.insert_task(taskOne)
    sm.insert_task(taskTwo)
    # Assert
    assert len(sm.listOfItems) == 2
    
    for i, task in enumerate(expectedList):
        assert task == sm.listOfItems[i]