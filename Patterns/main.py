class Flower:
    def __init__(self):
        self.name = "Some Flower"

class ComplicatedGardenClass:
    def __init__(self):
        self.planting_area = None

    def ready_pot(self):
        if self.planting_area is None:
                self.planting_area = "Ready for planting"
        else:
            print("Pot is already ready.")        

    def add_soil(self):
        if self.planting_area == "Ready for planting":
            self.planting_area = "Soil added"
        else:
            print("Prepare the pot first.")

    def add_fertilizer(self):
        if self.planting_area == "Soil added":
            self.planting_area = "Fertilizer added"
        else:
            print("Add soil before adding fertilizer.")

    def plant_seeds(self):
        if self.planting_area == "Fertilizer added":
            self.planting_area = "Seeds planted"
        else:
            print("Add fertilizer before planting seeds.")

    def water_plants(self):
        if self.planting_area == "Seeds planted":
            self.planting_area = "Plants watered"
        else:
            print("Plant seeds before watering.")

    def care_for_plants(self):
        if self.planting_area == "Plants watered":
            self.planting_area = "Plants cared for"
        else:
            print("Water the plants before caring for them.")

    def wait_for_harvest(self):
        if self.planting_area == "Plants cared for":
            self.planting_area = "Waiting for harvest"
        else:
            print("Care for the plants before waiting for harvest.")

    def harvest(self):
        if self.planting_area == "Waiting for harvest":
            self.planting_area = "Ready for planting"
            return Flower()
        else:
            print("Wait for harvest before harvesting.")

class FascadeGarden:
    def __init__(self):
        self.garden = ComplicatedGardenClass()

    def get_flower(self):
        self.garden.ready_pot()
        self.garden.add_soil()
        self.garden.add_fertilizer()
        self.garden.plant_seeds()
        self.garden.water_plants()
        self.garden.care_for_plants()
        self.garden.wait_for_harvest()
        return self.garden.harvest()

if __name__ == "__main__":
    facade_garden = FascadeGarden()
    flower = facade_garden.get_flower()
    print(f"Got a {flower.name} from the garden!")
