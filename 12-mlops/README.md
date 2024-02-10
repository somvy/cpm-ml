## запуск проекта

### в докере
    docker build . -t some_tag
    docker run -p 8000:8000 some_tag

### не в докере
    poetry install
    poetry run python main.py

## основные команды git
создать репу

    git init 

добавить файлик в индекс

    git add filename

добавить все файлики в индекс
    
    git add .

сделать коммит

    git commit -m "wow such commit"

пушим изменения на сервер 
    
    git push 
## poetry
удобный пип, который резолвит зависимости за вас -- особенно актуально в больших проектах

## add library
    poetry add numpy

### install libraries
    poetry install

### enter shell (python)
    poetry shell


tests

logger, metrics -- wandb


