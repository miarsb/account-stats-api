IMAGE_NAME := branden

help: ## Display help
	@awk -F ':|##' \
	'/^[^\t].+?:.*?##/ {\
	printf "\033[36m%-30s\033[0m %s\n", $$1, $$NF \
}' $(MAKEFILE_LIST) | sort

build: ## create image
	docker build -t "$(IMAGE_NAME)" .

run: build ## run and build
	docker run -it --env-file ./.env -p 8080:8080 "$(IMAGE_NAME)"

test: ## build and run tests
	docker build -f Dockerfile -t "$(IMAGE_NAME)" .
	docker run -it --env-file ./.env -v ${PWD}/tests:/api/tests -p 80:80 "$(IMAGE_NAME)" python -m unittest discover tests/
