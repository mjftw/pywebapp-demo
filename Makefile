IMAGE_NAME = brewinv
IMAGE_VERSION = latest
IMAGE_TAG = $(IMAGE_NAME):$(IMAGE_VERSION)

PORT_HOST = 8080
PORT_CONT = 8080
HOST_IP = 0.0.0.0

.DEFAULT_GOAL := run

run:: docker-build ## Run the server inside the docker container
	docker run \
		-p $(HOST_IP):$(PORT_HOST):$(PORT_CONT)/tcp \
		$(IMAGE_TAG)

docker-build:: ## Build the docker image
	@echo building $(IMAGE_TAG)
	@docker build --pull -t $(IMAGE_TAG) .


# A help target including self-documenting targets (see the awk statement)
define HELP_TEXT
Usage: make [TARGET]... [MAKEVAR1=SOMETHING]...

Available targets:
endef
export HELP_TEXT
help: ## Show this help
	@echo
	@echo "$$HELP_TEXT"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / \
		{printf "\033[36m%-30s\033[0m  %s\n", $$1, $$2}' $(MAKEFILE_LIST)