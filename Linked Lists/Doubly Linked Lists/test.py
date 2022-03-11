from LinkedDeque import LinkedDeque

x = LinkedDeque()

x.insert_first(1)
x.insert_first(2)
x.insert_last(100)

print(x.delete_first())
print(x.delete_last())
print(x.delete_last())
print(x.delete_last())

