build:
	docker build . --tag docker-dsmri:latest

# Executar o contêiner com um volume mapeado
run:
	docker run --rm --name my_container -v ./Results:/app/Results docker-dsmri:latest --inputdir "/home/andre/gitworkspace/ENACOM/FINEP/DATASETS/ID44_T1w_conformed/OAS30027"

# Copiar o arquivo do contêiner para o seu computador
cp:
	docker cp my_container:/app/Results/feature.csv /caminho/para/pasta/local/feature.csv

# Excluir o contêiner
rm:
	docker rm my_container
