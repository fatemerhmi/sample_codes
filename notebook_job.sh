#!/bin/bash
#SBATCH --time=10:00:00
#SBATCH --account=def-emilios
#SBATCH --job-name=notebook
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:1
#SBATCH --mem=0
#SBATCH --mem=32G
#SBATCH --output=%N-%j.out
#SBATCH --error=error_%j.e


module load python/3.6
# rm -rf env
python3 -m venv env

source env/bin/activate
#ln -s $SLURM_TMPDIR/env temp_env_`whoami` #useful when you want to use VSCODE
#echo $SLURM_TMPDIR
#module load scipy-stack
module load python/3.6
python3 -m pip install --user --no-index jupyter 
python3 -m pip install --user --no-index numPy
python3 -m pip install --user --no-index pandas
python3 -m pip install --user --index="http://pypi.org/simple/" scikit-learn
python3 -m pip install --user --no-index tensorflow_gpu
#python3 -m pip install --user --no-index tensorflow_gpu==1.15
python3 -m pip install --no-index torch torchvision
python3 -m pip install --no-index torchtext
python3 -m pip install --no-index keras
python3 -m pip install --no-index matplotlib

#python3 -m pip install --no-index sentencepiece
#python3 -m pip install -r requirements.txt

unset XDG_RUNTIME_DIR
python3 -u -m jupyter notebook --ip $(hostname -f) --no-browser
