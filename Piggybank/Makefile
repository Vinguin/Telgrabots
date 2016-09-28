build_piggybank:
	docker build -t telegram-piggybank . 

run_piggybank:
	docker run -it -d -v $(shell pwd):/root/Bot --name telegram-piggybank telegram-piggybank 

start_piggybank:
	docker start telegram-piggybank

stop_piggybank:
	docker stop telegram-piggybank
