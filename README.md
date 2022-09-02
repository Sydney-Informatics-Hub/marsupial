# marsupial
Lightning fast animal detection and identification models.


### Interactive Workflow (Google Colab)

For a detailed interactive demonstration of the workflow, check out the [Google Colab](https://colab.research.google.com/drive/1YQ1ck-3HQKToAZ5DwQKy5xamDsck7KTL?usp=sharing) jupyter notebook. 

### Basic Instructions (MacOS/Linux)

These steps should work for any MacOS or Linux system. 
They should also work for Windows systems if you have correctly installed a conda version on your system and have added it to your PATH, but I have not tested these specific steps on a Windows device.

1. Create a conda environment for our project, with Python 3.9.
 
```bash
conda create -n marsupial python=3.9
conda activate marsupial
```

2. Install requirements.

```bash
pip install gradio torch pandas numpy torchvision wandb jupyterlab kaggle
```

3. Train model

```bash
python train.py --img 640 --batch 64 --epochs 300 --data marsupial.yaml --weights yolov5s.pt
```

4. Evaluate model performance

```bash
python val.py --data marsupial.yaml --task "val"
```

5. Make predictions

```bash
python detect.py --source "image_dir/" --weights <your fitted weights>
```
