# Тестовое приложение helloworld (compose, k8s, helm, prometheus, grafana)

Исходные данные:
```
Реализовать тривиальное HTTP "Hello, world!" web-приложение на любом удобном Вам языке программирования и завернуть его в clound native окружение.

Требования:
 - Dockerfile, который докеризует приложение.
 - Приложение должно иметь health-check и ready-check.
 - Приложение должно предоставлять metrics endpoint для Prometheus (метрики - на Ваше усмотрение).
 - Grafana dashboard с визуализацией метрик.
 - docker-compose.yml, который запускает приложение со всем необходимым окружением (Prometheus и Grafana).

Временем и инструментом для выполнение тестового задания Вы не ограничены. Любые другие аспекты реализации, которые не указаны в требованиях, могут быть выполнены на Ваше усмотрение.

Следующее будет плюсом:
 - Kubernetes спеки приложения, либо Helm-чарт, для запуска его в Minikube (в дополнение к docker-compose.yaml).
 - E2E-тесты, которые проверяют корректность докеризации приложения.
```

Что сделано:
## Web-приложение 
Сделано на flask+gunicorn
## Docker compose
В compose варианте добавлены healthcheck в compose файле и readinesscheck в виде отдельного контейнера (shell script), ждущего, пока станет доступно web приложение.
Добавлены grafana и prometheus из официальных докер образов, в приложении добавлен endpoint /metrics с помощью библиотеки prometheus_flask_exporter.В графану добавлено несколько метрик.
Запуск:
1) Билдим контейнеры и запускаем
```
cd compose
docker-compose up --build -d
```
2) Проверяем
```
http://localhost:8080/
localhost:9090
localhost:3000
для grafana:
login:admin
pass:admin
дашборд называется backend
```

## K8s
В k8s варианте, сделаны liveness probe (/api/health-check/) и readiness probe (/)
Приложение деплоится чартом helm (helloworld)
Запуск:
1) Билдить не обязательно, образ пулится с dockerhub, запускаем:
```
cd k8s
helm upgrade -i helloworld helloworld
```
2)Inress не делал, поэтому доступ к приложению через port-forward:
```
kubectl port-forward service/helloworld-backend  8080:8080
```
3)Проверяем:
```
http://localhost:8080/
```

PS: E2E-тесты не делал, т.к. unit - знаю, интеграцию - знаю, UI - знаю, E2E - не, не слышал
