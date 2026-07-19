#python函数学习（上） ->不做代码复读机
#求扇形面积计算公式
def calculate_sector(central_angle,radius):
    sector_area = central_angle / 360*3.14*radius**2
    print(f'此扇形的面积为：{sector_area}')

calculate_sector(160,30)




