class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available_menus= []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return f'{self.name} is available at {self.start_time} and ends at  {self.end_time}'

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      if item in self.items:
        total += self.items[item]
    return f"your total is {total}"


brunch_items= {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch = Menu('Brunch', brunch_items, 1100, 1600)
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird= Menu('Early Bird', early_bird_items, 1500, 1800)

dinner_menu_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner= Menu('Dinner', dinner_menu_items, 1700, 2200)

kids_menu_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids= Menu('Kids', kids_menu_items, 1100, 2100)

menus=[brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)



print(flagship_store.available_menus(1200))