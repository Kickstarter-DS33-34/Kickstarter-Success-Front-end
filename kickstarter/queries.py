create_prediction_table = '''
    CREATE TABLE IF NOT EXISTS model_prediction(
        "submission_id" SERIAL PRIMARY KEY,
        "projectname" VARCHAR(30) NOT NULL,
        "category" VARCHAR(30) NOT NULL,
        "description" VARCHAR(300) NOt NULL,
        "city" VARCHAR(30) NOT NULL,
        "country" VARCHAR(30) NOT NULL,
        "goal" FLOAT NOT NULL,
        "currency" VARCHAR(10) NOT NULL,
        "duration" INT NOT NULL,
        "month" INT NOT NULL,
        "prediction" FLOAT NOT NULL);
'''