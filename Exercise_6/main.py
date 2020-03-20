from shipping import Shipping, ExpressShipping, StandardShipping

if __name__ == "__main__":

    shipping = Shipping(StandardShipping())
    shipping.print_shipping('South')

    print()
    
    shipping._strategy = ExpressShipping()
    shipping.print_shipping('Southeast', 10)

