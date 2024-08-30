import pytest
import allure
from lesson_9.Pages.Employee import Employer
from lesson_9.Pages.DataBase import DataBase

api = Employer("https://x-clients-be.onrender.com")
db = DataBase(
    "postgresql+psycopg2://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

@allure.epic("X-clients")
@allure.severity(severity_level="normal")
@allure.title("Список сотрудников")
@allure.description("Получаем список сотрудников из БД и АПИ, после чего сравниваем их")
@allure.feature('Тест 1')
def test_get_list_of_employers():
    with allure.step("БД - Создаем компанию"):
        db.create_company('Evgen testers', 'cool_company')
    with allure.step("БД - Получаем ID последней созданной компании"):
        max_id = db.last_company_id()
    with allure.step("БД - Добавляем сотрудника в компанию"):
        db.create_employer(max_id, "Evgen", "Voronov", 8002000600)
    with allure.step("БД - Получаем список сотрудников из последней созданной компании"):
        db_employer_list = db.get_list_employer(max_id)
    with allure.step("API - Получаем список сотрудников из последней созданной компании"):
        api_employer_list = api.get_list(max_id)
    with allure.step("Сравниваем списки сотрудников полученных из БД и через API"):
        assert len(db_employer_list) == len(api_employer_list)
    with allure.step("БД - Удаляем созданного сотрудника"):
        response = (api.get_list(max_id))[0]
        employer_id = response["id"]
        db.delete_employer(employer_id)
    with allure.step("БД - Удаляем последнюю созданную компанию"):
        db.delete(max_id)

@allure.epic("X-clients")
@allure.severity(severity_level="critical")
@allure.title("Добавление сотрудников")
@allure.description("Добавляем сотрудника в БД и сравниваем с АПИ имя, статус и фамилию")
@allure.feature('Тест 1')    
def test_add_new_employer():
    db.create_company('Evgen adding new employer', 'employer')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Evgen", "Voronov", 8002000600)
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    with allure.step("Сравниваем ID компании"):
        assert response["companyId"] == max_id
    with allure.step("Сравниваем имя сотрудника с заданным"):
        assert response["firstName"] == "Evgen"
    with allure.step("Удостоверяемся что имя сотрудника - True"):
        assert response["isActive"] == True
    with allure.step("Сравниваем фамилию сотрудника с заданной"):
        assert response["lastName"] == "Voronov"
    with allure.step("Удаляем созданного сотрудника"):
        db.delete_employer(employer_id)
    with allure.step("Удаляем последнюю созданную компанию"):
        db.delete(max_id)

@allure.epic("X-clients")
@allure.severity(severity_level="critical")
@allure.title("Сравнение информации")
@allure.description("Сравниваем информацию о сотруднике полученную по API с информацией из БД")
@allure.feature('Тест 1')    
def test_assertion_data():
    db.create_company('Employer get id company', 'new')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Evgen", "Voronov", 8002000600)
    employer_id = db.get_employer_id(max_id)
    with allure.step("Сравниваем информацию о сотруднике полученную по API с информацией из БД"):
        get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "Evgen"
    assert get_api_info["lastName"] == "Voronov"
    assert get_api_info["phone"] == "8002000600"
    with allure.step("Удаляем созданного сотрудника"):
        db.delete_employer(employer_id)
    with allure.step("Удаляем последнюю созданную компанию"):
        db.delete(max_id)

@allure.epic("X-clients")
@allure.severity(severity_level="critical")
@allure.title("Сравнение измененной информации")
@allure.description("Сравниваем информацию о сотруднике полученную по API с изменениями")
@allure.feature('Тест 1')        
def test_update_user_info():
    db.create_company('New updating company', 'test')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Evgen", "Voronov", 8002000600)
    employer_id = db.get_employer_id(max_id)
    db.update_employer_info("King", employer_id)
    with allure.step("Сравниваем информацию о сотруднике полученную по API с изменениями"):
        get_api_info = (api.get_info(employer_id)).json()
        assert get_api_info["firstName"] == "King"
        assert get_api_info["lastName"] == "Voronov"
        assert get_api_info["isActive"] == True
    with allure.step("Удаляем созданного сотрудника"):
        db.delete_employer(employer_id)
    with allure.step("Удаляем споследнюю созданную компанию"):
        db.delete(max_id)
        