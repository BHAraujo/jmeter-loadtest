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

# Gerar relatório
   Terminal:
      - jmeter -g <namecsv.csv> -o <pastadestino>

   IDE
      - Tools > Generate HTML Report
         - File user.properties está localizado dentro da pasta bin do Jmeter
                */opt/apache-jmeter-5.2.1/bin/user.properties*
              
