from py2neo import Graph
graph = Graph(password="123456")

from py2neo import Node, Relationship
alice = Node("Person", name="Alice")
bob = Node("Person", name="Bob")
alice_knows_bob = Relationship(alice, "KNOWS", bob)
graph.create(alice_knows_bob)
