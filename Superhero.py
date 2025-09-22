import Imports

def func(lo_flag, lo_sex):
    response = Imports.requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')
    big_json_data = response.json() 
    
    max_height = 0
    tallest_character = None
    
    rezult_list = []
    for character in big_json_data:
        try:
          
            occupation = str(character['work']['occupation'])
            gender = str(character['appearance']['gender'])
            
            if (occupation != "-") == lo_flag and gender == lo_sex:
                rezult_list.append(character)
                
                
                height_str = character['appearance']['height'][1]
                height_cm = int(height_str.split()[0])
            
                
                if height_cm > max_height:
                    max_height = height_cm
                    tallest_character = character
            Final_person_name = tallest_character['name']
                     
        except:
            
            continue
    
    
    return Final_person_name

def get_user_info():
    while True:
        try:
            work_input = input("Наличие работы (да/нет): ").strip()
            if work_input == 'да':
                has_work = True
            elif work_input == 'нет':
                has_work = False
            else:
                print("Пожалуйста, введите 'да' или 'нет'")
                continue
        
            gender_input = input("Введите пол (м/ж или '-'): ").strip()
            if gender_input == 'м':
                gender = 'Male'
            elif gender_input == 'ж':
                gender = 'Female'
            elif gender_input == '-':
                gender = '-'
            else:
                print("Пожалуйста, введите 'м' или 'ж' или '-'")
                continue
            
            return has_work, gender
            
        except KeyboardInterrupt:
            print("\nПрерывание")
            return None, None

work_status, gender_info = get_user_info()
print(func(work_status, gender_info))            