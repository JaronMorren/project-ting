import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    # Create an instance of PriorityQueue
    queue = PriorityQueue()
    assert len(queue) == 0

    # Test enqueue method
    queue.enqueue({"qtd_linhas": 3, "nome": "file1.txt"})
    queue.enqueue({"qtd_linhas": 6, "nome": "file2.txt"})
    queue.enqueue({"qtd_linhas": 2, "nome": "file3.txt"})

    # Test __len__ method
    assert len(queue) == 3

    # Test search method
    assert queue.search(0) == {"qtd_linhas": 3, "nome": "file1.txt"}

    # Test is_priority method
    assert queue.is_priority({"qtd_linhas": 4}) is True
    assert queue.is_priority({"qtd_linhas": 6}) is False

    # Test dequeue method
    assert queue.dequeue() == {"qtd_linhas": 3, "nome": "file1.txt"}

    # Test __len__ method after dequeue method
    assert len(queue) == 2

    # Test handling invalid index in search method
    with pytest.raises(IndexError):
        queue.search(300)
