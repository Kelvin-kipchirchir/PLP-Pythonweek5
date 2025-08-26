class Laptop:
    def __init__(self, brand, model, os, storage, ram):
        self.brand = brand
        self.model = model
        self.os = os
        self.storage = storage
        self.ram = ram
    
     # Encapsulation: private attribute
    __battery_health = 100 

    def laptop_info(self):
        return f"{self.brand} {self.model} | OS: {self.os}, Storage: {self.storage}GB, RAM: {self.ram}GB"

    def boot(self):
        print(f"{self.model} is booting into {self.os}")

    def upgrade_storage(self, extra_storage):
        self.storage += extra_storage
        print(f"Storage upgraded! Now {self.storage}GB")

    def charge(self):
        print(f"{self.model} is charging...")

    def use_battery(self, percent):
        if percent < self.__battery_health:
            self.__battery_health -= percent
        else:
            self.__battery_health = 0
        print(f"Battery health is now {self.__battery_health}%")

# Child Class (Inheritance)
class GamingLaptop(Laptop):
    def __init__(self, brand, model, os, storage, ram, graphics_card, cooling_system):
        super().__init__(brand, model, os, storage, ram)  # inherit Laptop attributes
        self.graphics_card = graphics_card
        self.cooling_system = cooling_system

    def laptop_info(self):
        # Polymorphism: extend parent method
        base_info = super().laptop_info()
        return f"{base_info}, GPU: {self.graphics_card}, Cooling: {self.cooling_system}"

    def start_game(self, game):
        print(f"Launching {game} on {self.model} with {self.graphics_card}")


# Example laptops as objects with their attributes
laptop1 = Laptop("Apple", "MacBook Pro 14", "macOS", 512, 16)
laptop2 = Laptop("Dell", "XPS15", "Windows 11", 1024, 32)
laptop3 = Laptop("Lenovo", "ThinkPad X1 Carbon", "Windows 11", 512, 16)
laptop4 = Laptop("HP", "Spectre x360", "Windows 11", 256, 8)
laptop5 = Laptop("Asus", "ROG", "Windows 11", 2048, 64)

gaming_laptop1 = GamingLaptop("Asus", "ROG", "Windows 12", 2048, 64, "NVIDIA RTX 4090", "Liquid Cooling")

print(laptop1.laptop_info())
laptop1.boot()

print(laptop2.laptop_info())
laptop2.upgrade_storage(512)

print(laptop5.laptop_info())
laptop5.use_battery(50)

#applying polymorhism,inheritance
print(gaming_laptop1.laptop_info())
gaming_laptop1.start_game("Mikey 2077")
gaming_laptop1.upgrade_storage(1024)