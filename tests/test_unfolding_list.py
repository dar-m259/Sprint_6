import allure

from pages.main_page import MainPage

class TestUnfoldingList:
    @allure.title("Проверить отображение ответа на вопрос о стоимости и оплате")
    def test_unfolding_list_answer1_text(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question1()
        assert result == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title("Проверить отображение ответа на вопрос о нескольких самокатах")
    def test_unfolding_list_answer2_text(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question2()
        assert result == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title("Проверить отображение ответа на вопрос о расчете времени аренды")
    def test_unfolding_list_answer3_text(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question3()
        assert result == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    
    @allure.title("Проверить отображение ответа на вопрос о заказе самоката на сегодня")
    def test_unfolding_list_answer4_text(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question4()
        assert result == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    
    @allure.title("Проверить отображение ответа на вопрос о продлении и возврате")
    def test_unfolding_list_answer5_text(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question5()
        assert result == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    
    @allure.title("Проверить отображение ответа на вопрос о зарядке")
    def test_unfolding_list_answer6_text(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question6()
        assert result == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    
    @allure.title("Проверить отображение ответа на вопрос об отмене заказа")
    def test_unfolding_list_answer7_text(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question7()
        assert result == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    
    @allure.title("Проверить отображение ответа на вопрос о доставке за МКАД")
    def test_unfolding_list_answer8_text(self, main_page_driver):
        main_page = MainPage(main_page_driver)

        result = main_page.get_question8()
        assert result == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

