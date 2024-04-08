# Backend Яндекс.Сфера
## Описание:


[Схема базы данных](https://dbdiagram.io/d/660941d537b7e33fd7237b92)   

## Возможности проета:

...

## Что сделано:

...

## Работа с Github в команде

Разработка ведется в ветке **develop**


1. Перейти в ветку develop:

```
git checkout develop
```

2. Создать свою ветку для разработки feature  и сразу в нее перейти, название ветки  <name>/<name_feature>

```
git checkout -b <name>/<name_feature> 
```

3. Когда разработка feature закончена, то перд тем как делать запрос на сливание своей ветки в develop проделать следующее: 

   - проверить в какой ветке находитесь:

```
git branch #  Проверили: "Где я?"
* <name>/<name_feature>  # Звездочка указывает в какой вы ветке
master 
develop
```
 - если не в своей ветке, то перейти в нее:

```
 git checkout <name>/<name_feature> 
```
 - если в своей, то все закомитить;
 - затем актуализировать свою ветку по последним изменениям из develop и решить конфликты, если есть:

```
 git rebase develop
```

 - затем отправить свою ветку в git (push).

4. Перейти на GitHub и сделать “Pull requests” своей feature в ветку develop

5. После этого остальных членов команды назначить Reviewer:
   - если не согласны, то добавляют комменарии;
   - если согласны, то выставляют статус “Approve”.

6. Когда получены апрувы от всех членов команды, владелец ветки делает “Merge pull request"


## Запуск среды разработки

### 1. Клонировать docker_wrapper

```
git clone git@github.com:Sphere-Ya/docker-wrapper.git 
```
или
```
git clone https://github.com/Sphere-Ya/docker-wrapper.git
```


### 2. В папку 'docker_wrapper' склонировать backend

```
git clone git@github.com:Sphere-Ya/backend.git -b develop backend 
```
или
```
git clone https://github.com/Sphere-Ya/backend.git -b develop backend
```

### 3. В папку 'docker_wrapper' склонировать frontend

```
git clone git@github.com:Sphere-Ya/frontend.git -b develop frontend
```
или
```
git clone https://github.com/Sphere-Ya/frontend.git -b develop frontend 
```

### 4.  Скопируйте все из файла .env.example в файл .env и актуализируйте данные по необходимости

### 5. В папке 'docker_wrapper' запустить docker-compose.yml:

```
docker-compose up -d
```

### 6. Остановить:

```
docker-compose down
```

### 7. Пересобрать

```
docker-compose build --no-cache --pull
```


## Пользователи

### 1. Суперпользоаватель:

      email: admin@h.com 

      password: 111111

### 2. Василий Пупкин:

      email: vasya@h.com

      password: zxc102938

### 3. Джо Блэк:

      email: joe@h.com

      password: mko091122

