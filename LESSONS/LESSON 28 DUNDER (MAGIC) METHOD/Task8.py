# Create a Basket class that stores a list of prices. 
# Implement __add__ so that adding two Basket objects (basket_1 + basket_2) 
# returns a new Basket containing the combined list of prices from both 
# (do not mutate either original basket). Verify with a test that the originals remain unchanged 
# after the addition.

class Basket:

  def __init__(self, prices):
    self.prices = prices

  def __add__(self, other):
    if not isinstance(other, Basket):
      return NotImplemented

    # Combines the lists without mutating self.prices or other.prices
    combined_prices = self.prices + other.prices
    return Basket(combined_prices)

  def __repr__(self):
    return f"Basket({self.prices!r})"


# --- Test & Verification ---
basket1 = Basket([10, 20, 30])
basket2 = Basket([40, 50, 60])

# Store original lengths/contents to verify non-mutation
orig_basket1_prices = basket1.prices.copy()
orig_basket2_prices = basket2.prices.copy()

# Addition
total_basket = basket1 + basket2

print(total_basket)  # Output: Basket([10, 20, 30, 40, 50, 60])

# Verify originals remain unchanged
print(basket1.prices == orig_basket1_prices)  # Output: True
print(basket2.prices == orig_basket2_prices)  # Output: True