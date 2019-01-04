Vagrant.configure("2") do |config|   
    config.vm.box = "ubuntu/xenial64" 
    config.vm.provider :virtualbox do |v|   
	    v.customize ["modifyvm", :id, "--memory", 4096] 
    end
    config.vm.provision "shell", inline: <<-SHELL
        sudo apt update 
        sudo apt upgrade
        wget -q https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86_64.sh -O miniconda.sh
        sudo chmod +x miniconda.sh
        ./miniconda.sh -b -p /home/vagrant/miniconda
        echo 'export PATH="/home/vagrant/miniconda/bin:$PATH"' >> /home/vagrant/.bashrc
        source /home/vagrant/.bashrc
        sudo chown -R vagrant:vagrant /home/vagrant/miniconda
        /home/vagrant/miniconda/bin/conda install conda-build anaconda-client anaconda-build -y -q
        /home/vagrant/miniconda/bin/conda create --name py27_active-learning python=2.7
        /home/vagrant/miniconda/bin/conda activate py27_active-learning
        /home/vagrant/miniconda/bin/conda install -y numpy
        /home/vagrant/miniconda/bin/conda install -y scipy
        /home/vagrant/miniconda/bin/conda install -y pandas
        /home/vagrant/miniconda/bin/conda install -y scikit-learn
        /home/vagrant/miniconda/bin/conda install -y matplotlib
        /home/vagrant/miniconda/bin/conda install -y tensorflow
        /home/vagrant/miniconda/bin/conda install -y keras
        /home/vagrant/miniconda/bin/conda install -y -c conda-forge google-apputils
    SHELL
end
