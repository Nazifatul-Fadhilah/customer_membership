from math import sqrt
from tabulate import tabulate

class Membership:
# data member
  user_data = {
      "Sumbul": "Platinum",
      "Ana": "Gold",
      "Cahya": "Platinum"
  }
# data membership
  membership = {
      'Membership': ['Platinum','Gold','Silver'],
      'Discount' : ['15%','10%','8%'],
      'Another Benefit' : ["Benefit Gold + Silver + Cashback max. 30%","Benefit Silver + Voucher Ojek Online","Voucher Makanan"]
      }

  requirements = {
      'Membership': ['Platinum','Gold','Silver'],
      'Monthly Expense (juta)' : [8,6,5],
      'Monthly Income (juta)': [15,10,7]
}
  def __init__(self,username):
    """
    Fungsi ini untuk menginisiasi objek user

    input: username (str)
    """
    self.username = username
  
  def show_benefit(self):
    """
    Fungsi ini untuk menampilkan all membership benefit
    """

    print(f"Benefit Membership PacCommerce\n")
    print(tabulate(self.membership,headers='keys',stralign='center'))

    # print(f"{self.headers}")
    # print('-'*50)
    # for row in range(len(self.list_benefit)):
    #   print(self.list_benefit[row])

  def show_requirements(self):
    """ 
    Fungsi ini untuk show all requirements membership
    """

    print("Requirements Membership PacCommers\n")
    print(tabulate(self.requirements,headers='keys',stralign='center'))

    # print(f'{self.headers}')
    # print('-'*50)
    # for row in range(len(self.requirement_membership)):
  