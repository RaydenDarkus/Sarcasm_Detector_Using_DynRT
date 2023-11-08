# DynRT
This repository contains (PyTorch) code and pre-trained models for Dynamic Routing Transformer Network (DynRT), described by the paper *Dynamic Routing Transformer Network for Multimodal Sarcasm Detection* accepted by ACL 2023.

```
### Datasets
Our experiments are based on Multimodal Sarcasm Detection (MSD) dataset. Please refer to our paper for more details about this datasets. The file size of image data is too large to submit as supplementary materials. 

Please download the image data from [data-of-multimodal-sarcasm-detection](https://github.com/headacheboy/data-of-multimodal-sarcasm-detection) and put all the images in the folder `dataset_image`. 

The text data and corresponding labels before preprocessing are in the folder `input/prepared`, which are the same with 
[data-of-multimodal-sarcasm-detection/text](https://github.com/headacheboy/data-of-multimodal-sarcasm-detection/tree/master/text). We follow [data-of-multimodal-sarcasm-detection/LoadData.py](https://github.com/headacheboy/data-of-multimodal-sarcasm-detection/blob/f42b16510208624d91fa545ca9bb64c6335f971e/codes/loadData.py#L80) to remove easy samples with regular words (e.g. humor, sarcasm, etc.) as all previous studies do. Please run `clean_dataset.py` to get preprocessed dataset in the folder `input/prepared_clean`. To save storage space, all the text data and corresponding labels are saved as binary files. To read these binary files, please use the following function:

```
def load_file(filename):
    with open(filename, 'rb') as filehandle:
        ret = pickle.load(filehandle)
        return ret
```


We preprocess the image and convert the image to a numpy array in order to save training time.  The numpy array file of the image will be saved in the fold `image_tensor/`. Please run the following command:
```
python convert_image_to_tensor_save.py
```

### Pretrained model
Download the pre-trained model roberta-base and corresponding files from 
[roberta-base](https://huggingface.co/roberta-base/). Put these files in `roberta-base/` folder.


## Model

### Train/evaluate the model
The parameter configuration files for training and testing are in the fold `config/`.
You can use `train.py` to train a DynRT model. A command template is as follows:
```bash
CUDA_VISIBLE_DEVICES=0 python train.py {path of the parameter configuration file} \
```
You can use `test.py` to evaluate an existing model. Please fill the model path as a value for the key  `test_on_checkpoint` in the config file. You can find our checkpoint file from the [ACL23-DynRT](https://drive.google.com/drive/folders/1sV9r-dlESCOeD2xsnpkd_lmgL_4MlT8U?usp=share_link). A command template is as follows:
```bash
python test.py config/DynRT.json \
```

The experimental results will be stored in a subfolder of the folder `exp/{date-time}/`. In this fold, `log.txt` is the log file, JSON file is the parameter configuration file. 

The configuration files are in the folder `config/`. 


## CheckList 

We train our model on GeForce RTX 3050 GPUs.

## Acknowledgements

Thanks for the dataset from https://github.com/headacheboy/data-of-multimodal-sarcasm-detection

Thanks for the RoBERTa model from https://huggingface.co/roberta-base/

Thanks for the TRAR from https://github.com/rentainhe/TRAR-VQA
