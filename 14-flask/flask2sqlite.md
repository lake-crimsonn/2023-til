# flask to sqlite

- 플라스크와 sqlite를 연결해보겠다.
- sqlite는 소규모 데이터베이스이며 프로토타입용으로 사용이 된다.
- https://wikidocs.net/81045

1.  pip install flask-migrate
    - SQLAlchemy와 함께 설치가 된다.
2.  루트 디렉터리에 config.py 파일 생성

    ```python
        import os

        BASE_DIR = os.path.dirname(__file__)

        SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    ```

    - ORM을 적용하기 위해 데이터베이스 설정
    - `SQLALCHEMY_DATABASE_URI`: 데이터베이스 접속 주소
    - `SQLALCHEMY_TRACK_MODIFICATIONS`: sqlalchemy 이벤트 처리 옵션. 사용하지 않음
    - pybo.db 파일이 데이터베이스.

3.  \_\_init\_\_.py 추가

    ```python
    from flask import Flask
    from flask_migrate import Migrate
    from flask_sqlalchemy import SQLAlchemy

    import config

    db = SQLAlchemy()
    migrate = Migrate()

    def create_app():
        app = Flask(__name__)
        app.config.from_object(config)

        # ORM
        db.init_app(app)
        migrate.init_app(app, db)
        from . import models

        # blueprint
        from .views import main_views
        app.register_blueprint(main_views.bp)

        return app
    ```

    - `app.config.from_obeject(config)`: config.py 읽어오기.
    - db, migrate는 전역변수, init_app() 메서드로 app 등록.
    - db를 create_app()함수 밖에서 전역변수로 이용하는 이유는 다른 모듈에서 사용하기 위함.

4.  flask db init

    - 데이터베이스 초기화
    - migrations 디렉터리가 자동으로 생성
    - Flask-Migrate 라이브러리가 내부적으로 사용하는 파일들.
    - 처음 한번만 수행.

5.  질문 모델 생성하기

    ```python
        from pybo import db

        class Question(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            subject = db.Column(db.String(200), nullable=False)
            content = db.Column(db.Text(), nullable=False)
            create_date = db.Column(db.DateTime(), nullable=False)
    ```

- pybo/models.py 생성
- 모델은 데이터를 다룰 목적으로 만든 파이썬 클래스다.
- 클래스는 테이블을 정의한다.
- 이닛 파일에서 생성한 알케미 객체를 상속받아야 한다. db.Model
- 프라이머리키는 중복된 값을 가질 수 없는 기본 키다. 데이터 구분하는 값이다. 자동으로 증가한다.

6.  답변 모델 생성하기

    ```python
    class Answer(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
        question = db.relationship('Question', backref=db.backref('answer_set'))
        content = db.Column(db.Text(), nullable=False)
        create_date = db.Column(db.DateTime(), nullable=False)
    ```

    - pybo/models.py에 추가해주기
    - `db.ForeignKey()`는 외래키 설정. 기존에 존재하는 모델의 기본키가 들어간다. 질문과 답변 테이블을 연결하기 위해서 사용한다. 답변은 어떤 질문에 대한 답변인지 알아야 하므로 질문 모델의 id가 필요하다.
      - `question.id`는 Question 모델로 생성한 테이블 question의 id 칼럼이다.
      - `ondelete=CASCADE`는 질문을 삭제하면 답변도 삭제된다는 의미다. 기본키 삭제 -> 외래키 삭제. CASCADE 옵션은 데이터베이스 설정이다. 따라서 질문을 데이터베시으 툴에서 쿼리로 삭제할 때만 질문에 달린 답변들이 삭제된다.
    - `db.relationship()`은 답변 모델에서 질문 모델을 참조하기 위해 추가했다.
      - 위와 같이 설정하면 `answer.question.subject`처럼 참조가 가능하다.
      - `backref`는 역참조 설정이다. 질문에서 답변을 거꾸로 참조할 수 있다.
      - 한 질문에는 여러 개의 답변이 달릴 수 있는데 역참조는 이 질문에 달린 답변들을 참조할 수 있다.
      - 질문에 해당하는 객체가 a_question이라면 a_question.answer_set와 같은 코드로 해당 질문에 달린 답변들을 참조할 수 있다.
      - `a_question.delete()`처럼 파이썬 코드로 질문 데이터를 삭제할 때 연결된 답변 모두 삭제 코드
        ```python
        question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))
        ```

7.  flask db migrate

    - 모델을 새로 생성하거나 변경
    - 123123123\_.py와 같은 리비전 파일이 생성된다.
    - 리비전 파일 내에는 테이블 생성을 위한 쿼리문이 들어있다.

8.  flask db upgrade

    - 모델의 변경 내용을 데이터베이스에 적용.
    - 데이터베이스에 리비전 파일 실행하기.

9.  flask shell

    - 플라스크 셸은 플라스크를 실행하는 데 필요한 환경이 자동으로 설정되어 실행이 된다.

10. 데이터베이스에 데이터 넣어보기

    ```python
    from pybo.models import Question, Answer
    from datetime import datetime
    q = Question(subject='pybo가 무엇인가여?', content='pybo에 대해 알고 싶습니다.', create_date=datetime.now())

    from pybo import db
    db.session.add(q)
    db.session.commit()
    ```

    - 데이터베이스를 처리하려면 데이터베이스와 연결된 세션이 필요하다.
    - 세션을 통해서 데이터를 저장, 수정, 삭제 작업을 한다.
    - 커밋으로 데이터베이스에 데이터를 보낸다.
    - 커밋은 취소할 수 없다. 커밋 이전으로 되돌아가려면 `db.session.rollback()`.
