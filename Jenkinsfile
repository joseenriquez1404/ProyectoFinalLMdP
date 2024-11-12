pipeline{
	agent any
	stages {
		stage('Pull Changes'){
			steps{
				deleteDir()
				git url:' https://github.com/joseenriquez1404/ProyectoFinalLMdP', branch : 'main'
			}	
		
		}


		stage('Copy to Local Directory') {
			steps {
			// Copia todos los archivos a un directorio permanente
				sh 'cp -r * /home/jose/ProyectoFinalLMdP'
			}
		}
	}


}
