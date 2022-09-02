# GB_strokepredict
The final work on cource ML in business
Итоговая работа по курсу ML в бизнесе
Проект реализует предсказание вероятность возникновения инсульта на основе датасета https://www.kaggle.com/datasets/zzettrkalpakbal/full-filled-brain-stroke-dataset
Обучение модели представлено в stroke_predict.ipynb
После успешного обучения мы экспортитуем модель и далее загружаем ее в простенький веб интерфейс на flask и упаковыем все это в docker.
_____________________________________________________________________________________________
Описание DataSet:
Attribute Information
1) gender: "Male", "Female" or "Other"
2) age: age of the patient
3) hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
4) heartdisease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease 5) evermarried: "No" or "Yes"
6) worktype: "children", "Govtjov", "Neverworked", "Private" or "Self-employed" 7) Residencetype: "Rural" or "Urban"
8) avgglucoselevel: average glucose level in blood
9) bmi: body mass index
10) smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"*
11) stroke: 1 if the patient had a stroke or 0 if not
*Note: "Unknown" in smoking_status means that the information is unavailable for this patient
Использованная модель RandomForestClassifier

______________________________________________________________________________________________

1. На основе блокнота нужно обучить модель и сохранить ее
2. Создаем docker образ, запускаем его указывая путь где лежит наша обученная модель

Клонируем репозиторий:

$ git clone https://github.com/ecoli79/GB_strokepredict.git
$ cd GB_strokepredict
$ docker build -t stroke_predict .


Запускаем созданный контейнер:

$ docker run -d -p 5000:5000 -v <your_local_path_to_pretrained_models>:/app/app/models stroke_predict


Запускаем браузер, открываем страницу http://localhost:5000 и работаем с моделью предсказания инсульта.
