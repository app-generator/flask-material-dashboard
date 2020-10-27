run: clean build
	docker run -t -p 80:80 gt-build.hdap.gatech.edu/african-american-women-childbirth-risk-2

build:
	docker build -t gt-build.hdap.gatech.edu/african-american-women-childbirth-risk-2 ./app

clean:
	docker container prune
	docker rmi -f gt-build.hdap.gatech.edu/african-american-women-childbirth-risk-2
	docker image prune