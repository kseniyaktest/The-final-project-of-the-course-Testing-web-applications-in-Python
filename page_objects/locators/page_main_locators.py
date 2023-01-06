from selenium.webdriver.common.by import By

class PageMain:

    BUTTON_COOKIE = [By.XPATH, ".//button[@id='rcc-confirm-button']"]
    BUTTON_ORDER_HEADER = [By.XPATH, ".//button[@class='Button_Button__ra12g']"]
    BUTTON_ORDER_BODY = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]
    BUTTON_SCOOTER = [By.XPATH, ".//img[@src='/assets/scooter.svg']"]
    BUTTON_YANDEX = [By.XPATH, ".//img[@src='/assets/ya.svg']"]
    PART_ABOUT_IMPORTANT = [By.CLASS_NAME, ".Home_FourPart__1uthg"]
    HEADER_ABOUT_IMPORTANT = [By.XPATH, ".//div[@class='Home_SubHeader__zwi_E' and text()='Вопросы о важном']"]
    QUESTION_HOW_MUCH_IS_IT = [By.XPATH, ".//div[@id='accordion__heading-0']"]
    ANSWER_HOW_MUCH_IS_IT = [By.XPATH, ".//div[@id='accordion__panel-0']/p"]
    QUESTION_WOULD_LIKE_SOME_SCOOTERS = [By.XPATH, ".//div[@id='accordion__heading-1']"]
    ANSWER_WOULD_LIKE_SOME_SCOOTERS = [By.XPATH, ".//div[@id='accordion__panel-1']/p"]
    QUESTION_RENTAL_TIME_IS_CALCULATED = [By.XPATH, ".//div[@id='accordion__heading-2']"]
    ANSWER_RENTAL_TIME_IS_CALCULATED = [By.XPATH, ".//div[@id='accordion__panel-2']/p"]
    QUESTION_ORDER_TODAY = [By.XPATH, ".//div[@id='accordion__heading-3']"]
    ANSWER_ORDER_TODAY = [By.XPATH, ".//div[@id='accordion__panel-3']/p"]
    QUESTION_EXTEND_ORDER = [By.XPATH, ".//div[@id='accordion__heading-4']"]
    ANSWER_EXTEND_ORDER = [By.XPATH, ".//div[@id='accordion__panel-4']/p"]
    QUESTION_BRING_CHANGING_WITH_SCOOTER = [By.XPATH, ".//div[@id='accordion__heading-5']"]
    ANSWER_BRING_CHANGING_WITH_SCOOTER = [By.XPATH, ".//div[@id='accordion__panel-5']/p"]
    QUESTION_CANCEL_ORDER = [By.XPATH, ".//div[@id='accordion__heading-6']"]
    ANSWER_CANCEL_ORDER = [By.XPATH, ".//div[@id='accordion__panel-6']/p"]
    QUESTION_I_FROM_MKAD = [By.XPATH, ".//div[@id='accordion__heading-7']"]
    ANSWER_I_FROM_MKAD = [By.XPATH, ".//div[@id='accordion__panel-7']/p"]