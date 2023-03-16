prepare_environment:
	@echo "Preparing environment ..."
	mv task.py app
	chmod +x app
	mv app /usr/local/bin
	@echo "Environment ready. Usage: app list_of_numbers target_int e.g.: app 1,2,3 1"
