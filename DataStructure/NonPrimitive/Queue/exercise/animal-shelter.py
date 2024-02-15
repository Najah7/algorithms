class Dog:
    def __str__(self) -> str:
        return "Dog"


class Cat:
    def __str__(self) -> str:
        return "Cat"


class AnimalShelter:
    def __init__(self) -> None:
        self.dogs = []
        self.cats = []

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dogs.append(animal)
        elif isinstance(animal, Cat):
            self.cats.append(animal)
        else:
            raise ValueError("Invalid animal type")

    def dequeue_any(self):
        if len(self.dogs) == 0:
            return self.dequeue_cat()
        elif len(self.cats) == 0:
            return self.dequeue_dog()

        if len(self.dogs) > len(self.cats):
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()

    def dequeue_dog(self):
        if len(self.dogs) == 0:
            return None
        return self.dogs.pop(0)

    def dequeue_cat(self):
        if len(self.cats) == 0:
            return None
        return self.cats.pop(0)


shelter = AnimalShelter()
dogs = [Dog() for _ in range(3)]
cats = [Cat() for _ in range(3)]

for dog, cat in zip(dogs, cats):
    shelter.enqueue(dog)
    shelter.enqueue(cat)
shelter.enqueue(Dog())
shelter.enqueue(Dog())
shelter.enqueue(Cat())

print(shelter.dequeue_any())
print(shelter.dequeue_dog())
print(shelter.dequeue_cat())
