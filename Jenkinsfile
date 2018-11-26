//comment
pipeline{
 agent any
 stages{
 	stage('Checkout-git'){
		steps{
		 git poll: true, url: 'https://github.com/RubenBaez/DEVSU.git'
		}
	}
	
	stage('Virtualenv'){
		steps{
		sh '''
			bash -c "virtualenv entorno && source entorno/bin/activate"
		'''
		}
	}
	stage('InstallRequirements'){
		steps{
		sh '''
			bash -c "pip install -r requirements.txt"
		'''
		}
	}
	stage('TestApp'){
		steps{
		sh '''
			bash -c "python test_app.py &"
		'''
		}
	}
	stage('RunApp'){
		steps{
		sh '''
			bash -c "python app.py &"
		'''
		}
	}
	stage('BuildDocker'){
		steps{
		sh '''
			docker build -t appd:latest .
		'''		
		}
	}
	stage(PushDocker){
		steps{
		sh '''
			docker tag appd:latest rubendario/devsu:latest
					docker push rubendario/devsu:latest
					docker rmi appd:latest
		'''
		}
	}
 }
}
