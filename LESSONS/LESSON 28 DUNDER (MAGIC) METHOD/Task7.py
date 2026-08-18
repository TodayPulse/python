# Create a Money class with amount and currency attributes.
#  Implement __eq__ so two Money objects are only equal if both the amount 
#  AND currency match (e.g. Money(10, "USD") != Money(10, "EUR")).

class Money:

  def __init__(self, amount, currency):
    self.amount = amount
    self.currency = currency

  def __eq__(self, other):
    if not isinstance(other, Money):
      return False
    return self.amount == other.amount and self.currency == other.currency



m1 = Money(10, "USD")
m2 = Money(10, "EUR")
m3 = Money(10, "USD")

print(m1 == m2) 
print(m1 == m3)  