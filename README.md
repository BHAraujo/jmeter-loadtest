# Jmeter LoadTest

Projeto de testes de performance, carga e estresse

# Configuração de ambiente

   - Download Jmeter: https://jmeter.apache.org/download_jmeter.cgi

# Instalação do plugin gerenciado de plugin

   - Jmeter Plugins Manager:  https://jmeter-plugins.org/wiki/PluginsManager

# Instalação do plugin
 - Para fazer a Instalação dos plugins **Options > Plugins Manager > Available Plugins**

   - plugin **Custom Thread Groups**
   - plugin **3 Basic Graphs**
   - plugin **Composite Timeline Graph**

# Ultimate Thread Group

  - Start Threads Count
     - Quantidade de Threads

  - initial Delay,sec:
      - Tem para esperar para iniciar a Threads

  - Startup Time, sec:
      - Se o  Start Threads Count for igual a 120 e o Startup Time, sec = a 60.  120/60= 2, ou seja,
      será enviado 2 Threads por segundo

  - Hold Load For, sec:
      - Tem para ficar repetindo as Thread, por exemplo, Hold Load For, sec = 180, ou seja, por 3 minutos
      o Jmeter ficara mandando 2 Threads por segundo

  - Shutdown Time:
      - Tempo para desligando das Threads, Hold Load For, sec = 180 e Shutdown Time = 10, ou seja,
      com 170 segundos irá começar o desligamento das Threads


# Gerar relatório
   Terminal:
      - jmeter -g <namecsv.csv> -o <pastadestino>

   IDE
      - Tools > Generate HTML Report
         - File user.properties está localizado dentro da pasta bin do Jmeter
                */opt/apache-jmeter-5.2.1/bin/user.properties*
