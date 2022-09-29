import json
import pathlib

file_path = pathlib.Path(__file__).parent.resolve() / 'address_data.json'

address_data = []


def safety_int_input(label):
    value = None
    while True:
        value = input(label)
        if value.isdigit():
            return int(value)


def insert_data():
    new_data = {
        'id': safety_int_input("ID : "),
        'address': input("주소 : "),
        'owner_name': input("이름 : "),
        'building_name': input("건물 이름 : "),
        'number_of_people': safety_int_input("사람의 수 : "),
        'data_of_construction': input("건설 날짜 : ")
    }

    address_data.append(new_data)


def delete_data():
    while True:
        id_of_deletedata = safety_int_input("삭제할 ID : ")
        for n in range(len(address_data)):
            if address_data[n]['id'] == id_of_deletedata:
                del address_data[n]
                return
            elif address_data is None:
                print('비어있음')
                yes_or_no = input('작업을 계속 하시겠습니까?(Y/N) : ')
                if yes_or_no == 'N' and yes_or_no == 'n':
                    return


def retrieve_data():
    while True:
        id_of_retrieve_data = safety_int_input("조회할 ID : ")

        for n in range(len(address_data)):
            if address_data[n]['id'] == id_of_retrieve_data:
                value_of_print = address_data[n]
                print(value_of_print)
                return

        print('비어있음')
        yes_or_no = input('작업을 계속 하시겠습니까?(Y/N) : ')
        if yes_or_no == 'N' or yes_or_no == 'n':
            return


def modify_data():
    while True:
        id_of_modifydata = safety_int_input("수정할 ID : ")
        item_of_modify = input(
            "수정할 아이템(id/address/owner_name/building_name/number_of_people/date_of_construction 입력 : ")
        data_of_modify = input("수정할 데이터 입력 : ")
        for n in range(len(address_data)):
            if address_data[n]['id'] == id_of_modifydata:
                address_data[n][item_of_modify] = data_of_modify
                return
            elif address_data[n] == None:
                print('비어있음')
                yes_or_no = input('작업을 계속 하시겠습니까?(Y/N) : ')
                if yes_or_no == 'N' or yes_or_no == 'n':
                    return


def save_file():
    with open(file_path, 'w') as f:
        json.dump(address_data, f, indent=4)


def call_file():
    with open("address_data.json", "r") as file:
        global address_data
        address_data = json.load(file)


if __name__ == '__main__':
    while True:
        print('|---------------AddressManagementSystem---------------|')
        print('1.데이터 삽입')
        print('2.데이터 조회')
        print('3.데이터 수정')
        print('4.데이터 삭제')
        print('5.파일 저장하기')
        print('6.파일 불러오기')
        print('0.나가기')
        navigation = safety_int_input("1/2/3/4/5/6/0 중 선택 : ")

        if navigation == 0:
            exit(0)
        elif navigation == 1:
            insert_data()
        elif navigation == 2:
            retrieve_data()
        elif navigation == 3:
            modify_data()
        elif navigation == 4:
            retrieve_data()
        elif navigation == 5:
            save_file()
        elif navigation == 6:
            call_file()
        else:
            print('다시 입력하세요!')
