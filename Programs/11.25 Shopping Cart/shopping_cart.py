class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description

    def print_item_cost(self):
        return self.item_price * float(self.item_quantity)

    def print_item_description(self):
        return ('{}: {}'.format(self.item_name, self.item_description))

class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[], named_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
        self.named_items = named_items

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        here = False
        for n in self.named_items:
            if n == item_name:
                here = True
        if here == True:
            self.cart_items.pop(self.named_items.index(item_name))
            self.named_items.remove(item_name)
            print()
        if here == False:
            print('Item not found in cart. Nothing removed.\n')

    def modify_item(self, ItemToPurchase, new_quantity):
        if ItemToPurchase in self.named_items:
            self.cart_items[self.named_items.index(ItemToPurchase)].item_quantity = new_quantity
            print()
        if ItemToPurchase not in self.named_items:
            print('Item not found in cart. Nothing modified.\n')

    def get_num_items_in_cart(self):
        count = 0
        for n in self.cart_items:
            count += float(n.item_quantity)
        return count

    def get_cost_of_cart(self):
        total = 0
        for n in self.cart_items:
            total += (n.item_price * float(n.item_quantity))
        return total

    def print_total(self):
        if len(self.cart_items) > 0:
            cart_total = 0
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Number of Items: {:.0f}\n'.format(self.get_num_items_in_cart()))
            for n in self.cart_items:
                print('{} {} @ ${:.0f} = ${:.0f}'.format(n.item_name, n.item_quantity, n.item_price, n.print_item_cost()))
            print('\nTotal: ${:.0f}\n'.format(self.get_cost_of_cart()))

        if len(self.cart_items) == 0:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Number of Items: {}\n'.format(self.get_num_items_in_cart()))
            print('SHOPPING CART IS EMPTY')
            print('\nTotal: ${:.0f}\n'.format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print('{}\'s Shopping Cart - {}\n\nItem Descriptions'.format(self.customer_name, self.current_date))
        for n in self.cart_items:
            print(n.print_item_description())
        print()

def print_menu(ShoppingCart):
    menu = 'MENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items\' descriptions\no - Output shopping cart\nq - Quit'
    print(menu)
    user_input = input('\nChoose an option:\n')

    while user_input != 'q':
        if user_input == 'o':
            print('OUTPUT SHOPPING CART')
            cart1.print_total()
            print(menu)
            user_input = input('\nChoose an option:\n')

        elif user_input == 'i':
            print('OUTPUT ITEMS\' DESCRIPTIONS')
            cart1.print_descriptions()
            print(menu)
            user_input = input('\nChoose an option:\n')

        elif user_input == 'a':
            print('ADD ITEM TO CART')
            add_name = input('Enter the item name:\n')
            item_des = input('Enter the item description:\n')
            add_price = float(input('Enter the item price:\n'))
            add_quantity = input('Enter the item quantity:\n')
            temp = add_name
            add_name = ItemToPurchase()
            add_name.item_name = temp
            add_name.item_price = add_price
            add_name.item_quantity = add_quantity
            add_name.item_description = item_des
            cart1.add_item(add_name)
            cart1.named_items.append(temp)
            print('\n{}'.format(menu))
            user_input = input('\nChoose an option:\n')

        elif user_input == 'r':
            print('REMOVE ITEM FROM CART')
            rem_item = input('Enter name of item to remove:\n')
            cart1.remove_item(rem_item)
            print(menu)
            user_input = input('\nChoose an option:\n')

        elif user_input == 'c':
            print('CHANGE ITEM QUANTITY')
            change_name = input('Enter the item name:\n')
            new_quantity = input('Enter the new quantity:\n')
            cart1.modify_item(ItemToPurchase=change_name, new_quantity=new_quantity)
            print(menu)
            user_input = input('\nChoose an option:\n')
        else:
            user_input = input('Choose an option:\n')

if __name__ == "__main__":
    customer_name = input('Enter customer\'s name:\n')
    current_date = input('Enter today\'s date:\n')
    cart1 = ShoppingCart()
    cart1.customer_name = customer_name
    cart1.current_date = current_date
    print('Customer name: {}\nToday\'s date: {}\n'.format(customer_name, current_date))
    print_menu(cart1)
