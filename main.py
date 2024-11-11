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
  membership_benefit = {
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
    print(tabulate(self.membership_benefit,headers='keys',stralign='center'))

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

  def predict_membership(self,username,monthly_expense,monthly_income):
    """
    Fungsi ini untuk memprediksi user akan masuk ke dalam membership mana 
    berdasarkan input parameter dan parameter masing - masing membership
    """
    res = []
    membership_parameter = [[8, 15], [6, 10], [5, 7]]

    #for index, _ in enumerate(membership_parameter):
    # enumerate(membership_parameter) menghasilkan pasangan (index, value) untuk setiap elemen dalam membership_parameter.
    # index adalah indeks atau posisi elemen dalam daftar, mulai dari 0.
    # value adalah nilai dari elemen di posisi tersebut, yaitu sub-daftar dua elemen dalam membership_parameter.
    # _ digunakan sebagai penanda variabel yang tidak dipakai. Ini berarti kita hanya membutuhkan index dari setiap elemen dan mengabaikan value. 
    for index,_ in enumerate(membership_parameter):
      tmp = round(sqrt( (monthly_expense-membership_parameter[index][0])**2 + (monthly_income-membership_parameter[index][1])**2 ))

      res.append(tmp)
    
    res_dict = {
        "Platinum": res[0],
        "Gold": res[1],
        "Silver": res[2]

    }

    print(f"Hasil perhitungan Euclidean Distance dari user {self.username} adalah {res_dict}")
    for member, distance in res_dict.items():
                if distance == min(res):
                    self.user_data[username] = member
                    return member
                
  def calculate_price(self,username,list_harga_barang):
    """
    Fungsi ini untuk menghitung final price yang harus dibayarkan, 
    terus akan mendapatkan diskon sesuai dengan ketentuan membership
    """
    total_barang = sum(list_harga_barang)
    discount = [float(row.strip('%'))/100 for row in self.membership_benefit['Discount']]
    
    try:
        if username in self.user_data.keys():
            membership = self.user_data.get(username)
            if membership in self.membership_benefit['Membership']:
                idx_member = self.membership_benefit['Membership'].index(membership)
                diskon = discount[idx_member] * total_barang
                final_price = total_barang - diskon
            print(f"Harga yang harus dibayar Rp. {final_price:,}")
            
            # return final_price
        else:
            raise Exception("User tidak ditemukan dalam database")
    except:
            raise Exception("Invalid process")
  